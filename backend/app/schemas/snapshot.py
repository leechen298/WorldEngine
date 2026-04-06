from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class RuntimeStateSnapshot(BaseModel):
    tick_id: int
    world_time_seconds: int
    step_seconds: int
    updated_at: Optional[str] = None


class Snapshot(BaseModel):
    id: str
    tick_id: int
    world_time_seconds: int
    created_at: str
    runtime_state: RuntimeStateSnapshot
    params: Dict[str, Any]


class SnapshotList(BaseModel):
    items: List[Snapshot]
    total: int
