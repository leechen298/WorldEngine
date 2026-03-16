import os
from dataclasses import dataclass, replace
from datetime import datetime, timezone
from typing import Optional


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

    def __init__(self, step_seconds: int = 600) -> None:
        self._state = RuntimeState(
            step_seconds=step_seconds,
            updated_at=_utc_now_iso(),
        )

    @classmethod
    def from_env(cls) -> "RuntimeEngine":
        raw_step_seconds = os.getenv("WORLD_STEP_SECONDS", "600")
        try:
            step_seconds = int(raw_step_seconds)
        except ValueError:
            step_seconds = 600

        if step_seconds <= 0:
            step_seconds = 600

        return cls(step_seconds=step_seconds)

    def get_state(self) -> RuntimeState:
        return replace(self._state)

    def step(self) -> RuntimeState:
        self._state.tick_id += 1
        self._state.world_time_seconds += self._state.step_seconds
        self._state.updated_at = _utc_now_iso()
        return self.get_state()
