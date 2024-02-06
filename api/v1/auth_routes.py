from fastapi import APIRouter, Request

from models.login import LoginRequest, RefreshTokenRequest
from models.token_pairs import TokenPairOut
from structure import structure

router = APIRouter(tags=["auth"], prefix="/v1")


@router.post("/auth/login", response_model=TokenPairOut)
async def create_token(login_request: LoginRequest) -> TokenPairOut:
    handler = structure.instantiate("login_handler")
    return await handler.handle(login_request)


@router.post("/auth/refresh", response_model=TokenPairOut)
async def refresh_token(refresh_request: RefreshTokenRequest) -> TokenPairOut:
    handler = structure.instantiate("refresh_handler")
    return await handler.handle(refresh_request)


@router.post("/auth/logout", response_model=None)
async def remove_token(request: Request) -> None:
    handler = structure.instantiate("logout_auth_handler")
    auth_headers = request.headers.get("Authorization")
    return await handler.handle(request, auth_headers)
