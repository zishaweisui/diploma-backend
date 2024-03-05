from pydantic import BaseModel, ConfigDict, Field, field_serializer

from models.base_model import PydanticObjectId


class BaseGame(BaseModel):
    steam_id: int
    name: str
    header_image: str | None = Field(pattern=r"^(http(s?)):\/\/.+\..+$")
    developer: str | None = None
    publisher: str | None = None
    genres: list[str] | None = None


class GameIn(BaseGame):
    ...


class GameUpdate(BaseGame):
    ...


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
        self.header_image = updated_game.header_image
        self.developer = updated_game.developer
        self.publisher = updated_game.publisher
        self.genres = updated_game.genres
