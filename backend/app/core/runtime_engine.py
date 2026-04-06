import os
from copy import deepcopy
from dataclasses import dataclass, replace
from datetime import datetime, timezone
from typing import Any, Callable, List, Optional
from uuid import uuid4

from app.core.event_bus import InMemoryEventLog
from app.schemas.event import Event
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
    ) -> None:
        self._state = RuntimeState(
            step_seconds=step_seconds,
            updated_at=_utc_now_iso(),
        )
        self._event_log = event_log
        self._world_root_module = world_root_module
        self._params_provider = params_provider
        self._on_step_callbacks: List[Callable[["RuntimeState", dict], None]] = []

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
        )

    def get_state(self) -> RuntimeState:
        return replace(self._state)

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
