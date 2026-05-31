from __future__ import annotations

from typing import TypeVar

from app.schemas.agent_memory import EpisodicMemoryRecord, WorkingMemoryRecord

T = TypeVar("T")


class InMemoryAgentMemoryStore:
    """Process-local store for generic agent memory records."""

    def __init__(self) -> None:
        self._working_memory: list[WorkingMemoryRecord] = []
        self._episodic_memory: list[EpisodicMemoryRecord] = []

    def add_working_memory(self, record: WorkingMemoryRecord) -> WorkingMemoryRecord:
        stored = record.model_copy(deep=True)
        self._working_memory.append(stored)
        return stored.model_copy(deep=True)

    def add_episodic_memory(self, record: EpisodicMemoryRecord) -> EpisodicMemoryRecord:
        stored = record.model_copy(deep=True)
        self._episodic_memory.append(stored)
        return stored.model_copy(deep=True)

    def list_working_memory(
        self,
        *,
        agent_id: str,
        world_id: str,
        limit: int | None = None,
    ) -> list[WorkingMemoryRecord]:
        records = [
            record
            for record in self._working_memory
            if record.agent_id == agent_id and record.world_id == world_id
        ]
        records.sort(
            key=lambda record: (
                -record.priority,
                _reverse_string(record.updated_at or record.created_at),
                record.memory_id,
            )
        )
        return [record.model_copy(deep=True) for record in _bounded(records, limit)]

    def list_episodic_memory(
        self,
        *,
        agent_id: str,
        world_id: str,
        limit: int | None = None,
    ) -> list[EpisodicMemoryRecord]:
        records = [
            record
            for record in self._episodic_memory
            if record.agent_id == agent_id and record.world_id == world_id
        ]
        records.sort(
            key=lambda record: (
                -record.tick,
                -record.world_time_seconds,
                _reverse_string(record.created_at),
                record.memory_id,
            )
        )
        return [record.model_copy(deep=True) for record in _bounded(records, limit)]


def _bounded(records: list[T], limit: int | None) -> list[T]:
    if limit is None:
        return records
    return records[: max(0, limit)]


def _reverse_string(value: str) -> tuple[int, ...]:
    return tuple(-ord(character) for character in value)
