from pydantic import BaseModel, Field, field_validator

from models.filtering import UserFiltering
from models.user import UserOut


class Page(BaseModel):
    items: list
    page: int = Field(None, ge=1)
    page_count: int = Field(None, ge=1)


class BasePaging(BaseModel):
    page: int | None = 1
    page_size: int | None = 60

    @field_validator("page")
    def set_page(cls, page):
        return page or 1

    @field_validator("page_size")
    def set_page_size(cls, page_size):
        return page_size or 60


class Paging(BasePaging):
    role: str | None


class UserPaging(Paging):
    filtering: UserFiltering


class BasePageOut(BaseModel):
    items: list[UserOut]
    page: int = Field(None, ge=1)
    page_count: int = Field(None, ge=1)


class UsersPageOut(BasePageOut):
    items: list[UserOut]
