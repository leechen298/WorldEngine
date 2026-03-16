from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from app.schemas.event import Event


@dataclass(frozen=True)
class TickContext:
    tick_id: int
    world_time_seconds: int
    params: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ModuleResult:
    events: List[Event] = field(default_factory=list)
    summary: Optional[str] = None
    state_delta: Dict[str, Any] = field(default_factory=dict)
