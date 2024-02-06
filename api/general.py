from fastapi import APIRouter

router = APIRouter()


@router.get("/health_check", tags=["general"])
async def ping():
    return {"message": "Healthy"}
