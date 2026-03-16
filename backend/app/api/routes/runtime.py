from fastapi import APIRouter, Request
from pydantic import BaseModel

from app.core.runtime_engine import RuntimeEngine, RuntimeState

router = APIRouter(prefix="/runtime", tags=["runtime"])


class RuntimeStateResponse(BaseModel):
    tick_id: int
    world_time_seconds: int
    step_seconds: int


def _get_runtime_engine(request: Request) -> RuntimeEngine:
    return request.app.state.runtime_engine


def _to_response(state: RuntimeState) -> RuntimeStateResponse:
    return RuntimeStateResponse(
        tick_id=state.tick_id,
        world_time_seconds=state.world_time_seconds,
        step_seconds=state.step_seconds,
    )


@router.get("/state", response_model=RuntimeStateResponse)
def get_runtime_state(request: Request) -> RuntimeStateResponse:
    return _to_response(_get_runtime_engine(request).get_state())


@router.post("/step", response_model=RuntimeStateResponse)
def step_runtime(request: Request) -> RuntimeStateResponse:
    return _to_response(_get_runtime_engine(request).step())
