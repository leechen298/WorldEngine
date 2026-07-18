from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, Request

from app.engine.session import (
    EngineV1ConflictError,
    EngineV1InternalError,
    EngineV1NotFoundError,
    EngineV1Service,
)
from app.schemas.api import ApiResponse
from app.schemas.engine_v1 import (
    ActionRequest,
    ActionResult,
    CapabilityManifest,
    DirectionDecision,
    DirectionRequest,
    EventPage,
    EvidenceBundle,
    FeedbackRequest,
    FeedbackResult,
    PublicProjection,
    RunnableWorldPackage,
    SessionCreateRequest,
    SessionStepRequest,
    SessionStepResult,
    WorldPackageCreateRequest,
    WorldSessionView,
)


router = APIRouter(prefix="/api/v1", tags=["engine-v1"])


def get_engine_v1_service(request: Request) -> EngineV1Service:
    return request.app.state.engine_v1_service


def _translate_error(exc: Exception) -> HTTPException:
    if isinstance(exc, EngineV1NotFoundError):
        return HTTPException(status_code=404, detail=str(exc))
    if isinstance(exc, EngineV1ConflictError):
        return HTTPException(
            status_code=409,
            detail={
                "message": str(exc),
                "data": {"reason_code": exc.reason_code, **exc.data},
            },
        )
    if isinstance(exc, EngineV1InternalError):
        return HTTPException(
            status_code=500,
            detail={
                "message": str(exc),
                "data": {"reason_code": exc.reason_code, **exc.data},
            },
        )
    return HTTPException(status_code=500, detail="Engine v1 request failed")


@router.get(
    "/capabilities",
    operation_id="capabilities.read",
    response_model=ApiResponse[CapabilityManifest],
)
def get_capabilities(
    service: EngineV1Service = Depends(get_engine_v1_service),
) -> ApiResponse[CapabilityManifest]:
    return ApiResponse(data=service.capabilities())


@router.post(
    "/world-packages",
    operation_id="world_packages.create",
    response_model=ApiResponse[RunnableWorldPackage],
)
def create_world_package(
    body: WorldPackageCreateRequest,
    service: EngineV1Service = Depends(get_engine_v1_service),
) -> ApiResponse[RunnableWorldPackage]:
    try:
        return ApiResponse(data=service.create_package(body))
    except (EngineV1ConflictError, EngineV1InternalError) as exc:
        raise _translate_error(exc) from exc


@router.get(
    "/world-packages/{package_id}",
    operation_id="world_packages.read",
    response_model=ApiResponse[RunnableWorldPackage],
)
def get_world_package(
    package_id: str,
    service: EngineV1Service = Depends(get_engine_v1_service),
) -> ApiResponse[RunnableWorldPackage]:
    try:
        return ApiResponse(data=service.get_package(package_id))
    except (
        EngineV1NotFoundError,
        EngineV1ConflictError,
        EngineV1InternalError,
    ) as exc:
        raise _translate_error(exc) from exc


@router.post(
    "/sessions",
    operation_id="sessions.create",
    response_model=ApiResponse[WorldSessionView],
)
def create_session(
    body: SessionCreateRequest,
    service: EngineV1Service = Depends(get_engine_v1_service),
) -> ApiResponse[WorldSessionView]:
    try:
        return ApiResponse(data=service.create_session(body))
    except (
        EngineV1NotFoundError,
        EngineV1ConflictError,
        EngineV1InternalError,
    ) as exc:
        raise _translate_error(exc) from exc


@router.get(
    "/sessions/{session_id}",
    operation_id="sessions.read",
    response_model=ApiResponse[WorldSessionView],
)
def get_session(
    session_id: str,
    service: EngineV1Service = Depends(get_engine_v1_service),
) -> ApiResponse[WorldSessionView]:
    try:
        return ApiResponse(data=service.get_session(session_id))
    except (
        EngineV1NotFoundError,
        EngineV1ConflictError,
        EngineV1InternalError,
    ) as exc:
        raise _translate_error(exc) from exc


@router.post(
    "/sessions/{session_id}/steps",
    operation_id="sessions.step",
    response_model=ApiResponse[SessionStepResult],
)
def step_session(
    session_id: str,
    body: SessionStepRequest,
    service: EngineV1Service = Depends(get_engine_v1_service),
) -> ApiResponse[SessionStepResult]:
    try:
        return ApiResponse(data=service.step_session(session_id, body))
    except (
        EngineV1NotFoundError,
        EngineV1ConflictError,
        EngineV1InternalError,
    ) as exc:
        raise _translate_error(exc) from exc


@router.post(
    "/sessions/{session_id}/directions",
    operation_id="directions.submit",
    response_model=ApiResponse[DirectionDecision],
)
def submit_direction(
    session_id: str,
    body: DirectionRequest,
    service: EngineV1Service = Depends(get_engine_v1_service),
) -> ApiResponse[DirectionDecision]:
    try:
        return ApiResponse(data=service.submit_direction(session_id, body))
    except (
        EngineV1NotFoundError,
        EngineV1ConflictError,
        EngineV1InternalError,
    ) as exc:
        raise _translate_error(exc) from exc


@router.post(
    "/sessions/{session_id}/actions",
    operation_id="actions.submit",
    response_model=ApiResponse[ActionResult],
)
def submit_action(
    session_id: str,
    body: ActionRequest,
    service: EngineV1Service = Depends(get_engine_v1_service),
) -> ApiResponse[ActionResult]:
    try:
        return ApiResponse(data=service.submit_action(session_id, body))
    except (
        EngineV1NotFoundError,
        EngineV1ConflictError,
        EngineV1InternalError,
    ) as exc:
        raise _translate_error(exc) from exc


@router.post(
    "/sessions/{session_id}/feedback",
    operation_id="feedback.submit",
    response_model=ApiResponse[FeedbackResult],
)
def submit_feedback(
    session_id: str,
    body: FeedbackRequest,
    service: EngineV1Service = Depends(get_engine_v1_service),
) -> ApiResponse[FeedbackResult]:
    try:
        return ApiResponse(data=service.submit_feedback(session_id, body))
    except (
        EngineV1NotFoundError,
        EngineV1ConflictError,
        EngineV1InternalError,
    ) as exc:
        raise _translate_error(exc) from exc


@router.get(
    "/sessions/{session_id}/projection",
    operation_id="projection.read",
    response_model=ApiResponse[PublicProjection],
)
def get_projection(
    session_id: str,
    service: EngineV1Service = Depends(get_engine_v1_service),
) -> ApiResponse[PublicProjection]:
    try:
        return ApiResponse(data=service.get_projection(session_id))
    except (
        EngineV1NotFoundError,
        EngineV1ConflictError,
        EngineV1InternalError,
    ) as exc:
        raise _translate_error(exc) from exc


@router.get(
    "/sessions/{session_id}/events",
    operation_id="events.poll",
    response_model=ApiResponse[EventPage],
)
def poll_events(
    session_id: str,
    after_sequence: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=200),
    service: EngineV1Service = Depends(get_engine_v1_service),
) -> ApiResponse[EventPage]:
    try:
        return ApiResponse(
            data=service.get_events(
                session_id,
                after_sequence=after_sequence,
                limit=limit,
            )
        )
    except (
        EngineV1NotFoundError,
        EngineV1ConflictError,
        EngineV1InternalError,
    ) as exc:
        raise _translate_error(exc) from exc


@router.get(
    "/sessions/{session_id}/evidence",
    operation_id="evidence.export",
    response_model=ApiResponse[EvidenceBundle],
)
def export_evidence(
    session_id: str,
    service: EngineV1Service = Depends(get_engine_v1_service),
) -> ApiResponse[EvidenceBundle]:
    try:
        return ApiResponse(data=service.get_evidence(session_id))
    except (
        EngineV1NotFoundError,
        EngineV1ConflictError,
        EngineV1InternalError,
    ) as exc:
        raise _translate_error(exc) from exc
