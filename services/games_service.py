from bson.objectid import ObjectId

from infrastructure_exceptions import InvalidRequestException, NotFoundException
from models.game import Game, GameIn, GameUpdate
from models.page import Page


class GamesService:
    def __init__(self, page_service, repository):
        self.page_service = page_service
        self.repository = repository

    async def create_game(self, model: GameIn, principal=None) -> Game:
        existing_game = await self.repository.find_by_steam_id(model.steam_id)
        if existing_game:
            error = {
                "game": [
                    {"message": "Game already in DB", "key": "error_already_exists"}
                ]
            }
            raise InvalidRequestException(error)
        game = Game.model_validate(model)
        game.id = await self.repository.create(game)
        return game

    async def get_game(self, game_id: ObjectId, principal=None) -> Game:
        game = await self.repository.get(game_id)
        return game

    async def get_game_by_name(self, game_name: str, principal=None) -> Game:
        game = await self.repository.get_by_name(game_name)
        return game

    async def get_games(self, principal=None) -> list[Game]:
        return await self.repository.get_list()

    async def update_game(self, game_id: ObjectId, updated_game: GameUpdate, principal=None) -> Game:
        game = await self.__get_game(game_id)
        game_collision = await self.repository.find_by_steam_id(updated_game.steam_id)
        if game_collision and game_collision.id != game_id:
            error = {
                "game": [
                    {"message": "Wrong Steam Id for existing game", "key": "error_wrong_id"}
                ]
            }
            raise InvalidRequestException(error)
        game.assign_request(updated_game)
        await self.repository.update(game)
        return game

    async def delete_game(self, game_id: ObjectId, principal=None) -> None:
        await self.__get_game(game_id)
        await self.repository.delete(game_id)

    async def __get_game(self, game_id: ObjectId):
        game = await self.repository.get(game_id)
        if not game:
            raise NotFoundException
        return game

    async def get_page(self, paging, principal=None) -> Page:
        return await self.page_service.get_page(
            paging,
            self.repository.get_page,
            self.repository.count,
            paging.filtering
        )

    async def upload_file(self, file):
        ...
