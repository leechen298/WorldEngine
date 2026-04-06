from __future__ import annotations

from typing import Dict, List, Optional, Tuple

from app.schemas.snapshot import Snapshot


class InMemorySnapshotStore:
    """Append-only in-memory store for world snapshots."""

    def __init__(self) -> None:
        self._snapshots: List[Snapshot] = []
        self._index_by_id: Dict[str, int] = {}

    def save(self, snapshot: Snapshot) -> None:
        self._index_by_id[snapshot.id] = len(self._snapshots)
        self._snapshots.append(snapshot)

    def list(
        self,
        *,
        from_tick: Optional[int] = None,
        to_tick: Optional[int] = None,
        limit: int = 200,
        order: str = "asc",
    ) -> Tuple[List[Snapshot], int]:
        capped = max(1, min(limit, 200))
        filtered = [
            s
            for s in self._snapshots
            if (from_tick is None or s.tick_id >= from_tick)
            and (to_tick is None or s.tick_id <= to_tick)
        ]
        if order == "desc":
            return list(reversed(filtered))[:capped], len(filtered)
        return filtered[:capped], len(filtered)

    def get(self, snapshot_id: str) -> Optional[Snapshot]:
        idx = self._index_by_id.get(snapshot_id)
        if idx is None:
            return None
        return self._snapshots[idx]
