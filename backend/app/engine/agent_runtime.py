from __future__ import annotations

from dataclasses import dataclass
from typing import List

from app.engine.models import EngineSessionRecord
from app.schemas.engine_v1 import AgentExperienceRef


@dataclass(frozen=True)
class AgentCyclePlan:
    agent_id: str
    action_id: str
    target_ref: str
    amount: int
    intent: str
    decision_mode: str
    experience_refs_used: List[AgentExperienceRef]


def plan_agent_cycle(record: EngineSessionRecord) -> AgentCyclePlan:
    agent_id = sorted(record.agents)[0]
    agent = record.agents[agent_id]
    variable = sorted(
        record.package.world_spec["state_variables"],
        key=lambda item: item["key"],
    )[0]
    target_ref = variable["key"]
    amount = variable["step"]
    if record.variables[target_ref] + amount > variable["maximum"]:
        amount = -variable["step"]

    experience_refs = list(agent.experience_refs[-5:])
    if experience_refs:
        intent = "repeat_rule_accepted_action"
        decision_mode = "experience_guided_policy"
    else:
        intent = "explore_allowed_action"
        decision_mode = "initial_policy"

    return AgentCyclePlan(
        agent_id=agent_id,
        action_id=f"action.adjust.{target_ref}",
        target_ref=target_ref,
        amount=amount,
        intent=intent,
        decision_mode=decision_mode,
        experience_refs_used=experience_refs,
    )
