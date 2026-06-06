"""World generation API routes."""

from fastapi import APIRouter

from app.agent.provider_config import provider_readiness_from_env
from app.agent.worldview_generation import generate_worldview_response
from app.core.world_generation import (
    check_core_readiness,
    check_runtime_readiness,
    preview_generation,
    regenerate_world,
)
from app.schemas.api import ApiResponse
from app.schemas.world_generation import (
    GenerationCoreReadinessRequest,
    GenerationCoreReadinessResult,
    GenerationPreviewRequest,
    GenerationPreviewResponse,
    GenerationRegenerationRequest,
    GenerationRegenerationResult,
    RuntimeReadinessRequest,
    RuntimeReadinessResult,
    WorldviewGenerationRequest,
    WorldviewGenerationResponse,
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


@router.post("/core-readiness", response_model=ApiResponse[GenerationCoreReadinessResult])
def check_world_generation_core_readiness(
    request_body: GenerationCoreReadinessRequest,
) -> ApiResponse[GenerationCoreReadinessResult]:
    return ApiResponse(data=check_core_readiness(request_body))


@router.post(
    "/worldview",
    response_model=ApiResponse[WorldviewGenerationResponse],
    operation_id="generate_world_from_worldview",
)
def generate_world_from_worldview(
    request_body: WorldviewGenerationRequest,
) -> ApiResponse[WorldviewGenerationResponse]:
    provider = provider_readiness_from_env()
    return ApiResponse(data=generate_worldview_response(request_body, provider))
