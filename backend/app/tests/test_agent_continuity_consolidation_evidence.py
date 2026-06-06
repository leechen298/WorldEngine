from __future__ import annotations

from fastapi.testclient import TestClient
from pydantic import ValidationError
import pytest

from app.api.app_factory import create_app
from app.schemas.agent_continuity import AgentContinuityEvaluationRequest


def _client() -> TestClient:
    return TestClient(create_app())


def _ref(ref_id: str, ref_type: str = "event", role: str | None = None) -> dict:
    payload = {"ref_id": ref_id, "ref_type": ref_type}
    if role is not None:
        payload["role"] = role
    return payload


def _post_continuity(
    client: TestClient,
    payload: dict,
    *,
    world_id: str = "world-1",
    agent_id: str = "agent.observer",
):
    return client.post(
        f"/worlds/{world_id}/agents/{agent_id}/continuity/evaluate",
        json=payload,
    )


def _event_items(client: TestClient) -> list[dict]:
    return client.get("/world/events?limit=200").json()["data"]["items"]


def test_continuity_request_rejects_extra_fields() -> None:
    with pytest.raises(ValidationError):
        AgentContinuityEvaluationRequest(state="observe", private_goal="hidden")


def test_private_extra_field_name_is_redacted_from_http_validation_error() -> None:
    client = _client()

    response = _post_continuity(
        client,
        {"state": "observe", "private_goal": "mutate hidden state"},
    )

    assert response.status_code == 422
    serialized = str(response.json()).lower()
    assert "private_goal" not in serialized
    assert "private goal" not in serialized
    assert "mutate hidden state" not in serialized
    assert "input" not in response.json()["data"]["errors"][0]


def test_chain_of_thought_extra_field_name_is_redacted_from_http_validation_error() -> None:
    client = _client()

    response = _post_continuity(
        client,
        {"state": "observe", "chain_of_thought": "private reasoning"},
    )

    assert response.status_code == 422
    serialized = str(response.json()).lower()
    assert "chain_of_thought" not in serialized
    assert "chain-of-thought" not in serialized
    assert "private reasoning" not in serialized
    assert "input" not in response.json()["data"]["errors"][0]


def test_no_intent_continuity_artifact_is_accepted_without_private_mutation() -> None:
    client = _client()

    response = _post_continuity(
        client,
        {
            "state": "no_intent",
            "working_memory_summary": "Agent observed public weather and has no safe action.",
            "perception_summary_refs": [_ref("event.tick.0", "event", "perception")],
            "evidence_refs": [_ref("runtime.tick.0", "runtime", "state")],
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "accepted"
    artifact = payload["continuity_artifact"]
    assert artifact["world_id"] == "world-1"
    assert artifact["agent_id"] == "agent.observer"
    assert artifact["tick_id"] == 0
    assert artifact["world_time_seconds"] == 0
    assert artifact["state"] == "no_intent"
    assert artifact["redaction_status"] == "passed"
    assert payload["applied_event_ids"] == []


@pytest.mark.parametrize("state", ["observe", "intent", "wait", "rest", "sleep"])
def test_public_continuity_states_are_accepted_with_public_evidence(state: str) -> None:
    client = _client()

    response = _post_continuity(
        client,
        {
            "state": state,
            "working_memory_summary": f"Agent public {state} summary.",
            "perception_summary_refs": [_ref(f"event.{state}.0", "event", "perception")],
            "evidence_refs": [_ref(f"runtime.{state}.0", "runtime", "state")],
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "accepted"
    artifact = payload["continuity_artifact"]
    assert artifact["state"] == state
    assert artifact["evidence_refs"][0]["ref_id"] == f"runtime.{state}.0"
    assert artifact["redaction_status"] == "passed"


@pytest.mark.parametrize("state", ["observe", "no_intent", "wait", "rest", "sleep"])
def test_public_continuity_without_evidence_refs_is_rejected_without_recording(
    state: str,
) -> None:
    client = _client()

    response = _post_continuity(
        client,
        {
            "state": state,
            "working_memory_summary": f"Agent public {state} summary.",
            "apply": True,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "rejected"
    assert "missing_public_evidence_ref" in {
        diagnostic["code"] for diagnostic in payload["diagnostics"]
    }
    assert payload["continuity_artifact"] is None
    assert payload["applied_event_ids"] == []
    assert not [
        event for event in _event_items(client) if event["type"] == "agent.continuity.recorded"
    ]


def test_apply_accepted_action_evidence_records_public_events() -> None:
    client = _client()
    loop_response = client.post(
        "/world/agent/loop/step",
        json={
            "intent": {
                "type": "params.patch",
                "reason": "public counter update",
                "patches": [{"op": "set", "path": "counter.increment", "value": 2}],
            }
        },
    )
    assert loop_response.status_code == 200
    action_event_id = loop_response.json()["data"]["result"]["event_id"]

    response = _post_continuity(
        client,
        {
            "state": "action",
            "intent_summary": "Agent selected a public counter update.",
            "autonomous_action_evidence": {
                "action_event_refs": [_ref(action_event_id, "event", "action")],
                "action_result_refs": [_ref(action_event_id, "event", "result")],
                "continuity_artifact_refs": [_ref("continuity.action.0", "continuity", "source")],
                "input_provenance": "worldengine_agent_loop",
                "public_action_summary": "WorldEngine-backed Agent action updated a public parameter.",
            },
            "evidence_refs": [_ref(action_event_id, "event", "agent_loop")],
            "apply": True,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["status"] == "accepted"
    assert len(payload["applied_event_ids"]) == 2
    assert payload["continuity_artifact"]["state"] == "action"
    assert payload["continuity_artifact"]["autonomous_action_evidence"]["input_provenance"] == (
        "worldengine_agent_loop"
    )
    assert payload["continuity_artifact"]["autonomous_action_evidence"]["continuity_artifact_refs"][0][
        "ref_id"
    ] == "continuity.action.0"
    assert "raw thought" not in serialized
    assert "private memory" not in serialized

    continuity_events = [
        event for event in _event_items(client) if event["type"] == "agent.continuity.recorded"
    ]
    action_events = [
        event for event in _event_items(client) if event["type"] == "agent.action.continuity.recorded"
    ]
    assert len(continuity_events) == 1
    assert len(action_events) == 1
    assert continuity_events[0]["payload"]["direct_private_mutation_applied"] is False
    assert action_events[0]["payload"]["client_scripted_action"] is False


def test_client_scripted_action_is_rejected_without_accepted_event() -> None:
    client = _client()

    response = _post_continuity(
        client,
        {
            "state": "action",
            "autonomous_action_evidence": {
                "action_event_refs": [_ref("client.event", "event", "action")],
                "action_result_refs": [_ref("client.result", "event", "result")],
                "input_provenance": "client_scripted",
                "public_action_summary": "Client supplied action should not count as autonomy.",
            },
            "apply": True,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "rejected"
    assert "client_scripted_autonomy" in {
        diagnostic["code"] for diagnostic in payload["diagnostics"]
    }
    assert payload["scripted_autonomy_rejection"]["code"] == "client_scripted_autonomy_rejected"
    assert payload["continuity_artifact"] is None
    assert payload["applied_event_ids"] == []
    assert not [
        event for event in _event_items(client) if event["type"] == "agent.continuity.recorded"
    ]


@pytest.mark.parametrize(
    "provenance",
    ["client_scripted", "fixture_script", "external_validation_script", "unknown"],
)
def test_non_agent_loop_action_provenance_is_rejected(provenance: str) -> None:
    client = _client()
    loop_response = client.post(
        "/world/agent/loop/step",
        json={
            "intent": {
                "type": "params.patch",
                "reason": "public counter update",
                "patches": [{"op": "set", "path": "counter.increment", "value": 3}],
            }
        },
    )
    action_event_id = loop_response.json()["data"]["result"]["event_id"]

    response = _post_continuity(
        client,
        {
            "state": "action",
            "autonomous_action_evidence": {
                "action_event_refs": [_ref(action_event_id, "event", "action")],
                "action_result_refs": [_ref(action_event_id, "event", "result")],
                "input_provenance": provenance,
                "public_action_summary": "Public client-provenance action should not count as autonomy.",
            },
            "apply": True,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "rejected"
    assert "client_scripted_autonomy" in {
        diagnostic["code"] for diagnostic in payload["diagnostics"]
    }
    assert payload["applied_event_ids"] == []


def test_falsely_declared_agent_loop_action_with_fake_refs_is_rejected() -> None:
    client = _client()

    response = _post_continuity(
        client,
        {
            "state": "action",
            "autonomous_action_evidence": {
                "action_event_refs": [_ref("fake-action-event", "event", "action")],
                "action_result_refs": [_ref("fake-action-result", "event", "result")],
                "input_provenance": "worldengine_agent_loop",
                "public_action_summary": "Forged Agent loop provenance should not be accepted.",
            },
            "apply": True,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "rejected"
    assert {
        "non_canonical_action_event_ref",
        "non_canonical_action_result_ref",
    }.issubset({diagnostic["code"] for diagnostic in payload["diagnostics"]})
    assert payload["applied_event_ids"] == []
    assert not [
        event for event in _event_items(client) if event["type"] == "agent.action.continuity.recorded"
    ]


def test_action_refs_must_come_from_agent_loop_events() -> None:
    client = _client()
    client.post("/runtime/step")
    tick_event = next(event for event in _event_items(client) if event["type"] == "tick.advanced")

    response = _post_continuity(
        client,
        {
            "state": "action",
            "autonomous_action_evidence": {
                "action_event_refs": [_ref(tick_event["id"], "event", "action")],
                "action_result_refs": [_ref(tick_event["id"], "event", "result")],
                "input_provenance": "worldengine_agent_loop",
                "public_action_summary": "Runtime event refs should not count as Agent loop action.",
            },
            "apply": True,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "rejected"
    assert {
        "non_canonical_action_event_ref",
        "non_canonical_action_result_ref",
    }.issubset({diagnostic["code"] for diagnostic in payload["diagnostics"]})


def test_reacting_state_requires_public_event_refs_and_can_be_accepted() -> None:
    client = _client()
    client.post("/runtime/step")
    tick_event = next(event for event in _event_items(client) if event["type"] == "tick.advanced")

    response = _post_continuity(
        client,
        {
            "state": "reacting",
            "event_reaction_evidence": {
                "event_refs": [_ref(tick_event["id"], "event", "stimulus")],
                "reaction_summary": "Agent reacted to public tick advancement.",
            },
            "evidence_refs": [_ref(tick_event["id"], "event", "reaction")],
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "accepted"
    assert payload["continuity_artifact"]["state"] == "reacting"
    assert payload["continuity_artifact"]["event_reaction_evidence"]["event_refs"][0]["ref_id"] == (
        tick_event["id"]
    )


def test_reacting_state_rejects_fake_public_event_refs() -> None:
    client = _client()

    response = _post_continuity(
        client,
        {
            "state": "reacting",
            "event_reaction_evidence": {
                "event_refs": [_ref("fake-event", "event", "stimulus")],
                "reaction_summary": "Agent reacted to a fake event.",
            },
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "rejected"
    assert "non_canonical_event_ref" in {
        diagnostic["code"] for diagnostic in payload["diagnostics"]
    }


def test_consolidation_can_span_multiple_ticks_and_records_no_per_tick_mutation() -> None:
    client = _client()
    client.post("/runtime/step")
    client.post("/runtime/step")
    tick_event = next(event for event in _event_items(client) if event["type"] == "tick.advanced")

    response = _post_continuity(
        client,
        {
            "state": "consolidating",
            "consolidation_artifact": {
                "phase_id": "consolidation-1",
                "world_id": "world-1",
                "agent_id": "agent.observer",
                "status": "completed",
                "start_tick": 0,
                "end_tick": 2,
                "start_world_time_seconds": 0,
                "end_world_time_seconds": 1200,
                "source_short_term_summary_refs": [_ref("wm-1", "working_memory", "source")],
                "emitted_long_term_summary_refs": [_ref("ltm-1", "long_term_summary", "emitted")],
                "event_refs": [_ref(tick_event["id"], "event", "consolidation_window")],
                "personality_summary_status": "stable",
                "skill_summary_status": "bounded_drift",
                "public_explanation": "Public summaries consolidated across a bounded rest phase.",
            },
            "evidence_refs": [_ref(tick_event["id"], "event", "consolidation")],
            "apply": True,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "accepted"
    assert payload["consolidation_artifact"]["start_tick"] == 0
    assert payload["consolidation_artifact"]["end_tick"] == 2
    assert payload["consolidation_artifact"]["event_refs"][0]["ref_id"] == tick_event["id"]
    assert len(payload["applied_event_ids"]) == 2
    consolidation_events = [
        event for event in _event_items(client) if event["type"] == "agent.consolidation.recorded"
    ]
    assert len(consolidation_events) == 1
    assert consolidation_events[0]["payload"]["automatic_per_tick_mutation"] is False


def test_private_markers_are_rejected_without_public_echo() -> None:
    client = _client()

    response = _post_continuity(
        client,
        {
            "state": "observe",
            "working_memory_summary": "raw thought with private memory sk-live-secret",
            "apply": True,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["status"] == "rejected"
    assert payload["redaction_status"] == "failed"
    assert "private_marker_detected" in {
        diagnostic["code"] for diagnostic in payload["diagnostics"]
    }
    assert "sk-live-secret" not in serialized
    assert "raw thought" not in serialized
    assert "private memory" not in serialized
    assert payload["applied_event_ids"] == []


@pytest.mark.parametrize(
    "private_marker",
    [
        "chain_of_thought",
        "raw prompt",
        "provider trace",
        "api key",
        "authorization bearer token",
        "private evaluator data",
        "provider secret",
    ],
)
def test_required_private_marker_variants_are_rejected_without_public_echo(
    private_marker: str,
) -> None:
    client = _client()

    response = _post_continuity(
        client,
        {
            "state": "observe",
            "working_memory_summary": f"contains {private_marker}",
        },
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["status"] == "rejected"
    assert "private_marker_detected" in {
        diagnostic["code"] for diagnostic in payload["diagnostics"]
    }
    assert private_marker not in serialized


def test_automatic_per_tick_personality_or_skill_mutation_is_rejected() -> None:
    client = _client()

    response = _post_continuity(
        client,
        {
            "state": "rest",
            "evidence_refs": [
                _ref(
                    "personality-drift",
                    "personality_summary",
                    "automatic per-tick mutation",
                )
            ],
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "rejected"
    assert "automatic_per_tick_mutation" in {
        diagnostic["code"] for diagnostic in payload["diagnostics"]
    }


def test_manifest_exposes_agent_continuity_endpoint() -> None:
    client = _client()

    response = client.get("/manifest")

    assert response.status_code == 200
    assert {
        "path": "/worlds/{world_id}/agents/{agent_id}/continuity/evaluate",
        "method": "POST",
        "operation_id": "evaluate_agent_continuity",
        "status": "available",
    } in response.json()["public_surfaces"]
