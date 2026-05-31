from __future__ import annotations

import pytest
from pydantic import ValidationError

from app.agent.memory import InMemoryAgentMemoryStore
from app.schemas.agent_memory import (
    EpisodicMemoryRecord,
    MemoryEvidenceRef,
    WorkingMemoryRecord,
)


def _evidence(ref_id: str) -> MemoryEvidenceRef:
    return MemoryEvidenceRef(type="event", id=ref_id, metadata={"kind": "test"})


def test_working_memory_records_validate_required_semantics() -> None:
    record = WorkingMemoryRecord(
        memory_id="wm-1",
        agent_id="agent-1",
        world_id="world-1",
        content="Remember the current objective.",
        source="operator",
        evidence_refs=[_evidence("event-1")],
        priority=3,
        created_at="2026-05-31T00:00:00+00:00",
        updated_at="2026-05-31T00:01:00+00:00",
        expires_at="2026-05-31T00:10:00+00:00",
    )

    dumped = record.model_dump()
    assert dumped["memory_id"] == "wm-1"
    assert dumped["agent_id"] == "agent-1"
    assert dumped["world_id"] == "world-1"
    assert dumped["evidence_refs"] == [
        {"type": "event", "id": "event-1", "metadata": {"kind": "test"}}
    ]
    assert dumped["priority"] == 3
    assert dumped["expires_at"] == "2026-05-31T00:10:00+00:00"


def test_working_memory_records_require_updated_at() -> None:
    with pytest.raises(ValidationError) as exc_info:
        WorkingMemoryRecord(
            memory_id="wm-1",
            agent_id="agent-1",
            world_id="world-1",
            content="Missing update time.",
            source="operator",
            created_at="2026-05-31T00:00:00+00:00",
        )

    assert exc_info.value.errors()[0]["loc"] == ("updated_at",)


def test_working_memory_store_scopes_and_bounds_records_deterministically() -> None:
    store = InMemoryAgentMemoryStore()
    store.add_working_memory(
        WorkingMemoryRecord(
            memory_id="low",
            agent_id="agent-1",
            world_id="world-1",
            content="lower priority",
            source="operator",
            priority=1,
            created_at="2026-05-31T00:00:00+00:00",
            updated_at="2026-05-31T00:03:00+00:00",
        )
    )
    store.add_working_memory(
        WorkingMemoryRecord(
            memory_id="high-old",
            agent_id="agent-1",
            world_id="world-1",
            content="high priority older",
            source="system",
            priority=5,
            created_at="2026-05-31T00:00:00+00:00",
            updated_at="2026-05-31T00:01:00+00:00",
        )
    )
    store.add_working_memory(
        WorkingMemoryRecord(
            memory_id="other-world",
            agent_id="agent-1",
            world_id="world-2",
            content="wrong world",
            source="system",
            priority=99,
            created_at="2026-05-31T00:00:00+00:00",
            updated_at="2026-05-31T00:04:00+00:00",
        )
    )
    store.add_working_memory(
        WorkingMemoryRecord(
            memory_id="high-new",
            agent_id="agent-1",
            world_id="world-1",
            content="high priority newer",
            source="derived",
            priority=5,
            created_at="2026-05-31T00:00:00+00:00",
            updated_at="2026-05-31T00:02:00+00:00",
        )
    )

    records = store.list_working_memory(
        agent_id="agent-1",
        world_id="world-1",
        limit=2,
    )

    assert [record.memory_id for record in records] == ["high-new", "high-old"]


def test_working_memory_uses_memory_id_tie_breaker_and_limit_bounds() -> None:
    store = InMemoryAgentMemoryStore()
    for memory_id in ("tie-b", "tie-a", "tie-c"):
        store.add_working_memory(
            WorkingMemoryRecord(
                memory_id=memory_id,
                agent_id="agent-1",
                world_id="world-1",
                content=f"content {memory_id}",
                source="operator",
                priority=1,
                created_at="2026-05-31T00:00:00+00:00",
                updated_at="2026-05-31T00:00:00+00:00",
            )
        )

    assert [
        record.memory_id
        for record in store.list_working_memory(agent_id="agent-1", world_id="world-1")
    ] == ["tie-a", "tie-b", "tie-c"]
    assert store.list_working_memory(agent_id="agent-1", world_id="world-1", limit=0) == []


def test_episodic_records_preserve_event_refs_and_list_by_scope() -> None:
    store = InMemoryAgentMemoryStore()
    store.add_episodic_memory(
        EpisodicMemoryRecord(
            memory_id="ep-old",
            agent_id="agent-1",
            world_id="world-1",
            summary="Earlier event.",
            event_refs=[_evidence("event-1")],
            tick=1,
            world_time_seconds=600,
            source="observed_event",
            created_at="2026-05-31T00:01:00+00:00",
        )
    )
    store.add_episodic_memory(
        EpisodicMemoryRecord(
            memory_id="ep-other-agent",
            agent_id="agent-2",
            world_id="world-1",
            summary="Wrong agent.",
            event_refs=[_evidence("event-2")],
            tick=99,
            world_time_seconds=9900,
            source="observed_event",
            created_at="2026-05-31T00:02:00+00:00",
        )
    )
    store.add_episodic_memory(
        EpisodicMemoryRecord(
            memory_id="ep-new",
            agent_id="agent-1",
            world_id="world-1",
            summary="Later event.",
            event_refs=[_evidence("event-3")],
            tick=2,
            world_time_seconds=1200,
            source="action_result",
            action_refs=[MemoryEvidenceRef(type="action_result", id="result-1")],
            created_at="2026-05-31T00:03:00+00:00",
        )
    )

    records = store.list_episodic_memory(agent_id="agent-1", world_id="world-1")

    assert [record.memory_id for record in records] == ["ep-new", "ep-old"]
    assert records[0].event_refs == [_evidence("event-3")]
    assert records[0].action_refs == [
        MemoryEvidenceRef(type="action_result", id="result-1")
    ]


def test_episodic_memory_uses_tie_breaker_and_copy_isolation() -> None:
    store = InMemoryAgentMemoryStore()
    added = store.add_episodic_memory(
        EpisodicMemoryRecord(
            memory_id="tie-b",
            agent_id="agent-1",
            world_id="world-1",
            summary="Tie b.",
            event_refs=[_evidence("event-b")],
            tick=3,
            world_time_seconds=1800,
            source="observed_event",
            created_at="2026-05-31T00:03:00+00:00",
        )
    )
    store.add_episodic_memory(
        EpisodicMemoryRecord(
            memory_id="tie-a",
            agent_id="agent-1",
            world_id="world-1",
            summary="Tie a.",
            event_refs=[_evidence("event-a")],
            tick=3,
            world_time_seconds=1800,
            source="observed_event",
            created_at="2026-05-31T00:03:00+00:00",
        )
    )

    added.summary = "mutated add return"
    added.event_refs[0].metadata["kind"] = "mutated"
    listed = store.list_episodic_memory(agent_id="agent-1", world_id="world-1")
    listed[0].summary = "mutated read return"
    listed[0].event_refs[0].metadata["kind"] = "mutated"

    fresh = store.list_episodic_memory(agent_id="agent-1", world_id="world-1")

    assert [record.memory_id for record in fresh] == ["tie-a", "tie-b"]
    assert fresh[1].summary == "Tie b."
    assert fresh[1].event_refs[0].metadata == {"kind": "test"}


def test_memory_store_reads_do_not_expose_mutable_backing_state() -> None:
    store = InMemoryAgentMemoryStore()
    store.add_working_memory(
        WorkingMemoryRecord(
            memory_id="wm-1",
            agent_id="agent-1",
            world_id="world-1",
            content="mutable check",
            source="operator",
            evidence_refs=[_evidence("event-1")],
            created_at="2026-05-31T00:00:00+00:00",
            updated_at="2026-05-31T00:01:00+00:00",
        )
    )

    first = store.list_working_memory(agent_id="agent-1", world_id="world-1")[0]
    first.content = "mutated outside store"
    first.evidence_refs[0].metadata["kind"] = "mutated"

    second = store.list_working_memory(agent_id="agent-1", world_id="world-1")[0]

    assert second.content == "mutable check"
    assert second.evidence_refs[0].metadata == {"kind": "test"}
