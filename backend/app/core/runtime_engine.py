import os
from copy import deepcopy
from dataclasses import dataclass, replace
from datetime import datetime, timezone
from typing import Any, Callable, List, Optional
from uuid import uuid4

from app.core.event_bus import InMemoryEventLog
from app.schemas.event import Event
from app.schemas.runtime import RuntimeControlState, RuntimeRunRequest, RuntimeRunSummary
from app.world.module_types import TickContext
from app.world.modules.base import WorldModule


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class RuntimeState:
    tick_id: int = 0
    world_time_seconds: int = 0
    step_seconds: int = 600
    is_running: bool = False
    updated_at: Optional[str] = None


class RuntimeEngine:
    """In-memory runtime engine for stepping world time."""

    def __init__(
        self,
        step_seconds: int = 600,
        event_log: Optional[InMemoryEventLog] = None,
        world_root_module: Optional[WorldModule] = None,
        params_provider: Optional[Callable[[], dict[str, Any]]] = None,
        runtime_context: Optional[Any] = None,
    ) -> None:
        self._state = RuntimeState(
            step_seconds=step_seconds,
            updated_at=_utc_now_iso(),
        )
        self._event_log = event_log
        self._world_root_module = world_root_module
        self._params_provider = params_provider
        self._runtime_context = runtime_context
        self._on_step_callbacks: List[Callable[["RuntimeState", dict], None]] = []
        self._control_status: str = "idle"

    def add_on_step_callback(
        self, callback: Callable[["RuntimeState", dict], None]
    ) -> None:
        self._on_step_callbacks.append(callback)

    @classmethod
    def from_env(
        cls,
        event_log: Optional[InMemoryEventLog] = None,
        world_root_module: Optional[WorldModule] = None,
        params_provider: Optional[Callable[[], dict[str, Any]]] = None,
        runtime_context: Optional[Any] = None,
    ) -> "RuntimeEngine":
        raw_step_seconds = os.getenv("WORLD_STEP_SECONDS", "600")
        try:
            step_seconds = int(raw_step_seconds)
        except ValueError:
            step_seconds = 600

        if step_seconds <= 0:
            step_seconds = 600

        return cls(
            step_seconds=step_seconds,
            event_log=event_log,
            world_root_module=world_root_module,
            params_provider=params_provider,
            runtime_context=runtime_context,
        )

    def get_state(self) -> RuntimeState:
        return replace(self._state)

    def get_runtime_context(self) -> Optional[Any]:
        return self._runtime_context

    def get_control_state(self) -> RuntimeControlState:
        return RuntimeControlState(status=self._control_status)

    def pause(self) -> RuntimeControlState:
        self._control_status = "paused"
        return self.get_control_state()

    def resume(self) -> RuntimeControlState:
        self._control_status = "idle"
        return self.get_control_state()

    def run_bounded(self, request: RuntimeRunRequest) -> RuntimeRunSummary:
        start_state = self.get_state()
        if self._control_status == "paused":
            return self._run_summary(
                request=request,
                start_state=start_state,
                end_state=start_state,
                status="blocked",
                stop_reason="paused",
                ticks_executed=0,
            )

        self._control_status = "running"
        ticks_executed = 0
        stop_reason = "requested_ticks_reached"
        target_ticks = self._target_ticks_for_request(request)
        try:
            while ticks_executed < target_ticks:
                if ticks_executed >= request.max_ticks:
                    stop_reason = "max_ticks_reached"
                    break
                elapsed_before_next = (
                    self._state.world_time_seconds
                    - start_state.world_time_seconds
                    + self._state.step_seconds
                )
                if elapsed_before_next > request.max_duration_seconds:
                    stop_reason = "max_duration_reached"
                    break
                self.step()
                ticks_executed += 1
            else:
                stop_reason = (
                    "requested_duration_reached"
                    if request.duration_seconds is not None
                    else "requested_ticks_reached"
                )
        finally:
            self._control_status = "idle"

        return self._run_summary(
            request=request,
            start_state=start_state,
            end_state=self.get_state(),
            status="completed",
            stop_reason=stop_reason,
            ticks_executed=ticks_executed,
        )

    def step(self) -> RuntimeState:
        self._state.tick_id += 1
        self._state.world_time_seconds += self._state.step_seconds
        self._state.updated_at = _utc_now_iso()
        params = self._params_provider() if self._params_provider is not None else {}
        if self._event_log is not None:
            self._event_log.append(
                Event(
                    id=str(uuid4()),
                    tick_id=self._state.tick_id,
                    world_time_seconds=self._state.world_time_seconds,
                    type="tick.advanced",
                    source="system",
                    payload={
                        "step_seconds": self._state.step_seconds,
                        "updated_at": self._state.updated_at,
                        "params": deepcopy(params),
                    },
                    created_at=self._state.updated_at,
                )
            )
        if self._world_root_module is not None:
            module_result = self._world_root_module.on_tick(
                TickContext(
                    tick_id=self._state.tick_id,
                    world_time_seconds=self._state.world_time_seconds,
                    params=params,
                )
            )
            if self._event_log is not None:
                for event in module_result.events:
                    self._event_log.append(event)
        for cb in self._on_step_callbacks:
            cb(self._state, params)
        return self.get_state()

    def _target_ticks_for_request(self, request: RuntimeRunRequest) -> int:
        if request.ticks is not None:
            return request.ticks
        assert request.duration_seconds is not None
        return max(
            1,
            (request.duration_seconds + self._state.step_seconds - 1)
            // self._state.step_seconds,
        )

    def _run_summary(
        self,
        *,
        request: RuntimeRunRequest,
        start_state: RuntimeState,
        end_state: RuntimeState,
        status: str,
        stop_reason: str,
        ticks_executed: int,
    ) -> RuntimeRunSummary:
        return RuntimeRunSummary(
            status=status,
            stop_reason=stop_reason,
            start_tick=start_state.tick_id,
            end_tick=end_state.tick_id,
            start_world_time_seconds=start_state.world_time_seconds,
            end_world_time_seconds=end_state.world_time_seconds,
            step_seconds=end_state.step_seconds,
            ticks_requested=request.ticks,
            duration_requested_seconds=request.duration_seconds,
            ticks_executed=ticks_executed,
            guard_summary={
                "max_ticks": request.max_ticks,
                "max_duration_seconds": request.max_duration_seconds,
                "max_provider_calls": request.max_provider_calls,
                "max_estimated_cost_units": request.max_estimated_cost_units,
            },
            provider_calls_used=0,
            estimated_cost_units_used=0,
            control_status=self._control_status,
        )
