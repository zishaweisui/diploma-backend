from pydantic import BaseModel, Field


class Profile(BaseModel):
    first_name: str = Field(..., min_length=1)
    last_name: str = Field(..., min_length=1)
