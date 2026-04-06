"""Archive service: generates snapshots and chunk summaries after each tick."""

from __future__ import annotations

import os
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
from typing import List, Optional
from uuid import uuid4

from app.core.event_bus import InMemoryEventLog
from app.core.runtime_engine import RuntimeState
from app.schemas.event import Event
from app.schemas.snapshot import RuntimeStateSnapshot, Snapshot
from app.schemas.summary import Summary, SummaryStats
from app.world.storage.snapshot_store import InMemorySnapshotStore
from app.world.storage.summary_store import InMemorySummaryStore


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _parse_env_int(name: str, default: int) -> int:
    raw = os.getenv(name, str(default))
    try:
        val = int(raw)
    except ValueError:
        return default
    return val if val > 0 else default


class ArchiveService:
    """Decides when to create snapshots / summaries and writes them to stores."""

    def __init__(
        self,
        snapshot_store: InMemorySnapshotStore,
        summary_store: InMemorySummaryStore,
        event_log: InMemoryEventLog,
        snapshot_interval: Optional[int] = None,
        summary_interval: Optional[int] = None,
    ) -> None:
        self._snapshot_store = snapshot_store
        self._summary_store = summary_store
        self._event_log = event_log
        self.snapshot_interval = snapshot_interval or _parse_env_int(
            "WORLD_SNAPSHOT_INTERVAL_TICKS", 10
        )
        self.summary_interval = summary_interval or _parse_env_int(
            "WORLD_SUMMARY_INTERVAL_TICKS", 20
        )
        self._last_summary_tick: int = 0

    def on_tick_completed(
        self, runtime_state: RuntimeState, params: dict
    ) -> None:
        tick = runtime_state.tick_id

        if tick > 0 and tick % self.snapshot_interval == 0:
            self._create_snapshot(runtime_state, params)

        if tick > 0 and tick % self.summary_interval == 0:
            self._create_summary(self._last_summary_tick + 1, tick)
            self._last_summary_tick = tick

    def _create_snapshot(
        self, runtime_state: RuntimeState, params: dict
    ) -> Snapshot:
        snap = Snapshot(
            id=str(uuid4()),
            tick_id=runtime_state.tick_id,
            world_time_seconds=runtime_state.world_time_seconds,
            created_at=_utc_now_iso(),
            runtime_state=RuntimeStateSnapshot(
                tick_id=runtime_state.tick_id,
                world_time_seconds=runtime_state.world_time_seconds,
                step_seconds=runtime_state.step_seconds,
                updated_at=runtime_state.updated_at,
            ),
            params=deepcopy(params),
        )
        self._snapshot_store.save(snap)
        return snap

    def _create_summary(self, from_tick: int, to_tick: int) -> Summary:
        all_events: List[Event] = [
            e
            for e in self._event_log.snapshot()
            if from_tick <= e.tick_id <= to_tick
        ]

        type_counts: Counter[str] = Counter()
        for e in all_events:
            type_counts[e.type] += 1

        stats = SummaryStats(
            total_events=len(all_events),
            type_counts=dict(type_counts),
        )

        text = _build_summary_text(from_tick, to_tick, all_events, stats)

        summary = Summary(
            id=str(uuid4()),
            from_tick=from_tick,
            to_tick=to_tick,
            created_at=_utc_now_iso(),
            text=text,
            stats=stats,
        )
        self._summary_store.save(summary)
        return summary


def _build_summary_text(
    from_tick: int,
    to_tick: int,
    events: List[Event],
    stats: SummaryStats,
) -> str:
    parts: List[str] = []
    parts.append(f"Ticks {from_tick}-{to_tick}: total {stats.total_events} events.")

    # Type counts sorted by count descending
    sorted_types = sorted(stats.type_counts.items(), key=lambda kv: -kv[1])
    type_parts = [f"{t}={c}" for t, c in sorted_types]
    if type_parts:
        parts.append(", ".join(type_parts) + ".")

    # Extract counter info from module.counter events
    counter_events = [e for e in events if e.type == "module.counter"]
    if counter_events:
        last_counter = counter_events[-1]
        counter_val = last_counter.payload.get("counter")
        increment = last_counter.payload.get("increment")
        if counter_val is not None:
            detail = f"Counter reached {counter_val}"
            if increment is not None:
                detail += f" (increment={increment})"
            parts.append(detail + ".")

    # Count params.applied
    params_applied_count = stats.type_counts.get("params.applied", 0)
    if params_applied_count:
        parts.append(f"Params changed {params_applied_count} time(s).")

    return " ".join(parts)
