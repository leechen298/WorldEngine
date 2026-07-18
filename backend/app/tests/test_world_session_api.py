from __future__ import annotations

from fastapi.testclient import TestClient

from app.api.app_factory import create_app


def _client() -> TestClient:
    return TestClient(create_app())


def test_create_world_session_returns_public_in_memory_contract() -> None:
    client = _client()

    response = client.post(
        "/sessions",
        json={"world_id": "world-alpha", "public_label": "Alpha session"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["code"] == 0
    data = payload["data"]
    serialized = str(payload).lower()
    assert data["session_id"].startswith("session-")
    assert data["world_id"] == "world-alpha"
    assert data["public_label"] == "Alpha session"
    assert data["status"] == "created"
    assert data["persistence"] == "in_memory"
    assert data["runtime_ref"]["tick_id"] == 0
    assert data["evidence_refs"]["event_count_at_create"] == 0
    assert data["evidence_refs"]["snapshot_count_at_create"] == 0
    assert "api_key" not in serialized
    assert "raw_prompt" not in serialized
    assert "provider_trace" not in serialized
    assert "private memory" not in serialized


def test_list_read_and_status_refresh_runtime_and_evidence_counts() -> None:
    client = _client()
    created = client.post("/sessions", json={}).json()["data"]
    session_id = created["session_id"]

    run = client.post("/runtime/step")
    assert run.status_code == 200

    listed = client.get("/sessions")
    assert listed.status_code == 200
    list_data = listed.json()["data"]
    assert list_data["total"] == 1
    assert list_data["items"][0]["session_id"] == session_id
    assert list_data["items"][0]["runtime_ref"]["tick_id"] == 1
    assert list_data["items"][0]["evidence_refs"]["event_count_at_create"] == 0
    assert list_data["items"][0]["evidence_refs"]["current_event_count"] >= 1

    read = client.get(f"/sessions/{session_id}")
    assert read.status_code == 200
    assert read.json()["data"]["runtime_ref"]["tick_id"] == 1

    status = client.get(f"/sessions/{session_id}/status")
    assert status.status_code == 200
    status_data = status.json()["data"]
    assert status_data["session_id"] == session_id
    assert status_data["status"] == "created"
    assert status_data["runtime_ref"]["tick_id"] == 1


def test_unknown_session_returns_existing_error_envelope() -> None:
    client = _client()

    response = client.get("/sessions/session-missing")

    assert response.status_code == 404
    payload = response.json()
    assert payload["code"] == 24
    assert payload["msg"] == "Unknown session_id"


def test_session_create_rejects_private_extra_fields_without_echoing_input() -> None:
    client = _client()

    response = client.post(
        "/sessions",
        json={
            "world_id": "world-alpha",
            "provider_trace": "sk-live-secret",
        },
    )

    assert response.status_code == 422
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["code"] == 30
    assert "provider_trace" not in serialized
    assert "sk-live-secret" not in serialized
    assert "input" not in payload["data"]["errors"][0]


def test_create_session_from_worldview_uses_deterministic_fallback_without_runtime_run(
    monkeypatch,
) -> None:
    monkeypatch.delenv("WORLDENGINE_LLM_PROVIDER", raising=False)
    monkeypatch.delenv("WORLDENGINE_LLM_MODEL", raising=False)
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)
    client = _client()

    response = client.post(
        "/sessions/from-worldview",
        json={
            "request_id": "worldview-session-1",
            "worldview_premise": "A public workshop world with shared tools",
            "public_constraints": {"scale": "small"},
        },
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    data = payload["data"]
    assert data["session_id"].startswith("session-")
    assert data["world_id"].startswith("world-")
    assert data["public_label"].startswith("generated-world-")
    assert data["status"] == "created"
    assert data["runtime_ref"]["tick_id"] == 0
    assert data["evidence_refs"]["event_count_at_create"] == 0
    summary = data["generation_summary"]
    assert summary["request_id"] == "worldview-session-1"
    assert summary["generation_status"] == "fallback"
    assert summary["generation_mode"] == "deterministic_fallback"
    assert summary["creation_mode"] == "deterministic_generic_fallback"
    assert summary["runtime_ready"] == "true"
    assert summary["provider_backed"] is False
    assert summary["llm_backed"] is False
    assert summary["deterministic_generic_fallback_detected"] is True
    assert summary["public_world_model_refs"]["title_label"] == data["public_label"]
    assert "api_key" not in serialized
    assert "raw_prompt" not in serialized
    assert "provider_trace" not in serialized

    listed = client.get("/sessions").json()["data"]
    assert listed["total"] == 1
    assert listed["items"][0]["session_id"] == data["session_id"]
    assert listed["items"][0]["generation_summary"]["generation_id"] == summary["generation_id"]


def test_create_session_from_worldview_blocks_configured_provider_without_live_call(
    monkeypatch,
) -> None:
    monkeypatch.setenv("WORLDENGINE_LLM_PROVIDER", "deepseek")
    monkeypatch.setenv("WORLDENGINE_LLM_MODEL", "sk-live-secret-model")
    monkeypatch.setenv("DEEPSEEK_API_KEY", "sk-live-secret-key")
    client = _client()

    response = client.post(
        "/sessions/from-worldview",
        json={
            "request_id": "worldview-session-blocked",
            "worldview_premise": "A public city world",
        },
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    data = payload["data"]
    assert data["status"] == "blocked"
    summary = data["generation_summary"]
    assert summary["generation_status"] == "blocked"
    assert summary["generation_mode"] == "blocked"
    assert summary["creation_mode"] == "blocked"
    assert summary["runtime_ready"] == "blocked"
    assert summary["provider_class"] == "deepseek_api"
    assert summary["provider_backed"] is False
    assert summary["llm_backed"] is False
    assert summary["blockers"] == ["live_provider_call_not_authorized"]
    assert "sk-live-secret-key" not in serialized
    assert "sk-live-secret-model" not in serialized
    assert "raw_response" not in serialized


def test_create_session_from_worldview_rejects_private_markers_without_echoing_input() -> None:
    client = _client()

    response = client.post(
        "/sessions/from-worldview",
        json={
            "request_id": "worldview-session-private",
            "worldview_premise": "raw_prompt contains provider_trace sk-live-secret",
        },
    )

    assert response.status_code == 422
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["code"] == 30
    assert "raw_prompt" not in serialized
    assert "provider_trace" not in serialized
    assert "sk-live-secret" not in serialized
    assert "input" not in payload["data"]["errors"][0]


def test_session_run_advances_bounded_ticks_and_returns_public_evidence(
    monkeypatch,
) -> None:
    monkeypatch.setenv("WORLD_SNAPSHOT_INTERVAL_TICKS", "1")
    client = _client()
    session = client.post("/sessions", json={"world_id": "world-run"}).json()["data"]
    session_id = session["session_id"]

    response = client.post(
        f"/sessions/{session_id}/run",
        json={"ticks": 2, "max_ticks": 5},
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    data = payload["data"]
    assert data["session_id"] == session_id
    assert data["world_id"] == "world-run"
    assert data["run_summary"]["status"] == "completed"
    assert data["run_summary"]["stop_reason"] == "requested_ticks_reached"
    assert data["run_summary"]["ticks_executed"] == 2
    assert data["runtime_delta"]["start_tick"] == 0
    assert data["runtime_delta"]["end_tick"] == 2
    assert data["event_evidence"]["event_delta_count"] >= 2
    assert data["snapshot_evidence"]["snapshot_delta_count"] == 2
    assert data["snapshot_evidence"]["snapshot_ids"]
    assert "timeline branch" in data["timeline_label"].lower()
    assert "parent" not in data["timeline_label"].lower()
    assert "source world" not in data["timeline_label"].lower()
    assert "api_key" not in serialized
    assert "raw_prompt" not in serialized
    assert "provider_trace" not in serialized

    status = client.get(f"/sessions/{session_id}/status").json()["data"]
    assert status["runtime_ref"]["tick_id"] == 2
    assert status["evidence_refs"]["current_snapshot_count"] == 2


def test_repeated_session_run_reports_new_snapshot_delta(monkeypatch) -> None:
    monkeypatch.setenv("WORLD_SNAPSHOT_INTERVAL_TICKS", "1")
    client = _client()
    session_id = client.post("/sessions", json={}).json()["data"]["session_id"]
    first = client.post(f"/sessions/{session_id}/run", json={"ticks": 2})
    assert first.status_code == 200
    assert first.json()["data"]["snapshot_evidence"]["snapshot_delta_count"] == 2

    second = client.post(f"/sessions/{session_id}/run", json={"ticks": 2})

    assert second.status_code == 200
    evidence = second.json()["data"]["snapshot_evidence"]
    assert evidence["snapshot_count_before"] == 2
    assert evidence["snapshot_count_after"] == 4
    assert evidence["snapshot_delta_count"] == 2
    assert len(evidence["snapshot_ids"]) == 2


def test_session_pause_blocks_run_until_resume() -> None:
    client = _client()
    session_id = client.post("/sessions", json={}).json()["data"]["session_id"]

    pause = client.post(f"/sessions/{session_id}/pause")
    assert pause.status_code == 200
    assert pause.json()["data"]["status"] == "paused"

    blocked = client.post(f"/sessions/{session_id}/run", json={"ticks": 2})
    assert blocked.status_code == 200
    blocked_data = blocked.json()["data"]
    assert blocked_data["run_summary"]["status"] == "blocked"
    assert blocked_data["run_summary"]["stop_reason"] == "paused"
    assert blocked_data["run_summary"]["ticks_executed"] == 0

    resume = client.post(f"/sessions/{session_id}/resume")
    assert resume.status_code == 200
    assert resume.json()["data"]["status"] == "ready"

    run = client.post(f"/sessions/{session_id}/run", json={"ticks": 1})
    assert run.status_code == 200
    assert run.json()["data"]["run_summary"]["ticks_executed"] == 1


def test_session_snapshots_list_returns_bounded_public_snapshot_view(monkeypatch) -> None:
    monkeypatch.setenv("WORLD_SNAPSHOT_INTERVAL_TICKS", "1")
    client = _client()
    session_id = client.post("/sessions", json={}).json()["data"]["session_id"]
    client.post(f"/sessions/{session_id}/run", json={"ticks": 3})

    response = client.get(f"/sessions/{session_id}/snapshots?limit=2&order=desc")

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    data = payload["data"]
    assert data["session_id"] == session_id
    assert data["total"] == 3
    assert len(data["items"]) == 2
    assert data["items"][0]["tick_id"] == 3
    assert data["items"][1]["tick_id"] == 2
    assert data["items"][0]["runtime_state"]["tick_id"] == 3
    assert data["timeline_label"].startswith("timeline branch")
    assert "api_key" not in serialized
    assert "raw_prompt" not in serialized
    assert "provider_trace" not in serialized


def test_session_runtime_routes_return_unknown_session_envelope() -> None:
    client = _client()

    run = client.post("/sessions/session-missing/run", json={"ticks": 1})
    pause = client.post("/sessions/session-missing/pause")
    snapshots = client.get("/sessions/session-missing/snapshots")

    assert run.status_code == 404
    assert pause.status_code == 404
    assert snapshots.status_code == 404
    assert run.json()["msg"] == "Unknown session_id"


def test_session_run_rejects_unbounded_request_with_sanitized_error() -> None:
    client = _client()
    session_id = client.post("/sessions", json={}).json()["data"]["session_id"]

    response = client.post(f"/sessions/{session_id}/run", json={})

    assert response.status_code == 422
    payload = response.json()
    assert payload["code"] == 30
    serialized = str(payload).lower()
    assert "runtime run request" in serialized
    assert "raw_prompt" not in serialized
