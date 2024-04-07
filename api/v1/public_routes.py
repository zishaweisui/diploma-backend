from fastapi import APIRouter, Request

from models import UserIn
from models.base_model import PyObjectId
from models.game import GameOut
from models.game_release import GameReleaseOut
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


@router.get("/public/games", response_model=list[GameOut])
async def get_public_games(request: Request) -> list[GameOut]:
    handler = structure.instantiate("get_public_games_auth_handler")
    return await handler.handle(request)


@router.get("/public/games_releases", response_model=list[GameReleaseOut])
async def get_public_games_releases(request: Request) -> list[GameReleaseOut]:
    handler = structure.instantiate("get_public_games_releases_auth_handler")
    return await handler.handle(request)
