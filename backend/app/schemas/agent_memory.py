from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class MemoryEvidenceRef(BaseModel):
    type: str
    id: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class WorkingMemoryRecord(BaseModel):
    memory_id: str
    agent_id: str
    world_id: str
    content: str
    source: str
    evidence_refs: List[MemoryEvidenceRef] = Field(default_factory=list)
    priority: int = 0
    created_at: str
    updated_at: str
    expires_at: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class EpisodicMemoryRecord(BaseModel):
    memory_id: str
    agent_id: str
    world_id: str
    summary: str
    event_refs: List[MemoryEvidenceRef] = Field(default_factory=list)
    tick: int
    world_time_seconds: int
    source: str
    action_refs: List[MemoryEvidenceRef] = Field(default_factory=list)
    outcome_refs: List[MemoryEvidenceRef] = Field(default_factory=list)
    created_at: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
