from typing import Optional

from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel

from app.core.runtime_engine import RuntimeEngine, RuntimeState
from app.schemas.api import ApiResponse

router = APIRouter(prefix="/runtime", tags=["runtime"])


class RuntimeStateResponse(BaseModel):
    tick_id: int
    world_time_seconds: int
    step_seconds: int
    updated_at: Optional[str] = None


def get_runtime_engine(request: Request) -> RuntimeEngine:
    return request.app.state.runtime_engine


def _to_response(state: RuntimeState) -> RuntimeStateResponse:
    return RuntimeStateResponse(
        tick_id=state.tick_id,
        world_time_seconds=state.world_time_seconds,
        step_seconds=state.step_seconds,
        updated_at=state.updated_at,
    )


@router.get("/state", response_model=ApiResponse[RuntimeStateResponse])
def get_runtime_state(
    runtime_engine: RuntimeEngine = Depends(get_runtime_engine),
) -> ApiResponse[RuntimeStateResponse]:
    return ApiResponse(data=_to_response(runtime_engine.get_state()))


@router.post("/step", response_model=ApiResponse[RuntimeStateResponse])
def step_runtime(
    runtime_engine: RuntimeEngine = Depends(get_runtime_engine),
) -> ApiResponse[RuntimeStateResponse]:
    return ApiResponse(data=_to_response(runtime_engine.step()))
