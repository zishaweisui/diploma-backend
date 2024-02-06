from pydantic import BaseModel, Field

from .base_model import PyObjectId


class TokenPair(BaseModel):
    id: PyObjectId = Field(...)
    access_token: str
    refresh_token: str


class TokenPairOut(BaseModel):
    access_token: str
    refresh_token: str
