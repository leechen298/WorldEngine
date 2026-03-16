from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime, timezone
from typing import Any, Dict, Optional
from uuid import uuid4

from app.schemas.event import Event
from app.world.module_types import ModuleResult, TickContext


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def build_module_event(
    ctx: TickContext,
    *,
    event_type: str,
    module_path: str,
    payload: Optional[Dict[str, Any]] = None,
) -> Event:
    event_payload = dict(payload or {})
    event_payload["module_path"] = module_path
    created_at = _utc_now_iso()
    return Event(
        id=str(uuid4()),
        tick_id=ctx.tick_id,
        world_time_seconds=ctx.world_time_seconds,
        type=event_type,
        source=module_path,
        payload=event_payload,
        created_at=created_at,
    )


class WorldModule(ABC):
    def __init__(self, name: str, module_path: Optional[str] = None) -> None:
        self.name = name
        self.module_path = module_path or name

    def set_module_path(self, module_path: str) -> None:
        self.module_path = module_path

    @abstractmethod
    def on_tick(self, ctx: TickContext) -> ModuleResult:
        raise NotImplementedError
