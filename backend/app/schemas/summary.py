from __future__ import annotations

from typing import Any, Dict, List

from pydantic import BaseModel


class SummaryStats(BaseModel):
    total_events: int
    type_counts: Dict[str, int]


class Summary(BaseModel):
    id: str
    from_tick: int
    to_tick: int
    created_at: str
    text: str
    stats: SummaryStats


class SummaryList(BaseModel):
    items: List[Summary]
    total: int
