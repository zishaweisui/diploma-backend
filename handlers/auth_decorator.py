from fastapi.responses import JSONResponse

from infrastructure_exceptions import UnauthenticatedException, UnauthorizedException


class Auth:
    def __init__(self, roles, allow_anonymous):
        self.roles = roles
        self.allow_anonymous = allow_anonymous


class AuthFactory:
    def strict(self, roles):
        return Auth(roles, False)

    def liberal(self):
        return Auth("*", True)


class AuthDecoratorFactory:
    def __init__(self, auth_service):
        self.auth_service = auth_service

    def decorate(self, handler, policy):
        return AuthDecorator(self.auth_service, policy, handler)


class AuthDecorator:
    def __init__(self, auth_service, policy, decoratee):
        self.auth_service = auth_service
        self.policy = policy
        self.decoratee = decoratee

    async def handle(self, request, *args, principal=None):
        auth_header = request.headers.get("Authorization")
        try:
            user = await self.auth_service.authenticate(
                auth_header, self.policy.allow_anonymous)
            await self.auth_service.authorize(user, self.policy.roles)
        except UnauthenticatedException:

            response = {"status_code": 401, "body": {}}
            return JSONResponse(
                content=response["body"],
                status_code=response["status_code"]
            )

        except UnauthorizedException:
            response = {
                "status_code": 403,
                "body": {"message": "access_not_allowed"},
            }

            return JSONResponse(
                content=response["body"],
                status_code=response["status_code"]
            )
        return await self.decoratee.handle(*args, principal=user)
