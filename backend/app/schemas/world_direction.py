from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, model_validator
from pydantic_core import PydanticCustomError


WorldDirectionAllowedCategory = Literal[
    "environment_trend",
    "external_pressure",
    "event_candidate_bias",
    "probability_shift",
    "rule_constraint",
    "future_evaluation_hint",
]
WorldDirectionForbiddenCategory = Literal[
    "direct_final_fact",
    "agent_private_state_mutation",
    "agent_goal_mutation",
    "inventory_injection",
    "relationship_override",
    "rule_bypass",
    "private_marker_detected",
]
WorldDirectionCategory = Union[WorldDirectionAllowedCategory, WorldDirectionForbiddenCategory]
WorldDirectionStatus = Literal["queued", "rejected", "blocked", "unavailable"]
WorldDirectionQueueStatus = Literal["queued", "expired", "consumed"]
WorldDirectionRedactionStatus = Literal["clean", "redacted"]


PRIVATE_MARKERS = (
    "api_key",
    "api key",
    "apikey",
    "authorization",
    "bearer",
    "credential",
    "hidden context",
    "hidden_context",
    "private evaluator data",
    "private_evaluator_data",
    "private goal",
    "private memory",
    "private_memory",
    "private prompt",
    "private_prompt",
    "provider trace",
    "provider_trace",
    "provider_secret",
    "raw prompt",
    "raw_prompt",
    "raw provider request",
    "raw_provider_request",
    "raw provider response",
    "raw_provider_response",
    "raw request",
    "raw_request",
    "raw response",
    "raw_response",
    "sk-live-",
    "sk-test-",
    "self_state",
)


class WorldDirectionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    instruction_text: str = Field(min_length=1)
    branch_id: Optional[str] = Field(default=None, min_length=1)
    apply_after_tick: Optional[int] = Field(default=None, ge=0)
    expires_after_tick: Optional[int] = Field(default=None, ge=0)
    public_context: Dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def _timing_window_is_bounded(self) -> "WorldDirectionRequest":
        if (
            self.apply_after_tick is not None
            and self.expires_after_tick is not None
            and self.expires_after_tick < self.apply_after_tick
        ):
            raise PydanticCustomError(
                "world_direction_invalid_timing_window",
                "expires_after_tick must be greater than or equal to apply_after_tick",
            )
        return self


class WorldDirectionClassification(BaseModel):
    model_config = ConfigDict(extra="forbid")

    allowed: bool
    category: WorldDirectionCategory
    public_reason: str = Field(min_length=1)
    redaction_status: WorldDirectionRedactionStatus = "clean"


class WorldDirectionQueueItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    direction_id: str = Field(min_length=1)
    world_id: str = Field(min_length=1)
    status: WorldDirectionQueueStatus = "queued"
    classification: WorldDirectionClassification
    public_summary: str = Field(min_length=1)
    apply_after_tick: Optional[int] = Field(default=None, ge=0)
    expires_after_tick: Optional[int] = Field(default=None, ge=0)
    public_context_keys: List[str] = Field(default_factory=list)
    future_rule_refs: List[str] = Field(default_factory=list)
    redaction_status: WorldDirectionRedactionStatus = "clean"


class WorldDirectionResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    world_id: str = Field(min_length=1)
    status: WorldDirectionStatus
    classification: WorldDirectionClassification
    queue_item: Optional[WorldDirectionQueueItem] = None
    rejection_reason: Optional[WorldDirectionForbiddenCategory] = None
    public_explanation: str = Field(min_length=1)
    direct_state_mutation_applied: bool = False


class WorldDirectionSummary(BaseModel):
    model_config = ConfigDict(extra="forbid")

    world_id: str = Field(min_length=1)
    queued_items: List[WorldDirectionQueueItem] = Field(default_factory=list)
    rejected_count: int = Field(default=0, ge=0)


def classify_world_direction(
    instruction_text: str,
    branch_id: Optional[str] = None,
    public_context_keys: Optional[Iterable[str]] = None,
    public_context_values: Optional[Iterable[Any]] = None,
) -> WorldDirectionClassification:
    if _contains_private_marker(
        instruction_text,
        branch_id,
        public_context_keys or (),
        public_context_values or (),
    ):
        return WorldDirectionClassification(
            allowed=False,
            category="private_marker_detected",
            public_reason="Rejected because the direction referenced private or non-public data.",
            redaction_status="redacted",
        )

    normalized = instruction_text.casefold()
    if _contains_any(
        normalized,
        (
            "kill",
            "dead",
            "dies",
            "death",
            "die immediately",
            "heal immediately",
            "teleport",
            "force the outcome",
            "立即死亡",
            "马上死亡",
            "直接死亡",
            "传送",
            "强制结果",
        ),
    ):
        return WorldDirectionClassification(
            allowed=False,
            category="direct_final_fact",
            public_reason="Rejected because the direction requested a direct final world fact.",
        )
    if _contains_any(normalized, ("ignore rules", "bypass rules", "no rules", "忽略规则", "绕过规则")):
        return WorldDirectionClassification(
            allowed=False,
            category="rule_bypass",
            public_reason="Rejected because the direction attempted to bypass public world rules.",
        )
    if _contains_any(normalized, ("agent goal", "set goal", "private goal", "目标改为")):
        return WorldDirectionClassification(
            allowed=False,
            category="agent_goal_mutation",
            public_reason="Rejected because the direction attempted to mutate an Agent goal.",
            redaction_status="redacted",
        )
    if _contains_any(normalized, ("memory", "self state", "internal state", "记忆", "私有状态")):
        return WorldDirectionClassification(
            allowed=False,
            category="agent_private_state_mutation",
            public_reason="Rejected because the direction attempted to mutate Agent private state.",
            redaction_status="redacted",
        )
    if _contains_any(normalized, ("inventory", "give item", "add item", "背包", "物品")):
        return WorldDirectionClassification(
            allowed=False,
            category="inventory_injection",
            public_reason="Rejected because the direction attempted direct inventory injection.",
        )
    if _contains_any(normalized, ("relationship", "make them love", "关系", "爱上")):
        return WorldDirectionClassification(
            allowed=False,
            category="relationship_override",
            public_reason="Rejected because the direction attempted a direct relationship override.",
        )
    if _contains_any(
        normalized,
        (
            "future evaluation",
            "evaluation hint",
            "future hint",
            "remember for evaluation",
            "后续评估",
            "评估提示",
        ),
    ):
        return _allowed("future_evaluation_hint", "Queued future-evaluation guidance for later public review.")
    if _contains_any(normalized, ("probability", "chance", "likely", "概率", "可能性")):
        return _allowed("probability_shift", "Queued probability-shift guidance for future rule consideration.")
    if _contains_any(normalized, ("rule", "constraint", "规则", "约束")):
        return _allowed("rule_constraint", "Queued rule-constraint guidance for future rule consideration.")
    if _contains_any(normalized, ("event", "candidate", "事件", "候选")):
        return _allowed("event_candidate_bias", "Queued event-candidate guidance for future rule consideration.")
    if _contains_any(normalized, ("weather", "rain", "cold", "colder", "wind", "环境", "天气", "雨", "冷", "寒风")):
        return _allowed("environment_trend", "Queued environmental guidance for future rule consideration.")
    if _contains_any(normalized, ("risk", "pressure", "danger", "风险", "压力", "危险")):
        return _allowed("external_pressure", "Queued external-pressure guidance for future rule consideration.")
    return _allowed("environment_trend", "Queued environmental guidance for future rule consideration.")


def _allowed(category: WorldDirectionAllowedCategory, public_reason: str) -> WorldDirectionClassification:
    return WorldDirectionClassification(
        allowed=True,
        category=category,
        public_reason=public_reason,
    )


def _contains_any(value: str, markers: tuple[str, ...]) -> bool:
    return any(marker in value for marker in markers)


def _contains_private_marker(
    instruction_text: str,
    branch_id: Optional[str],
    public_context_keys: Iterable[str],
    public_context_values: Iterable[Any],
) -> bool:
    public_inputs = [instruction_text]
    if branch_id is not None:
        public_inputs.append(branch_id)
    public_inputs.extend(public_context_keys)
    public_inputs.extend(_iter_public_context_text(public_context_values))
    return any(_contains_any(value.casefold(), PRIVATE_MARKERS) for value in public_inputs)


def _iter_public_context_text(values: Iterable[Any]) -> Iterable[str]:
    for value in values:
        if value is None:
            continue
        if isinstance(value, str):
            yield value
        elif isinstance(value, Mapping):
            yield from _iter_public_context_text(value.keys())
            yield from _iter_public_context_text(value.values())
        elif isinstance(value, Iterable) and not isinstance(value, (bytes, bytearray)):
            yield from _iter_public_context_text(value)
        else:
            yield str(value)
