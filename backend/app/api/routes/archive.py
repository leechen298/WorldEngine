from typing import Literal, Optional

from fastapi import APIRouter, Depends, Request
from starlette.exceptions import HTTPException

from app.schemas.api import ApiResponse
from app.schemas.snapshot import Snapshot, SnapshotList
from app.schemas.summary import Summary, SummaryList
from app.world.storage.snapshot_store import InMemorySnapshotStore
from app.world.storage.summary_store import InMemorySummaryStore

router = APIRouter(prefix="/world", tags=["archive"])


def get_snapshot_store(request: Request) -> InMemorySnapshotStore:
    return request.app.state.snapshot_store


def get_summary_store(request: Request) -> InMemorySummaryStore:
    return request.app.state.summary_store


@router.get("/snapshots", response_model=ApiResponse[SnapshotList])
def list_snapshots(
    from_tick: Optional[int] = None,
    to_tick: Optional[int] = None,
    limit: int = 200,
    order: Literal["asc", "desc"] = "asc",
    store: InMemorySnapshotStore = Depends(get_snapshot_store),
) -> ApiResponse[SnapshotList]:
    items, total = store.list(from_tick=from_tick, to_tick=to_tick, limit=limit, order=order)
    return ApiResponse(data=SnapshotList(items=items, total=total))


@router.get("/snapshots/{snapshot_id}", response_model=ApiResponse[Snapshot])
def get_snapshot(
    snapshot_id: str,
    store: InMemorySnapshotStore = Depends(get_snapshot_store),
) -> ApiResponse[Snapshot]:
    snapshot = store.get(snapshot_id)
    if snapshot is None:
        raise HTTPException(status_code=404, detail=f"Snapshot not found: {snapshot_id}")
    return ApiResponse(data=snapshot)


@router.get("/summaries", response_model=ApiResponse[SummaryList])
def list_summaries(
    limit: int = 200,
    order: Literal["asc", "desc"] = "asc",
    store: InMemorySummaryStore = Depends(get_summary_store),
) -> ApiResponse[SummaryList]:
    items, total = store.list(limit=limit, order=order)
    return ApiResponse(data=SummaryList(items=items, total=total))


@router.get("/summaries/{summary_id}", response_model=ApiResponse[Summary])
def get_summary(
    summary_id: str,
    store: InMemorySummaryStore = Depends(get_summary_store),
) -> ApiResponse[Summary]:
    summary = store.get(summary_id)
    if summary is None:
        raise HTTPException(status_code=404, detail=f"Summary not found: {summary_id}")
    return ApiResponse(data=summary)
