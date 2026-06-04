from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict

from fastapi.testclient import TestClient

from app.api.app_factory import create_app
from app.schemas.agent_memory import WorkingMemoryRecord
from app.schemas.event import Event


def _worldspec_payload() -> Dict[str, Any]:
    return {
        "schema_version": "0.2",
        "id": "worldspec-core-ready",
        "label": "Core Ready WorldSpec",
        "root": {
            "id": "cell-root",
            "label": "Cell Root",
            "kind": "world",
            "entity_refs": [{"id": "agent.default", "kind": "agent"}],
            "child_cells": [],
            "metadata": {"visibility": "public"},
        },
        "metadata": {"purpose": "core-readiness-test"},
    }


def _template_preview_request() -> Dict[str, Any]:
    return {
        "request_id": "core-preview-source",
        "source_kind": "template",
        "template_request": {
            "request_id": "core-preview-template",
            "template": {
                "id": "template.core-ready",
                "version": "1",
                "root": {
                    "id": "root",
                    "label": "Root",
                    "entity_refs": [{"id": "agent.root", "kind": "agent"}],
                    "metadata": {"visibility": "public"},
                    "child_cells": [],
                },
                "metadata": {"category": "generic"},
                "constraints": {},
            },
            "seed_material": {"seed": "core-ready"},
            "constraints": {},
        },
    }


def _client() -> TestClient:
    return TestClient(create_app())


def test_core_readiness_endpoint_probes_candidate_worldspec_without_mutating_app_state() -> None:
    app = create_app()
    app.state.event_log.append(
        Event(
            id="app-event-1",
            tick_id=1,
            world_time_seconds=600,
            type="app.existing",
            source="test",
            payload={"keep": True},
            created_at="2026-06-02T00:00:00+00:00",
        )
    )
    app.state.agent_memory_store.add_working_memory(
        WorkingMemoryRecord(
            memory_id="working-app-1",
            agent_id="agent.default",
            world_id="world.default",
            content="private app memory should stay out of probe evidence",
            source="test",
            priority=1,
            created_at="2026-06-02T00:00:00+00:00",
            updated_at="2026-06-02T00:00:00+00:00",
        )
    )
    client = TestClient(app)
    before_runtime = client.get("/runtime/state").json()["data"]
    before_events = client.get("/world/events").json()["data"]["items"]
    before_params = client.get("/world/params").json()["data"]

    response = client.post(
        "/world/generation/core-readiness",
        json={
            "request_id": "core-ready-worldspec",
            "worldspec": _worldspec_payload(),
            "source_label": "candidate.core",
            "event_limit": 5,
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["code"] == 0
    data = body["data"]
    assert data["request_id"] == "core-ready-worldspec"
    assert data["validation_status"] == "passed"
    assert data["runtime_readiness"]["validation_status"] == "passed"
    assert data["runtime_readiness"]["runtime_context_passed"] is True
    assert data["isolated_runtime_step"]["tick_id"] == 1
    assert data["isolated_runtime_step"]["world_time_seconds"] == 600
    assert [event["type"] for event in data["isolated_events"]] == ["tick.advanced"]
    assert data["agent_loop_probe"]["intent"]["type"] == "noop"
    assert data["agent_loop_probe"]["result"]["status"] == "noop"
    assert data["agent_loop_probe"]["result"]["applied"] is False
    assert data["agent_loop_probe"]["perception"]["runtime_context_summary"]["root_cell_id"] == "cell-root"
    assert data["does_not_mutate_app_runtime"] is True

    assert client.get("/runtime/state").json()["data"] == before_runtime
    assert client.get("/world/events").json()["data"]["items"] == before_events
    assert client.get("/world/params").json()["data"] == before_params

    serialized = str(data).lower()
    assert "private app memory" not in serialized
    assert "prompt" not in serialized
    assert "provider_trace" not in serialized
    assert "secret" not in serialized


def test_core_readiness_endpoint_accepts_preview_request_and_returns_preview_evidence() -> None:
    client = _client()

    response = client.post(
        "/world/generation/core-readiness",
        json={
            "request_id": "core-ready-preview",
            "preview_request": _template_preview_request(),
        },
    )

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["validation_status"] == "passed"
    assert data["preview"]["validation_status"] == "passed"
    assert data["preview"]["worldspec_preview"]["root"]["id"] == "root"
    assert data["runtime_readiness"]["runtime_context_summary"]["root_cell_id"] == "root"


def test_core_readiness_endpoint_redacts_private_source_label_paths() -> None:
    client = _client()

    response = client.post(
        "/world/generation/core-readiness",
        json={
            "request_id": "core-ready-private-label",
            "worldspec": _worldspec_payload(),
            "source_label": "/Users/leechen/private/repo",
        },
    )

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["validation_status"] == "passed"
    assert data["runtime_readiness"]["runtime_context_summary"]["source_label"] == "redacted"
    assert (
        data["agent_loop_probe"]["perception"]["runtime_context_summary"]["source_label"]
        == "redacted"
    )
    serialized = str(data)
    assert "/Users/leechen/private/repo" not in serialized
    assert "private/repo" not in serialized


def test_core_readiness_endpoint_redacts_secret_like_source_labels() -> None:
    client = _client()

    secret_like_labels = [
        "api-key-abc123",
        "password=abc123",
        "bearer abc123",
        "sk-live-abc123",
    ]

    for index, source_label in enumerate(secret_like_labels):
        response = client.post(
            "/world/generation/core-readiness",
            json={
                "request_id": f"core-ready-secret-label-{index}",
                "worldspec": _worldspec_payload(),
                "source_label": source_label,
            },
        )

        assert response.status_code == 200
        data = response.json()["data"]
        serialized = str(data).lower()
        assert data["runtime_readiness"]["runtime_context_summary"]["source_label"] == "redacted"
        assert (
            data["agent_loop_probe"]["perception"]["runtime_context_summary"]["source_label"]
            == "redacted"
        )
        assert source_label.lower() not in serialized


def test_core_readiness_endpoint_agent_loop_probe_uses_bounded_perception_summary() -> None:
    client = _client()

    response = client.post(
        "/world/generation/core-readiness",
        json={
            "request_id": "core-ready-bounded-perception",
            "worldspec": _worldspec_payload(),
            "event_limit": 5,
        },
    )

    assert response.status_code == 200
    data = response.json()["data"]
    perception = data["agent_loop_probe"]["perception"]

    assert perception["runtime"]["tick_id"] == 1
    assert perception["runtime_context_summary"]["root_cell_id"] == "cell-root"
    assert perception["recent_events"] == [
        {
            "id": data["isolated_events"][0]["id"],
            "tick_id": 1,
            "world_time_seconds": 600,
            "type": "tick.advanced",
            "source": data["isolated_events"][0]["source"],
        }
    ]
    assert "payload" not in perception["recent_events"][0]
    assert "created_at" not in perception["recent_events"][0]
    assert "params" not in perception
    assert "memory_context" not in perception


def test_core_readiness_endpoint_rejects_extra_fields_with_existing_422_envelope() -> None:
    client = _client()

    response = client.post(
        "/world/generation/core-readiness",
        json={
            "request_id": "core-ready-extra",
            "worldspec": _worldspec_payload(),
            "provider_trace": "must not be accepted",
        },
    )

    assert response.status_code == 422
    body = response.json()
    assert body["code"] == 30
    assert body["data"]["errors"][0]["type"] == "extra_forbidden"


def test_core_readiness_endpoint_requires_exactly_one_candidate_source() -> None:
    client = _client()

    response = client.post(
        "/world/generation/core-readiness",
        json={
            "request_id": "core-ready-ambiguous",
            "worldspec": _worldspec_payload(),
            "preview_request": _template_preview_request(),
        },
    )

    assert response.status_code == 422
    assert response.json()["code"] == 30


def test_core_readiness_endpoint_failed_candidate_returns_no_runtime_or_agent_success() -> None:
    client = _client()
    invalid = deepcopy(_worldspec_payload())
    invalid["root"]["id"] = ""

    response = client.post(
        "/world/generation/core-readiness",
        json={
            "request_id": "core-ready-invalid",
            "worldspec": invalid,
        },
    )

    assert response.status_code == 200
    data = response.json()["data"]
    assert data["validation_status"] == "failed"
    assert data["runtime_readiness"]["validation_status"] == "failed"
    assert data["isolated_runtime_step"] is None
    assert data["agent_loop_probe"] is None
    assert data["diagnostics"]
