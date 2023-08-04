from fastapi import APIRouter
from starlette import status

from fastchat.schemas import PingResponse


router = APIRouter(
    prefix="/health_check",
    tags=["Application Health"],
)


@router.get(
    "/ping_application",
    response_model=PingResponse,
    status_code=status.HTTP_200_OK,
)
async def ping_application() -> dict:
    return {"message": "Application worked!"}
