from pydantic import BaseModel, Field, field_serializer, ConfigDict

from models.base_model import PydanticObjectId, PyObjectId


class BaseGame(BaseModel):
    steam_id: int
    name: str
    header_image: str | None = Field(pattern=r"^(http(s?)):\/\/.+\..+$")
    url: str | None = Field(pattern=r"^(http(s?)):\/\/.+\..+$")


class GameIn(BaseGame):
    ...


class GameUpdate(BaseGame):
    ...


# class RatedGame(BaseGame):
#     id: PydanticObjectId = Field(...)
#     user_id: PyObjectId = Field(...)
#     rating: int
#
#     @field_serializer("id", check_fields=False)
#     def serialize_id(self, v, _info):
#         return str(v)


class GameOut(BaseGame):
    id: PydanticObjectId = Field(...)

    @field_serializer("id", check_fields=False)
    def serialize_id(self, v, _info):
        return str(v)


class Game(BaseGame):
    model_config = ConfigDict(from_attributes=True)

    id: PydanticObjectId | None = Field(None, alias="_id")

    def assign_request(self, updated_game: GameUpdate):
        self.name = updated_game.name
        self.url = updated_game.url
        self.header_image = updated_game.header_image
