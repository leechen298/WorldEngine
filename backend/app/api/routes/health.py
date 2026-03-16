from fastapi import APIRouter

from app.schemas.api import ApiResponse
from app.schemas.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=ApiResponse[HealthResponse])
def health() -> ApiResponse[HealthResponse]:
    return ApiResponse(
        data=HealthResponse(status="ok", service="worldengine-backend"),
    )
