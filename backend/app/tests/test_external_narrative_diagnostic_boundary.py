from __future__ import annotations

from fastapi.testclient import TestClient
from pydantic import ValidationError
import pytest

from app.api.app_factory import create_app
from app.schemas.external_projection import (
    DiagnosticDialogueEvaluationRequest,
    NarrativeProjectionRequest,
)


def _client() -> TestClient:
    return TestClient(create_app())


def _ref(ref_id: str, ref_type: str = "event", role: str | None = None) -> dict:
    payload = {"ref_id": ref_id, "ref_type": ref_type}
    if role is not None:
        payload["role"] = role
    return payload


def _event_items(client: TestClient) -> list[dict]:
    return client.get("/world/events?limit=200").json()["data"]["items"]


def _post_projection(client: TestClient, payload: dict, *, world_id: str = "world-1"):
    return client.post(f"/worlds/{world_id}/narrative/project", json=payload)


def _post_diagnostic(
    client: TestClient,
    payload: dict,
    *,
    world_id: str = "world-1",
    agent_id: str = "agent.observer",
):
    return client.post(
        f"/worlds/{world_id}/agents/{agent_id}/diagnostics/dialogue/evaluate",
        json=payload,
    )


def test_projection_request_rejects_extra_fields() -> None:
    with pytest.raises(ValidationError):
        NarrativeProjectionRequest(
            public_narrative_summary="Public summary.",
            private_memory="hidden",
        )


def test_diagnostic_request_rejects_extra_fields() -> None:
    with pytest.raises(ValidationError):
        DiagnosticDialogueEvaluationRequest(
            question_summary="Public question.",
            response_summary="Public answer.",
            raw_provider_request="hidden",
        )


def test_projection_schema_rejects_private_markers() -> None:
    with pytest.raises(ValidationError):
        NarrativeProjectionRequest(public_narrative_summary="private memory should fail")


def test_projection_private_extra_field_name_is_redacted_from_http_validation_error() -> None:
    client = _client()

    response = _post_projection(
        client,
        {"public_narrative_summary": "Public summary.", "private_memory": "hidden"},
    )

    assert response.status_code == 422
    serialized = str(response.json()).lower()
    assert "private_memory" not in serialized
    assert "hidden" not in serialized
    assert "input" not in response.json()["data"]["errors"][0]


def test_raw_provider_request_extra_field_name_is_redacted_from_http_validation_error() -> None:
    client = _client()

    response = _post_projection(
        client,
        {
            "public_narrative_summary": "Public summary.",
            "raw_provider_request": "hidden request",
        },
    )

    assert response.status_code == 422
    serialized = str(response.json()).lower()
    assert "raw_provider_request" not in serialized
    assert "hidden request" not in serialized
    assert "input" not in response.json()["data"]["errors"][0]


def test_accepted_narrative_projection_uses_public_sources_and_does_not_mutate_state(
    monkeypatch,
) -> None:
    monkeypatch.setenv("WORLD_SNAPSHOT_INTERVAL_TICKS", "1")
    client = _client()
    step_response = client.post("/runtime/step")
    assert step_response.status_code == 200
    tick_event = next(event for event in _event_items(client) if event["type"] == "tick.advanced")
    snapshot_id = client.get("/world/snapshots").json()["data"]["items"][0]["id"]
    before_events = len(_event_items(client))

    response = _post_projection(
        client,
        {
            "public_narrative_summary": "Public projection says the world advanced one tick.",
            "projection_provenance": "worldengine_public_evidence",
            "source_event_refs": [_ref(tick_event["id"], "event", "source")],
            "source_snapshot_refs": [_ref(snapshot_id, "snapshot", "source")],
            "source_agent_continuity_refs": [
                _ref("continuity-public-1", "agent_continuity", "context")
            ],
        },
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["status"] == "accepted"
    artifact = payload["narrative_projection"]
    assert artifact["world_id"] == "world-1"
    assert artifact["source_event_refs"][0]["ref_id"] == tick_event["id"]
    assert artifact["source_snapshot_refs"][0]["ref_id"] == snapshot_id
    assert artifact["projection_provenance"] == "worldengine_public_evidence"
    assert payload["canonical_state_mutation_applied"] is False
    assert payload["canonical_event_appended"] is False
    assert payload["agent_memory_write_applied"] is False
    assert payload["in_world_dialogue_recorded"] is False
    assert len(_event_items(client)) == before_events
    assert "private memory" not in serialized
    assert "raw thought" not in serialized


def test_projection_rejects_canonical_mutation_attempt_without_appending_event() -> None:
    client = _client()
    client.post("/runtime/step")
    tick_event = next(event for event in _event_items(client) if event["type"] == "tick.advanced")
    before_events = len(_event_items(client))

    response = _post_projection(
        client,
        {
            "public_narrative_summary": "Public projection claims it changed the world.",
            "source_event_refs": [_ref(tick_event["id"], "event", "source")],
            "canonical_state_mutation_applied": True,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "rejected"
    assert "canonical_mutation_attempt" in {
        diagnostic["code"] for diagnostic in payload["diagnostics"]
    }
    assert payload["narrative_projection"] is None
    assert len(_event_items(client)) == before_events


def test_projection_rejects_fake_event_refs() -> None:
    client = _client()

    response = _post_projection(
        client,
        {
            "public_narrative_summary": "Public projection with fake source.",
            "source_event_refs": [_ref("fake-event", "event", "source")],
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "rejected"
    assert "non_canonical_public_ref" in {
        diagnostic["code"] for diagnostic in payload["diagnostics"]
    }


def test_projection_rejects_empty_public_evidence_refs() -> None:
    client = _client()

    response = _post_projection(
        client,
        {"public_narrative_summary": "Public projection without evidence refs."},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "rejected"
    assert "missing_public_evidence_ref" in {
        diagnostic["code"] for diagnostic in payload["diagnostics"]
    }


def test_projection_rejects_textual_canonical_mutation_claim() -> None:
    client = _client()
    client.post("/runtime/step")
    tick_event = next(event for event in _event_items(client) if event["type"] == "tick.advanced")

    response = _post_projection(
        client,
        {
            "public_narrative_summary": (
                "This directly mutated canonical state and appended a canonical event."
            ),
            "source_event_refs": [_ref(tick_event["id"], "event", "source")],
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "rejected"
    assert "textual_canonical_mutation_claim" in {
        diagnostic["code"] for diagnostic in payload["diagnostics"]
    }


@pytest.mark.parametrize(
    "private_marker",
    [
        "chain_of_thought",
        "raw prompt",
        "raw provider request",
        "raw provider response",
        "provider trace",
        "api key",
        "authorization bearer token",
        "private evaluator data",
    ],
)
def test_projection_private_markers_are_rejected_without_public_echo(
    private_marker: str,
) -> None:
    client = _client()

    response = _post_projection(
        client,
        {"public_narrative_summary": f"contains {private_marker}"},
    )

    assert response.status_code == 422
    payload = response.json()
    serialized = str(payload).lower()
    assert private_marker not in serialized
    assert "input" not in payload["data"]["errors"][0]


def test_accepted_diagnostic_dialogue_stays_outside_timeline_and_memory() -> None:
    client = _client()
    app = client.app
    client.post("/runtime/step")
    tick_event = next(event for event in _event_items(client) if event["type"] == "tick.advanced")
    before_events = len(_event_items(client))
    before_memory = app.state.agent_memory_store.list_working_memory(
        agent_id="agent.observer",
        world_id="world-1",
    )

    response = _post_diagnostic(
        client,
        {
            "question_summary": "What public event did the Agent observe?",
            "response_summary": "The Agent can publicly reference one tick advancement.",
            "diagnostic_provenance": "worldengine_public_evidence",
            "source_event_refs": [_ref(tick_event["id"], "event", "source")],
            "source_agent_continuity_refs": [
                _ref("continuity-public-1", "agent_continuity", "context")
            ],
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "accepted"
    artifact = payload["diagnostic_dialogue"]
    assert artifact["world_id"] == "world-1"
    assert artifact["agent_id"] == "agent.observer"
    assert artifact["source_event_refs"][0]["ref_id"] == tick_event["id"]
    assert artifact["canonical_event_appended"] is False
    assert artifact["agent_memory_write_applied"] is False
    assert artifact["in_world_dialogue_recorded"] is False
    assert len(_event_items(client)) == before_events
    after_memory = app.state.agent_memory_store.list_working_memory(
        agent_id="agent.observer",
        world_id="world-1",
    )
    assert after_memory == before_memory


def test_diagnostic_rejects_memory_write_or_in_world_dialogue_claims() -> None:
    client = _client()

    response = _post_diagnostic(
        client,
        {
            "question_summary": "Can this enter memory?",
            "response_summary": "It should be rejected.",
            "agent_memory_write_applied": True,
            "in_world_dialogue_recorded": True,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "rejected"
    assert "canonical_mutation_attempt" in {
        diagnostic["code"] for diagnostic in payload["diagnostics"]
    }
    assert payload["diagnostic_dialogue"] is None


def test_diagnostic_rejects_empty_public_evidence_refs() -> None:
    client = _client()

    response = _post_diagnostic(
        client,
        {
            "question_summary": "What happened?",
            "response_summary": "A public answer without evidence should be rejected.",
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "rejected"
    assert "missing_public_evidence_ref" in {
        diagnostic["code"] for diagnostic in payload["diagnostics"]
    }


def test_projection_rejects_canonical_event_append_flag() -> None:
    client = _client()
    client.post("/runtime/step")
    tick_event = next(event for event in _event_items(client) if event["type"] == "tick.advanced")

    response = _post_projection(
        client,
        {
            "public_narrative_summary": "Public projection with explicit event append flag.",
            "source_event_refs": [_ref(tick_event["id"], "event", "source")],
            "canonical_event_appended": True,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "rejected"
    assert "canonical_mutation_attempt" in {
        diagnostic["code"] for diagnostic in payload["diagnostics"]
    }


def test_manifest_exposes_projection_and_diagnostic_endpoints() -> None:
    client = _client()

    response = client.get("/manifest")

    assert response.status_code == 200
    surfaces = response.json()["public_surfaces"]
    assert any(
        surface["path"] == "/worlds/{world_id}/narrative/project"
        and surface["method"] == "POST"
        and surface["operation_id"] == "project_world_narrative"
        and surface["status"] == "available"
        for surface in surfaces
    )
    assert any(
        surface["path"]
        == "/worlds/{world_id}/agents/{agent_id}/diagnostics/dialogue/evaluate"
        and surface["method"] == "POST"
        and surface["operation_id"] == "evaluate_agent_diagnostic_dialogue"
        and surface["status"] == "available"
        for surface in surfaces
    )
