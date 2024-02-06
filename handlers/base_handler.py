from fastapi.responses import JSONResponse

from infrastructure_exceptions import (
    InvalidRequestException,
    NotFoundException,
    NotImplementedException,
    ThirdPartyServiceException,
    UnauthenticatedException,
    UnauthorizedException,
)


class BaseHandler:
    def __init__(self, service, presenter) -> None:
        self.service = service
        self.presenter = presenter

    async def execute(self, principal, handler_function, *args, **kwargs):
        try:
            kwargs["principal"] = principal
            result = await handler_function(*args, **kwargs)
        except InvalidRequestException as e:
            response = {"status_code": 400, "body": e.errors}
        except NotFoundException:
            response = {"status_code": 404, "body": {}}
        except UnauthorizedException:
            response = {
                "status_code": 403,
                "body": {"message": "access_not_allowed"},
            }
        except UnauthenticatedException:
            response = {"status_code": 401, "body": {}}
        except ThirdPartyServiceException as e:
            response = {
                "status_code": 503,
                "body": e.errors
            }
        except NotImplementedException:
            response = {
                "status_code": 500,
                "body": {"message": "Something went wrong"}
            }
        else:
            return result
        return JSONResponse(
            content=response["body"],
            status_code=response["status_code"]
        )
