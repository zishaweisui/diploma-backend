from bson.objectid import ObjectId

from infrastructure_exceptions import (
    InvalidRequestException,
    UnauthenticatedException,
    UnauthorizedException,
)
from models.login import LoginRequest
from models.token_pairs import TokenPair


class AuthService:
    def __init__(self, users_repository, password_service, tokens_service):
        self.users_repository = users_repository
        self.password_service = password_service
        self.tokens_service = tokens_service

    async def login(self, login_request, principal=None) -> TokenPair:
        user = await self.users_repository.find_by_email(login_request.email)
        if not user:
            raise UnauthenticatedException

        if not await self.password_service.check(
                login_request.password, user.password_hash):
            raise UnauthenticatedException

        new_pair = self.__create_pair(user)

        user.token_pairs.append(new_pair)
        await self.users_repository.update(user)
        return new_pair

    async def refresh(self, refresh_token_request, principal=None) -> TokenPair:
        refresh_payload = self.__get_payload(refresh_token_request.refresh_token)
        user = await self.__get_user_by_token(refresh_payload)

        pair_id = refresh_payload.get("id")
        refreshed_pairs = [p for p in user.token_pairs if str(p.id) == pair_id]
        if not refreshed_pairs or len(refreshed_pairs) == 0:
            raise UnauthenticatedException()

        pair = refreshed_pairs[0]
        if self.tokens_service.decode(pair.access_token):
            return pair

        new_pair = self.__create_pair(user, refresh_token_request.refresh_token, pair_id)
        user.token_pairs = self.__remove_token_pairs(user.token_pairs, pair_id)
        user.token_pairs.append(new_pair)
        await self.users_repository.update(user)
        return new_pair

    async def logout(self, auth_header, principal=None):
        token = self.__get_token_from_header(auth_header)
        payload = self.__get_payload(token)
        user = await self.__get_user_by_token(payload)

        pair_id = payload.get("id")
        user.token_pairs = self.__remove_token_pairs(user.token_pairs, pair_id)

        await self.users_repository.update(user)

    async def authenticate(self, auth_header, allow_anonymous):
        jwt = self.__get_token_from_header(auth_header, allow_anonymous)
        if not jwt:
            if allow_anonymous:
                return None
            else:
                raise UnauthenticatedException
        payload = self.__get_payload(jwt)
        user = await self.__get_user_by_token(payload, allow_anonymous)

        access_tokens = {pair.access_token for pair in user.token_pairs}

        if jwt not in access_tokens:
            if allow_anonymous:
                return None
            else:
                raise UnauthenticatedException
        return user

    async def authorize(self, user, roles):
        if roles == "*":
            return
        if not user:
            raise UnauthorizedException
        user_roles = [user.role, *user.roles]
        cross_roles = [role for role in user_roles if role in roles]
        if not cross_roles:
            raise UnauthorizedException

    async def change_password(self, attributes, principal=None) -> TokenPair:
        user_id = attributes.get("user_id")
        if str(principal.id) != user_id:
            raise UnauthorizedException
        auth_header = attributes.get("Authorization")
        principal = await self.authenticate(auth_header, False)

        old_password = attributes.get("old_password")
        if not await self.password_service.check(old_password, principal.password_hash):
            error = {
                "old_password": [
                    {
                        "message": "Invalid password",
                        "key": "error_invalid_password"
                    }
                ]
            }
            raise InvalidRequestException(error)
        principal.password_hash = await self.password_service.create_hash(
            attributes["new_password"])
        principal.token_pairs = []
        await self.users_repository.update(principal)
        login_attrs = {
            "email": principal.email,
            "password": attributes["new_password"]
        }
        login_request = LoginRequest(**login_attrs)
        token_pair = await self.login(login_request)
        return token_pair

    def __create_pair(self, user, refresh_token=None, token_id=None):
        if not token_id:
            token_id = ObjectId()
        claims = {
            "id": str(token_id),
            "user_id": str(user.id),
            "roles": ",".join(user.roles),
            "role": user.role
        }
        access = self.tokens_service.encode("access", claims)
        if not refresh_token:
            refresh_token = self.tokens_service.encode("refresh", claims)
        return TokenPair(id=token_id, access_token=access, refresh_token=refresh_token)

    async def __get_user_by_token(self, payload, allow_anonymous=None):
        user_id = payload.get("user_id")
        user = None
        if ObjectId.is_valid(user_id):
            user = await self.users_repository.get(ObjectId(user_id))

        if not user:
            if allow_anonymous:
                return None
            else:
                raise UnauthenticatedException

        return user

    def __get_token_from_header(self, auth_header, allow_anonymous=None) -> str | None:
        if not auth_header:
            if allow_anonymous:
                return None
            raise UnauthenticatedException
        authorization = auth_header.split(" ")
        if len(authorization) != 2 or authorization[0].lower() != "token":
            if allow_anonymous:
                return None
            raise UnauthenticatedException
        token = authorization[1]
        return token

    def __get_payload(self, token):
        payload = self.tokens_service.decode(token)
        if not payload:
            raise UnauthenticatedException
        return payload

    def __remove_token_pairs(self, token_pairs, pair_id):
        return [p for p in token_pairs if str(p.id) != str(pair_id)]
