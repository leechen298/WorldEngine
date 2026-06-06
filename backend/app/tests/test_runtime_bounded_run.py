from __future__ import annotations

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from app.api.app_factory import create_app
from app.core.runtime_engine import RuntimeEngine
from app.schemas.runtime import RuntimeRunRequest


def test_runtime_engine_runs_bounded_ticks_and_returns_public_summary() -> None:
    engine = RuntimeEngine(step_seconds=300)

    summary = engine.run_bounded(RuntimeRunRequest(ticks=3, max_ticks=5))

    assert summary.status == "completed"
    assert summary.stop_reason == "requested_ticks_reached"
    assert summary.start_tick == 0
    assert summary.end_tick == 3
    assert summary.ticks_requested == 3
    assert summary.ticks_executed == 3
    assert summary.start_world_time_seconds == 0
    assert summary.end_world_time_seconds == 900
    assert summary.provider_calls_used == 0
    assert summary.estimated_cost_units_used == 0
    assert summary.redaction_status == "passed"
    assert summary.control_status == "idle"
    assert engine.get_state().tick_id == 3


def test_runtime_engine_runs_bounded_duration_by_existing_step_seconds() -> None:
    engine = RuntimeEngine(step_seconds=300)

    summary = engine.run_bounded(
        RuntimeRunRequest(duration_seconds=750, max_duration_seconds=900, max_ticks=10)
    )

    assert summary.status == "completed"
    assert summary.stop_reason == "requested_duration_reached"
    assert summary.ticks_executed == 3
    assert summary.end_tick == 3
    assert summary.end_world_time_seconds == 900


def test_runtime_engine_pause_blocks_bounded_run_until_resume() -> None:
    engine = RuntimeEngine()
    paused = engine.pause()

    blocked = engine.run_bounded(RuntimeRunRequest(ticks=2))

    assert paused.status == "paused"
    assert blocked.status == "blocked"
    assert blocked.stop_reason == "paused"
    assert blocked.ticks_executed == 0
    assert blocked.control_status == "paused"
    assert engine.get_state().tick_id == 0

    resumed = engine.resume()
    summary = engine.run_bounded(RuntimeRunRequest(ticks=1))

    assert resumed.status == "idle"
    assert summary.status == "completed"
    assert summary.ticks_executed == 1


def test_runtime_run_request_rejects_unbounded_or_over_guard_requests() -> None:
    with pytest.raises(ValidationError):
        RuntimeRunRequest()

    with pytest.raises(ValidationError):
        RuntimeRunRequest(ticks=1, duration_seconds=600)

    with pytest.raises(ValidationError):
        RuntimeRunRequest(ticks=6, max_ticks=5)

    with pytest.raises(ValidationError):
        RuntimeRunRequest(duration_seconds=1200, max_duration_seconds=600)

    with pytest.raises(ValidationError):
        RuntimeRunRequest(ticks=1, unexpected=True)


def test_runtime_engine_tick_run_stops_at_max_duration_guard() -> None:
    engine = RuntimeEngine(step_seconds=600)

    summary = engine.run_bounded(
        RuntimeRunRequest(ticks=3, max_ticks=3, max_duration_seconds=1)
    )

    assert summary.status == "completed"
    assert summary.stop_reason == "max_duration_reached"
    assert summary.ticks_executed == 0
    assert summary.start_world_time_seconds == 0
    assert summary.end_world_time_seconds == 0


def test_runtime_run_api_advances_and_exposes_public_summary_fields() -> None:
    client = TestClient(create_app())

    response = client.post("/runtime/run", json={"ticks": 2, "max_ticks": 5})

    assert response.status_code == 200
    payload = response.json()
    assert payload["code"] == 0
    data = payload["data"]
    assert data["status"] == "completed"
    assert data["stop_reason"] == "requested_ticks_reached"
    assert data["start_tick"] == 0
    assert data["end_tick"] == 2
    assert data["ticks_requested"] == 2
    assert data["ticks_executed"] == 2
    assert data["provider_calls_used"] == 0
    assert data["estimated_cost_units_used"] == 0
    assert data["guard_summary"]["max_ticks"] == 5
    assert data["control_status"] == "idle"

    state = client.get("/runtime/state").json()["data"]
    assert state["tick_id"] == 2


def test_runtime_pause_resume_api_controls_bounded_run_without_breaking_step() -> None:
    client = TestClient(create_app())

    pause = client.post("/runtime/pause")
    assert pause.status_code == 200
    assert pause.json()["data"]["status"] == "paused"

    blocked = client.post("/runtime/run", json={"ticks": 2})
    assert blocked.status_code == 200
    blocked_data = blocked.json()["data"]
    assert blocked_data["status"] == "blocked"
    assert blocked_data["stop_reason"] == "paused"
    assert blocked_data["ticks_executed"] == 0

    step = client.post("/runtime/step")
    assert step.status_code == 200
    assert step.json()["data"]["tick_id"] == 1

    resume = client.post("/runtime/resume")
    assert resume.status_code == 200
    assert resume.json()["data"]["status"] == "idle"

    run = client.post("/runtime/run", json={"ticks": 1})
    assert run.status_code == 200
    assert run.json()["data"]["ticks_executed"] == 1


def test_runtime_run_api_rejects_invalid_unbounded_requests() -> None:
    client = TestClient(create_app())

    response = client.post("/runtime/run", json={})

    assert response.status_code == 422
    payload = response.json()
    assert payload["code"] == 30
    serialized = str(payload).lower()
    assert "run request" in serialized

    extra_response = client.post("/runtime/run", json={"ticks": 1, "extra": True})
    assert extra_response.status_code == 422
    extra_payload = extra_response.json()
    assert extra_payload["code"] == 30
    assert "extra" in str(extra_payload).lower()
