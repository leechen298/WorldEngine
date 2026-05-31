"""World generation API routes."""

from fastapi import APIRouter

from app.core.world_generation import (
    check_runtime_readiness,
    preview_generation,
    regenerate_world,
)
from app.schemas.api import ApiResponse
from app.schemas.world_generation import (
    GenerationPreviewRequest,
    GenerationPreviewResponse,
    GenerationRegenerationRequest,
    GenerationRegenerationResult,
    RuntimeReadinessRequest,
    RuntimeReadinessResult,
)

router = APIRouter(prefix="/world/generation", tags=["world-generation"])


@router.post("/preview", response_model=ApiResponse[GenerationPreviewResponse])
def preview_world_generation(
    request_body: GenerationPreviewRequest,
) -> ApiResponse[GenerationPreviewResponse]:
    return ApiResponse(data=preview_generation(request_body))


@router.post("/regenerate", response_model=ApiResponse[GenerationRegenerationResult])
def regenerate_world_generation(
    request_body: GenerationRegenerationRequest,
) -> ApiResponse[GenerationRegenerationResult]:
    return ApiResponse(data=regenerate_world(request_body))


@router.post("/runtime-readiness", response_model=ApiResponse[RuntimeReadinessResult])
def check_world_generation_runtime_readiness(
    request_body: RuntimeReadinessRequest,
) -> ApiResponse[RuntimeReadinessResult]:
    return ApiResponse(data=check_runtime_readiness(request_body))
