from bson.objectid import ObjectId

from infrastructure_exceptions import InvalidRequestException, NotFoundException
from models.login import LoginRequest
from models.page import Page
from models.token_pairs import TokenPair
from models.user import User, UserIn, UserUpdate
from models.password import UpdatePassword


class UsersService:
    def __init__(self, page_service, password_service, repository, auth_service):
        self.page_service = page_service
        self.password_service = password_service
        self.repository = repository
        self.auth_service = auth_service

    async def create_user(self, model: UserIn, principal=None) -> User:
        existing_user = await self.repository.find_by_email(model.email)
        if existing_user:
            error = {
                "user": [
                    {"message": "Email is already taken", "key": "error_already_exists"}
                ]
            }
            raise InvalidRequestException(error)
        model.role = "user"
        user = User.model_validate(model)
        user.password_hash = await self.password_service.create_hash(model.password)
        user.token_pairs = []
        user.id = await self.repository.create(user)
        return user

    async def change_password(
            self, user_id: ObjectId, update_password: UpdatePassword, principal=None) -> TokenPair:
        user = await self.__get_user(user_id)
        old_password = update_password.old_password
        if not await self.password_service.check(old_password, user.password_hash):
            error = {
                "old_password": [
                    {
                        "message": "Invalid password",
                        "key": "error_invalid_password"
                    }
                ]
            }
            raise InvalidRequestException(error)

        user.password_hash = await self.password_service.create_hash(
            update_password.new_password
        )
        user.token_pairs = []
        await self.repository.update(user)

        login_request = LoginRequest(
            email=user.email,
            password=update_password.new_password
        )
        token_pair = await self.auth_service.login(login_request)
        return token_pair

    async def get_principal(self, principal=None):
        return principal

    async def get_user(self, user_id: ObjectId, principal=None) -> User:
        user = await self.repository.get(user_id)
        return user

    async def get_users(self, principal=None) -> list[User]:
        return await self.repository.get_list()

    async def update_user(self, user_id: ObjectId, updated_user: UserUpdate, principal=None) -> User:
        user = await self.__get_user(user_id)
        email_collision = await self.repository.find_by_email(updated_user.email)
        if email_collision and email_collision.id != user_id:
            error = {
                "user": [
                    {"message": "Email is already taken", "key": "error_already_exists"}
                ]
            }
            raise InvalidRequestException(error)
        user.assign_request(updated_user)
        await self.repository.update(user)
        return user

    async def delete_user(self, user_id: ObjectId, principal=None) -> None:
        await self.__get_user(user_id)
        await self.repository.delete(user_id)

    async def __get_user(self, user_id: ObjectId):
        user = await self.repository.get(user_id)
        if not user:
            raise NotFoundException
        return user

    async def get_page(self, paging, principal=None) -> Page:
        role = paging.role or "user"

        return await self.page_service.get_page(
            paging,
            self.repository.get_page,
            self.repository.count,
            role
        )

    async def upload_file(self, file):
        ...
