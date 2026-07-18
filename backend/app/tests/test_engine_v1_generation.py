from __future__ import annotations

from copy import deepcopy
from typing import Any

from fastapi.testclient import TestClient

from app.api.app_factory import create_app


def _client() -> TestClient:
    return TestClient(create_app())


def _data(response: Any, expected_status: int = 200) -> dict[str, Any]:
    assert response.status_code == expected_status, response.text
    payload = response.json()
    assert isinstance(payload, dict), payload
    data = payload.get("data")
    return data if isinstance(data, dict) else payload


def _generic_world_brief(
    *,
    seed: str = "engine-v1-seed-130013",
    premise: str = "A bounded abstract system evolves through declared public rules.",
) -> dict[str, Any]:
    return {
        "seed": seed,
        "premise": premise,
        "constraints": {
            "capability_set": ["projection", "runtime"],
            "canonical_mutations": "rule_judged",
            "execution_mode": "deterministic_lockstep",
        },
        "state_variables": [
            {
                "key": "system_capacity",
                "initial": 4,
                "minimum": 0,
                "maximum": 8,
                "step": 1,
            },
            {
                "key": "system_signal",
                "initial": 0,
                "minimum": 0,
                "maximum": 10,
                "step": 1,
            },
        ],
        "agent_count": 1,
        "step_seconds": 1.0,
    }


def _create_package(
    client: TestClient,
    brief: dict[str, Any] | None = None,
    *,
    request_id: str = "package-create-default",
) -> dict[str, Any]:
    return _data(
        client.post(
            "/api/v1/world-packages",
            json={
                "request_id": request_id,
                "brief": brief or _generic_world_brief(),
            },
        )
    )


def _boot_session(
    client: TestClient,
    package: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    package = package or _create_package(client)
    session = _data(
        client.post(
            "/api/v1/sessions",
            json={
                "request_id": "session-create-default",
                "package_id": package["package_id"],
                "package_hash": package["package_hash"],
            },
        )
    )
    return package, session


def _projection(client: TestClient, session_id: str) -> dict[str, Any]:
    return _data(client.get(f"/api/v1/sessions/{session_id}/projection"))


def _evidence(client: TestClient, session_id: str) -> dict[str, Any]:
    return _data(client.get(f"/api/v1/sessions/{session_id}/evidence"))


def _events(
    client: TestClient,
    session_id: str,
    *,
    after_sequence: int = 0,
) -> list[dict[str, Any]]:
    data = _data(
        client.get(
            f"/api/v1/sessions/{session_id}/events",
            params={"after_sequence": after_sequence},
        )
    )
    events = data["items"]
    assert isinstance(events, list)
    return events


def _assert_ready_package(package: dict[str, Any]) -> None:
    readiness = package.get("readiness")
    if isinstance(readiness, dict):
        assert readiness["status"] == "ready"
        assert readiness.get("errors", []) == []
    else:
        assert package["status"] == "ready"

    assert package["package_id"]
    assert package["package_hash"]
    for section in (
        "world_spec",
        "rule_catalog",
        "action_catalog",
        "agent_seed_set",
        "projection_manifest",
        "evidence_policy",
    ):
        assert section in package


def test_ac_01_same_normalized_brief_and_seed_have_same_package_hash() -> None:
    client = _client()
    brief = _generic_world_brief()

    first = _create_package(client, brief, request_id="package-normalized-one")

    reordered_brief = {
        "step_seconds": brief["step_seconds"],
        "agent_count": brief["agent_count"],
        "state_variables": list(reversed(deepcopy(brief["state_variables"]))),
        "constraints": {
            **dict(reversed(list(brief["constraints"].items()))),
            "capability_set": list(
                reversed(brief["constraints"]["capability_set"])
            ),
        },
        "premise": brief["premise"],
        "seed": brief["seed"],
    }
    second = _create_package(
        client,
        reordered_brief,
        request_id="package-normalized-two",
    )

    _assert_ready_package(first)
    _assert_ready_package(second)
    assert second["package_hash"] == first["package_hash"]

    fetched = _data(
        client.get(f"/api/v1/world-packages/{first['package_id']}")
    )
    assert fetched["package_hash"] == first["package_hash"]
    assert fetched["world_spec"] == first["world_spec"]


def test_ac_01_allowed_brief_change_updates_public_field_and_hash() -> None:
    client = _client()
    original = _create_package(client, request_id="package-premise-original")
    changed_premise = (
        "A bounded abstract system evolves through an alternate declared premise."
    )
    changed = _create_package(
        client,
        _generic_world_brief(premise=changed_premise),
        request_id="package-premise-changed",
    )

    _assert_ready_package(original)
    _assert_ready_package(changed)
    assert changed["package_hash"] != original["package_hash"]
    assert changed["world_spec"]["premise"] == changed_premise
    assert changed["world_spec"]["premise"] != original["world_spec"]["premise"]


def test_ready_package_exposes_scale_and_resolved_public_references() -> None:
    client = _client()
    package = _create_package(client, request_id="package-reference-readiness")

    assert package["readiness"] == {"status": "ready", "diagnostics": []}
    scale = package["world_spec"]["scale_bounds"]
    assert scale["minimum_locations"] == scale["maximum_locations"] == 1
    assert scale["minimum_agents"] == scale["maximum_agents"] == 1

    locations = package["world_spec"]["location_graph"]
    entities = package["world_spec"]["entity_catalog"]
    assert len(locations) == 1
    assert entities[0]["location_id"] == locations[0]["location_id"]
    assert package["agent_seed_set"][0]["location_id"] == locations[0]["location_id"]

    rule_ids = {item["rule_id"] for item in package["rule_catalog"]}
    assert {
        "rule.session.ready-package",
        "rule.runtime.lockstep",
        "rule.direction.no-direct-fact",
        "rule.feedback.manifest",
    }.issubset(rule_ids)
    assert all(
        set(action["rule_refs"]).issubset(rule_ids)
        for action in package["action_catalog"]
    )
    assert {"locations", "entities", "agents"}.issubset(
        package["projection_manifest"]["public_fields"]
    )


def test_private_markers_are_rejected_without_echoing_input() -> None:
    client = _client()
    response = client.post(
        "/api/v1/world-packages",
        json={
            "request_id": "sk-live-secret-value",
            "brief": {"seed": "seed", "premise": "public premise"},
        },
    )

    assert response.status_code == 422
    serialized = str(response.json()).lower()
    assert "sk-live-secret-value" not in serialized
    assert "input" not in serialized

    private_field_response = client.post(
        "/api/v1/world-packages",
        json={
            "request_id": "package-private-field",
            "brief": {
                "seed": "seed",
                "premise": "public premise",
                "constraints": {"token": "do-not-echo-this-value"},
            },
        },
    )
    assert private_field_response.status_code == 422
    private_field_body = str(private_field_response.json()).lower()
    assert "do-not-echo-this-value" not in private_field_body
    assert "input" not in private_field_body

    public_story = _create_package(
        client,
        _generic_world_brief(
            premise="A secret society uses a token economy under public rules."
        ),
        request_id="package-public-story-vocabulary",
    )
    assert public_story["readiness"]["status"] == "ready"


def test_state_variable_requires_at_least_one_runnable_step() -> None:
    client = _client()
    brief = _generic_world_brief()
    brief["state_variables"] = [
        {
            "key": "blocked_signal",
            "initial": 5,
            "minimum": 0,
            "maximum": 10,
            "step": 6,
        }
    ]

    response = client.post(
        "/api/v1/world-packages",
        json={"request_id": "package-non-runnable-step", "brief": brief},
    )

    assert response.status_code == 422
    assert "engine_v1_variable_has_no_runnable_step" in str(response.json())


def test_package_idempotency_key_reuse_with_different_brief_conflicts() -> None:
    client = _client()
    first = _create_package(
        client,
        _generic_world_brief(premise="First public premise."),
        request_id="package-reused-request-id",
    )
    before_count = len(client.app.state.engine_v1_service._packages)

    response = client.post(
        "/api/v1/world-packages",
        json={
            "request_id": "package-reused-request-id",
            "brief": _generic_world_brief(premise="Different public premise."),
        },
    )
    conflict = _data(response, expected_status=409)

    assert conflict["reason_code"] == "idempotency_key_reused"
    assert len(client.app.state.engine_v1_service._packages) == before_count
    fetched = _data(client.get(f"/api/v1/world-packages/{first['package_id']}"))
    assert fetched["package_hash"] == first["package_hash"]
