from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from app.schemas.engine_v1 import (
    ActionRequest,
    DirectionRequest,
    FeedbackRequest,
    RunnableWorldPackage,
)


@dataclass(frozen=True)
class RuleDecision:
    accepted: bool
    reason_code: str
    public_reason: str
    rule_refs: List[str]
    target_ref: Optional[str] = None
    delta: Optional[int] = None


def _variable_spec(package: RunnableWorldPackage, target_ref: str) -> dict | None:
    for item in package.world_spec["state_variables"]:
        if item["key"] == target_ref:
            return item
    return None


def judge_direction(
    package: RunnableWorldPackage,
    request: DirectionRequest,
) -> RuleDecision:
    if request.kind == "direct_final_fact":
        return RuleDecision(
            accepted=False,
            reason_code="direct_final_fact_forbidden",
            public_reason="Direction cannot assign a final canonical fact.",
            rule_refs=["rule.direction.no-direct-fact"],
        )

    variable = _variable_spec(package, request.target_ref)
    if variable is None:
        return RuleDecision(
            accepted=False,
            reason_code="unknown_direction_target",
            public_reason="Direction target is not declared by the runnable package.",
            rule_refs=[],
        )
    magnitude = request.magnitude or 0
    maximum = variable["step"] * 3
    if magnitude == 0 or abs(magnitude) > maximum:
        return RuleDecision(
            accepted=False,
            reason_code="direction_magnitude_out_of_bounds",
            public_reason="Direction magnitude exceeds the declared bounded rule.",
            rule_refs=[f"rule.direction.{request.target_ref}"],
        )
    return RuleDecision(
        accepted=True,
        reason_code="bounded_direction_queued",
        public_reason="Bounded direction was queued for later rule evaluation.",
        rule_refs=[f"rule.direction.{request.target_ref}"],
        target_ref=request.target_ref,
        delta=magnitude,
    )


def judge_action(
    package: RunnableWorldPackage,
    request: ActionRequest,
    current_value: int,
) -> RuleDecision:
    action = next(
        (item for item in package.action_catalog if item["action_id"] == request.action_id),
        None,
    )
    if action is None or action["target_ref"] != request.target_ref:
        return RuleDecision(
            accepted=False,
            reason_code="unknown_action",
            public_reason="Action is not declared by the runnable package.",
            rule_refs=[],
        )
    if not action["minimum_amount"] <= request.amount <= action["maximum_amount"]:
        return RuleDecision(
            accepted=False,
            reason_code="action_amount_out_of_bounds",
            public_reason="Action amount exceeds the declared action bounds.",
            rule_refs=list(action["rule_refs"]),
        )
    variable = _variable_spec(package, request.target_ref)
    if variable is None:
        return RuleDecision(
            accepted=False,
            reason_code="unknown_action_target",
            public_reason="Action target is not declared by the runnable package.",
            rule_refs=list(action["rule_refs"]),
        )
    next_value = current_value + request.amount
    if not variable["minimum"] <= next_value <= variable["maximum"]:
        return RuleDecision(
            accepted=False,
            reason_code="action_target_range_violation",
            public_reason="Action result would violate the target range.",
            rule_refs=list(action["rule_refs"]),
        )
    return RuleDecision(
        accepted=True,
        reason_code="action_rule_accepted",
        public_reason="Action passed the declared package rule.",
        rule_refs=list(action["rule_refs"]),
        target_ref=request.target_ref,
        delta=request.amount,
    )


def judge_feedback(
    package: RunnableWorldPackage,
    request: FeedbackRequest,
) -> RuleDecision:
    allowed = package.projection_manifest["allowed_feedback_types"]
    if request.feedback_type not in allowed:
        return RuleDecision(
            accepted=False,
            reason_code="feedback_type_not_allowed",
            public_reason="Feedback type is not declared by the projection manifest.",
            rule_refs=["rule.feedback.manifest"],
        )
    return RuleDecision(
        accepted=True,
        reason_code="feedback_accepted",
        public_reason="Feedback was accepted as a typed public observation.",
        rule_refs=["rule.feedback.manifest"],
    )
