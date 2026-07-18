from __future__ import annotations

from fastapi.testclient import TestClient

from app.api.app_factory import create_app


PRIVATE_PUBLIC_MARKERS = (
    "api_key",
    "authorization",
    "hidden context",
    "private memory",
    "provider_trace",
    "raw_prompt",
    "raw provider response",
    "sk-live-secret",
)


def _client() -> TestClient:
    return TestClient(create_app())


def _create_session(client: TestClient, world_id: str = "world-inspection") -> str:
    response = client.post("/sessions", json={"world_id": world_id})
    assert response.status_code == 200
    return response.json()["data"]["session_id"]


def _serialized(value: object) -> str:
    return str(value).lower()


def _event_items(client: TestClient) -> list[dict]:
    return client.get("/world/events?limit=200").json()["data"]["items"]


def _seed_agent_evidence(client: TestClient, session_id: str) -> None:
    client.post("/runtime/step")
    step = client.post(
        f"/sessions/{session_id}/agents/agent.observer/step",
        json={"event_limit": 10},
    )
    assert step.status_code == 200
    rest = client.post(
        f"/sessions/{session_id}/agents/agent.observer/step",
        json={"mode_hint": "rest"},
    )
    assert rest.status_code == 200
    consolidation = client.post(
        f"/sessions/{session_id}/agents/agent.observer/memory/consolidate",
        json={"mode": "rest", "event_limit": 20},
    )
    assert consolidation.status_code == 200


def test_session_narrative_projection_accepts_public_filters_and_stays_read_only() -> None:
    client = _client()
    session_id = _create_session(client)
    _seed_agent_evidence(client, session_id)
    before_events = len(_event_items(client))
    before_memory = client.get(
        f"/sessions/{session_id}/agents/agent.observer/memory"
    ).json()["data"]
    before_directions = client.get(f"/sessions/{session_id}/directions").json()["data"]

    response = client.post(
        f"/sessions/{session_id}/narrative/project",
        json={
            "tick_start": 0,
            "tick_end": 5,
            "branch_id": "branch-public-a",
            "agent_id": "agent.observer",
            "summary_hint": "Summarize public Agent behavior.",
        },
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = _serialized(payload)
    data = payload["data"]
    assert data["session_id"] == session_id
    assert data["world_id"] == "world-inspection"
    assert data["agent_id"] == "agent.observer"
    assert data["status"] == "accepted"
    assert data["tick_range"] == {"start": 0, "end": 5}
    assert data["branch_id"] == "branch-public-a"
    assert data["inspection_provenance"] == "worldengine_public_evidence"
    assert data["public_narrative_summary"]
    assert data["source_event_refs"]
    assert data["source_agent_refs"]
    assert data["source_memory_refs"]
    assert all(ref["ref_type"] == "summary" for ref in data["source_memory_refs"])
    assert data["canonical_state_mutation_applied"] is False
    assert data["canonical_event_appended"] is False
    assert data["agent_memory_write_applied"] is False
    assert data["in_world_dialogue_recorded"] is False
    assert data["redaction_status"] == "passed"
    assert len(_event_items(client)) == before_events
    assert client.get(f"/sessions/{session_id}/directions").json()["data"] == before_directions
    assert (
        client.get(f"/sessions/{session_id}/agents/agent.observer/memory").json()["data"]
        == before_memory
    )
    assert not any(marker in serialized for marker in PRIVATE_PUBLIC_MARKERS)


def test_session_diagnostic_inspection_uses_public_evidence_and_is_out_of_world() -> None:
    client = _client()
    session_id = _create_session(client)
    _seed_agent_evidence(client, session_id)
    before_events = len(_event_items(client))
    before_memory = client.get(
        f"/sessions/{session_id}/agents/agent.observer/memory"
    ).json()["data"]

    response = client.post(
        f"/sessions/{session_id}/diagnostics/inspect",
        json={
            "question_summary": "What public Agent evidence exists?",
            "tick_start": 0,
            "tick_end": 5,
            "agent_id": "agent.observer",
        },
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = _serialized(payload)
    data = payload["data"]
    assert data["session_id"] == session_id
    assert data["agent_id"] == "agent.observer"
    assert data["status"] == "accepted"
    assert data["classification"] == "out_of_world_diagnostic"
    assert data["public_answer_summary"]
    assert data["source_event_refs"]
    assert data["source_agent_refs"]
    assert data["agent_memory_write_applied"] is False
    assert data["in_world_dialogue_recorded"] is False
    assert len(_event_items(client)) == before_events
    assert (
        client.get(f"/sessions/{session_id}/agents/agent.observer/memory").json()["data"]
        == before_memory
    )
    assert not any(marker in serialized for marker in PRIVATE_PUBLIC_MARKERS)


def test_session_inspection_rejects_missing_public_evidence_and_invalid_tick_range() -> None:
    client = _client()
    session_id = _create_session(client)

    missing = client.post(
        f"/sessions/{session_id}/narrative/project",
        json={"tick_start": 99, "tick_end": 100, "agent_id": "agent.observer"},
    )
    invalid_range = client.post(
        f"/sessions/{session_id}/diagnostics/inspect",
        json={"question_summary": "What happened?", "tick_start": 5, "tick_end": 1},
    )

    assert missing.status_code == 200
    assert missing.json()["data"]["status"] == "rejected"
    assert "missing_public_evidence_ref" in {
        diagnostic["code"] for diagnostic in missing.json()["data"]["diagnostics"]
    }
    assert invalid_range.status_code == 200
    assert invalid_range.json()["data"]["status"] == "rejected"
    assert "invalid_tick_range" in {
        diagnostic["code"] for diagnostic in invalid_range.json()["data"]["diagnostics"]
    }


def test_session_inspection_rejects_fake_caller_supplied_refs() -> None:
    client = _client()
    session_id = _create_session(client)
    _seed_agent_evidence(client, session_id)

    response = client.post(
        f"/sessions/{session_id}/narrative/project",
        json={
            "tick_start": 0,
            "tick_end": 5,
            "agent_id": "agent.observer",
            "source_event_refs": [
                {"ref_id": "fake-event", "ref_type": "event", "role": "source"}
            ],
        },
    )

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["status"] == "rejected"
    assert "non_canonical_public_ref" in {
        diagnostic["code"] for diagnostic in data["diagnostics"]
    }


def test_session_inspection_rejects_private_markers_without_echo() -> None:
    client = _client()
    session_id = _create_session(client)

    response = client.post(
        f"/sessions/{session_id}/diagnostics/inspect",
        json={
            "question_summary": "raw_prompt provider_trace sk-live-secret",
            "agent_id": "agent.observer",
        },
    )

    assert response.status_code == 422
    payload = response.json()
    serialized = _serialized(payload)
    assert payload["code"] == 30
    assert "raw_prompt" not in serialized
    assert "provider_trace" not in serialized
    assert "sk-live-secret" not in serialized
    assert "input" not in payload["data"]["errors"][0]


def test_session_inspection_rejects_mutation_flags_without_side_effects() -> None:
    client = _client()
    session_id = _create_session(client)
    _seed_agent_evidence(client, session_id)
    before_events = len(_event_items(client))
    before_directions = client.get(f"/sessions/{session_id}/directions").json()["data"]

    response = client.post(
        f"/sessions/{session_id}/narrative/project",
        json={
            "tick_start": 0,
            "tick_end": 5,
            "agent_id": "agent.observer",
            "canonical_event_appended": True,
            "agent_memory_write_applied": True,
        },
    )

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["status"] == "rejected"
    assert "canonical_mutation_attempt" in {
        diagnostic["code"] for diagnostic in data["diagnostics"]
    }
    assert len(_event_items(client)) == before_events
    assert client.get(f"/sessions/{session_id}/directions").json()["data"] == before_directions


def test_manifest_exposes_session_inspection_surfaces() -> None:
    client = _client()

    response = client.get("/manifest")

    assert response.status_code == 200
    surfaces = response.json()["public_surfaces"]
    assert {
        "path": "/sessions/{session_id}/narrative/project",
        "method": "POST",
        "operation_id": "project_session_narrative",
        "status": "available",
        "maturity": "implemented",
        "validation_status": "pass",
        "required_for_mvp": False,
        "notes": ["session-scoped read-only narrative inspection surface"],
    } in surfaces
    assert {
        "path": "/sessions/{session_id}/diagnostics/inspect",
        "method": "POST",
        "operation_id": "inspect_session_diagnostics",
        "status": "available",
        "maturity": "implemented",
        "validation_status": "pass",
        "required_for_mvp": False,
        "notes": ["session-scoped out-of-world diagnostic inspection surface"],
    } in surfaces
