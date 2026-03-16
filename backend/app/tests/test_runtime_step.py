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

    events = payload["data"]["items"]
    tick_advanced_events = [event for event in events if event["type"] == "tick.advanced"]
    assert len(tick_advanced_events) == 3
    assert [event["tick_id"] for event in tick_advanced_events] == [3, 2, 1]
    assert payload["data"]["has_more"] is False
    assert payload["data"]["next_cursor"] is None
    assert payload["data"]["limit"] == 20


def test_world_events_endpoint_applies_filters() -> None:
    app = create_app()
    client = TestClient(app)

    for _ in range(4):
        client.post("/runtime/step")

    filtered_response = client.get("/world/events?from_tick=2&to_tick=3")
    assert filtered_response.status_code == 200
    filtered_events = filtered_response.json()["data"]["items"]
    assert filtered_events
    assert all(2 <= event["tick_id"] <= 3 for event in filtered_events)
    filtered_tick_ids = [event["tick_id"] for event in filtered_events]
    assert filtered_tick_ids == sorted(filtered_tick_ids, reverse=True)

    full_response = client.get("/world/events")
    assert full_response.status_code == 200
    full_events = full_response.json()["data"]["items"]
    limited_response = client.get("/world/events?limit=2")
    assert limited_response.status_code == 200
    limited_payload = limited_response.json()["data"]
    limited_events = limited_payload["items"]
    assert len(limited_events) == 2
    assert [event["id"] for event in limited_events] == [event["id"] for event in full_events[:2]]
    assert limited_payload["has_more"] is True
    assert limited_payload["next_cursor"] == limited_events[-1]["id"]


def test_world_events_endpoint_supports_cursor_pagination() -> None:
    app = create_app()
    client = TestClient(app)

    for _ in range(5):
        response = client.post("/runtime/step")
        assert response.status_code == 200

    full_response = client.get("/world/events")
    assert full_response.status_code == 200
    full_events = full_response.json()["data"]["items"]

    first_page_response = client.get("/world/events?limit=2")
    assert first_page_response.status_code == 200
    first_page = first_page_response.json()["data"]
    assert [event["id"] for event in first_page["items"]] == [event["id"] for event in full_events[:2]]
    assert first_page["has_more"] is True

    second_page_response = client.get(
        f"/world/events?limit=2&cursor={first_page['next_cursor']}"
    )
    assert second_page_response.status_code == 200
    second_page = second_page_response.json()["data"]
    assert [event["id"] for event in second_page["items"]] == [event["id"] for event in full_events[2:4]]
    assert second_page["has_more"] is True

    third_page_response = client.get(
        f"/world/events?limit=2&cursor={second_page['next_cursor']}"
    )
    assert third_page_response.status_code == 200
    third_page = third_page_response.json()["data"]
    assert [event["id"] for event in third_page["items"]] == [event["id"] for event in full_events[4:6]]


def test_world_event_steps_endpoint_returns_grouped_steps() -> None:
    app = create_app()
    client = TestClient(app)

    for _ in range(3):
        response = client.post("/runtime/step")
        assert response.status_code == 200

    response = client.get("/world/event-steps")
    assert response.status_code == 200

    payload = response.json()
    assert payload["code"] == 0

    steps = payload["data"]["items"]
    assert [step["tick_id"] for step in steps] == [3, 2, 1]
    assert all(step["event_count"] == len(step["items"]) for step in steps)
    assert all(step["items"][0]["tick_id"] == step["tick_id"] for step in steps)
    assert payload["data"]["has_more"] is False
    assert payload["data"]["next_cursor"] is None


def test_world_event_steps_endpoint_supports_cursor_pagination() -> None:
    app = create_app()
    client = TestClient(app)

    for _ in range(5):
        response = client.post("/runtime/step")
        assert response.status_code == 200

    first_page_response = client.get("/world/event-steps?limit=2")
    assert first_page_response.status_code == 200
    first_page = first_page_response.json()["data"]
    assert [step["tick_id"] for step in first_page["items"]] == [5, 4]
    assert first_page["has_more"] is True
    assert first_page["next_cursor"] == "4"

    second_page_response = client.get(f"/world/event-steps?limit=2&cursor={first_page['next_cursor']}")
    assert second_page_response.status_code == 200
    second_page = second_page_response.json()["data"]
    assert [step["tick_id"] for step in second_page["items"]] == [3, 2]
    assert second_page["has_more"] is True


def test_world_event_steps_endpoint_rejects_unknown_cursor() -> None:
    app = create_app()
    client = TestClient(app)

    response = client.get("/world/event-steps?cursor=missing-step")

    assert response.status_code == 400
    payload = response.json()
    assert payload["code"] == 10
    assert payload["msg"] == "Unknown cursor: missing-step"


def test_world_events_endpoint_rejects_unknown_cursor() -> None:
    app = create_app()
    client = TestClient(app)

    response = client.get("/world/events?cursor=missing-event-id")

    assert response.status_code == 400
    payload = response.json()
    assert payload["code"] == 10
    assert payload["msg"] == "Unknown cursor: missing-event-id"


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
