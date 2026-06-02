from __future__ import annotations

from typing import Any, Dict

from app.core import world_generation
from app.schemas import world_generation as generation_schemas


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


def test_check_core_readiness_returns_isolated_runtime_and_noop_agent_evidence() -> None:
    assert hasattr(world_generation, "check_core_readiness")
    assert hasattr(generation_schemas, "GenerationCoreReadinessRequest")

    result = world_generation.check_core_readiness(
        generation_schemas.GenerationCoreReadinessRequest(
            request_id="core-ready-worldspec",
            worldspec=_worldspec_payload(),
            source_label="candidate.core",
        )
    )

    assert result.validation_status == "passed"
    assert result.runtime_readiness.validation_status == "passed"
    assert result.runtime_readiness.runtime_context_passed is True
    assert result.isolated_runtime_step is not None
    assert result.isolated_runtime_step.tick_id == 1
    assert result.agent_loop_probe is not None
    assert result.agent_loop_probe.intent["type"] == "noop"
    assert result.agent_loop_probe.result["status"] == "noop"
    assert result.agent_loop_probe.result["applied"] is False
    assert result.does_not_mutate_app_runtime is True


def test_check_core_readiness_failure_path_has_no_runtime_or_agent_success() -> None:
    invalid = _worldspec_payload()
    invalid["root"]["id"] = ""
    assert hasattr(generation_schemas, "GenerationCoreReadinessRequest")

    result = world_generation.check_core_readiness(
        generation_schemas.GenerationCoreReadinessRequest(
            request_id="core-ready-invalid",
            worldspec=invalid,
        )
    )

    assert result.validation_status == "failed"
    assert result.runtime_readiness.validation_status == "failed"
    assert result.isolated_runtime_step is None
    assert result.agent_loop_probe is None
    assert result.diagnostics
