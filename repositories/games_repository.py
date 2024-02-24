from bson.objectid import ObjectId

from models.filtering import GameFiltering
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

    async def get_page(self, skip, limit, filtering: GameFiltering):
        filtering_pipeline = filtering.build_pipeline()
        if not filtering_pipeline:
            filtering_pipeline = [{"$match": {}}]
        sort_step = {"$sort": {"_id": -1}}
        limit_step = {"$limit": limit}
        skip_step = {"$skip": skip}
        pipeline = [*filtering_pipeline, sort_step, skip_step, limit_step]
        return await self._find_by_aggregation(pipeline)

    async def count(self, filtering: GameFiltering):
        pipeline = filtering.build_pipeline()
        if not pipeline:
            pipeline = [{"$match": {}}]
        return await self._count_by_aggregation(pipeline)

    async def find_by_steam_id(self, steam_id: int) -> Game | None:
        game_data = await self.collection.find_one({"steam_id": steam_id})
        return self.translator.from_document(game_data) if game_data else None
