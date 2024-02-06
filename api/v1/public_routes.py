from typing import Annotated

from fastapi import APIRouter, Query, Request

from models.base_model import PyObjectId

from models.mlo import (
    PublicMLOOut,
    PublicMLOWebAppInfoOut,
)
from structure import structure

router = APIRouter(tags=["public"], prefix="/v1")


@router.get("/public/mlos/{web_app_id}", response_model=PublicMLOOut)
async def get_mlo_web_app(web_app_id: str, request: Request) -> PublicMLOOut | None:
    handler = structure.instantiate("get_mlo_web_app_auth_handler")
    return await handler.handle(request, web_app_id)


@router.get("/public/mlos/{mlo_id}/web_app_info", response_model=PublicMLOWebAppInfoOut)
async def get_web_app_info(mlo_id: PyObjectId, request: Request):
    handler = structure.instantiate("get_mlo_web_app_info_auth_handler")
    return await handler.handle(request, mlo_id)


@router.get("/public/nearest_mlo", response_model=None)
async def find_nearest_mlo(
        request: Request,
        zip_code: Annotated[str, Query(max_length=7)]) -> None:
    handler = structure.instantiate("find_nearest_mlo_auth_handler")
    return await handler.handle(request, zip_code)
