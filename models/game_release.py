from pydantic import BaseModel, Field, field_serializer
from typing import List

from models.base_model import PydanticObjectId


class Publisher(BaseModel):
    name: str | None


class GameRelease(BaseModel):
    id: PydanticObjectId | None = Field(None, alias="_id")
    release_date: str | None
    distribution_type: str | None
    name: str | None
    region: str | None
    platform: str | None
    publishers: List[Publisher] | None
    image_url: str | None


class GameReleaseOut(GameRelease):
    id: PydanticObjectId = Field(...)

    @field_serializer("id", check_fields=False)
    def serialize_id(self, v, _info):
        return str(v)
