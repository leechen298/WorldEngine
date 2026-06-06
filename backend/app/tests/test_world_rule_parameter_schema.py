from __future__ import annotations

from app.core.world_rule_parameters import (
    build_public_world_rule_summary,
    validate_generated_rule_parameter_set,
)
from app.schemas.world_generation import GeneratedRuleParameterSet


def _valid_rule_parameter_set() -> GeneratedRuleParameterSet:
    return GeneratedRuleParameterSet(
        world_id="world-public-1",
        generation_id="generation-public-1",
        premise_digest="abcdef123456",
        parameters=[
            {
                "parameter_id": "param.weather_intensity",
                "path": "environment.weather_intensity",
                "value_type": "int",
                "initial_value": 2,
                "visibility": "public",
                "description": "public weather intensity",
                "constraints": {"min": 0, "max": 10},
                "source": {"kind": "generated", "ref": "0.9.3-test"},
                "rule_refs": ["rule.weather_drift"],
            },
            {
                "parameter_id": "param.robot_patience",
                "path": "agent_public.robot_patience",
                "value_type": "float",
                "initial_value": 0.6,
                "visibility": "public",
                "description": "public aggregate patience signal",
                "constraints": {"min": 0, "max": 1},
                "source": {"kind": "generated", "ref": "0.9.3-test"},
                "rule_refs": [],
            },
        ],
        rules=[
            {
                "rule_id": "rule.weather_drift",
                "rule_kind": "environment_trend",
                "trigger": {"type": "tick_interval", "interval": 3},
                "conditions": [{"type": "parameter_min", "parameter_ref": "param.weather_intensity", "min": 0}],
                "effects": [
                    {
                        "op": "set",
                        "parameter_ref": "param.weather_intensity",
                        "value_expression": {"type": "bounded_delta", "delta": 1, "min": 0, "max": 10},
                    }
                ],
                "target_parameter_refs": ["param.weather_intensity"],
                "allowed_ops": ["set"],
                "priority": 10,
                "cooldown": {"ticks": 1},
                "evidence": {"public_explanation": "weather may intensify within public bounds"},
            }
        ],
        constraints=[
            {
                "constraint_id": "constraint.weather_bounds",
                "scope": "parameter",
                "target_refs": ["param.weather_intensity"],
                "rule_refs": ["rule.weather_drift"],
                "expression": {"type": "range", "min": 0, "max": 10},
                "public_explanation": "weather intensity remains bounded",
            }
        ],
        boundaries=[
            {
                "boundary_id": "boundary.no_private_state",
                "category": "private_state",
                "target_refs": ["param.robot_patience"],
                "public_explanation": "rules cannot mutate private agent memory",
            }
        ],
    )


def test_valid_generated_rule_parameter_set_is_accepted_and_summarized() -> None:
    rule_set = _valid_rule_parameter_set()

    result = validate_generated_rule_parameter_set(rule_set)
    summary = build_public_world_rule_summary(rule_set, result)

    assert result.validation_status == "accepted"
    assert result.accepted_parameter_count == 2
    assert result.accepted_rule_count == 1
    assert result.rejected_parameter_count == 0
    assert result.rejected_rule_count == 0
    assert result.redaction_status == "passed"
    assert result.diagnostics == []
    assert summary.world_id == "world-public-1"
    assert summary.parameter_paths == [
        "agent_public.robot_patience",
        "environment.weather_intensity",
    ]
    assert summary.rule_ids == ["rule.weather_drift"]
    assert summary.boundary_ids == ["boundary.no_private_state"]


def test_duplicate_parameter_ids_are_rejected() -> None:
    payload = _valid_rule_parameter_set().model_dump()
    payload["parameters"][1]["parameter_id"] = "param.weather_intensity"

    result = validate_generated_rule_parameter_set(GeneratedRuleParameterSet.model_validate(payload))

    assert result.validation_status == "rejected"
    assert any(diagnostic.code == "duplicate_parameter_id" for diagnostic in result.diagnostics)


def test_duplicate_rule_ids_are_rejected() -> None:
    payload = _valid_rule_parameter_set().model_dump()
    duplicate_rule = dict(payload["rules"][0])
    payload["rules"].append(duplicate_rule)

    result = validate_generated_rule_parameter_set(GeneratedRuleParameterSet.model_validate(payload))

    assert result.validation_status == "rejected"
    assert any(diagnostic.code == "duplicate_rule_id" for diagnostic in result.diagnostics)


def test_unresolved_rule_and_parameter_refs_are_rejected() -> None:
    payload = _valid_rule_parameter_set().model_dump()
    payload["parameters"][0]["rule_refs"] = ["rule.missing"]
    payload["rules"][0]["target_parameter_refs"] = ["param.missing"]
    payload["rules"][0]["effects"][0]["parameter_ref"] = "param.missing"
    payload["constraints"][0]["target_refs"] = ["param.missing"]
    payload["constraints"][0]["rule_refs"] = ["rule.missing"]

    result = validate_generated_rule_parameter_set(GeneratedRuleParameterSet.model_validate(payload))
    codes = {diagnostic.code for diagnostic in result.diagnostics}

    assert result.validation_status == "rejected"
    assert "unresolved_rule_ref" in codes
    assert "unresolved_parameter_ref" in codes


def test_initial_value_type_mismatch_is_rejected() -> None:
    payload = _valid_rule_parameter_set().model_dump()
    payload["parameters"][0]["initial_value"] = "stormy"

    result = validate_generated_rule_parameter_set(GeneratedRuleParameterSet.model_validate(payload))

    assert result.validation_status == "rejected"
    assert any(diagnostic.code == "parameter_type_mismatch" for diagnostic in result.diagnostics)


def test_prose_only_rules_are_rejected() -> None:
    payload = _valid_rule_parameter_set().model_dump()
    payload["rules"][0]["trigger"] = {}
    payload["rules"][0]["effects"] = []
    payload["rules"][0]["target_parameter_refs"] = []

    result = validate_generated_rule_parameter_set(GeneratedRuleParameterSet.model_validate(payload))
    codes = {diagnostic.code for diagnostic in result.diagnostics}

    assert result.validation_status == "rejected"
    assert "missing_rule_trigger" in codes
    assert "missing_rule_effects" in codes
    assert "missing_rule_targets" in codes


def test_private_markers_in_public_fields_are_rejected_without_echo() -> None:
    payload = _valid_rule_parameter_set().model_dump()
    payload["parameters"][0]["description"] = "raw prompt sk-live-secret"
    payload["rules"][0]["evidence"]["public_explanation"] = "provider_trace hidden context"
    payload["boundaries"][0]["public_explanation"] = "private memory"

    result = validate_generated_rule_parameter_set(GeneratedRuleParameterSet.model_validate(payload))
    serialized = str(result.model_dump()).lower()

    assert result.validation_status == "rejected"
    assert any(diagnostic.code == "private_marker_detected" for diagnostic in result.diagnostics)
    assert "sk-live-secret" not in serialized
    assert "raw prompt" not in serialized
    assert "provider_trace" not in serialized
    assert "hidden context" not in serialized
    assert "private memory" not in serialized


def test_private_markers_in_initial_values_are_rejected_without_echo() -> None:
    payload = _valid_rule_parameter_set().model_dump()
    payload["parameters"][0]["value_type"] = "string"
    payload["parameters"][0]["initial_value"] = "raw prompt sk-live-secret"

    result = validate_generated_rule_parameter_set(GeneratedRuleParameterSet.model_validate(payload))
    serialized = str(result.model_dump()).lower()

    assert result.validation_status == "rejected"
    assert result.redaction_status == "failed"
    assert any(diagnostic.code == "private_marker_detected" for diagnostic in result.diagnostics)
    assert "sk-live-secret" not in serialized
    assert "raw prompt" not in serialized


def test_private_markers_in_refs_are_redaction_failures_without_echo() -> None:
    payload = _valid_rule_parameter_set().model_dump()
    payload["rules"][0]["target_parameter_refs"] = ["raw_prompt.sk-live-secret"]
    payload["rules"][0]["effects"][0]["parameter_ref"] = "provider_trace.hidden_context"
    payload["constraints"][0]["target_refs"] = ["private memory"]
    payload["constraints"][0]["rule_refs"] = ["raw response"]

    result = validate_generated_rule_parameter_set(GeneratedRuleParameterSet.model_validate(payload))
    serialized = str(result.model_dump()).lower()

    assert result.validation_status == "rejected"
    assert result.redaction_status == "failed"
    assert any(diagnostic.code == "private_marker_detected" for diagnostic in result.diagnostics)
    assert "sk-live-secret" not in serialized
    assert "provider_trace" not in serialized
    assert "private memory" not in serialized
    assert "raw response" not in serialized


def test_rejected_rule_summary_does_not_echo_private_marker_fields() -> None:
    payload = _valid_rule_parameter_set().model_dump()
    payload["parameters"][0]["path"] = "raw_prompt.sk-live-secret"
    payload["rules"][0]["rule_id"] = "provider_trace.rule"
    payload["boundaries"][0]["boundary_id"] = "private memory boundary"
    rule_set = GeneratedRuleParameterSet.model_validate(payload)
    result = validate_generated_rule_parameter_set(rule_set)

    summary = build_public_world_rule_summary(rule_set, result)
    serialized = str(summary.model_dump()).lower()

    assert result.validation_status == "rejected"
    assert result.redaction_status == "failed"
    assert summary.redaction_status == "failed"
    assert summary.parameter_paths == []
    assert summary.rule_ids == []
    assert summary.boundary_ids == []
    assert "sk-live-secret" not in serialized
    assert "raw_prompt" not in serialized
    assert "provider_trace" not in serialized
    assert "private memory" not in serialized


def test_generated_parameter_definitions_do_not_make_runtime_paths_writable() -> None:
    payload = _valid_rule_parameter_set().model_dump()
    payload["parameters"][0]["path"] = "generated.weather_intensity"
    rule_set = GeneratedRuleParameterSet.model_validate(payload)

    result = validate_generated_rule_parameter_set(rule_set)

    assert result.validation_status == "accepted"
    assert result.compatibility_summary["runtime_paths_granted"] == []
