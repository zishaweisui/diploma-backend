import re
from enum import StrEnum, auto

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_serializer

from models.base_model import PydanticObjectId, PyObjectId
from models.uploaded_file import UploadedFile, SharedUploadedFile


class BaseMLO(BaseModel):
    first_name: str = Field(..., min_length=1)
    last_name: str = Field(..., min_length=1)
    headshot: UploadedFile | None = Field(None)
    phone_number: str = Field(...)
    website: str | None = Field(pattern=r"^(http(s?)):\/\/.+\..+$")
    email: EmailStr
    nmls_license: str = Field(...)
    zip_code: str | None = Field(None)
    web_app_id: str | None = Field(None)
    app_deep_link: str | None = Field(None)

    def get_files(self):
        files = []
        if self.headshot:
            files.append(self.headshot)
        return files


class MLOOut(BaseMLO):
    id: PydanticObjectId = Field(...)
    status: str = Field(...)
    headshot: SharedUploadedFile | None = Field(None)

    @field_serializer("id", check_fields=False)
    def serialize_id(self, v, _info):
        return str(v)


class PublicMLOOut(BaseModel):
    id: PydanticObjectId = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    phone_number: str = Field(...)
    website: str | None = Field(...)
    headshot: SharedUploadedFile | None = Field(None)

    @field_serializer("id", check_fields=False)
    def serialize_id(self, v, _info):
        return str(v)


class PublicMLOHeadshotOut(BaseModel):
    headshot: SharedUploadedFile | None = Field(None)


class MLOStatus(StrEnum):
    PUBLISHED = "published"
    UNPUBLISHED = "unpublished"
    DRAFT = "draft"
    PROSPECT = auto()


class MLOIn(BaseMLO):
    status: MLOStatus | None = MLOStatus.PROSPECT
    theme_id: PyObjectId = Field(...)

    def generate_web_app_id(self) -> str:
        concatenated_field = f"{self.first_name.lower()}{self.last_name.lower()}-{self.nmls_license}"
        return re.sub(r"[^a-zA-Z0-9-]", "", concatenated_field)


class MLOUpdate(BaseMLO):
    theme_id: PyObjectId = Field(...)


class MLO(BaseMLO):
    model_config = ConfigDict(from_attributes=True)

    id: PydanticObjectId | None = Field(None, alias="_id")
    status: MLOStatus = Field(...)
    web_app_id: str | None = Field(None)
    app_deep_link: str | None = Field(None)
    theme_id: PyObjectId = Field(...)

    def assign_request(self, updated_mlo: MLOUpdate):
        self.first_name = updated_mlo.first_name
        self.last_name = updated_mlo.last_name
        self.phone_number = updated_mlo.phone_number
        self.email = updated_mlo.email
        self.website = updated_mlo.website
        self.nmls_license = updated_mlo.nmls_license
        self.zip_code = updated_mlo.zip_code
        self.theme_id = updated_mlo.theme_id
        self.web_app_id = updated_mlo.web_app_id


class QRcodeMLO(MLO):
    model_config = ConfigDict(from_attributes=True)
    id: PydanticObjectId = Field(...)

    @field_serializer("id", check_fields=False)
    def serialize_id(self, v, _info):
        return str(v)


class MLOStatusIn(BaseModel):
    status: MLOStatus


class MLOCount(BaseModel):
    count: int = Field(...)


class PublicMLOWebAppInfo(BaseModel):
    url: str = Field(...)


class PublicMLOWebAppInfoOut(BaseModel):
    url: str = Field(...)


class MLOProspect(BaseModel):
    email: EmailStr
    nmls_license: str
    zip_code: str
