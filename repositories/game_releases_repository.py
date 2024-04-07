from bson.objectid import ObjectId

from models.game_release import GameRelease

from .base_repository import BaseRepository


class GameReleasesRepository(BaseRepository):
    async def get(self, game_release_id: ObjectId) -> GameRelease | None:
        data = await self.collection.find_one({"_id": game_release_id})
        return self.translator.from_document(data) if data else None

