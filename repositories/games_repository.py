from bson.objectid import ObjectId

from models.game import Game

from .base_repository import BaseRepository


class GamesRepository(BaseRepository):
    async def get(self, game_id: ObjectId) -> Game | None:
        game_data = await self.collection.find_one({"_id": game_id})
        return self.translator.from_document(game_data) if game_data else None

    async def get_by_name(self, game_name: str) -> Game | None:
        game_data = await self.collection.find_one({"name": game_name})
        return self.translator.from_document(game_data) if game_data else None

    async def update(self, updated_game: Game) -> None:
        document = self.translator.to_document(updated_game)
        await self.collection.update_one({"_id": updated_game.id}, {"$set": document})

    async def delete(self, game_id: ObjectId) -> None:
        await self.collection.delete_one({"_id": game_id})

    async def find_by_steam_id(self, steam_id: int) -> Game | None:
        game_data = await self.collection.find_one({"steam_id": steam_id})
        return self.translator.from_document(game_data) if game_data else None
