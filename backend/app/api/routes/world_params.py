from typing import Any, Dict
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Request

from app.core.event_bus import InMemoryEventLog
from app.core.runtime_engine import RuntimeEngine
from app.schemas.api import ApiResponse
from app.schemas.event import Event
from app.schemas.params import ApplyParamsRequest
from app.world.state import WorldState
from app.world.validation import ParamValidator

router = APIRouter(prefix="/world", tags=["world"])


def get_world_state(request: Request) -> WorldState:
    return request.app.state.world_state


def get_event_log(request: Request) -> InMemoryEventLog:
    return request.app.state.event_log


def get_runtime_engine(request: Request) -> RuntimeEngine:
    return request.app.state.runtime_engine


def get_param_validator(request: Request) -> ParamValidator:
    return request.app.state.param_validator


@router.get("/params", response_model=ApiResponse[Dict[str, Any]])
def get_world_params(
    world_state: WorldState = Depends(get_world_state),
) -> ApiResponse[Dict[str, Any]]:
    return ApiResponse(data=world_state.get_params())


@router.post("/params/apply", response_model=ApiResponse[Dict[str, Any]])
def apply_world_params(
    request_body: ApplyParamsRequest,
    world_state: WorldState = Depends(get_world_state),
    event_log: InMemoryEventLog = Depends(get_event_log),
    runtime_engine: RuntimeEngine = Depends(get_runtime_engine),
    param_validator: ParamValidator = Depends(get_param_validator),
) -> ApiResponse[Dict[str, Any]]:
    validation_result = param_validator.validate(request_body.patches)
    if not validation_result.ok:
        raise HTTPException(
            status_code=422,
            detail={
                "msg": "Param validation failed",
                "errors": [error.to_dict() for error in validation_result.errors],
            },
        )

    params = world_state.apply_patch(request_body.patches)
    runtime_state = runtime_engine.get_state()

    event_log.append(
        Event(
            id=str(uuid4()),
            tick_id=runtime_state.tick_id,
            world_time_seconds=runtime_state.world_time_seconds,
            type="params.applied",
            source="world.params",
            payload={
                "patches": [patch.model_dump() for patch in request_body.patches],
                "updated_at": world_state.updated_at,
            },
            created_at=world_state.updated_at,
        )
    )

    return ApiResponse(data=params)
