from __future__ import annotations

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
    assert later_decision != first_cycle["decision"]
    assert later_cycle["tick"] > first_cycle["tick"]

    assert first_experience["ref_id"] in {
        event["event_id"] for event in first_evidence["events"]
    }
