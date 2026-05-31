from app.agent.perception import PerceptionBuilder
from app.agent.memory import InMemoryAgentMemoryStore
from app.core.event_bus import InMemoryEventLog
from app.core.runtime_context import RuntimeContext
from app.core.runtime_engine import RuntimeEngine
from app.schemas.agent_memory import EpisodicMemoryRecord, WorkingMemoryRecord
from app.schemas.event import Event
from app.world.state import WorldState


DEFAULT_AGENT_ID = "agent.default"
DEFAULT_WORLD_ID = "world.default"


def _event(event_id: str, tick_id: int, event_type: str) -> Event:
    return Event(
        id=event_id,
        tick_id=tick_id,
        world_time_seconds=tick_id * 600,
        type=event_type,
        source="test",
        payload={"index": tick_id},
        created_at=f"2026-05-30T00:0{tick_id}:00+00:00",
    )


def _working_memory(
    memory_id: str,
    *,
    content: str,
    priority: int,
    updated_at: str,
    agent_id: str = DEFAULT_AGENT_ID,
    world_id: str = DEFAULT_WORLD_ID,
) -> WorkingMemoryRecord:
    return WorkingMemoryRecord(
        memory_id=memory_id,
        agent_id=agent_id,
        world_id=world_id,
        content=content,
        source="test",
        priority=priority,
        created_at="2026-05-30T00:00:00+00:00",
        updated_at=updated_at,
    )


def _episodic_memory(
    memory_id: str,
    *,
    summary: str,
    tick: int,
    world_time_seconds: int,
    agent_id: str = DEFAULT_AGENT_ID,
    world_id: str = DEFAULT_WORLD_ID,
) -> EpisodicMemoryRecord:
    return EpisodicMemoryRecord(
        memory_id=memory_id,
        agent_id=agent_id,
        world_id=world_id,
        summary=summary,
        tick=tick,
        world_time_seconds=world_time_seconds,
        source="test",
        created_at="2026-05-30T00:00:00+00:00",
    )


def test_perception_frame_reads_runtime_params_and_latest_events() -> None:
    event_log = InMemoryEventLog()
    event_log.append(_event("event-1", 1, "test.oldest"))
    event_log.append(_event("event-2", 2, "test.middle"))
    event_log.append(_event("event-3", 3, "test.newest"))
    world_state = WorldState(params={"scene": {"weather": "rain"}})
    runtime_engine = RuntimeEngine(
        event_log=event_log,
        params_provider=world_state.get_params,
    )
    runtime_engine.step()

    frame = PerceptionBuilder(
        runtime_engine=runtime_engine,
        event_log=event_log,
        world_state=world_state,
    ).build(event_limit=2)

    assert frame.runtime.tick_id == 1
    assert frame.runtime.world_time_seconds == 600
    assert frame.params == {"scene": {"weather": "rain"}}
    assert [event.id for event in frame.recent_events] == [
        event_log.snapshot()[-1].id,
        "event-3",
    ]


def test_perception_frame_includes_bounded_runtime_context_summary() -> None:
    runtime_context = RuntimeContext(
        worldspec_id="worldspec-1",
        schema_version="0.2",
        root_cell_id="root-cell",
        root_cell_type="world",
        source_type="dict",
        source_label="test-world",
        metadata={"source": "unit-test"},
    )
    runtime_engine = RuntimeEngine(runtime_context=runtime_context)

    frame = PerceptionBuilder(
        runtime_engine=runtime_engine,
        event_log=InMemoryEventLog(),
        world_state=WorldState(),
    ).build()

    assert frame.runtime_context_summary is not None
    summary = frame.runtime_context_summary.model_dump()
    assert summary == {
        "worldspec_id": "worldspec-1",
        "schema_version": "0.2",
        "root_cell_id": "root-cell",
        "root_cell_type": "world",
        "source_type": "dict",
        "source_label": "test-world",
        "metadata": {"source": "unit-test"},
    }
    assert "root" not in summary


def test_perception_builder_does_not_mutate_runtime_events_or_params() -> None:
    event_log = InMemoryEventLog()
    event_log.append(_event("event-1", 1, "test.event"))
    world_state = WorldState(params={"counter": {"increment": 2}})
    runtime_engine = RuntimeEngine(
        event_log=event_log,
        params_provider=world_state.get_params,
    )
    before_runtime = runtime_engine.get_state()
    before_events = event_log.snapshot()
    before_params = world_state.get_params()

    frame = PerceptionBuilder(
        runtime_engine=runtime_engine,
        event_log=event_log,
        world_state=world_state,
    ).build()

    assert frame.params == before_params
    assert runtime_engine.get_state() == before_runtime
    assert event_log.snapshot() == before_events
    assert world_state.get_params() == before_params


def test_perception_frame_does_not_expose_mutable_backing_state() -> None:
    nested_metadata = {"nested": {"level": 1}}
    runtime_context = RuntimeContext(
        worldspec_id="worldspec-1",
        schema_version="0.2",
        root_cell_id="root-cell",
        root_cell_type="world",
        source_type="dict",
        source_label=None,
        metadata=nested_metadata,
    )
    event_log = InMemoryEventLog()
    event_log.append(_event("event-1", 1, "test.event"))
    world_state = WorldState(params={"scene": {"weather": "rain"}})
    runtime_engine = RuntimeEngine(runtime_context=runtime_context)

    frame = PerceptionBuilder(
        runtime_engine=runtime_engine,
        event_log=event_log,
        world_state=world_state,
    ).build()

    frame.params["scene"]["weather"] = "mutated"
    frame.recent_events[0].payload["index"] = "mutated"
    assert frame.runtime_context_summary is not None
    frame.runtime_context_summary.metadata["nested"]["level"] = 99

    assert world_state.get_params() == {"scene": {"weather": "rain"}}
    assert event_log.snapshot()[0].payload == {"index": 1}
    assert runtime_context.metadata == {"nested": {"level": 1}}


def test_perception_frame_includes_bounded_read_only_memory_context() -> None:
    memory_store = InMemoryAgentMemoryStore()
    memory_store.add_working_memory(
        _working_memory(
            "working-low",
            content="lower priority",
            priority=1,
            updated_at="2026-05-30T00:01:00+00:00",
        )
    )
    memory_store.add_working_memory(
        _working_memory(
            "working-high",
            content="higher priority",
            priority=10,
            updated_at="2026-05-30T00:02:00+00:00",
        )
    )
    memory_store.add_working_memory(
        _working_memory(
            "working-other-agent",
            content="other agent",
            priority=99,
            updated_at="2026-05-30T00:03:00+00:00",
            agent_id="agent.other",
        )
    )
    memory_store.add_episodic_memory(
        _episodic_memory(
            "episodic-old",
            summary="older event",
            tick=1,
            world_time_seconds=600,
        )
    )
    memory_store.add_episodic_memory(
        _episodic_memory(
            "episodic-new",
            summary="newer event",
            tick=2,
            world_time_seconds=1200,
        )
    )

    frame = PerceptionBuilder(
        runtime_engine=RuntimeEngine(),
        event_log=InMemoryEventLog(),
        world_state=WorldState(),
        memory_store=memory_store,
        working_memory_limit=1,
        episodic_memory_limit=1,
    ).build()

    assert frame.memory_context is not None
    assert [item.memory_id for item in frame.memory_context.working_memory] == [
        "working-high"
    ]
    assert [item.memory_id for item in frame.memory_context.episodic_memory] == [
        "episodic-new"
    ]

    frame.memory_context.working_memory[0].content = "mutated"
    frame.memory_context.episodic_memory[0].summary = "mutated"

    assert (
        memory_store.list_working_memory(
            agent_id=DEFAULT_AGENT_ID,
            world_id=DEFAULT_WORLD_ID,
            limit=1,
        )[0].content
        == "higher priority"
    )
    assert (
        memory_store.list_episodic_memory(
            agent_id=DEFAULT_AGENT_ID,
            world_id=DEFAULT_WORLD_ID,
            limit=1,
        )[0].summary
        == "newer event"
    )
