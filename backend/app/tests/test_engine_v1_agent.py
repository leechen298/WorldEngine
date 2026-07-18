from __future__ import annotations

import app.engine.session as engine_session_module

from app.tests.test_engine_v1_generation import (
    _boot_session,
    _client,
    _data,
    _evidence,
    _projection,
)


def _step(client, session_id: str, revision: int, request_id: str) -> None:
    _data(
        client.post(
            f"/api/v1/sessions/{session_id}/steps",
            json={
                "request_id": request_id,
                "step_count": 1,
                "expected_revision": revision,
            },
        )
    )


def test_ac_04_agent_cycle_has_complete_public_causal_chain() -> None:
    client = _client()
    _, session = _boot_session(client)
    session_id = session["session_id"]
    _step(
        client,
        session_id,
        session["projection"]["revision"],
        "step-agent-cycle-one",
    )

    evidence = _evidence(client, session_id)
    projection = _projection(client, session_id)
    cycle = evidence["agent_cycles"][0]

    for phase in (
        "perception",
        "decision",
        "action_request",
        "rule_judgment",
        "action_result",
    ):
        assert cycle[phase]

    action_request = cycle["action_request"]
    judgment = cycle["rule_judgment"]
    result = cycle["action_result"]
    experience = result["experience_ref"]
    assert judgment["accepted"] is True
    assert judgment["rule_refs"]
    assert result["status"] == "accepted"
    assert result["event_ref"]
    assert result["diff_refs"]

    events_by_id = {event["event_id"]: event for event in evidence["events"]}
    diffs_by_id = {diff["diff_id"]: diff for diff in evidence["diffs"]}
    assert result["event_ref"] in events_by_id
    assert set(result["diff_refs"]).issubset(diffs_by_id)
    result_event = events_by_id[result["event_ref"]]
    assert result_event["status"] == "accepted"
    assert result_event["request_id"] == action_request["request_id"]
    assert all(
        diffs_by_id[diff_id]["operations"]
        and diffs_by_id[diff_id]["request_id"] == action_request["request_id"]
        for diff_id in result["diff_refs"]
    )
    assert cycle["event_refs"] == [result["event_ref"]]
    assert cycle["diff_refs"] == result["diff_refs"]

    assert experience["ref_id"] == result["event_ref"]
    assert experience["ref_type"] == "action_result"
    assert cycle["agent_id"] in {
        agent["agent_id"] for agent in projection["agents"]
    }

    serialized = str(cycle).lower()
    for forbidden in (
        "chain_of_thought",
        "private_memory",
        "private_goal",
        "raw_prompt",
        "raw_response",
        "raw_thought",
    ):
        assert forbidden not in serialized


def test_ac_05_later_decision_cites_prior_experience_and_changes_evidence() -> None:
    client = _client()
    _, session = _boot_session(client)
    session_id = session["session_id"]

    _step(
        client,
        session_id,
        session["projection"]["revision"],
        "step-agent-experience-one",
    )
    first_evidence = _evidence(client, session_id)
    first_cycle = first_evidence["agent_cycles"][0]
    first_experience = first_cycle["action_result"]["experience_ref"]
    first_projection = _projection(client, session_id)

    _step(
        client,
        session_id,
        first_projection["revision"],
        "step-agent-experience-two",
    )
    later_evidence = _evidence(client, session_id)
    later_cycle = later_evidence["agent_cycles"][-1]
    later_decision = later_cycle["decision"]

    cited_experience_ids = {
        ref["ref_id"] for ref in later_cycle["experience_refs_used"]
    }
    assert first_experience["ref_id"] in cited_experience_ids
    assert first_experience["ref_id"] in later_decision["experience_ref_ids"]
    assert later_decision["decision_mode"] == "experience_guided_policy"
    assert (
        later_cycle["action_request"]["amount"]
        == first_cycle["action_request"]["amount"]
        == first_experience["amount"]
    )
    assert later_decision != first_cycle["decision"]
    assert later_cycle["tick"] > first_cycle["tick"]

    assert first_experience["ref_id"] in {
        event["event_id"] for event in first_evidence["events"]
    }


def test_agent_perception_is_constructed_before_and_passed_to_planning(
    monkeypatch,
) -> None:
    client = _client()
    _, session = _boot_session(client)
    captured = []
    original = engine_session_module.plan_agent_cycle

    def capture_perception(perception):
        captured.append(perception)
        return original(perception)

    monkeypatch.setattr(engine_session_module, "plan_agent_cycle", capture_perception)
    _step(
        client,
        session["session_id"],
        session["projection"]["revision"],
        "step-agent-perception-passed",
    )

    assert len(captured) == 1
    perception = captured[0]
    cycle = _evidence(client, session["session_id"])["agent_cycles"][0]
    assert cycle["perception"] == perception.public_payload()
    assert perception.state_hash != session["projection"]["state_hash"]
    assert perception.visible_variables == session["projection"]["variables"]
    assert perception.feedback_count == 0
    assert perception.experience_refs == []
    assert perception.available_actions == session["projection"]["allowed_actions"]


def test_current_variable_changes_agent_action_direction() -> None:
    baseline_client = _client()
    _, baseline_session = _boot_session(baseline_client)
    _step(
        baseline_client,
        baseline_session["session_id"],
        baseline_session["projection"]["revision"],
        "step-agent-baseline-variable",
    )
    baseline_cycle = _evidence(
        baseline_client,
        baseline_session["session_id"],
    )["agent_cycles"][0]

    high_client = _client()
    package, high_session = _boot_session(high_client)
    high_action = package["action_catalog"][0]
    shifted = _data(
        high_client.post(
            f"/api/v1/sessions/{high_session['session_id']}/actions",
            json={
                "request_id": "action-shift-agent-variable",
                "expected_revision": high_session["projection"]["revision"],
                "action_id": high_action["action_id"],
                "target_ref": high_action["target_ref"],
                "amount": 3,
            },
        )
    )
    _step(
        high_client,
        high_session["session_id"],
        shifted["projection"]["revision"],
        "step-agent-shifted-variable",
    )
    shifted_cycle = _evidence(high_client, high_session["session_id"])[
        "agent_cycles"
    ][0]

    assert baseline_cycle["perception"]["visible_variables"]["system_capacity"] == 4
    assert shifted_cycle["perception"]["visible_variables"]["system_capacity"] == 7
    assert baseline_cycle["action_request"]["amount"] == 1
    assert shifted_cycle["action_request"]["amount"] == -1
    assert baseline_cycle["decision"]["influence_factors"] == [
        "current_variables"
    ]
    assert shifted_cycle["decision"]["influence_factors"] == [
        "current_variables"
    ]


def test_feedback_changes_agent_mode_and_action_with_same_state_and_experience() -> None:
    control_client = _client()
    _, control_session = _boot_session(control_client)
    feedback_client = _client()
    _, feedback_session = _boot_session(feedback_client)

    _step(
        control_client,
        control_session["session_id"],
        control_session["projection"]["revision"],
        "step-control-agent-one",
    )
    _step(
        feedback_client,
        feedback_session["session_id"],
        feedback_session["projection"]["revision"],
        "step-feedback-agent-one",
    )
    control_after_first = _projection(control_client, control_session["session_id"])
    feedback_after_first = _projection(feedback_client, feedback_session["session_id"])
    feedback_first_cycle = _evidence(
        feedback_client,
        feedback_session["session_id"],
    )["agent_cycles"][0]

    feedback_result = _data(
        feedback_client.post(
            f"/api/v1/sessions/{feedback_session['session_id']}/feedback",
            json={
                "request_id": "feedback-before-agent-two",
                "expected_revision": feedback_after_first["revision"],
                "feedback_type": "local_outcome_observed",
                "summary": "Use this typed public outcome on the next cycle.",
                "related_event_ref": feedback_first_cycle["action_result"]["event_ref"],
            },
        )
    )
    _step(
        control_client,
        control_session["session_id"],
        control_after_first["revision"],
        "step-control-agent-two",
    )
    _step(
        feedback_client,
        feedback_session["session_id"],
        feedback_result["projection"]["revision"],
        "step-feedback-agent-two",
    )

    control_evidence = _evidence(control_client, control_session["session_id"])
    feedback_evidence = _evidence(feedback_client, feedback_session["session_id"])
    control_cycle = control_evidence["agent_cycles"][-1]
    feedback_cycle = feedback_evidence["agent_cycles"][-1]

    assert (
        control_cycle["perception"]["visible_variables"]
        == feedback_cycle["perception"]["visible_variables"]
    )
    assert [
        item["public_effect"]
        for item in control_cycle["perception"]["experience_refs"]
    ] == [
        item["public_effect"]
        for item in feedback_cycle["perception"]["experience_refs"]
    ]
    assert control_cycle["perception"]["feedback_count"] == 0
    assert feedback_cycle["perception"]["feedback_count"] == 1
    assert control_cycle["decision"]["decision_mode"] == "experience_guided_policy"
    assert (
        feedback_cycle["decision"]["decision_mode"]
        == "feedback_adjusted_experience_policy"
    )
    assert feedback_cycle["decision"]["influence_factors"] == [
        "current_variables",
        "experience",
        "feedback_count",
    ]
    assert (
        control_cycle["action_request"]["amount"]
        == -feedback_cycle["action_request"]["amount"]
    )
    coverage = feedback_evidence["completeness"]["scenario_coverage"]
    assert coverage["checks"]["feedback"] is True
    assert coverage["checks"]["agent_feedback_influence"] is True
