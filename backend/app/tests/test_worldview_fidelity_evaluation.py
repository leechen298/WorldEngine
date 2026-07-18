from __future__ import annotations

from app.core.worldview_fidelity import (
    build_worldview_fidelity_scorecard,
    evaluate_bounded_run_worldview_fidelity,
    evaluate_immediate_worldview_fidelity,
)
from app.schemas.world_generation import (
    PublicGeneratedWorldModel,
    PublicWorldCreationSummary,
    PublicWorldRuleSummary,
)


def _public_world_model(
    *,
    tags: list[str] | None = None,
    premise_summary: str = "coastal research robots changing weather",
    sparse: bool = False,
) -> PublicGeneratedWorldModel:
    public_tags = tags or ["coastal", "research", "robots", "weather"]
    if sparse:
        return PublicGeneratedWorldModel(
            title_label="generated-world-research",
            premise_summary=premise_summary,
            world_parameters_outline={"public_tags": public_tags},
            runtime_readiness_inputs={"can_be_checked_for_structure": True},
        )
    return PublicGeneratedWorldModel(
        title_label="generated-world-coastal-research",
        premise_summary=premise_summary,
        world_parameters_outline={
            "public_tags": public_tags,
            "environment": "coastal changing weather",
            "agents": "careful research robots",
        },
        locations_outline=[{"public_label": "coastal research station"}],
        entities_outline=[{"kind": "environment", "public_label": "changing weather"}],
        agents_outline=[{"public_role": "careful research robot"}],
        environment_outline={"public_state": "coastal weather system"},
        rules_outline=[
            {
                "rule_id": "rule.weather_drift",
                "public_summary": "weather changes within coastal bounds",
            }
        ],
        boundary_conditions=["robots remain careful"],
        runtime_readiness_inputs={"can_be_checked_for_structure": True},
    )


def _creation_summary(
    *,
    creation_mode: str = "llm_backed_generation",
    llm_backed: bool = True,
    provider_backed: bool = True,
    fallback: bool = False,
    runtime_ready: str = "true",
) -> PublicWorldCreationSummary:
    return PublicWorldCreationSummary(
        premise_specific="true",
        system_digestible=True,
        redacted=True,
        runtime_ready=runtime_ready,
        distinct_from_deterministic_generic_response=not fallback,
        creation_mode=creation_mode,
        llm_backed=llm_backed,
        provider_backed=provider_backed,
        deterministic_generic_fallback_detected=fallback,
        public_initial_state_refs={"world_id": "world-public-1"},
    )


def _rule_summary(redaction_status: str = "passed") -> PublicWorldRuleSummary:
    return PublicWorldRuleSummary(
        world_id="world-public-1",
        generation_id="generation-public-1",
        premise_digest="abcdef123456",
        validation_status="accepted",
        parameter_paths=["environment.weather", "agent_public.robot_caution"],
        rule_ids=["rule.weather_drift"],
        boundary_ids=["boundary.robot_caution"],
        redaction_status=redaction_status,
    )


def test_immediate_fidelity_passes_when_public_premise_is_covered() -> None:
    artifact = evaluate_immediate_worldview_fidelity(
        world_id="world-public-1",
        generation_id="generation-public-1",
        premise_digest="abcdef123456",
        public_premise="A coastal research world with careful robots and changing weather",
        public_world_model=_public_world_model(),
        world_creation_summary=_creation_summary(),
        rule_summary=_rule_summary(),
    )

    assert artifact.status == "pass"
    assert artifact.covered_indicators == [
        "coastal",
        "research",
        "robots",
        "weather",
    ]
    assert artifact.missing_indicators == []
    assert artifact.contradictions == []
    assert artifact.redaction_status == "passed"


def test_immediate_fidelity_fails_when_material_premise_indicators_are_missing() -> None:
    artifact = evaluate_immediate_worldview_fidelity(
        world_id="world-public-1",
        generation_id="generation-public-1",
        premise_digest="abcdef123456",
        public_premise="A coastal research world with careful robots and changing weather",
        public_world_model=_public_world_model(
            tags=["research"],
            premise_summary="research world",
            sparse=True,
        ),
        world_creation_summary=_creation_summary(),
        rule_summary=_rule_summary(),
    )

    assert artifact.status == "fail"
    assert "coastal" in artifact.missing_indicators
    assert "robots" in artifact.missing_indicators
    assert any(
        contradiction.category == "missing_premise"
        for contradiction in artifact.contradictions
    )


def test_immediate_fidelity_fails_deterministic_generic_fallback() -> None:
    artifact = evaluate_immediate_worldview_fidelity(
        world_id="world-public-1",
        generation_id="generation-public-1",
        premise_digest="abcdef123456",
        public_premise="A coastal research world with careful robots and changing weather",
        public_world_model=_public_world_model(),
        world_creation_summary=_creation_summary(
            creation_mode="deterministic_generic_fallback",
            llm_backed=False,
            provider_backed=False,
            fallback=True,
        ),
        rule_summary=_rule_summary(),
    )

    assert artifact.status == "fail"
    assert any(
        contradiction.category == "generic_fallback"
        for contradiction in artifact.contradictions
    )


def test_immediate_fidelity_rejects_private_markers_without_echo() -> None:
    artifact = evaluate_immediate_worldview_fidelity(
        world_id="world-public-1",
        generation_id="generation-public-1",
        premise_digest="abcdef123456",
        public_premise="A coastal research world with careful robots and changing weather",
        public_world_model=_public_world_model(
            premise_summary="raw prompt sk-live-secret"
        ),
        world_creation_summary=_creation_summary(),
        rule_summary=_rule_summary(),
    )
    serialized = str(artifact.model_dump()).lower()

    assert artifact.status == "fail"
    assert artifact.redaction_status == "failed"
    assert any(
        contradiction.category == "redaction"
        for contradiction in artifact.contradictions
    )
    assert "raw prompt" not in serialized
    assert "sk-live-secret" not in serialized


def test_bounded_run_fidelity_blocks_when_public_run_evidence_is_missing() -> None:
    artifact = evaluate_bounded_run_worldview_fidelity(
        world_id="world-public-1",
        generation_id="generation-public-1",
        premise_digest="abcdef123456",
        public_premise="A coastal research world with careful robots and changing weather",
        public_runtime_summary=None,
    )

    assert artifact.status == "blocked"
    assert any(
        contradiction.category == "evidence_gap"
        for contradiction in artifact.contradictions
    )


def test_bounded_run_fidelity_fails_explicit_runtime_contradictions() -> None:
    artifact = evaluate_bounded_run_worldview_fidelity(
        world_id="world-public-1",
        generation_id="generation-public-1",
        premise_digest="abcdef123456",
        public_premise="A coastal research world with careful robots and changing weather",
        public_runtime_summary={
            "status": "pass",
            "events": ["robots abandon all caution during desert heatwave"],
            "contradictions": [
                {
                    "category": "runtime_contradiction",
                    "path": "/events/0",
                    "public_summary": "runtime leaves coastal weather premise",
                }
            ],
        },
    )

    assert artifact.status == "fail"
    assert any(
        contradiction.category == "runtime_contradiction"
        for contradiction in artifact.contradictions
    )


def test_bounded_run_fidelity_fails_when_runtime_evidence_misses_premise() -> None:
    artifact = evaluate_bounded_run_worldview_fidelity(
        world_id="world-public-1",
        generation_id="generation-public-1",
        premise_digest="abcdef123456",
        public_premise="A coastal research world with careful robots and changing weather",
        public_runtime_summary={
            "status": "pass",
            "events": ["careful robots observe coastal weather changes"],
            "contradictions": [],
        },
    )

    assert artifact.status == "fail"
    assert "research" in artifact.missing_indicators
    assert any(
        contradiction.category == "missing_premise"
        for contradiction in artifact.contradictions
    )


def test_bounded_run_fidelity_redaction_failure_does_not_echo_private_summary() -> None:
    artifact = evaluate_bounded_run_worldview_fidelity(
        world_id="world-public-1",
        generation_id="generation-public-1",
        premise_digest="abcdef123456",
        public_premise="A coastal research world with careful robots and changing weather",
        public_runtime_summary={
            "status": "fail",
            "contradictions": [
                {
                    "category": "runtime_contradiction",
                    "path": "/events/raw_prompt/sk-live-secret",
                    "public_summary": "raw prompt sk-live-secret hidden context",
                }
            ],
        },
    )
    serialized = str(artifact.model_dump()).lower()

    assert artifact.status == "fail"
    assert artifact.redaction_status == "failed"
    assert any(
        contradiction.category == "redaction"
        for contradiction in artifact.contradictions
    )
    assert "raw prompt" not in serialized
    assert "sk-live-secret" not in serialized
    assert "hidden context" not in serialized


def test_scorecard_blocks_final_pass_when_bounded_run_is_blocked() -> None:
    immediate = evaluate_immediate_worldview_fidelity(
        world_id="world-public-1",
        generation_id="generation-public-1",
        premise_digest="abcdef123456",
        public_premise="A coastal research world with careful robots and changing weather",
        public_world_model=_public_world_model(),
        world_creation_summary=_creation_summary(),
        rule_summary=_rule_summary(),
    )
    bounded_run = evaluate_bounded_run_worldview_fidelity(
        world_id="world-public-1",
        generation_id="generation-public-1",
        premise_digest="abcdef123456",
        public_premise="A coastal research world with careful robots and changing weather",
        public_runtime_summary=None,
    )

    scorecard = build_worldview_fidelity_scorecard(
        world_id="world-public-1",
        generation_id="generation-public-1",
        premise_digest="abcdef123456",
        immediate=immediate,
        bounded_run=bounded_run,
    )

    assert immediate.status == "pass"
    assert bounded_run.status == "blocked"
    assert scorecard.final_status == "blocked"
    assert "immediate_worldview_fidelity" in scorecard.score_items
    assert "bounded_run_worldview_fidelity" in scorecard.score_items


def test_scorecard_passes_when_immediate_and_bounded_run_fidelity_pass() -> None:
    immediate = evaluate_immediate_worldview_fidelity(
        world_id="world-public-1",
        generation_id="generation-public-1",
        premise_digest="abcdef123456",
        public_premise="A coastal research world with careful robots and changing weather",
        public_world_model=_public_world_model(),
        world_creation_summary=_creation_summary(),
        rule_summary=_rule_summary(),
    )
    bounded_run = evaluate_bounded_run_worldview_fidelity(
        world_id="world-public-1",
        generation_id="generation-public-1",
        premise_digest="abcdef123456",
        public_premise="A coastal research world with careful robots and changing weather",
        public_runtime_summary={
            "status": "pass",
            "events": ["careful research robots observe coastal weather changes"],
            "contradictions": [],
        },
    )

    scorecard = build_worldview_fidelity_scorecard(
        world_id="world-public-1",
        generation_id="generation-public-1",
        premise_digest="abcdef123456",
        immediate=immediate,
        bounded_run=bounded_run,
    )

    assert scorecard.final_status == "pass"
    assert scorecard.redaction_status == "passed"
    assert scorecard.critical_failures == []
