from typing import Annotated

from fastapi import APIRouter, Query, Request

from models.game import GameOut
from models.page import Paging, GamesPageOut
from structure import structure

router = APIRouter(tags=["public"], prefix="/v1")


@router.get("/public/games/{game_id}", response_model=GameOut)
async def get_public_game(game_id: str, request: Request) -> GameOut | None:
    handler = structure.instantiate("get_game_auth_handler")
    return await handler.handle(request, game_id)


@router.get("/public/games", response_model=GamesPageOut)
async def get_games_page(
        request: Request,
        page_size: Annotated[int | None, Query()] = None,
        page: Annotated[int | None, Query()] = None,
        game_name: Annotated[str | None, Query(max_length=50)] = None,
):
    paging = Paging(page_size=page_size, page=page, game_name=game_name)
    handler = structure.instantiate("get_games_page_auth_handler")
    return await handler.handle(request, paging)
