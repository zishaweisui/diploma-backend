from typing import Annotated

from fastapi import APIRouter, Query, Request, UploadFile

from models import SharedUploadedFile
from models.base_model import PyObjectId
from models.page import UserPaging, UsersPageOut
from models.filtering import UserFiltering
from models.token_pairs import TokenPairOut
from models.user import UserOut, UserUpdate
from models.password import UpdatePassword
from structure import structure

router = APIRouter(tags=["users"], prefix="/v1")


@router.get("/users/{user_id}", response_model=UserOut)
async def get_user(user_id: PyObjectId, request: Request) -> UserOut | None:
    handler = structure.instantiate("get_user_auth_handler")
    return await handler.handle(request, user_id)


@router.get("/all_users", response_model=list[UserOut])
async def get_all_users(request: Request) -> list[UserOut]:
    handler = structure.instantiate("get_users_auth_handler")
    return await handler.handle(request)


@router.put("/users/{user_id}", response_model=UserOut)
async def update_user(user_id: PyObjectId, updated_user: UserUpdate, request: Request) -> UserOut:
    handler = structure.instantiate("update_user_auth_handler")
    return await handler.handle(request, user_id, updated_user)


@router.delete("/users/{user_id}", response_model=None)
async def delete_user(user_id: PyObjectId, request: Request) -> None:
    handler = structure.instantiate("delete_user_auth_handler")
    return await handler.handle(request, user_id)


@router.get("/me", response_model=UserOut)
async def get_me(request: Request) -> UserOut:
    handler = structure.instantiate("get_me_auth_handler")
    return await handler.handle(request)


@router.get("/users", response_model=UsersPageOut)
async def get_users_page(
        request: Request,
        page_size: Annotated[int | None, Query()] = None,
        page: Annotated[int | None, Query()] = None,
        role: Annotated[str | None, Query(max_length=50)] = None,
        query: Annotated[str | None, Query(max_length=100)] = None,
):
    filtering = UserFiltering(query=query)
    paging = UserPaging(page_size=page_size, page=page, role=role, filtering=filtering)
    handler = structure.instantiate("get_users_page_auth_handler")
    return await handler.handle(request, paging)


@router.post("/users/{user_id}/change_password", response_model=TokenPairOut)
async def change_password(user_id: PyObjectId, updated_password: UpdatePassword, request: Request) -> TokenPairOut:
    handler = structure.instantiate("change_password_auth_handler")
    return await handler.handle(request, user_id, updated_password)


# @router.post("/users/files", response_model=SharedUploadedFile)
# async def upload_file(request: Request, file: UploadFile):
#     handler = structure.instantiate("upload_user_file_auth_handler")
#     return await handler.handle(request, file)
