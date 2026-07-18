from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Dict, List

from app.schemas.engine_v1 import AgentExperienceRef


@dataclass(frozen=True)
class AgentPerception:
    agent_id: str
    state_hash: str
    visible_variables: Dict[str, int]
    variable_specs: Dict[str, Dict[str, int]]
    available_actions: List[str]
    feedback_count: int
    experience_refs: List[AgentExperienceRef]
    recent_event_refs: List[str]

    def public_payload(self) -> Dict[str, Any]:
        return {
            "state_hash": self.state_hash,
            "visible_variables": deepcopy(self.visible_variables),
            "variable_specs": deepcopy(self.variable_specs),
            "available_actions": list(self.available_actions),
            "feedback_count": self.feedback_count,
            "experience_refs": [
                ref.model_dump(mode="json") for ref in self.experience_refs
            ],
            "recent_event_refs": list(self.recent_event_refs),
        }


@dataclass(frozen=True)
class AgentCyclePlan:
    agent_id: str
    action_id: str
    target_ref: str
    amount: int
    intent: str
    decision_mode: str
    experience_refs_used: List[AgentExperienceRef]
    visible_value: int
    feedback_count_used: int
    influence_factors: List[str]


def plan_agent_cycle(perception: AgentPerception) -> AgentCyclePlan:
    target_refs = [
        target_ref
        for target_ref in sorted(perception.visible_variables)
        if f"action.adjust.{target_ref}" in perception.available_actions
        and target_ref in perception.variable_specs
    ]
    if not target_refs:
        raise ValueError("Agent perception contains no runnable public action")

    target_ref = target_refs[0]
    variable = perception.variable_specs[target_ref]
    visible_value = perception.visible_variables[target_ref]
    midpoint = (variable["minimum"] + variable["maximum"]) / 2
    direction = 1 if visible_value <= midpoint else -1
    influence_factors = ["current_variables"]

    experience_refs = list(perception.experience_refs[-5:])
    if experience_refs:
        influence_factors.append("experience")
        matching_experience = next(
            (
                ref
                for ref in reversed(experience_refs)
                if ref.target_ref == target_ref
                and ref.amount is not None
                and ref.amount != 0
            ),
            None,
        )
        if matching_experience is not None:
            direction = 1 if matching_experience.amount > 0 else -1

    if perception.feedback_count % 2 == 1:
        direction *= -1
    if perception.feedback_count:
        influence_factors.append("feedback_count")

    amount = variable["step"] * direction
    if not variable["minimum"] <= visible_value + amount <= variable["maximum"]:
        amount = -amount
    if not variable["minimum"] <= visible_value + amount <= variable["maximum"]:
        raise ValueError("Agent perception contains no in-range action direction")

    if perception.feedback_count and experience_refs:
        intent = "adapt_to_feedback_with_experience"
        decision_mode = "feedback_adjusted_experience_policy"
    elif perception.feedback_count:
        intent = "adapt_to_feedback"
        decision_mode = "feedback_adjusted_policy"
    elif experience_refs:
        intent = "repeat_rule_accepted_action"
        decision_mode = "experience_guided_policy"
    else:
        intent = "explore_allowed_action"
        decision_mode = "initial_policy"

    return AgentCyclePlan(
        agent_id=perception.agent_id,
        action_id=f"action.adjust.{target_ref}",
        target_ref=target_ref,
        amount=amount,
        intent=intent,
        decision_mode=decision_mode,
        experience_refs_used=experience_refs,
        visible_value=visible_value,
        feedback_count_used=perception.feedback_count,
        influence_factors=influence_factors,
    )
