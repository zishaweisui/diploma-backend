from fastapi import APIRouter, Request

from models.base_model import PyObjectId
from models.game import GameIn, GameOut, GameUpdate
from structure import structure

router = APIRouter(tags=["games"], prefix="/v1")


@router.post("/games", response_model=GameOut)
async def create_game(game: GameIn, request: Request) -> GameOut:
    handler = structure.instantiate("create_game_auth_handler")
    return await handler.handle(request, game)


@router.put("/games/{game_id}", response_model=GameOut)
async def update_game(game_id: PyObjectId, updated_game: GameUpdate, request: Request) -> GameOut:
    handler = structure.instantiate("update_game_auth_handler")
    return await handler.handle(request, game_id, updated_game)


@router.delete("/games/{game_id}", response_model=None)
async def delete_game(game_id: PyObjectId, request: Request) -> None:
    handler = structure.instantiate("delete_game_auth_handler")
    return await handler.handle(request, game_id)
