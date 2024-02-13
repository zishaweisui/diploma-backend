from pydantic import BaseModel
#
# from models.mlo import MLOStatus
#
#
# class MLOFiltering(BaseModel):
#     query: str | None
#     status: str | None
#     query_targets: tuple = ("name", "nmls_license", "zip_code")
#     excluded_statuses: tuple = ("all", MLOStatus.PROSPECT)
#
#     def build_pipeline(self) -> list:
#         pipeline = [{"$match": {"status": {"$ne": MLOStatus.PROSPECT}}}]
#         if self.query:
#             or_targets = [
#                 {target: {"$regex": self.query, "$options": "i"}}
#                 for target
#                 in self.query_targets
#             ]
#             pipeline.append({"$match": {"$or": or_targets}})
#         if self.status and self.status not in self.excluded_statuses:
#             pipeline.append({"$match": {"status": self.status}})
#         return pipeline


class GameFiltering(BaseModel):
    def build_pipeline(self):
        ...
