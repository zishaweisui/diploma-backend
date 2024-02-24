from fastapi import APIRouter, Request

from models.base_model import PyObjectId
from models.game import GameOut
from structure import structure

router = APIRouter(tags=["recommendation"], prefix="/v1")


@router.get("/recommendation", response_model=list[GameOut])
async def get_recommendation(user_id: PyObjectId, request: Request) -> list[GameOut] | None:
    handler = structure.instantiate("get_game_recommendation_auth_handler")
    return await handler.handle(request, user_id)
