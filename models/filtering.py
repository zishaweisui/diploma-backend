from pydantic import BaseModel


class UserFiltering(BaseModel):
    query: str | None
    query_targets: tuple = ("name", "email", "nickname")

    def build_pipeline(self) -> list:
        pipeline = [{"$match": {"role": {"$ne": "admin"}}}]
        if self.query:
            or_targets = [
                {target: {"$regex": self.query, "$options": "i"}}
                for target
                in self.query_targets
            ]
            pipeline.append({"$match": {"$or": or_targets}})
        return pipeline


class GameFiltering(BaseModel):
    query: str | None
    query_targets: tuple = ("name", "genre", "developer", "publisher")

    def build_pipeline(self) -> list:
        pipeline = [{"$match": {}}]
        if self.query:
            or_targets = [
                {target: {"$regex": self.query, "$options": "i"}}
                for target
                in self.query_targets
            ]
            pipeline.append({"$match": {"$or": or_targets}})
        return pipeline
