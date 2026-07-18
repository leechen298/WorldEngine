from __future__ import annotations

from copy import deepcopy

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from app.api.app_factory import create_app
from app.core.rule_linked_evolution import evaluate_world_event_candidate
from app.schemas.world_evolution import WorldEventCandidate
from app.schemas.world_generation import GeneratedRuleParameterSet


def _client() -> TestClient:
    return TestClient(create_app())


def _rule_set() -> dict:
    return {
        "world_id": "world-1",
        "generation_id": "generation-1",
        "premise_digest": "abcdef123456",
        "parameters": [
            {
                "parameter_id": "param.weather_intensity",
                "path": "environment.weather_intensity",
                "value_type": "int",
                "initial_value": 2,
                "visibility": "public",
                "description": "public weather intensity",
                "constraints": {"min": 0, "max": 10},
                "source": {"kind": "generated", "ref": "0.9.7-test"},
                "rule_refs": ["rule.weather_drift"],
            }
        ],
        "rules": [
            {
                "rule_id": "rule.weather_drift",
                "rule_kind": "environment_trend",
                "trigger": {"type": "direction_or_tick"},
                "conditions": [{"type": "public_weather_state"}],
                "effects": [
                    {
                        "op": "set",
                        "parameter_ref": "param.weather_intensity",
                        "value_expression": {"type": "bounded_value", "min": 0, "max": 10},
                    }
                ],
                "target_parameter_refs": ["param.weather_intensity"],
                "allowed_ops": ["set"],
                "priority": 10,
                "cooldown": {"ticks": 1},
                "evidence": {"public_explanation": "weather intensity can change within bounds"},
            }
        ],
        "constraints": [
            {
                "constraint_id": "constraint.weather_bounds",
                "scope": "parameter",
                "target_refs": ["param.weather_intensity"],
                "rule_refs": ["rule.weather_drift"],
                "expression": {"type": "range", "min": 0, "max": 10},
                "public_explanation": "weather intensity remains bounded",
            }
        ],
        "boundaries": [],
    }


def _candidate(**overrides) -> dict:
    payload = {
        "candidate_id": "candidate-weather-1",
        "world_id": "world-1",
        "event_type": "environment.weather_shift",
        "source": "world_rule",
        "proposed_tick": 0,
        "proposed_world_time_seconds": 0,
        "rule_refs": ["rule.weather_drift"],
        "parameter_patches": [
            {
                "parameter_ref": "param.weather_intensity",
                "op": "set",
                "value": 4,
                "rule_ref": "rule.weather_drift",
                "public_explanation": "public weather pressure increased",
            }
        ],
        "cause_refs": ["event.tick.0"],
        "location_refs": ["location.public-test"],
        "probability_evidence": {"weight": 0.7, "source": "public_rule"},
        "causality_evidence": {"cause": "public weather pressure", "effect": "intensity rises"},
        "public_summary": "Weather intensity changes within public rule bounds.",
    }
    payload.update(overrides)
    return payload


def _post_candidate(client: TestClient, candidate: dict | None = None, *, apply: bool = False):
    return client.post(
        "/worlds/world-1/evolution/evaluate-event",
        json={
            "candidate": candidate or _candidate(),
            "rule_set": _rule_set(),
            "apply": apply,
        },
    )


def _event_items(client: TestClient) -> list[dict]:
    return client.get("/world/events?limit=200").json()["data"]["items"]


def test_world_event_candidate_rejects_extra_fields() -> None:
    with pytest.raises(ValidationError):
        WorldEventCandidate(**_candidate(private_goal="mutate hidden state"))


def test_legal_candidate_is_accepted_with_public_diff_and_no_private_mutation() -> None:
    result = evaluate_world_event_candidate(
        candidate=WorldEventCandidate.model_validate(_candidate()),
        rule_set=GeneratedRuleParameterSet.model_validate(_rule_set()),
        current_params={},
        runtime_tick=0,
        runtime_world_time_seconds=0,
    )

    assert result.status == "accepted"
    assert result.diagnostics == []
    assert result.matched_rule_ids == ["rule.weather_drift"]
    assert result.checked_constraint_ids == ["constraint.weather_bounds"]
    assert result.referenced_parameter_ids == ["param.weather_intensity"]
    assert result.state_diff is not None
    assert result.state_diff.direct_private_mutation_applied is False
    item = result.state_diff.items[0]
    assert item.parameter_ref == "param.weather_intensity"
    assert item.old_public_value == 2
    assert item.new_public_value == 4
    assert item.rule_id == "rule.weather_drift"
    assert result.evidence is not None
    assert result.evidence.direct_state_mutation_applied is False


def test_apply_route_updates_only_public_parameter_and_records_evidence_event() -> None:
    client = _client()

    response = _post_candidate(client, apply=True)

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["result"]["status"] == "accepted"
    assert payload["result"]["applied_event_id"]
    assert payload["result"]["state_diff"]["changed_parameter_ids"] == [
        "param.weather_intensity"
    ]
    assert "raw prompt" not in serialized
    assert "provider_trace" not in serialized
    assert "private memory" not in serialized

    params_response = client.get("/world/params")
    assert params_response.status_code == 200
    assert params_response.json()["data"] == {"environment": {"weather_intensity": 4}}

    events = _event_items(client)
    accepted_events = [event for event in events if event["type"] == "world.evolution.accepted"]
    assert len(accepted_events) == 1
    event_payload = accepted_events[0]["payload"]
    assert event_payload["candidate_id"] == "candidate-weather-1"
    assert event_payload["matched_rule_ids"] == ["rule.weather_drift"]
    assert event_payload["changed_parameter_ids"] == ["param.weather_intensity"]
    assert event_payload["state_diff"]["items"][0]["old_public_value"] == 2
    assert event_payload["state_diff"]["items"][0]["new_public_value"] == 4
    assert event_payload["evidence"]["legality_status"] == "accepted"
    assert event_payload["direct_state_mutation_applied"] is False


@pytest.mark.parametrize(
    "private_path",
    [
        "agents.agent1.personality",
        "agents.agent1.skills",
        "agents.agent1.goals",
        "world.agents.agent1.personality",
    ],
)
def test_agent_private_parameter_path_is_rejected_without_state_mutation(
    private_path: str,
) -> None:
    client = _client()
    rule_set = deepcopy(_rule_set())
    private_segment = private_path.rsplit(".", 1)[-1]
    rule_set["parameters"][0].update(
        {
            "parameter_id": f"param.agent_{private_segment}",
            "path": private_path,
            "value_type": "string",
            "initial_value": "cautious",
            "description": "agent private state must not be a public evolution target",
        }
    )
    rule_set["rules"][0]["effects"][0]["parameter_ref"] = f"param.agent_{private_segment}"
    rule_set["rules"][0]["target_parameter_refs"] = [f"param.agent_{private_segment}"]
    rule_set["constraints"] = []
    candidate = _candidate(
        parameter_patches=[
            {
                "parameter_ref": f"param.agent_{private_segment}",
                "op": "set",
                "value": "reckless",
                "rule_ref": "rule.weather_drift",
                "public_explanation": "attempt to mutate agent private state through world rules",
            }
        ],
        public_summary="Attempted Agent private-state mutation through public rule-linked evolution.",
    )

    response = client.post(
        "/worlds/world-1/evolution/evaluate-event",
        json={"candidate": candidate, "rule_set": rule_set, "apply": True},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["result"]["status"] == "rejected"
    assert "agent_private_parameter_path" in {
        diagnostic["code"] for diagnostic in payload["result"]["diagnostics"]
    }
    assert payload["result"]["state_diff"] is None
    assert client.get("/world/params").json()["data"] == {}
    assert not [
        event for event in _event_items(client) if event["type"] == "world.evolution.accepted"
    ]


@pytest.mark.parametrize(
    ("candidate_patch", "expected_code"),
    [
        ({"rule_refs": ["rule.missing"]}, "unknown_rule_ref"),
        (
            {
                "parameter_patches": [
                    {
                        "parameter_ref": "param.missing",
                        "op": "set",
                        "value": 4,
                        "rule_ref": "rule.weather_drift",
                        "public_explanation": "public weather pressure increased",
                    }
                ]
            },
            "unknown_parameter_ref",
        ),
        (
            {
                "parameter_patches": [
                    {
                        "parameter_ref": "param.weather_intensity",
                        "op": "add",
                        "value": 4,
                        "rule_ref": "rule.weather_drift",
                        "public_explanation": "public weather pressure increased",
                    }
                ]
            },
            "operation_not_allowed",
        ),
        (
            {
                "parameter_patches": [
                    {
                        "parameter_ref": "param.weather_intensity",
                        "op": "set",
                        "value": 99,
                        "rule_ref": "rule.weather_drift",
                        "public_explanation": "public weather pressure increased",
                    }
                ]
            },
            "constraint_violation",
        ),
        ({"proposed_tick": 99}, "timing_outside_window"),
        ({"probability_evidence": {}}, "missing_probability_evidence"),
        ({"causality_evidence": {}}, "missing_causality_evidence"),
        (
            {
                "event_type": "direct_final_fact",
                "public_summary": "force outcome that agent is dead",
            },
            "direct_final_fact_or_private_state",
        ),
    ],
)
def test_illegal_candidates_are_rejected_without_event_or_state_mutation(
    candidate_patch: dict,
    expected_code: str,
) -> None:
    client = _client()
    candidate = _candidate(**candidate_patch)

    response = _post_candidate(client, candidate=candidate, apply=True)

    assert response.status_code == 200
    payload = response.json()
    assert payload["result"]["status"] == "rejected"
    assert expected_code in {
        diagnostic["code"] for diagnostic in payload["result"]["diagnostics"]
    }
    assert payload["result"]["state_diff"] is None
    assert client.get("/world/params").json()["data"] == {}
    assert not [
        event for event in _event_items(client) if event["type"] == "world.evolution.accepted"
    ]


def test_private_markers_are_rejected_without_public_echo() -> None:
    client = _client()
    candidate = _candidate(public_summary="raw prompt sk-live-secret provider_trace")

    response = _post_candidate(client, candidate=candidate, apply=True)

    assert response.status_code == 422
    serialized = str(response.json()).lower()
    assert "sk-live-secret" not in serialized
    assert "raw prompt" not in serialized
    assert "provider_trace" not in serialized
    assert "input" not in serialized
    assert client.get("/world/params").json()["data"] == {}


def test_private_extra_field_name_is_redacted_from_http_validation_error() -> None:
    client = _client()
    candidate = _candidate(private_goal="mutate hidden state")

    response = _post_candidate(client, candidate=candidate, apply=True)

    assert response.status_code == 422
    serialized = str(response.json()).lower()
    assert "private_goal" not in serialized
    assert "private goal" not in serialized
    assert "mutate hidden state" not in serialized
    assert "input" not in response.json()["data"]["errors"][0]
    assert client.get("/world/params").json()["data"] == {}


def test_direct_final_or_agent_private_markers_in_evidence_and_values_are_rejected() -> None:
    client = _client()
    candidate = _candidate(
        probability_evidence={
            "weight": 0.8,
            "selection_note": "force_outcome through public-looking evidence",
        },
        causality_evidence={
            "cause": "public weather pressure",
            "effect": "agent_private inventory override",
        },
        parameter_patches=[
            {
                "parameter_ref": "param.weather_intensity",
                "op": "set",
                "value": "relationship override",
                "rule_ref": "rule.weather_drift",
                "public_explanation": "public weather pressure increased",
            }
        ],
    )

    response = _post_candidate(client, candidate=candidate, apply=True)

    assert response.status_code == 200
    payload = response.json()
    assert payload["result"]["status"] == "rejected"
    codes = {diagnostic["code"] for diagnostic in payload["result"]["diagnostics"]}
    assert "direct_final_fact_or_private_state" in codes
    assert payload["result"]["state_diff"] is None
    assert client.get("/world/params").json()["data"] == {}
    assert not [
        event for event in _event_items(client) if event["type"] == "world.evolution.accepted"
    ]


def test_direction_biased_candidate_is_accepted_only_after_public_direction_queue() -> None:
    client = _client()
    direction_response = client.post(
        "/worlds/world-1/direction",
        json={
            "instruction_text": "increase probability of public rain event",
            "apply_after_tick": 0,
            "expires_after_tick": 2,
        },
    )
    direction_id = direction_response.json()["queue_item"]["direction_id"]

    response = _post_candidate(
        client,
        candidate=_candidate(direction_refs=[direction_id]),
        apply=True,
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["result"]["status"] == "accepted"
    assert payload["result"]["evidence"]["direction_refs"] == [direction_id]
    assert client.get("/world/params").json()["data"] == {
        "environment": {"weather_intensity": 4}
    }


def test_unresolved_direction_ref_is_rejected_without_mutation() -> None:
    client = _client()

    response = _post_candidate(
        client,
        candidate=_candidate(direction_refs=["direction.missing"]),
        apply=True,
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["result"]["status"] == "rejected"
    assert "unknown_direction_ref" in {
        diagnostic["code"] for diagnostic in payload["result"]["diagnostics"]
    }
    assert client.get("/world/params").json()["data"] == {}


def test_snapshot_event_step_replay_evidence_matches_accepted_state_diff() -> None:
    client = _client()

    apply_response = _post_candidate(client, apply=True)
    assert apply_response.status_code == 200
    applied_event_id = apply_response.json()["result"]["applied_event_id"]

    steps_response = client.get("/world/event-steps?limit=1")
    assert steps_response.status_code == 200
    step = steps_response.json()["data"]["items"][0]
    accepted_event = next(
        event for event in step["items"] if event["id"] == applied_event_id
    )
    diff_item = accepted_event["payload"]["state_diff"]["items"][0]

    assert step["tick_id"] == 0
    assert accepted_event["type"] == "world.evolution.accepted"
    assert diff_item["path"] == "environment.weather_intensity"
    assert diff_item["old_public_value"] == 2
    assert diff_item["new_public_value"] == 4
    assert client.get("/world/params").json()["data"] == {
        "environment": {"weather_intensity": 4}
    }


def test_manifest_exposes_rule_linked_evolution_endpoint() -> None:
    client = _client()

    response = client.get("/manifest")

    assert response.status_code == 200
    surfaces = response.json()["public_surfaces"]
    surface = next(
        item
        for item in surfaces
        if item["path"] == "/worlds/{world_id}/evolution/evaluate-event"
        and item["method"] == "POST"
    )
    assert surface["operation_id"] == "evaluate_world_event_candidate"
    assert surface["status"] == "available"


def test_rule_set_redaction_failure_is_rejected_without_echo() -> None:
    client = _client()
    unsafe_rule_set = deepcopy(_rule_set())
    unsafe_rule_set["parameters"][0]["description"] = "private memory raw response"

    response = client.post(
        "/worlds/world-1/evolution/evaluate-event",
        json={
            "candidate": _candidate(),
            "rule_set": unsafe_rule_set,
            "apply": True,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    assert payload["result"]["status"] == "rejected"
    assert "private_marker_detected" in {
        diagnostic["code"] for diagnostic in payload["result"]["diagnostics"]
    }
    assert "private memory" not in serialized
    assert "raw response" not in serialized
    assert client.get("/world/params").json()["data"] == {}
