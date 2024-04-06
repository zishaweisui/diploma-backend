from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_serializer

from models.base_model import PydanticObjectId
from models.profile import Profile
from models.token_pairs import TokenPair


class BaseUser(BaseModel):
    role: str | None = Field(None)
    email: EmailStr
    profile: Profile | None
    nickname: str


class UserUpdate(BaseUser):
    ...


class UserIn(BaseUser):
    password: str = Field(..., min_length=6)


class UserOut(BaseUser):
    id: PydanticObjectId = Field(...)

    @field_serializer("id", check_fields=False)
    def serialize_id(self, v, _info):
        return str(v)


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: PydanticObjectId | None = Field(None, alias="_id")
    role: str = Field(...)
    email: str = Field(...)
    nickname: str
    profile: Profile | None
    password_hash: bytes | None = None
    token_pairs: list[TokenPair] | None = None

    def assign_request(self, model: UserUpdate):
        self.email = model.email
        self.nickname = model.nickname
        self.profile.first_name = model.profile.first_name
        self.profile.last_name = model.profile.last_name
