from typing import Annotated

from fastapi import APIRouter, Query, Request, UploadFile

from models.base_model import PyObjectId
from models.filtering import MLOFiltering
from models.mlo import (
    MLOCount,
    MLOIn,
    MLOOut,
    MLOStatusIn,
    MLOUpdate,
)
from models.page import MLOPaging, MLOsPageOut
from models.uploaded_file import SharedUploadedFile
from structure import structure

router = APIRouter(tags=["mlos"], prefix="/v1")


@router.get("/mlos/count", response_model=MLOCount)
async def get_count(
        request: Request,
        status: Annotated[str | None, Query(max_length=15)] = None,
        query: Annotated[str | None, Query(max_length=50)] = None):
    filtering = MLOFiltering(status=status, query=query)
    handler = structure.instantiate("get_mlo_count_auth_handler")
    return await handler.handle(request, filtering)


@router.post("/mlos", response_model=MLOOut)
async def create_mlo(mlo: MLOIn, request: Request) -> MLOOut:
    handler = structure.instantiate("create_mlo_auth_handler")
    return await handler.handle(request, mlo)


@router.get("/mlos/{mlo_id}", response_model=MLOOut)
async def get_mlo(mlo_id: PyObjectId, request: Request) -> MLOOut | None:
    handler = structure.instantiate("get_mlo_auth_handler")
    return await handler.handle(request, mlo_id)


@router.put("/mlos/{mlo_id}", response_model=MLOOut)
async def update_mlo(mlo_id: PyObjectId, updated_mlo: MLOUpdate, request: Request):
    handler = structure.instantiate("update_mlo_auth_handler")
    return await handler.handle(request, mlo_id, updated_mlo)


@router.delete("/mlos/{mlo_id}", response_model=None)
async def delete_mlo(mlo_id: PyObjectId, request: Request) -> None:
    handler = structure.instantiate("delete_mlo_auth_handler")
    return await handler.handle(request, mlo_id)


@router.get("/mlos", response_model=MLOsPageOut)
async def get_mlos_page(
        request: Request,
        page_size: Annotated[int | None, Query()] = None,
        page: Annotated[int | None, Query()] = None,
        status: Annotated[str | None, Query(max_length=15)] = None,
        query: Annotated[str | None, Query(max_length=50)] = None,
):
    filtering = MLOFiltering(status=status, query=query)
    paging = MLOPaging(page_size=page_size, page=page, filtering=filtering)
    handler = structure.instantiate("get_mlos_page_auth_handler")
    return await handler.handle(request, paging)


@router.post("/mlos/files", response_model=SharedUploadedFile)
async def upload_file(request: Request, file: UploadFile):
    handler = structure.instantiate("upload_mlo_file_auth_handler")
    return await handler.handle(request, file)


@router.post("/mlos/{mlo_id}/headshot", response_model=SharedUploadedFile)
async def upload_headshot(mlo_id: PyObjectId, request: Request, file: UploadFile):
    handler = structure.instantiate("upload_mlo_headshot_auth_handler")
    return await handler.handle(request, mlo_id, file)


@router.put("/mlos/{mlo_id}/status", response_model=MLOOut)
async def change_mlo_status(
        mlo_id: PyObjectId, status: MLOStatusIn, request: Request):
    handler = structure.instantiate("change_mlo_status_auth_handler")
    return await handler.handle(request, mlo_id, status)
