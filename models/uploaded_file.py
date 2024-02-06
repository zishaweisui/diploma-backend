from pydantic import BaseModel, Field


class UploadedFile(BaseModel):
    filename: str = Field(...)
    path: str = Field(...)


class SharedUploadedFile(UploadedFile):
    link: str | None = Field(None)

