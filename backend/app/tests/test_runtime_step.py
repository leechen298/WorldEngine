from fastapi.testclient import TestClient

from app.api.app_factory import create_app
from app.core.event_bus import InMemoryEventLog
from app.core.runtime_engine import RuntimeEngine


def test_runtime_engine_initial_state() -> None:
    engine = RuntimeEngine()
    state = engine.get_state()

    assert state.tick_id == 0
    assert state.world_time_seconds == 0
    assert state.step_seconds == 600


def test_runtime_engine_step_advances_tick_and_time() -> None:
    engine = RuntimeEngine(step_seconds=600)

    first_state = engine.step()
    assert first_state.tick_id == 1
    assert first_state.world_time_seconds == 600

    second_state = engine.step()
    assert second_state.tick_id == 2
    assert second_state.world_time_seconds == 1200


def test_runtime_engine_step_appends_tick_advanced_event() -> None:
    event_log = InMemoryEventLog()
    engine = RuntimeEngine(step_seconds=600, event_log=event_log)

    engine.step()

    events = event_log.list()
    assert len(events) >= 1
    assert events[0].type == "tick.advanced"
    assert events[0].tick_id == 1
    assert events[0].world_time_seconds == 600


def test_runtime_engine_from_env_uses_world_step_seconds(monkeypatch) -> None:
    monkeypatch.setenv("WORLD_STEP_SECONDS", "60")

    engine = RuntimeEngine.from_env()
    state = engine.get_state()

    assert state.step_seconds == 60


def test_runtime_state_endpoint_returns_initial_state() -> None:
    app = create_app()
    client = TestClient(app)

    response = client.get("/runtime/state")
    assert response.status_code == 200

    payload = response.json()
    assert payload["code"] == 0
    assert payload["msg"] == "ok"
    assert payload["data"]["tick_id"] == 0
    assert payload["data"]["world_time_seconds"] == 0
    assert payload["data"]["updated_at"] is not None
    assert "tick_id" in payload["data"]


def test_health_endpoint_returns_api_envelope() -> None:
    app = create_app()
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["code"] == 0
    assert payload["msg"] == "ok"
    assert payload["data"]["status"] == "ok"
    assert payload["data"]["service"] == "worldengine-backend"


def test_runtime_step_endpoint_increments_tick() -> None:
    app = create_app()
    client = TestClient(app)

    before_step = client.get("/runtime/state").json()["data"]
    step_response = client.post("/runtime/step")
    assert step_response.status_code == 200

    payload = step_response.json()
    assert payload["code"] == 0
    assert payload["data"]["tick_id"] == before_step["tick_id"] + 1
    assert payload["data"]["world_time_seconds"] == (
        before_step["world_time_seconds"] + payload["data"]["step_seconds"]
    )
    assert payload["data"]["updated_at"] is not None


def test_world_events_endpoint_returns_step_timeline() -> None:
    app = create_app()
    client = TestClient(app)

    for _ in range(3):
        response = client.post("/runtime/step")
        assert response.status_code == 200

    events_response = client.get("/world/events")
    assert events_response.status_code == 200

    payload = events_response.json()
    assert payload["code"] == 0

    events = payload["data"]
    tick_advanced_events = [event for event in events if event["type"] == "tick.advanced"]
    assert len(tick_advanced_events) == 3
    assert [event["tick_id"] for event in tick_advanced_events] == [1, 2, 3]


def test_world_events_endpoint_applies_filters() -> None:
    app = create_app()
    client = TestClient(app)

    for _ in range(4):
        client.post("/runtime/step")

    filtered_response = client.get("/world/events?from_tick=2&to_tick=3")
    assert filtered_response.status_code == 200
    filtered_events = filtered_response.json()["data"]
    assert filtered_events
    assert all(2 <= event["tick_id"] <= 3 for event in filtered_events)

    full_response = client.get("/world/events")
    assert full_response.status_code == 200
    full_events = full_response.json()["data"]
    limited_response = client.get("/world/events?limit=2")
    assert limited_response.status_code == 200
    limited_events = limited_response.json()["data"]
    assert len(limited_events) == 2
    assert [event["id"] for event in limited_events] == [event["id"] for event in full_events[:2]]


def test_validation_errors_use_api_error_shape() -> None:
    app = create_app()
    client = TestClient(app)

    response = client.get("/world/events?limit=0")

    assert response.status_code == 422
    payload = response.json()
    assert payload["code"] == 30
    assert payload["msg"]
    assert "errors" in payload["data"]


def test_not_found_errors_use_api_error_shape() -> None:
    app = create_app()
    client = TestClient(app)

    response = client.get("/missing-route")

    assert response.status_code == 404
    payload = response.json()
    assert payload["code"] == 24
    assert payload["msg"] == "Not Found"
    assert payload["data"] is None
