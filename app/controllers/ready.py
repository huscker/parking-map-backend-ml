from fastapi import APIRouter
from views import ReadyResponse


router = APIRouter()


@router.get(
    "/ready",
    tags=["ready"],
    response_model=ReadyResponse,
    summary="Simple health check.",
    status_code=200
)
async def ready_check():
    return ReadyResponse(status="ok")
