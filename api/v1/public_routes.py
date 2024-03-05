from typing import Annotated

from fastapi import APIRouter, Query, Request

from models import UserIn
from models.base_model import PyObjectId
from models.game import GameOut
from models.page import GamePaging, GamesPageOut, GameFiltering
from models.user import UserOut
from structure import structure

router = APIRouter(tags=["public"], prefix="/v1")


@router.post("/signup", response_model=UserOut)
async def create_user(user: UserIn, request: Request) -> UserOut:
    handler = structure.instantiate("create_user_auth_handler")
    return await handler.handle(request, user)


@router.get("/public/games/{game_id}", response_model=GameOut)
async def get_public_game(game_id: PyObjectId, request: Request) -> GameOut | None:
    handler = structure.instantiate("get_game_auth_handler")
    return await handler.handle(request, game_id)


@router.get("/public/games", response_model=GamesPageOut)
async def get_games_page(
        request: Request,
        page_size: Annotated[int | None, Query()] = None,
        page: Annotated[int | None, Query()] = None,
        query: Annotated[str | None, Query(max_length=50)] = None,
):
    filtering = GameFiltering(query=query)
    paging = GamePaging(page_size=page_size, page=page, filtering=filtering)
    handler = structure.instantiate("get_games_page_auth_handler")
    return await handler.handle(request, paging)
