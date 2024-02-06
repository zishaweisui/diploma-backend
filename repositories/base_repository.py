class BaseRepository:
    def __init__(self, collection, translator, indexes) -> None:
        self.collection = collection
        self.translator = translator
        self.indexes = indexes

    async def get_list(self):
        pipeline = [
            {"$match": {}}
        ]
        return await self._find_by_aggregation(pipeline)

    async def create(self, model):
        document = self.translator.to_document(model)
        document.pop("_id", None)
        document.pop("id", None)
        result = await self.collection.insert_one(document)
        return result.inserted_id

    async def _count_by_aggregation(self, pipeline) -> int:
        group_step = {"$group": {"_id": None, "count": {"$sum": 1}}}
        project_step = {"$project": {"_id": 0}}

        pipeline = [*pipeline, group_step, project_step]
        result = [item.get("count") async for item in self.collection.aggregate(pipeline)]
        if not result:
            return 0
        return result[0]

    async def _find_by_aggregation(self, pipeline) -> list:
        return [
            self.translator.from_document(d)
            async for d
            in self.collection.aggregate(pipeline)
        ]

    async def configure_indexes(self):
        if not self.indexes or not isinstance(self.indexes, list):
            return
        existing_indexes = await self.collection.index_information()
        new_indexes = [
            index
            for index in self.indexes
            if index not in existing_indexes
        ]
        if new_indexes:
            await self.collection.create_indexes(new_indexes)
