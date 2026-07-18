"""Deterministic public worldview fidelity evaluation helpers."""

from __future__ import annotations

import re
from typing import Any

from app.schemas.world_generation import (
    BoundedRunWorldviewFidelityArtifact,
    ImmediateWorldviewFidelityArtifact,
    PublicGeneratedWorldModel,
    PublicWorldCreationSummary,
    PublicWorldRuleSummary,
    WorldviewContradiction,
    WorldviewFidelityScorecard,
    _private_mapping_markers,
)


_STOP_WORDS = {
    "and",
    "with",
    "world",
    "public",
    "generated",
    "careful",
    "changing",
    "basic",
    "user",
    "from",
    "that",
    "this",
}


def evaluate_immediate_worldview_fidelity(
    *,
    world_id: str,
    generation_id: str,
    premise_digest: str,
    public_premise: str,
    public_world_model: PublicGeneratedWorldModel,
    world_creation_summary: PublicWorldCreationSummary,
    rule_summary: PublicWorldRuleSummary | None = None,
) -> ImmediateWorldviewFidelityArtifact:
    indicators = _premise_indicators(public_premise)
    evidence = {
        "public_world_model": public_world_model.model_dump(),
        "world_creation_summary": world_creation_summary.model_dump(),
        "rule_summary": rule_summary.model_dump() if rule_summary else {},
    }
    contradictions: list[WorldviewContradiction] = []
    redaction_status = "passed"

    if _private_mapping_markers(evidence):
        redaction_status = "failed"
        contradictions.append(
            _contradiction(
                "redaction",
                "/public_evidence",
                "public fidelity evidence contains private markers",
            )
        )

    evidence_text = _public_text(evidence)
    covered = [indicator for indicator in indicators if indicator in evidence_text]
    missing = [indicator for indicator in indicators if indicator not in evidence_text]

    if world_creation_summary.deterministic_generic_fallback_detected:
        contradictions.append(
            _contradiction(
                "generic_fallback",
                "/world_creation_summary",
                "deterministic generic fallback cannot be final fidelity pass",
            )
        )
    if not world_creation_summary.system_digestible:
        contradictions.append(
            _contradiction(
                "evidence_gap",
                "/world_creation_summary/system_digestible",
                "generated world is not system digestible",
            )
        )
    if missing:
        contradictions.append(
            _contradiction(
                "missing_premise",
                "/public_world_model",
                "generated public model is missing material premise indicators",
            )
        )

    status = "pass"
    if redaction_status == "failed" or any(
        item.category in {"generic_fallback", "missing_premise"}
        for item in contradictions
    ):
        status = "fail"
    elif not world_creation_summary.system_digestible:
        status = "blocked"

    return ImmediateWorldviewFidelityArtifact(
        world_id=world_id,
        generation_id=generation_id,
        premise_digest=premise_digest,
        status=status,
        evaluated_indicators=indicators,
        covered_indicators=covered,
        missing_indicators=missing,
        creation_mode=world_creation_summary.creation_mode,
        deterministic_generic_fallback_detected=(
            world_creation_summary.deterministic_generic_fallback_detected
        ),
        system_digestible=world_creation_summary.system_digestible,
        redaction_status=redaction_status,
        contradictions=contradictions,
        evidence_refs={
            "public_world_model": "supplied",
            "world_creation_summary": "supplied",
            "rule_summary": "supplied" if rule_summary else "not_supplied",
        },
    )


def evaluate_bounded_run_worldview_fidelity(
    *,
    world_id: str,
    generation_id: str,
    premise_digest: str,
    public_premise: str,
    public_runtime_summary: dict[str, Any] | None,
) -> BoundedRunWorldviewFidelityArtifact:
    indicators = _premise_indicators(public_premise)
    contradictions: list[WorldviewContradiction] = []
    redaction_status = "passed"

    if public_runtime_summary is None:
        contradictions.append(
            _contradiction(
                "evidence_gap",
                "/public_runtime_summary",
                "bounded-run public evidence is missing",
            )
        )
        return BoundedRunWorldviewFidelityArtifact(
            world_id=world_id,
            generation_id=generation_id,
            premise_digest=premise_digest,
            status="blocked",
            evaluated_indicators=indicators,
            runtime_summary_present=False,
            contradictions=contradictions,
            evidence_refs={"public_runtime_summary": "not_supplied"},
        )

    if _private_mapping_markers(public_runtime_summary):
        redaction_status = "failed"
        contradictions.append(
            _contradiction(
                "redaction",
                "/public_runtime_summary",
                "public runtime summary contains private markers",
            )
        )

    status_hint = public_runtime_summary.get("status")
    covered: list[str] = []
    missing: list[str] = []
    if redaction_status == "passed" and status_hint not in {"blocked", "not_run"}:
        evidence_text = _public_text(public_runtime_summary)
        covered = [indicator for indicator in indicators if indicator in evidence_text]
        missing = [indicator for indicator in indicators if indicator not in evidence_text]
        if missing:
            contradictions.append(
                _contradiction(
                    "missing_premise",
                    "/public_runtime_summary",
                    "bounded-run public evidence is missing material premise indicators",
                )
            )

    for index, item in enumerate(public_runtime_summary.get("contradictions", [])):
        if not isinstance(item, dict):
            continue
        category = item.get("category", "runtime_contradiction")
        if category not in {
            "missing_premise",
            "generic_fallback",
            "runtime_contradiction",
            "rule_contradiction",
            "redaction",
            "evidence_gap",
            "checker_gap",
        }:
            category = "runtime_contradiction"
        if redaction_status == "failed":
            contradictions.append(
                _contradiction(
                    category,
                    f"/contradictions/{index}",
                    "runtime contradiction omitted because public runtime summary failed redaction",
                )
            )
            continue
        contradictions.append(
            _contradiction(
                category,
                str(item.get("path") or f"/contradictions/{index}"),
                str(item.get("public_summary") or "runtime contradicts public premise"),
            )
        )

    status = "pass"
    if redaction_status == "failed" or contradictions:
        status = "fail"
    elif status_hint in {"blocked", "not_run"}:
        status = status_hint

    return BoundedRunWorldviewFidelityArtifact(
        world_id=world_id,
        generation_id=generation_id,
        premise_digest=premise_digest,
        status=status,
        evaluated_indicators=indicators,
        covered_indicators=covered,
        missing_indicators=missing,
        runtime_summary_present=True,
        redaction_status=redaction_status,
        contradictions=contradictions,
        evidence_refs={"public_runtime_summary": "supplied"},
    )


def build_worldview_fidelity_scorecard(
    *,
    world_id: str,
    generation_id: str,
    premise_digest: str,
    immediate: ImmediateWorldviewFidelityArtifact,
    bounded_run: BoundedRunWorldviewFidelityArtifact,
) -> WorldviewFidelityScorecard:
    score_items = {
        "immediate_worldview_fidelity": immediate.status,
        "bounded_run_worldview_fidelity": bounded_run.status,
    }
    critical_failures = [
        *immediate.contradictions,
        *bounded_run.contradictions,
    ]
    redaction_status = (
        "failed"
        if immediate.redaction_status == "failed" or bounded_run.redaction_status == "failed"
        else "passed"
    )
    unverified_items = [
        name
        for name, status in score_items.items()
        if status in {"blocked", "not_run"}
    ]

    if redaction_status == "failed":
        final_status = "fail"
    elif any(status == "fail" for status in score_items.values()):
        final_status = "fail"
    elif any(status == "blocked" for status in score_items.values()):
        final_status = "blocked"
    elif any(status == "not_run" for status in score_items.values()):
        final_status = "not_run"
    else:
        final_status = "pass"

    return WorldviewFidelityScorecard(
        world_id=world_id,
        generation_id=generation_id,
        premise_digest=premise_digest,
        final_status=final_status,
        score_items=score_items,
        critical_failures=critical_failures,
        unverified_items=unverified_items,
        redaction_status=redaction_status,
        immediate=immediate,
        bounded_run=bounded_run,
    )


def _premise_indicators(public_premise: str) -> list[str]:
    indicators: list[str] = []
    for token in re.findall(r"[a-zA-Z0-9]{3,24}", public_premise.lower()):
        if token not in _STOP_WORDS and token not in indicators:
            indicators.append(token)
    return indicators[:8]


def _public_text(value: Any) -> str:
    if isinstance(value, dict):
        return " ".join(_public_text(item) for item in value.values()).lower()
    if isinstance(value, list):
        return " ".join(_public_text(item) for item in value).lower()
    return str(value).lower()


def _contradiction(
    category: str,
    path: str,
    public_summary: str,
) -> WorldviewContradiction:
    return WorldviewContradiction(
        category=category,
        path=path,
        public_summary=public_summary,
    )
