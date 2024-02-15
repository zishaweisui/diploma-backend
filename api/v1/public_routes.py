from typing import Annotated

from fastapi import APIRouter, Query, Request

from models.game import GameOut
from structure import structure

router = APIRouter(tags=["public"], prefix="/v1")


@router.get("/public/games/{game_id}", response_model=GameOut)
async def get_public_game(game_id: str, request: Request) -> GameOut | None:
    handler = structure.instantiate("get_public_game_auth_handler")
    return await handler.handle(request, game_id)


@router.get("/public/games", response_model=None)
async def get_games_page(
        request: Request,
        game_name: Annotated[str, Query(max_length=50)]) -> None:
    handler = structure.instantiate("get_games_page_auth_handler")
    return await handler.handle(request, game_name)
