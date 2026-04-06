from __future__ import annotations

from typing import Dict, List, Optional, Tuple

from app.schemas.summary import Summary


class InMemorySummaryStore:
    """Append-only in-memory store for chunk summaries."""

    def __init__(self) -> None:
        self._summaries: List[Summary] = []
        self._index_by_id: Dict[str, int] = {}

    def save(self, summary: Summary) -> None:
        self._index_by_id[summary.id] = len(self._summaries)
        self._summaries.append(summary)

    def list(self, *, limit: int = 200) -> Tuple[List[Summary], int]:
        capped = max(1, min(limit, 200))
        return self._summaries[:capped], len(self._summaries)

    def get(self, summary_id: str) -> Optional[Summary]:
        idx = self._index_by_id.get(summary_id)
        if idx is None:
            return None
        return self._summaries[idx]
