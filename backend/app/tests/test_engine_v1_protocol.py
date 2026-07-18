from __future__ import annotations

from typing import Any

from fastapi.testclient import TestClient

from app.tests.test_engine_v1_generation import (
    _client,
    _data,
    _generic_world_brief,
)


_CONTRACT_OPERATIONS = {
    ("GET", "/health"),
    ("GET", "/api/v1/capabilities"),
    ("GET", "/openapi.json"),
    ("POST", "/api/v1/world-packages"),
    ("GET", "/api/v1/world-packages/{package_id}"),
    ("POST", "/api/v1/sessions"),
    ("GET", "/api/v1/sessions/{session_id}"),
    ("POST", "/api/v1/sessions/{session_id}/steps"),
    ("POST", "/api/v1/sessions/{session_id}/directions"),
    ("POST", "/api/v1/sessions/{session_id}/actions"),
    ("POST", "/api/v1/sessions/{session_id}/feedback"),
    ("GET", "/api/v1/sessions/{session_id}/projection"),
    ("GET", "/api/v1/sessions/{session_id}/events"),
    ("GET", "/api/v1/sessions/{session_id}/evidence"),
}


class _ManifestClient:
    def __init__(self, client: TestClient, manifest: dict[str, Any]) -> None:
        self.client = client
        self.operations = {
            (operation["method"].upper(), operation["path"]): operation
            for operation in manifest["operations"]
        }
        self.used_operation_ids: list[str] = []

    def request(
        self,
        method: str,
        contract_path: str,
        *,
        path_parameters: dict[str, str] | None = None,
        **kwargs: Any,
    ) -> Any:
        operation = self.operations[(method.upper(), contract_path)]
        self.used_operation_ids.append(operation["operation_id"])
        path = operation["path"].format(**(path_parameters or {}))
        return self.client.request(method, path, **kwargs)


def _capabilities(client: TestClient) -> dict[str, Any]:
    return _data(client.get("/api/v1/capabilities"))


def test_capabilities_and_openapi_discover_every_contract_operation() -> None:
    client = _client()
    capabilities = _capabilities(client)

    for field in (
        "engine_build",
        "instance_id",
        "contract_version",
        "schema_version",
    ):
        assert capabilities[field]

    operations = capabilities["operations"]
    actual_operations = {
        (operation["method"].upper(), operation["path"])
        for operation in operations
    }
    assert _CONTRACT_OPERATIONS.issubset(actual_operations)
    assert all(operation["operation_id"] for operation in operations)
    assert all(operation["maturity"] for operation in operations)
    operation_ids = [operation["operation_id"] for operation in operations]
    assert len(operation_ids) == len(set(operation_ids))

    openapi = _data(client.get("/openapi.json"))
    for operation in operations:
        path = operation["path"]
        if path == "/openapi.json":
            continue
        method = operation["method"].lower()
        assert path in openapi["paths"]
        assert method in openapi["paths"][path]
        assert (
            openapi["paths"][path][method]["operationId"]
            == operation["operation_id"]
        )

    serialized = str({"capabilities": capabilities, "openapi": openapi}).lower()
    for forbidden in (
        "godot",
        "scene_tree",
        "scene-tree",
        "collision_shape",
        "collision-shape",
        "animation_player",
    ):
        assert forbidden not in serialized


def test_ac_10_manifest_only_black_box_flow() -> None:
    client = _client()
    capabilities = _capabilities(client)
    api = _ManifestClient(client, capabilities)

    health = api.request("GET", "/health")
    assert health.status_code == 200

    package = _data(
        api.request(
            "POST",
            "/api/v1/world-packages",
            json={
                "request_id": "black-box-package-create",
                "brief": _generic_world_brief(),
            },
        )
    )
    fetched_package = _data(
        api.request(
            "GET",
            "/api/v1/world-packages/{package_id}",
            path_parameters={"package_id": package["package_id"]},
        )
    )
    assert fetched_package["package_hash"] == package["package_hash"]

    session = _data(
        api.request(
            "POST",
            "/api/v1/sessions",
            json={
                "request_id": "black-box-session-create",
                "package_id": package["package_id"],
                "package_hash": package["package_hash"],
            },
        )
    )
    session_id = session["session_id"]
    assert session["source_package_hash"] == package["package_hash"]

    projection = _data(
        api.request(
            "GET",
            "/api/v1/sessions/{session_id}/projection",
            path_parameters={"session_id": session_id},
        )
    )
    window = projection["active_intervention_window"]

    accepted = _data(
        api.request(
            "POST",
            "/api/v1/sessions/{session_id}/directions",
            path_parameters={"session_id": session_id},
            json={
                "request_id": "black-box-bounded-direction",
                "expected_revision": projection["revision"],
                "window_id": window["window_id"],
                "kind": "bounded_pressure",
                "target_ref": "system_signal",
                "summary": "Apply one bounded unit of public pressure.",
                "magnitude": 1,
            },
        )
    )
    after_accepted = _data(
        api.request(
            "GET",
            "/api/v1/sessions/{session_id}/projection",
            path_parameters={"session_id": session_id},
        )
    )
    rejected = _data(
        api.request(
            "POST",
            "/api/v1/sessions/{session_id}/directions",
            path_parameters={"session_id": session_id},
            json={
                "request_id": "black-box-final-fact-direction",
                "expected_revision": after_accepted["revision"],
                "window_id": window["window_id"],
                "kind": "direct_final_fact",
                "target_ref": "system_signal",
                "summary": "Assign a final public value directly.",
                "final_value": 10,
            },
        )
    )

    assert accepted["status"] == "accepted"
    assert rejected["status"] == "rejected"
    assert accepted["window_id"] == rejected["window_id"] == window["window_id"]
    assert rejected["reason_code"]
    assert "window" not in rejected["reason_code"]

    step_result = _data(
        api.request(
            "POST",
            "/api/v1/sessions/{session_id}/steps",
            path_parameters={"session_id": session_id},
            json={
                "request_id": "black-box-step-two",
                "step_count": 2,
                "expected_revision": after_accepted["revision"],
            },
        )
    )
    final_session_view = _data(
        api.request(
            "GET",
            "/api/v1/sessions/{session_id}",
            path_parameters={"session_id": session_id},
        )
    )
    final_session = final_session_view["projection"]
    final_projection = _data(
        api.request(
            "GET",
            "/api/v1/sessions/{session_id}/projection",
            path_parameters={"session_id": session_id},
        )
    )
    events = _data(
        api.request(
            "GET",
            "/api/v1/sessions/{session_id}/events",
            path_parameters={"session_id": session_id},
            params={"after_sequence": 0},
        )
    )["items"]
    evidence = _data(
        api.request(
            "GET",
            "/api/v1/sessions/{session_id}/evidence",
            path_parameters={"session_id": session_id},
        )
    )

    assert step_result["end_tick"] == final_session["tick"] == 2
    assert final_session["tick"] == final_projection["tick"]
    assert final_session["revision"] == final_projection["revision"]
    assert final_session["state_hash"] == final_projection["state_hash"]
    assert final_projection["agents"]
    assert evidence["agent_cycles"]
    assert len(evidence["agent_cycles"]) >= 2
    assert evidence["agent_cycles"][-1]["experience_refs_used"]
    assert events
    assert evidence["events"]
    assert evidence["diffs"]
    assert evidence["snapshots"]
    assert evidence["direction_decisions"]
    assert evidence["projection"]["state_hash"] == final_projection["state_hash"]
    assert api.used_operation_ids
