from bson.objectid import ObjectId

from models.user import User

from .base_repository import BaseRepository


class UsersRepository(BaseRepository):
    async def get(self, user_id: ObjectId) -> User | None:
        user_data = await self.collection.find_one({"_id": user_id})
        return self.translator.from_document(user_data) if user_data else None

    async def update(self, updated_user: User) -> None:
        document = self.translator.to_document(updated_user)
        await self.collection.update_one({"_id": updated_user.id}, {"$set": document})

    async def delete(self, user_id: ObjectId) -> None:
        await self.collection.delete_one({"_id": user_id})

    async def get_page(self, skip, limit, role):
        sort_step = {"$sort": {"_id": -1}}
        match_step = {"$match": {}}
        limit_step = {"$limit": limit}
        skip_step = {"$skip": skip}
        if role:
            match_step["$match"] = {"role": role}
        pipeline = [match_step, sort_step, skip_step, limit_step]
        return await self._find_by_aggregation(pipeline)

    async def count(self, role):
        find_filter = {}
        if role:
            find_filter["role"] = role
        pipeline = [
            {"$match": find_filter}
        ]
        return await self._count_by_aggregation(pipeline)

    async def find_by_email(self, email: str) -> User | None:
        user_data = await self.collection.find_one({"email": email})
        return self.translator.from_document(user_data) if user_data else None
