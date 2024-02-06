from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_serializer

from models.base_model import PydanticObjectId
from models.profile import Profile
from models.token_pairs import TokenPair


class BaseUser(BaseModel):
    role: str = Field(...)
    roles: list[str] = Field(...)
    email: EmailStr
    profile: Profile

    def get_roles(self):
        return [self.role, *self.roles]


class UserUpdate(BaseUser):
    password: str | None = Field(None, min_length=6)


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
    roles: list[str] = Field(...)
    email: str = Field(...)
    profile: Profile
    password_hash: bytes | None = None
    token_pairs: list[TokenPair] | None = None

    def assign_request(self, model: UserIn):
        self.email = model.email
        self.profile = model.profile
