from __future__ import annotations

from copy import deepcopy

from app.agent.memory import InMemoryAgentMemoryStore
from app.core.event_bus import InMemoryEventLog
from app.core.runtime_context import (
    RuntimeContext,
    summarize_runtime_context,
)
from app.core.runtime_engine import RuntimeEngine
from app.schemas.agent_loop import (
    MemoryContextSummary,
    PerceptionFrame,
    RuntimeContextSummary,
    RuntimeStateSummary,
)
from app.world.state import WorldState


DEFAULT_AGENT_ID = "agent.default"
DEFAULT_WORLD_ID = "world.default"


class PerceptionBuilder:
    """Builds a bounded, read-only agent perception frame."""

    def __init__(
        self,
        *,
        runtime_engine: RuntimeEngine,
        event_log: InMemoryEventLog,
        world_state: WorldState,
        memory_store: InMemoryAgentMemoryStore | None = None,
        agent_id: str = DEFAULT_AGENT_ID,
        world_id: str = DEFAULT_WORLD_ID,
        default_event_limit: int = 20,
        working_memory_limit: int = 5,
        episodic_memory_limit: int = 5,
    ) -> None:
        self._runtime_engine = runtime_engine
        self._event_log = event_log
        self._world_state = world_state
        self._memory_store = memory_store
        self._agent_id = agent_id
        self._world_id = world_id
        self._default_event_limit = default_event_limit
        self._working_memory_limit = working_memory_limit
        self._episodic_memory_limit = episodic_memory_limit

    def build(self, *, event_limit: int | None = None) -> PerceptionFrame:
        runtime_state = self._runtime_engine.get_state()
        limit = self._normalize_event_limit(event_limit)
        recent_events = [
            event.model_copy(deep=True)
            for event in self._event_log.list_page(limit=limit).items
        ]

        return PerceptionFrame(
            runtime=RuntimeStateSummary(
                tick_id=runtime_state.tick_id,
                world_time_seconds=runtime_state.world_time_seconds,
                step_seconds=runtime_state.step_seconds,
                is_running=runtime_state.is_running,
                updated_at=runtime_state.updated_at,
            ),
            params=self._world_state.get_params(),
            recent_events=recent_events,
            runtime_context_summary=self._runtime_context_summary(),
            memory_context=self._memory_context_summary(),
        )

    def _normalize_event_limit(self, event_limit: int | None) -> int:
        raw_limit = self._default_event_limit if event_limit is None else event_limit
        return max(1, min(raw_limit, 200))

    def _runtime_context_summary(self) -> RuntimeContextSummary | None:
        runtime_context = self._runtime_engine.get_runtime_context()
        if not isinstance(runtime_context, RuntimeContext):
            return None

        summary = summarize_runtime_context(runtime_context)
        return RuntimeContextSummary(
            worldspec_id=summary.worldspec_id,
            schema_version=summary.schema_version,
            root_cell_id=summary.root_cell_id,
            root_cell_type=summary.root_cell_type,
            source_type=summary.source_type,
            source_label=summary.source_label,
            metadata=deepcopy(dict(summary.metadata)),
        )

    def _memory_context_summary(self) -> MemoryContextSummary | None:
        if self._memory_store is None:
            return None

        return MemoryContextSummary(
            working_memory=self._memory_store.list_working_memory(
                agent_id=self._agent_id,
                world_id=self._world_id,
                limit=self._working_memory_limit,
            ),
            episodic_memory=self._memory_store.list_episodic_memory(
                agent_id=self._agent_id,
                world_id=self._world_id,
                limit=self._episodic_memory_limit,
            ),
        )
