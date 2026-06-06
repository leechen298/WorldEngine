from __future__ import annotations

from collections import Counter
from typing import Any, Iterable

from app.schemas.world_generation import (
    GeneratedRuleParameterSet,
    PublicWorldRuleSummary,
    RuleParameterDiagnostic,
    RuleParameterValidationResult,
    _private_mapping_markers,
)


def validate_generated_rule_parameter_set(
    rule_set: GeneratedRuleParameterSet,
) -> RuleParameterValidationResult:
    diagnostics: list[RuleParameterDiagnostic] = []
    parameter_ids = [parameter.parameter_id for parameter in rule_set.parameters]
    parameter_paths = [parameter.path for parameter in rule_set.parameters]
    rule_ids = [rule.rule_id for rule in rule_set.rules]
    parameter_id_set = set(parameter_ids)
    rule_id_set = set(rule_ids)

    diagnostics.extend(
        _duplicate_diagnostics(
            parameter_ids,
            code="duplicate_parameter_id",
            message="parameter ids must be unique",
            path="/parameters",
        )
    )
    diagnostics.extend(
        _duplicate_diagnostics(
            parameter_paths,
            code="duplicate_parameter_path",
            message="parameter paths must be unique",
            path="/parameters",
        )
    )
    diagnostics.extend(
        _duplicate_diagnostics(
            rule_ids,
            code="duplicate_rule_id",
            message="rule ids must be unique",
            path="/rules",
        )
    )

    for index, parameter in enumerate(rule_set.parameters):
        if not _value_matches_type(parameter.initial_value, parameter.value_type):
            diagnostics.append(
                _diagnostic(
                    "parameter_type_mismatch",
                    "initial value must match declared value_type",
                    f"/parameters/{index}/initial_value",
                )
            )
        for rule_ref in parameter.rule_refs:
            if rule_ref not in rule_id_set:
                diagnostics.append(
                    _diagnostic(
                        "unresolved_rule_ref",
                        "parameter rule_refs must resolve to rule ids in the same set",
                        f"/parameters/{index}/rule_refs",
                    )
                )

    for index, rule in enumerate(rule_set.rules):
        if not rule.trigger:
            diagnostics.append(
                _diagnostic(
                    "missing_rule_trigger",
                    "rule trigger must be structured",
                    f"/rules/{index}/trigger",
                )
            )
        if not rule.effects:
            diagnostics.append(
                _diagnostic(
                    "missing_rule_effects",
                    "rule effects must be structured",
                    f"/rules/{index}/effects",
                )
            )
        if not rule.target_parameter_refs:
            diagnostics.append(
                _diagnostic(
                    "missing_rule_targets",
                    "rule must target at least one parameter",
                    f"/rules/{index}/target_parameter_refs",
                )
            )
        for parameter_ref in rule.target_parameter_refs:
            diagnostics.extend(
                _parameter_ref_diagnostics(
                    parameter_ref,
                    parameter_id_set,
                    f"/rules/{index}/target_parameter_refs",
                )
            )
        for effect_index, effect in enumerate(rule.effects):
            diagnostics.extend(
                _parameter_ref_diagnostics(
                    effect.parameter_ref,
                    parameter_id_set,
                    f"/rules/{index}/effects/{effect_index}/parameter_ref",
                )
            )

    for index, constraint in enumerate(rule_set.constraints):
        for target_ref in constraint.target_refs:
            diagnostics.extend(
                _parameter_ref_diagnostics(
                    target_ref,
                    parameter_id_set,
                    f"/constraints/{index}/target_refs",
                )
            )
        for rule_ref in constraint.rule_refs:
            if rule_ref not in rule_id_set:
                diagnostics.append(
                    _diagnostic(
                        "unresolved_rule_ref",
                        "constraint rule_refs must resolve to rule ids in the same set",
                        f"/constraints/{index}/rule_refs",
                    )
                )

    diagnostics.extend(_private_marker_diagnostics(rule_set))

    rejected_parameter_count = _count_rejected_prefix(diagnostics, "/parameters/")
    rejected_rule_count = _count_rejected_prefix(diagnostics, "/rules/")
    validation_status = "rejected" if diagnostics else "accepted"
    redaction_status = (
        "failed"
        if any(diagnostic.code == "private_marker_detected" for diagnostic in diagnostics)
        else "passed"
    )
    return RuleParameterValidationResult(
        validation_status=validation_status,
        diagnostics=diagnostics,
        accepted_parameter_count=0 if diagnostics else len(rule_set.parameters),
        accepted_rule_count=0 if diagnostics else len(rule_set.rules),
        rejected_parameter_count=rejected_parameter_count,
        rejected_rule_count=rejected_rule_count,
        redaction_status=redaction_status,
        compatibility_summary={
            "runtime_paths_granted": [],
            "existing_world_params_behavior": "unchanged",
        },
    )


def build_public_world_rule_summary(
    rule_set: GeneratedRuleParameterSet,
    result: RuleParameterValidationResult,
) -> PublicWorldRuleSummary:
    if result.redaction_status == "failed":
        parameter_paths: list[str] = []
        rule_ids: list[str] = []
        boundary_ids: list[str] = []
    else:
        parameter_paths = sorted(parameter.path for parameter in rule_set.parameters)
        rule_ids = sorted(rule.rule_id for rule in rule_set.rules)
        boundary_ids = sorted(boundary.boundary_id for boundary in rule_set.boundaries)

    return PublicWorldRuleSummary(
        world_id=rule_set.world_id,
        generation_id=rule_set.generation_id,
        premise_digest=rule_set.premise_digest,
        validation_status=result.validation_status,
        parameter_paths=parameter_paths,
        rule_ids=rule_ids,
        boundary_ids=boundary_ids,
        diagnostics_count=len(result.diagnostics),
        redaction_status=result.redaction_status,
    )


def _duplicate_diagnostics(
    values: Iterable[str],
    *,
    code: str,
    message: str,
    path: str,
) -> list[RuleParameterDiagnostic]:
    return [
        _diagnostic(code, message, path)
        for value, count in Counter(values).items()
        if count > 1
    ]


def _parameter_ref_diagnostics(
    parameter_ref: str,
    parameter_ids: set[str],
    path: str,
) -> list[RuleParameterDiagnostic]:
    if parameter_ref in parameter_ids:
        return []
    return [
        _diagnostic(
            "unresolved_parameter_ref",
            "parameter reference must resolve to a parameter id in the same set",
            path,
        )
    ]


def _private_marker_diagnostics(
    rule_set: GeneratedRuleParameterSet,
) -> list[RuleParameterDiagnostic]:
    diagnostics: list[RuleParameterDiagnostic] = []
    scan_targets: list[tuple[str, Any]] = [
        ("/world_id", rule_set.world_id),
        ("/generation_id", rule_set.generation_id),
        ("/premise_digest", rule_set.premise_digest),
        ("/metadata", rule_set.metadata),
    ]
    for index, parameter in enumerate(rule_set.parameters):
        scan_targets.extend(
            [
                (f"/parameters/{index}/parameter_id", parameter.parameter_id),
                (f"/parameters/{index}/path", parameter.path),
                (f"/parameters/{index}/initial_value", parameter.initial_value),
                (f"/parameters/{index}/description", parameter.description),
                (f"/parameters/{index}/constraints", parameter.constraints),
                (f"/parameters/{index}/source", parameter.source),
                (f"/parameters/{index}/rule_refs", parameter.rule_refs),
            ]
        )
    for index, rule in enumerate(rule_set.rules):
        scan_targets.extend(
            [
                (f"/rules/{index}/rule_id", rule.rule_id),
                (f"/rules/{index}/trigger", rule.trigger),
                (f"/rules/{index}/conditions", rule.conditions),
                (f"/rules/{index}/target_parameter_refs", rule.target_parameter_refs),
                (f"/rules/{index}/allowed_ops", rule.allowed_ops),
                (f"/rules/{index}/evidence", rule.evidence),
            ]
        )
        for effect_index, effect in enumerate(rule.effects):
            scan_targets.append(
                (f"/rules/{index}/effects/{effect_index}", effect.model_dump())
            )
    for index, constraint in enumerate(rule_set.constraints):
        scan_targets.extend(
            [
                (f"/constraints/{index}/constraint_id", constraint.constraint_id),
                (f"/constraints/{index}/target_refs", constraint.target_refs),
                (f"/constraints/{index}/rule_refs", constraint.rule_refs),
                (f"/constraints/{index}/expression", constraint.expression),
                (f"/constraints/{index}/public_explanation", constraint.public_explanation),
            ]
        )
    for index, boundary in enumerate(rule_set.boundaries):
        scan_targets.extend(
            [
                (f"/boundaries/{index}/boundary_id", boundary.boundary_id),
                (f"/boundaries/{index}/category", boundary.category),
                (f"/boundaries/{index}/target_refs", boundary.target_refs),
                (f"/boundaries/{index}/public_explanation", boundary.public_explanation),
            ]
        )

    for path, value in scan_targets:
        if _private_mapping_markers(value):
            diagnostics.append(
                _diagnostic(
                    "private_marker_detected",
                    "public rule parameter fields must not contain private markers",
                    path,
                )
            )
    return diagnostics


def _value_matches_type(value: Any, value_type: str) -> bool:
    if value_type == "int":
        return isinstance(value, int) and not isinstance(value, bool)
    if value_type == "float":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if value_type == "bool":
        return isinstance(value, bool)
    if value_type == "string":
        return isinstance(value, str)
    if value_type == "json":
        return _is_json_value(value)
    return False


def _is_json_value(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, (str, int, float, bool)):
        return True
    if isinstance(value, list):
        return all(_is_json_value(item) for item in value)
    if isinstance(value, dict):
        return all(isinstance(key, str) and _is_json_value(item) for key, item in value.items())
    return False


def _count_rejected_prefix(
    diagnostics: list[RuleParameterDiagnostic],
    prefix: str,
) -> int:
    return len({diagnostic.path for diagnostic in diagnostics if (diagnostic.path or "").startswith(prefix)})


def _diagnostic(
    code: str,
    message: str,
    path: str,
) -> RuleParameterDiagnostic:
    return RuleParameterDiagnostic(
        code=code,
        message=message,
        path=path,
    )
