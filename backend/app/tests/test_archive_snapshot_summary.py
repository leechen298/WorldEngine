"""Tests for Step 6: archive snapshots and chunk summaries."""

from fastapi.testclient import TestClient

from app.api.app_factory import create_app
from app.core.event_bus import InMemoryEventLog
from app.core.runtime_engine import RuntimeEngine
from app.world.archive import ArchiveService
from app.world.service import get_default_module_tree
from app.world.state import WorldState
from app.world.storage import InMemorySnapshotStore, InMemorySummaryStore


# ---------------------------------------------------------------------------
# Helper: build a minimal engine with archive wired in
# ---------------------------------------------------------------------------

def _make_engine(
    snapshot_interval: int = 10,
    summary_interval: int = 20,
    step_seconds: int = 600,
):
    event_log = InMemoryEventLog()
    world_state = WorldState()
    root = get_default_module_tree()
    snap_store = InMemorySnapshotStore()
    summ_store = InMemorySummaryStore()

    engine = RuntimeEngine(
        step_seconds=step_seconds,
        event_log=event_log,
        world_root_module=root,
        params_provider=world_state.get_params,
    )
    archive = ArchiveService(
        snapshot_store=snap_store,
        summary_store=summ_store,
        event_log=event_log,
        snapshot_interval=snapshot_interval,
        summary_interval=summary_interval,
    )
    engine.add_on_step_callback(archive.on_tick_completed)
    return engine, snap_store, summ_store


# ---------------------------------------------------------------------------
# Unit tests: snapshot interval
# ---------------------------------------------------------------------------

def test_snapshot_interval_creates_at_correct_ticks():
    engine, snap_store, _ = _make_engine(snapshot_interval=2, summary_interval=100)

    for _ in range(5):
        engine.step()

    items, total = snap_store.list()
    assert total == 2  # tick 2 and tick 4
    assert [s.tick_id for s in items] == [2, 4]


def test_snapshot_contains_runtime_state_and_params():
    engine, snap_store, _ = _make_engine(snapshot_interval=1, summary_interval=100)
    engine.step()

    items, _ = snap_store.list()
    snap = items[0]
    assert snap.tick_id == 1
    assert snap.runtime_state.tick_id == 1
    assert snap.runtime_state.step_seconds == 600
    assert isinstance(snap.params, dict)


# ---------------------------------------------------------------------------
# Unit tests: summary interval
# ---------------------------------------------------------------------------

def test_summary_interval_creates_at_correct_ticks():
    engine, _, summ_store = _make_engine(snapshot_interval=100, summary_interval=3)

    for _ in range(7):
        engine.step()

    items, total = summ_store.list()
    assert total == 2  # ticks 1-3 and 4-6
    assert items[0].from_tick == 1
    assert items[0].to_tick == 3
    assert items[1].from_tick == 4
    assert items[1].to_tick == 6


def test_summary_stats_has_type_counts():
    engine, _, summ_store = _make_engine(snapshot_interval=100, summary_interval=3)

    for _ in range(3):
        engine.step()

    items, _ = summ_store.list()
    summary = items[0]
    assert summary.stats.total_events > 0
    assert "tick.advanced" in summary.stats.type_counts
    assert summary.stats.type_counts["tick.advanced"] == 3


def test_summary_text_contains_tick_range():
    engine, _, summ_store = _make_engine(snapshot_interval=100, summary_interval=3)

    for _ in range(3):
        engine.step()

    items, _ = summ_store.list()
    assert "Ticks 1-3" in items[0].text


def test_summary_text_mentions_counter():
    engine, _, summ_store = _make_engine(snapshot_interval=100, summary_interval=3)

    for _ in range(3):
        engine.step()

    items, _ = summ_store.list()
    assert "Counter reached" in items[0].text


# ---------------------------------------------------------------------------
# Integration tests: API endpoints
# ---------------------------------------------------------------------------

def _step_app(client: TestClient, n: int) -> None:
    for _ in range(n):
        resp = client.post("/runtime/step")
        assert resp.status_code == 200


def test_api_snapshots_list(monkeypatch):
    monkeypatch.setenv("WORLD_SNAPSHOT_INTERVAL_TICKS", "2")
    monkeypatch.setenv("WORLD_SUMMARY_INTERVAL_TICKS", "100")
    app = create_app()
    client = TestClient(app)

    _step_app(client, 5)

    resp = client.get("/world/snapshots")
    assert resp.status_code == 200
    payload = resp.json()
    assert payload["code"] == 0
    data = payload["data"]
    assert data["total"] == 2
    assert len(data["items"]) == 2
    assert [s["tick_id"] for s in data["items"]] == [2, 4]


def test_api_snapshots_filter_by_tick(monkeypatch):
    monkeypatch.setenv("WORLD_SNAPSHOT_INTERVAL_TICKS", "2")
    monkeypatch.setenv("WORLD_SUMMARY_INTERVAL_TICKS", "100")
    app = create_app()
    client = TestClient(app)

    _step_app(client, 6)

    resp = client.get("/world/snapshots?from_tick=3&to_tick=5")
    assert resp.status_code == 200
    data = resp.json()["data"]
    assert data["total"] == 1
    assert data["items"][0]["tick_id"] == 4


def test_api_snapshot_get_by_id(monkeypatch):
    monkeypatch.setenv("WORLD_SNAPSHOT_INTERVAL_TICKS", "1")
    monkeypatch.setenv("WORLD_SUMMARY_INTERVAL_TICKS", "100")
    app = create_app()
    client = TestClient(app)

    _step_app(client, 1)

    list_resp = client.get("/world/snapshots")
    snap_id = list_resp.json()["data"]["items"][0]["id"]

    resp = client.get(f"/world/snapshots/{snap_id}")
    assert resp.status_code == 200
    assert resp.json()["data"]["id"] == snap_id


def test_api_snapshot_not_found():
    app = create_app()
    client = TestClient(app)

    resp = client.get("/world/snapshots/nonexistent")
    assert resp.status_code == 404
    assert resp.json()["code"] == 24


def test_api_summaries_list(monkeypatch):
    monkeypatch.setenv("WORLD_SNAPSHOT_INTERVAL_TICKS", "100")
    monkeypatch.setenv("WORLD_SUMMARY_INTERVAL_TICKS", "3")
    app = create_app()
    client = TestClient(app)

    _step_app(client, 3)

    resp = client.get("/world/summaries")
    assert resp.status_code == 200
    payload = resp.json()
    assert payload["code"] == 0
    data = payload["data"]
    assert data["total"] >= 1
    summary = data["items"][0]
    assert summary["from_tick"] == 1
    assert summary["to_tick"] == 3
    assert summary["stats"]["total_events"] > 0
    assert "tick.advanced" in summary["stats"]["type_counts"]


def test_api_summary_get_by_id(monkeypatch):
    monkeypatch.setenv("WORLD_SNAPSHOT_INTERVAL_TICKS", "100")
    monkeypatch.setenv("WORLD_SUMMARY_INTERVAL_TICKS", "3")
    app = create_app()
    client = TestClient(app)

    _step_app(client, 3)

    list_resp = client.get("/world/summaries")
    summary_id = list_resp.json()["data"]["items"][0]["id"]

    resp = client.get(f"/world/summaries/{summary_id}")
    assert resp.status_code == 200
    assert resp.json()["data"]["id"] == summary_id


def test_api_summary_not_found():
    app = create_app()
    client = TestClient(app)

    resp = client.get("/world/summaries/nonexistent")
    assert resp.status_code == 404
    assert resp.json()["code"] == 24


def test_api_response_shape_items_and_total(monkeypatch):
    """Verify both list endpoints return data.items + data.total."""
    monkeypatch.setenv("WORLD_SNAPSHOT_INTERVAL_TICKS", "2")
    monkeypatch.setenv("WORLD_SUMMARY_INTERVAL_TICKS", "4")
    app = create_app()
    client = TestClient(app)

    _step_app(client, 4)

    for path in ["/world/snapshots", "/world/summaries"]:
        resp = client.get(path)
        assert resp.status_code == 200
        data = resp.json()["data"]
        assert "items" in data
        assert "total" in data
        assert isinstance(data["items"], list)
        assert isinstance(data["total"], int)
