from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

from app.schemas.engine_v1 import (
    AgentCycleEvidence,
    AgentPublicState,
    DiffRecord,
    DirectionDecision,
    DirectionRequest,
    EventRecord,
    InterventionWindow,
    RunnableWorldPackage,
    SnapshotRecord,
)


@dataclass
class QueuedDirection:
    request: DirectionRequest
    decision: DirectionDecision


@dataclass
class EngineSessionRecord:
    session_id: str
    package: RunnableWorldPackage
    world_id: str
    status: str
    tick: int
    world_time_seconds: float
    revision: int
    variables: Dict[str, int]
    feedback_count: int
    agents: Dict[str, AgentPublicState]
    windows: Dict[str, InterventionWindow]
    active_window_id: str
    events: List[EventRecord] = field(default_factory=list)
    diffs: List[DiffRecord] = field(default_factory=list)
    snapshots: List[SnapshotRecord] = field(default_factory=list)
    agent_cycles: List[AgentCycleEvidence] = field(default_factory=list)
    direction_decisions: List[DirectionDecision] = field(default_factory=list)
    queued_directions: List[QueuedDirection] = field(default_factory=list)
    request_results: Dict[Tuple[str, str], Any] = field(default_factory=dict)
    request_fingerprints: Dict[Tuple[str, str], str] = field(default_factory=dict)
    request_correlations: List[Dict[str, Any]] = field(default_factory=list)
