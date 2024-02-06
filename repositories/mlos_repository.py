from bson.objectid import ObjectId

from models.filtering import MLOFiltering
from models.mlo import MLO, MLOStatus

from .base_repository import BaseRepository


class MLOsRepository(BaseRepository):
    def __init__(self, collection, translator, indexes, file_translator):
        super().__init__(collection, translator, indexes)
        self.file_translator = file_translator

    async def get(self, mlo_id: ObjectId) -> MLO | None:
        mlo_data = await self.collection.find_one({"_id": mlo_id})
        return self.translator.from_document(mlo_data) if mlo_data else None

    async def update(self, updated_mlo: MLO) -> None:
        document = self.translator.to_document(updated_mlo)
        await self.collection.update_one({"_id": updated_mlo.id}, {"$set": document})

    async def delete(self, mlo_id: ObjectId) -> None:
        await self.collection.delete_one({"_id": mlo_id})

    async def __concat_name_step(self) -> list:
        return [
            {
                "$addFields": {
                    "name": {
                        "$concat": [
                            {
                                "$ifNull": [
                                    "$first_name",
                                    ""
                                ]
                            },
                            " ",
                            {
                                "$ifNull": [
                                    "$last_name",
                                    ""
                                ]
                            }
                        ]
                    }
                }
            }
        ]

    async def get_page(self, skip, limit, filtering: MLOFiltering):
        sort_step = {"$sort": {"_id": -1}}
        filtering_pipeline = filtering.build_pipeline()
        if not filtering_pipeline:
            filtering_pipeline = [{"$match": {}}]
        concat_step = await self.__concat_name_step()
        limit_step = {"$limit": limit}
        skip_step = {"$skip": skip}
        detailed_location_step = [
            {
                "$lookup": {
                    "from": "locations",
                    "localField": "zip_code",
                    "foreignField": "zip_code",
                    "as": "location"
                }
            }, {
                "$unwind": {
                    "path": "$location",
                    "preserveNullAndEmptyArrays": True
                }
            }
        ]
        pipeline = [*concat_step, *filtering_pipeline, sort_step,
                    skip_step, limit_step, *detailed_location_step]
        return await self._find_by_aggregation(pipeline)

    # async def _find_detailed_by_aggregation(self, pipeline) -> list:
    #     return [
    #         self.detailed_translator.from_document(d)
    #         async for d
    #         in self.collection.aggregate(pipeline)
    #     ]

    async def count(self, filtering: MLOFiltering):
        pipeline = filtering.build_pipeline()
        if not pipeline:
            pipeline = [{"$match": {}}]
        concat_step = await self.__concat_name_step()
        return await self._count_by_aggregation([*concat_step, *pipeline])

    async def find_by_email(self, email: str) -> MLO | None:
        document = await self.collection.find_one({"email": email})
        return self.translator.from_document(document) if document else None

    async def find_strict_by_email(self, raw_email: str) -> MLO | None:
        email = raw_email.strip()
        document = await self.collection.find_one(
            {"email": {"$regex": f"^{email}", "$options": "i"}}
        )
        return self.translator.from_document(document) if document else None

    async def find_by_nmls(self, license_number: str) -> MLO | None:
        mlo_data = await self.collection.find_one({"nmls_license": license_number})
        return self.translator.from_document(mlo_data) if mlo_data else None

    async def find_by_web_app_id(self, web_app_id: str) -> MLO | None:
        mlo_data = await self.collection.find_one(
            {"web_app_id": {"$regex": f"{web_app_id}$", "$options": "i"}}
        )
        return self.translator.from_document(mlo_data) if mlo_data else None

    async def change_headshot(self, mlo_id: ObjectId, uploaded_file):
        return await self.collection.update_many(
            {"_id": mlo_id},
            {"$set": {"headshot": self.file_translator.to_document(uploaded_file)}}
        )

    async def change_status(self, mlo_id: ObjectId, status: MLOStatus):
        await self.collection.update_one(
            {"_id": mlo_id},
            {"$set": {"status": status}}
        )
