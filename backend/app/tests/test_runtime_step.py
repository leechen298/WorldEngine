from fastapi.testclient import TestClient

from app.api.app_factory import create_app
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
    assert payload["tick_id"] == 0
    assert payload["world_time_seconds"] == 0
    assert payload["updated_at"] is not None
    assert "tick_id" in payload


def test_runtime_step_endpoint_increments_tick() -> None:
    app = create_app()
    client = TestClient(app)

    before_step = client.get("/runtime/state").json()
    step_response = client.post("/runtime/step")
    assert step_response.status_code == 200

    payload = step_response.json()
    assert payload["tick_id"] == before_step["tick_id"] + 1
    assert payload["world_time_seconds"] == (
        before_step["world_time_seconds"] + payload["step_seconds"]
    )
    assert payload["updated_at"] is not None
