from __future__ import annotations

from copy import deepcopy
from typing import Any, Iterable, Mapping

from app.core.world_rule_parameters import (
    _value_matches_type,
    validate_generated_rule_parameter_set,
)
from app.schemas.world_direction import WorldDirectionQueueItem
from app.schemas.world_evolution import (
    WorldEventCandidate,
    WorldEventLegalityDiagnostic,
    WorldEventLegalityResult,
    WorldEvolutionEvidence,
    WorldParameterPatch,
    WorldStateDiff,
    WorldStateDiffItem,
)
from app.schemas.world_generation import (
    GeneratedRuleParameterSet,
    WorldConstraint,
    WorldEvolutionRule,
    WorldParameterDefinition,
    _private_mapping_markers,
)


_DIRECT_FINAL_MARKERS = (
    "direct_final_fact",
    "final_fact",
    "force_outcome",
    "dead",
    "death",
    "kill",
    "life_death",
    "relationship",
    "inventory",
    "private_location",
    "agent.private",
    "agent_private",
    "private_state",
    "private_memory",
    "private_goal",
)


_AGENT_PUBLIC_PARAMETER_PREFIXES = (
    "agent_public_pressure.",
    "world.agent_public_pressure.",
)
_AGENT_PRIVATE_PARAMETER_SEGMENTS = {
    "goal",
    "goals",
    "inventory",
    "life_status",
    "memory",
    "personality",
    "private_goal",
    "private_memory",
    "private_location",
    "private_state",
    "relationship",
    "relationships",
    "self_state",
    "skill",
    "skills",
}


def evaluate_world_event_candidate(
    *,
    candidate: WorldEventCandidate,
    rule_set: GeneratedRuleParameterSet,
    current_params: Mapping[str, Any],
    runtime_tick: int,
    runtime_world_time_seconds: int,
    direction_queue: Iterable[WorldDirectionQueueItem] = (),
) -> WorldEventLegalityResult:
    diagnostics: list[WorldEventLegalityDiagnostic] = []
    rule_validation = validate_generated_rule_parameter_set(rule_set)
    if rule_validation.validation_status != "accepted":
        diagnostics.append(
            _diagnostic(
                "rule_set_rejected",
                "rule parameter set must be publicly accepted before event legality evaluation",
                "/rule_set",
            )
        )
    if rule_validation.redaction_status == "failed":
        diagnostics.append(
            _diagnostic(
                "private_marker_detected",
                "rule parameter set contains private markers",
                "/rule_set",
            )
        )

    if candidate.world_id != rule_set.world_id:
        diagnostics.append(
            _diagnostic(
                "world_id_mismatch",
                "candidate world_id must match rule set world_id",
                "/candidate/world_id",
            )
        )

    if _private_mapping_markers(candidate.model_dump()):
        diagnostics.append(
            _diagnostic(
                "private_marker_detected",
                "candidate contains private markers",
                "/candidate",
            )
        )

    rule_by_id = {rule.rule_id: rule for rule in rule_set.rules}
    parameter_by_id = {parameter.parameter_id: parameter for parameter in rule_set.parameters}
    parameter_index_by_id = {
        parameter.parameter_id: index for index, parameter in enumerate(rule_set.parameters)
    }

    matched_rules: list[WorldEvolutionRule] = []
    for rule_ref in candidate.rule_refs:
        rule = rule_by_id.get(rule_ref)
        if rule is None:
            diagnostics.append(
                _diagnostic(
                    "unknown_rule_ref",
                    "candidate rule_refs must resolve to public rule ids",
                    "/candidate/rule_refs",
                )
            )
            continue
        matched_rules.append(rule)

    if not candidate.cause_refs:
        diagnostics.append(
            _diagnostic(
                "missing_public_cause",
                "candidate requires at least one public cause ref",
                "/candidate/cause_refs",
            )
        )
    if not candidate.probability_evidence:
        diagnostics.append(
            _diagnostic(
                "missing_probability_evidence",
                "candidate requires public probability evidence",
                "/candidate/probability_evidence",
            )
        )
    if not candidate.causality_evidence:
        diagnostics.append(
            _diagnostic(
                "missing_causality_evidence",
                "candidate requires public causality evidence",
                "/candidate/causality_evidence",
            )
        )

    diagnostics.extend(
        _timing_diagnostics(
            candidate=candidate,
            runtime_tick=runtime_tick,
            runtime_world_time_seconds=runtime_world_time_seconds,
        )
    )
    diagnostics.extend(_direct_final_fact_diagnostics(candidate))
    diagnostics.extend(
        _direction_ref_diagnostics(
            candidate=candidate,
            direction_queue=direction_queue,
            runtime_tick=runtime_tick,
        )
    )

    diff_items: list[WorldStateDiffItem] = []
    checked_constraint_ids: set[str] = set()
    referenced_parameter_ids: set[str] = set()
    matched_rule_ids = {rule.rule_id for rule in matched_rules}

    for index, patch in enumerate(candidate.parameter_patches):
        rule = rule_by_id.get(patch.rule_ref)
        parameter = parameter_by_id.get(patch.parameter_ref)
        if patch.rule_ref not in candidate.rule_refs:
            diagnostics.append(
                _diagnostic(
                    "patch_rule_not_in_candidate",
                    "patch rule_ref must be listed in candidate rule_refs",
                    f"/candidate/parameter_patches/{index}/rule_ref",
                )
            )
        if rule is None:
            diagnostics.append(
                _diagnostic(
                    "unknown_rule_ref",
                    "patch rule_ref must resolve to a public rule id",
                    f"/candidate/parameter_patches/{index}/rule_ref",
                )
            )
            continue
        if parameter is None:
            diagnostics.append(
                _diagnostic(
                    "unknown_parameter_ref",
                    "patch parameter_ref must resolve to a public parameter id",
                    f"/candidate/parameter_patches/{index}/parameter_ref",
                )
            )
            continue
        referenced_parameter_ids.add(parameter.parameter_id)
        if _is_agent_private_parameter_path(parameter.path):
            parameter_index = parameter_index_by_id[parameter.parameter_id]
            diagnostics.append(
                _diagnostic(
                    "agent_private_parameter_path",
                    "rule-linked evolution must not target Agent personality, skills, or private state paths",
                    f"/rule_set/parameters/{parameter_index}/path",
                )
            )
            continue
        if parameter.parameter_id not in rule.target_parameter_refs:
            diagnostics.append(
                _diagnostic(
                    "parameter_not_targeted_by_rule",
                    "patch parameter_ref must be targeted by the matched rule",
                    f"/candidate/parameter_patches/{index}/parameter_ref",
                )
            )
        if patch.op not in rule.allowed_ops:
            diagnostics.append(
                _diagnostic(
                    "operation_not_allowed",
                    "patch op must be listed in the matched rule allowed_ops",
                    f"/candidate/parameter_patches/{index}/op",
                )
            )
        old_value = _get_public_param_value(current_params, parameter.path, parameter.initial_value)
        new_value = _apply_patch_value(old_value, patch)
        if patch.op != "remove" and not _value_matches_type(new_value, parameter.value_type):
            diagnostics.append(
                _diagnostic(
                    "parameter_type_mismatch",
                    "post-patch value must match the public parameter value_type",
                    f"/candidate/parameter_patches/{index}/value",
                )
            )

        constraint_ids = _constraint_ids_for_patch(
            constraints=rule_set.constraints,
            parameter=parameter,
            rule=rule,
        )
        checked_constraint_ids.update(constraint_ids)
        diagnostics.extend(
            _constraint_diagnostics(
                constraints=rule_set.constraints,
                parameter=parameter,
                rule=rule,
                value=new_value,
                patch_index=index,
            )
        )
        diff_items.append(
            WorldStateDiffItem(
                parameter_ref=parameter.parameter_id,
                path=parameter.path,
                old_public_value=old_value,
                new_public_value=new_value,
                op=patch.op,
                rule_id=rule.rule_id,
                constraint_ids=constraint_ids,
                public_explanation=patch.public_explanation,
            )
        )

    status = "rejected" if diagnostics else "accepted"
    state_diff = None
    evidence = None
    if status == "accepted":
        state_diff = WorldStateDiff(
            changed_parameter_ids=sorted({item.parameter_ref for item in diff_items}),
            items=diff_items,
            direct_private_mutation_applied=False,
            redaction_status="passed",
        )
        evidence = WorldEvolutionEvidence(
            world_id=candidate.world_id,
            candidate_id=candidate.candidate_id,
            legality_status="accepted",
            matched_rule_ids=sorted(matched_rule_ids),
            checked_constraint_ids=sorted(checked_constraint_ids),
            referenced_parameter_ids=sorted(referenced_parameter_ids),
            direction_refs=list(candidate.direction_refs),
            state_snapshot_refs={
                "runtime_tick": runtime_tick,
                "runtime_world_time_seconds": runtime_world_time_seconds,
            },
            diagnostics_count=0,
            state_diff_summary={
                "changed_parameter_ids": sorted({item.parameter_ref for item in diff_items}),
                "changed_count": len(diff_items),
            },
            redaction_status="passed",
            direct_state_mutation_applied=False,
        )

    redaction_status = (
        "failed"
        if any(diagnostic.code == "private_marker_detected" for diagnostic in diagnostics)
        else "passed"
    )
    return WorldEventLegalityResult(
        status=status,
        legality_classification="legal" if status == "accepted" else "illegal",
        diagnostics=diagnostics,
        matched_rule_ids=sorted(matched_rule_ids),
        checked_constraint_ids=sorted(checked_constraint_ids),
        referenced_parameter_ids=sorted(referenced_parameter_ids),
        timing_evidence={
            "runtime_tick": runtime_tick,
            "runtime_world_time_seconds": runtime_world_time_seconds,
            "candidate_tick": candidate.proposed_tick,
            "candidate_world_time_seconds": candidate.proposed_world_time_seconds,
        },
        probability_evidence=deepcopy(candidate.probability_evidence) if redaction_status == "passed" else {},
        causality_evidence=deepcopy(candidate.causality_evidence) if redaction_status == "passed" else {},
        redaction_status=redaction_status,
        state_diff=state_diff,
        evidence=evidence,
        direct_state_mutation_applied=False,
    )


def build_rule_bound_session_event_candidate(
    *,
    world_id: str,
    rule_set: GeneratedRuleParameterSet,
    current_params: Mapping[str, Any],
    runtime_tick: int,
    runtime_world_time_seconds: int,
    direction_queue: Iterable[WorldDirectionQueueItem] = (),
) -> WorldEventCandidate | None:
    rule_by_priority = sorted(
        rule_set.rules,
        key=lambda item: (-item.priority, item.rule_id),
    )
    parameter_by_id = {parameter.parameter_id: parameter for parameter in rule_set.parameters}
    directions = _applicable_direction_ids(
        world_id=world_id,
        direction_queue=direction_queue,
        runtime_tick=runtime_tick,
    )

    for rule in rule_by_priority:
        for effect in rule.effects:
            parameter = parameter_by_id.get(effect.parameter_ref)
            if parameter is None or parameter.visibility != "public":
                continue
            if _is_agent_private_parameter_path(parameter.path):
                continue
            if rule.target_parameter_refs and parameter.parameter_id not in rule.target_parameter_refs:
                continue
            if rule.allowed_ops and effect.op not in rule.allowed_ops:
                continue
            old_value = _get_public_param_value(
                current_params,
                parameter.path,
                parameter.initial_value,
            )
            new_value = _next_public_value(
                old_value=old_value,
                parameter=parameter,
                effect_value_expression=effect.value_expression,
            )
            return WorldEventCandidate(
                candidate_id=f"candidate-session-{runtime_tick}-{rule.rule_id}",
                world_id=world_id,
                event_type=f"world.rule.{rule.rule_kind}",
                source="world_rule",
                proposed_tick=runtime_tick,
                proposed_world_time_seconds=runtime_world_time_seconds,
                rule_refs=[rule.rule_id],
                parameter_patches=[
                    WorldParameterPatch(
                        parameter_ref=parameter.parameter_id,
                        op=effect.op,
                        value=new_value,
                        rule_ref=rule.rule_id,
                        public_explanation=(
                            "Public rule-bound session evolution selected this parameter change."
                        ),
                    )
                ],
                direction_refs=directions[:1],
                cause_refs=[f"runtime.tick.{runtime_tick}"],
                probability_evidence={
                    "source": "public_rule_bound_session_step",
                    "selection": "deterministic",
                    "direction_ref_count": len(directions),
                },
                causality_evidence={
                    "rule_id": rule.rule_id,
                    "parameter_ref": parameter.parameter_id,
                    "cause": "public rule and current session state",
                },
                public_summary="Rule-bound public session evolution candidate.",
            )
    return None


def _applicable_direction_ids(
    *,
    world_id: str,
    direction_queue: Iterable[WorldDirectionQueueItem],
    runtime_tick: int,
) -> list[str]:
    direction_ids: list[str] = []
    for item in direction_queue:
        if item.world_id != world_id or item.status != "queued" or not item.classification.allowed:
            continue
        if item.apply_after_tick is not None and runtime_tick < item.apply_after_tick:
            continue
        if item.expires_after_tick is not None and runtime_tick > item.expires_after_tick:
            continue
        direction_ids.append(item.direction_id)
    return sorted(direction_ids)


def _next_public_value(
    *,
    old_value: Any,
    parameter: WorldParameterDefinition,
    effect_value_expression: Mapping[str, Any],
) -> Any:
    expression_type = effect_value_expression.get("type")
    minimum = effect_value_expression.get("min", parameter.constraints.get("min"))
    maximum = effect_value_expression.get("max", parameter.constraints.get("max"))

    if expression_type == "bounded_value" or minimum is not None or maximum is not None:
        lower = minimum if isinstance(minimum, (int, float)) else None
        upper = maximum if isinstance(maximum, (int, float)) else None
        if isinstance(old_value, (int, float)) and not isinstance(old_value, bool):
            next_value: Any = old_value + 1
        elif lower is not None:
            next_value = lower
        else:
            next_value = parameter.initial_value
        if upper is not None and isinstance(next_value, (int, float)):
            next_value = min(next_value, upper)
        if lower is not None and isinstance(next_value, (int, float)):
            next_value = max(next_value, lower)
        return next_value

    if "value" in effect_value_expression:
        return deepcopy(effect_value_expression["value"])
    return deepcopy(parameter.initial_value)


def _is_agent_private_parameter_path(path: str) -> bool:
    normalized = path.casefold().replace("/", ".").replace("-", "_")
    if normalized.startswith(_AGENT_PUBLIC_PARAMETER_PREFIXES):
        return False
    segments = [segment for segment in normalized.split(".") if segment]
    for index, segment in enumerate(segments):
        if segment in {"agent", "agents"}:
            return any(
                candidate in _AGENT_PRIVATE_PARAMETER_SEGMENTS
                for candidate in segments[index + 1 :]
            )
    return False


def _timing_diagnostics(
    *,
    candidate: WorldEventCandidate,
    runtime_tick: int,
    runtime_world_time_seconds: int,
) -> list[WorldEventLegalityDiagnostic]:
    diagnostics: list[WorldEventLegalityDiagnostic] = []
    if candidate.proposed_tick is not None and candidate.proposed_tick != runtime_tick:
        diagnostics.append(
            _diagnostic(
                "timing_outside_window",
                "candidate proposed_tick must match the current bounded runtime tick",
                "/candidate/proposed_tick",
            )
        )
    if (
        candidate.proposed_world_time_seconds is not None
        and candidate.proposed_world_time_seconds != runtime_world_time_seconds
    ):
        diagnostics.append(
            _diagnostic(
                "timing_outside_window",
                "candidate proposed_world_time_seconds must match current runtime world time",
                "/candidate/proposed_world_time_seconds",
            )
        )
    return diagnostics


def _direct_final_fact_diagnostics(
    candidate: WorldEventCandidate,
) -> list[WorldEventLegalityDiagnostic]:
    public_text = " ".join(_public_candidate_strings(candidate.model_dump())).casefold()
    if not any(marker in public_text for marker in _DIRECT_FINAL_MARKERS):
        return []
    return [
        _diagnostic(
            "direct_final_fact_or_private_state",
            "candidate attempts direct final fact or Agent private-state mutation",
            "/candidate",
        )
    ]


def _public_candidate_strings(value: Any) -> list[str]:
    if isinstance(value, dict):
        strings: list[str] = []
        for key, item in value.items():
            strings.append(str(key))
            strings.extend(_public_candidate_strings(item))
        return strings
    if isinstance(value, list):
        strings = []
        for item in value:
            strings.extend(_public_candidate_strings(item))
        return strings
    if isinstance(value, str):
        return [value]
    return []


def _direction_ref_diagnostics(
    *,
    candidate: WorldEventCandidate,
    direction_queue: Iterable[WorldDirectionQueueItem],
    runtime_tick: int,
) -> list[WorldEventLegalityDiagnostic]:
    if not candidate.direction_refs:
        return []
    queued_by_id = {item.direction_id: item for item in direction_queue}
    diagnostics: list[WorldEventLegalityDiagnostic] = []
    for direction_ref in candidate.direction_refs:
        item = queued_by_id.get(direction_ref)
        if item is None or item.world_id != candidate.world_id:
            diagnostics.append(
                _diagnostic(
                    "unknown_direction_ref",
                    "direction_refs must resolve to queued public world direction items",
                    "/candidate/direction_refs",
                )
            )
            continue
        if item.status != "queued" or not item.classification.allowed:
            diagnostics.append(
                _diagnostic(
                    "direction_ref_not_queued",
                    "direction_refs must point to allowed queued public direction items",
                    "/candidate/direction_refs",
                )
            )
        if item.apply_after_tick is not None and runtime_tick < item.apply_after_tick:
            diagnostics.append(
                _diagnostic(
                    "direction_ref_before_apply_window",
                    "direction guidance is not yet inside its apply window",
                    "/candidate/direction_refs",
                )
            )
        if item.expires_after_tick is not None and runtime_tick > item.expires_after_tick:
            diagnostics.append(
                _diagnostic(
                    "direction_ref_expired",
                    "direction guidance has expired",
                    "/candidate/direction_refs",
                )
            )
    return diagnostics


def _constraint_ids_for_patch(
    *,
    constraints: Iterable[WorldConstraint],
    parameter: WorldParameterDefinition,
    rule: WorldEvolutionRule,
) -> list[str]:
    return sorted(
        constraint.constraint_id
        for constraint in constraints
        if parameter.parameter_id in constraint.target_refs
        and (not constraint.rule_refs or rule.rule_id in constraint.rule_refs)
    )


def _constraint_diagnostics(
    *,
    constraints: Iterable[WorldConstraint],
    parameter: WorldParameterDefinition,
    rule: WorldEvolutionRule,
    value: Any,
    patch_index: int,
) -> list[WorldEventLegalityDiagnostic]:
    diagnostics: list[WorldEventLegalityDiagnostic] = []
    for constraint in constraints:
        if parameter.parameter_id not in constraint.target_refs:
            continue
        if constraint.rule_refs and rule.rule_id not in constraint.rule_refs:
            continue
        if not _value_satisfies_constraint(value, constraint.expression):
            diagnostics.append(
                _diagnostic(
                    "constraint_violation",
                    "post-patch value must satisfy public constraints",
                    f"/candidate/parameter_patches/{patch_index}/value",
                )
            )
    return diagnostics


def _value_satisfies_constraint(value: Any, expression: Mapping[str, Any]) -> bool:
    if not expression:
        return True
    if "enum" in expression:
        enum_values = expression["enum"]
        if isinstance(enum_values, list) and value not in enum_values:
            return False
    minimum = expression.get("min")
    maximum = expression.get("max")
    if minimum is not None or maximum is not None:
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            return False
        if minimum is not None and value < minimum:
            return False
        if maximum is not None and value > maximum:
            return False
    return True


def _apply_patch_value(old_value: Any, patch: WorldParameterPatch) -> Any:
    if patch.op == "set":
        return deepcopy(patch.value)
    if patch.op == "add":
        if isinstance(old_value, (int, float)) and isinstance(patch.value, (int, float)):
            return old_value + patch.value
        return deepcopy(patch.value)
    return None


def _get_public_param_value(
    current_params: Mapping[str, Any],
    path: str,
    fallback: Any,
) -> Any:
    current: Any = current_params
    for key in [segment for segment in path.split(".") if segment]:
        if not isinstance(current, Mapping) or key not in current:
            return deepcopy(fallback)
        current = current[key]
    return deepcopy(current)


def _diagnostic(
    code: str,
    message: str,
    path: str,
) -> WorldEventLegalityDiagnostic:
    return WorldEventLegalityDiagnostic(
        code=code,
        message=message,
        path=path,
    )
