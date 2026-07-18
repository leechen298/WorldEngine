from __future__ import annotations

from typing import Any

from app.tests.test_engine_v1_generation import (
    _boot_session,
    _client,
    _create_package,
    _data,
    _events,
    _evidence,
    _generic_world_brief,
    _projection,
)


def _open_window(projection: dict[str, Any]) -> dict[str, Any]:
    window = projection["active_intervention_window"]
    assert window["status"] == "open"
    assert window["window_id"]
    assert window["open_tick"] == projection["tick"]
    return window


def _projection_head(projection: dict[str, Any]) -> tuple[Any, ...]:
    return (
        projection["tick"],
        projection["revision"],
        projection["state_hash"],
        projection["event_cursor"],
    )


def _bounded_direction(
    *,
    request_id: str,
    revision: int,
    window_id: str,
    target_ref: str = "system_signal",
    magnitude: int = 1,
) -> dict[str, Any]:
    return {
        "request_id": request_id,
        "expected_revision": revision,
        "window_id": window_id,
        "kind": "bounded_pressure",
        "target_ref": target_ref,
        "summary": "Apply one bounded unit of public pressure.",
        "magnitude": magnitude,
    }


def _final_fact_direction(
    *, request_id: str, revision: int, window_id: str
) -> dict[str, Any]:
    return {
        "request_id": request_id,
        "expected_revision": revision,
        "window_id": window_id,
        "kind": "direct_final_fact",
        "target_ref": "system_signal",
        "summary": "Assign a final public value directly.",
        "final_value": 10,
    }


def test_ac_06_ac_07_same_window_accepts_bounded_and_rejects_final_fact() -> None:
    client = _client()
    _, session = _boot_session(client)
    session_id = session["session_id"]
    initial_projection = _projection(client, session_id)
    window = _open_window(initial_projection)

    accepted = _data(
        client.post(
            f"/api/v1/sessions/{session_id}/directions",
            json=_bounded_direction(
                request_id="direction-bounded-one",
                revision=initial_projection["revision"],
                window_id=window["window_id"],
            ),
        )
    )
    after_accepted = _projection(client, session_id)

    assert accepted["status"] == "accepted"
    assert accepted["window_id"] == window["window_id"]
    assert accepted["event_ref"]
    assert accepted["queued"] is True
    assert accepted["application_status"] == "queued"
    assert accepted["application_event_refs"] == []
    assert accepted["applied_diff_refs"] == []
    assert after_accepted["state_hash"] == initial_projection["state_hash"]

    rejected = _data(
        client.post(
            f"/api/v1/sessions/{session_id}/directions",
            json=_final_fact_direction(
                request_id="direction-final-fact-one",
                revision=after_accepted["revision"],
                window_id=window["window_id"],
            ),
        )
    )
    after_rejected = _projection(client, session_id)

    assert rejected["status"] == "rejected"
    assert rejected["window_id"] == window["window_id"]
    assert rejected["reason_code"]
    assert rejected["queued"] is False
    assert rejected["application_status"] == "not_applicable"
    assert "window" not in rejected["reason_code"]
    assert "revision" not in rejected["reason_code"]
    assert rejected["applied_diff_refs"] == []
    assert after_rejected["state_hash"] == after_accepted["state_hash"]
    assert _open_window(after_rejected)["window_id"] == window["window_id"]

    before_step_evidence = _evidence(client, session_id)
    rejected_event = next(
        event
        for event in before_step_evidence["events"]
        if event["request_id"] == "direction-final-fact-one"
    )
    assert rejected_event["status"] == "rejected"
    assert rejected_event["payload"]["reason_code"] == rejected["reason_code"]
    assert rejected_event["diff_refs"] == []

    _data(
        client.post(
            f"/api/v1/sessions/{session_id}/steps",
            json={
                "request_id": "step-apply-bounded-direction",
                "step_count": 1,
                "expected_revision": after_rejected["revision"],
            },
        )
    )
    final_projection = _projection(client, session_id)
    final_evidence = _evidence(client, session_id)
    applied_event = next(
        event
        for event in final_evidence["events"]
        if event["request_id"] == accepted["request_id"]
        and event["event_type"] == "direction.applied"
        and event["status"] == "accepted"
        and event["diff_refs"]
    )
    applied_decision = next(
        item
        for item in final_evidence["direction_decisions"]
        if item["request_id"] == accepted["request_id"]
    )
    correlation = next(
        item
        for item in final_evidence["request_correlations"]
        if item["operation_id"] == "directions.submit"
        and item["request_id"] == accepted["request_id"]
    )

    assert applied_event["tick"] > window["open_tick"]
    assert applied_event["rule_refs"]
    diff_by_id = {diff["diff_id"]: diff for diff in final_evidence["diffs"]}
    assert all(
        diff_by_id[diff_id]["operations"]
        for diff_id in applied_event["diff_refs"]
    )
    assert applied_decision["queued"] is False
    assert applied_decision["application_status"] == "applied"
    assert applied_decision["application_reason_code"] == "direction_applied"
    assert applied_decision["application_event_refs"] == [applied_event["event_id"]]
    assert applied_decision["applied_diff_refs"] == applied_event["diff_refs"]
    assert correlation["status"] == "accepted"
    assert correlation["application_status"] == "applied"
    assert correlation["event_refs"] == [
        accepted["event_ref"],
        applied_event["event_id"],
    ]
    assert correlation["diff_refs"] == applied_decision["applied_diff_refs"]
    assert final_projection["state_hash"] != after_rejected["state_hash"]


def test_step_100_catalog_accepts_action_and_direction_at_300() -> None:
    client = _client()
    brief = _generic_world_brief()
    brief["state_variables"] = [
        {
            "key": "wide_signal",
            "initial": 0,
            "minimum": -1000,
            "maximum": 1000,
            "step": 100,
        }
    ]
    package = _create_package(
        client,
        brief,
        request_id="package-step-100-range",
    )
    _, session = _boot_session(client, package)
    session_id = session["session_id"]
    projection = session["projection"]
    action_spec = package["action_catalog"][0]

    assert action_spec["minimum_amount"] == -300
    assert action_spec["maximum_amount"] == 300
    direction_rule = next(
        item
        for item in package["rule_catalog"]
        if item["rule_id"] == "rule.direction.wide_signal"
    )
    assert direction_rule["maximum_magnitude"] == 300

    action = _data(
        client.post(
            f"/api/v1/sessions/{session_id}/actions",
            json={
                "request_id": "action-positive-300",
                "expected_revision": projection["revision"],
                "action_id": action_spec["action_id"],
                "target_ref": "wide_signal",
                "amount": 300,
            },
        )
    )
    assert action["status"] == "accepted"
    assert action["projection"]["variables"]["wide_signal"] == 300

    direction = _data(
        client.post(
            f"/api/v1/sessions/{session_id}/directions",
            json=_bounded_direction(
                request_id="direction-negative-300",
                revision=action["projection"]["revision"],
                window_id=_open_window(action["projection"])["window_id"],
                target_ref="wide_signal",
                magnitude=-300,
            ),
        )
    )
    assert direction["status"] == "accepted"
    assert direction["application_status"] == "queued"

    _data(
        client.post(
            f"/api/v1/sessions/{session_id}/steps",
            json={
                "request_id": "step-apply-negative-300",
                "step_count": 1,
                "expected_revision": action["projection"]["revision"],
            },
        )
    )
    evidence = _evidence(client, session_id)
    applied = next(
        item
        for item in evidence["direction_decisions"]
        if item["request_id"] == direction["request_id"]
    )
    applied_diff = next(
        item
        for item in evidence["diffs"]
        if item["diff_id"] in applied["applied_diff_refs"]
    )

    assert applied["queued"] is False
    assert applied["application_status"] == "applied"
    variable_change = next(
        operation
        for operation in applied_diff["operations"]
        if operation["path"] == "/variables/wide_signal"
    )
    assert variable_change == {
        "path": "/variables/wide_signal",
        "before": 300,
        "after": 0,
    }


def test_direction_application_range_rejection_finishes_queue_and_correlates() -> None:
    client = _client()
    brief = _generic_world_brief()
    brief["state_variables"] = [
        {
            "key": "wide_signal",
            "initial": 950,
            "minimum": -1000,
            "maximum": 1000,
            "step": 100,
        }
    ]
    package = _create_package(
        client,
        brief,
        request_id="package-direction-application-rejection",
    )
    _, session = _boot_session(client, package)
    session_id = session["session_id"]
    projection = session["projection"]
    direction = _data(
        client.post(
            f"/api/v1/sessions/{session_id}/directions",
            json=_bounded_direction(
                request_id="direction-application-out-of-range",
                revision=projection["revision"],
                window_id=_open_window(projection)["window_id"],
                target_ref="wide_signal",
                magnitude=300,
            ),
        )
    )

    _data(
        client.post(
            f"/api/v1/sessions/{session_id}/steps",
            json={
                "request_id": "step-reject-direction-application",
                "step_count": 1,
                "expected_revision": projection["revision"],
            },
        )
    )
    evidence = _evidence(client, session_id)
    decision = next(
        item
        for item in evidence["direction_decisions"]
        if item["request_id"] == direction["request_id"]
    )
    application_event = next(
        event
        for event in evidence["events"]
        if event["event_id"] in decision["application_event_refs"]
    )
    correlation = next(
        item
        for item in evidence["request_correlations"]
        if item["operation_id"] == "directions.submit"
        and item["request_id"] == direction["request_id"]
    )

    assert decision["queued"] is False
    assert decision["application_status"] == "application_rejected"
    assert (
        decision["application_reason_code"]
        == "direction_target_range_violation"
    )
    assert decision["applied_diff_refs"] == []
    assert application_event["event_type"] == "direction.application_rejected"
    assert application_event["status"] == "rejected"
    assert application_event["diff_refs"] == []
    assert correlation["application_status"] == "application_rejected"
    assert correlation["event_refs"] == [
        direction["event_ref"],
        application_event["event_id"],
    ]
    assert correlation["diff_refs"] == []
    assert evidence["completeness"]["integrity"]["status"] == "valid"


def test_ac_08_action_and_feedback_duplicates_are_idempotent() -> None:
    client = _client()
    package, session = _boot_session(client)
    session_id = session["session_id"]
    projection = _projection(client, session_id)
    action = package["action_catalog"][0]

    action_request = {
        "request_id": "client-action-idempotent-one",
        "expected_revision": projection["revision"],
        "action_id": action["action_id"],
        "target_ref": action["target_ref"],
        "amount": 1,
    }
    first_action = _data(
        client.post(
            f"/api/v1/sessions/{session_id}/actions",
            json=action_request,
        )
    )
    after_first_action = _projection(client, session_id)
    action_events = _events(client, session_id)

    duplicate_action = _data(
        client.post(
            f"/api/v1/sessions/{session_id}/actions",
            json=action_request,
        )
    )
    after_duplicate_action = _projection(client, session_id)

    assert first_action["status"] == "accepted"
    assert duplicate_action == first_action
    assert _projection_head(after_duplicate_action) == _projection_head(
        after_first_action
    )
    assert _events(client, session_id) == action_events

    mismatched_action_response = client.post(
        f"/api/v1/sessions/{session_id}/actions",
        json={**action_request, "amount": -1},
    )
    mismatched_action = _data(mismatched_action_response, expected_status=409)
    assert mismatched_action["reason_code"] == "idempotency_key_reused"
    assert _projection_head(_projection(client, session_id)) == _projection_head(
        after_first_action
    )
    assert _events(client, session_id) == action_events

    feedback_request = {
        "request_id": "client-feedback-idempotent-one",
        "expected_revision": after_duplicate_action["revision"],
        "feedback_type": "local_outcome_observed",
        "summary": "The accepted public action result was observed.",
        "related_event_ref": first_action["event_ref"],
    }
    first_feedback = _data(
        client.post(
            f"/api/v1/sessions/{session_id}/feedback",
            json=feedback_request,
        )
    )
    after_first_feedback = _projection(client, session_id)
    feedback_events = _events(client, session_id)

    duplicate_feedback = _data(
        client.post(
            f"/api/v1/sessions/{session_id}/feedback",
            json=feedback_request,
        )
    )
    after_duplicate_feedback = _projection(client, session_id)

    assert first_feedback["status"] == "accepted"
    assert duplicate_feedback == first_feedback
    assert _projection_head(after_duplicate_feedback) == _projection_head(
        after_first_feedback
    )
    assert _events(client, session_id) == feedback_events

    mismatched_feedback_response = client.post(
        f"/api/v1/sessions/{session_id}/feedback",
        json={**feedback_request, "summary": "Different public observation."},
    )
    mismatched_feedback = _data(
        mismatched_feedback_response,
        expected_status=409,
    )
    assert mismatched_feedback["reason_code"] == "idempotency_key_reused"
    assert _projection_head(_projection(client, session_id)) == _projection_head(
        after_first_feedback
    )
    assert _events(client, session_id) == feedback_events


def test_ac_08_stale_revision_conflicts_without_mutation() -> None:
    client = _client()
    package, session = _boot_session(client)
    session_id = session["session_id"]
    stale_projection = _projection(client, session_id)
    action = package["action_catalog"][0]

    _data(
        client.post(
            f"/api/v1/sessions/{session_id}/steps",
            json={
                "request_id": "step-create-new-revision",
                "step_count": 1,
                "expected_revision": stale_projection["revision"],
            },
        )
    )
    current_projection = _projection(client, session_id)
    assert current_projection["revision"] > stale_projection["revision"]

    response = client.post(
        f"/api/v1/sessions/{session_id}/actions",
        json={
            "request_id": "client-action-stale-revision",
            "expected_revision": stale_projection["revision"],
            "action_id": action["action_id"],
            "target_ref": action["target_ref"],
            "amount": 1,
        },
    )
    conflict = _data(response, expected_status=409)
    after_conflict = _projection(client, session_id)

    assert conflict["reason_code"] == "stale_revision"
    assert conflict["expected_revision"] == stale_projection["revision"]
    assert conflict["current_revision"] == current_projection["revision"]
    assert _projection_head(after_conflict) == _projection_head(current_projection)


def test_closed_intervention_window_conflicts_without_mutation() -> None:
    client = _client()
    _, session = _boot_session(client)
    session_id = session["session_id"]
    initial = _projection(client, session_id)
    old_window = _open_window(initial)

    _data(
        client.post(
            f"/api/v1/sessions/{session_id}/steps",
            json={
                "request_id": "step-close-window",
                "step_count": 1,
                "expected_revision": initial["revision"],
            },
        )
    )
    current = _projection(client, session_id)
    response = client.post(
        f"/api/v1/sessions/{session_id}/directions",
        json=_bounded_direction(
            request_id="direction-on-closed-window",
            revision=current["revision"],
            window_id=old_window["window_id"],
        ),
    )
    conflict = _data(response, expected_status=409)

    assert conflict["reason_code"] == "intervention_window_closed"
    assert _projection(client, session_id) == current


def test_feedback_with_unknown_event_reference_is_rejected_without_diff() -> None:
    client = _client()
    _, session = _boot_session(client)
    session_id = session["session_id"]
    before = _projection(client, session_id)

    result = _data(
        client.post(
            f"/api/v1/sessions/{session_id}/feedback",
            json={
                "request_id": "feedback-unknown-event",
                "expected_revision": before["revision"],
                "feedback_type": "local_outcome_observed",
                "summary": "Observed a typed public outcome.",
                "related_event_ref": "event-missing",
            },
        )
    )
    after = _projection(client, session_id)

    assert result["status"] == "rejected"
    assert result["reason_code"] == "feedback_reference_not_found"
    assert result["applied_diff_refs"] == []
    assert after["revision"] == before["revision"]
    assert after["state_hash"] == before["state_hash"]


def test_completeness_cannot_splice_direction_proof_across_windows() -> None:
    client = _client()
    _, session = _boot_session(client)
    session_id = session["session_id"]
    initial = _projection(client, session_id)
    first_window = _open_window(initial)

    _data(
        client.post(
            f"/api/v1/sessions/{session_id}/directions",
            json=_bounded_direction(
                request_id="direction-applied-in-first-window",
                revision=initial["revision"],
                window_id=first_window["window_id"],
            ),
        )
    )
    _data(
        client.post(
            f"/api/v1/sessions/{session_id}/steps",
            json={
                "request_id": "step-after-first-window-direction",
                "step_count": 2,
                "expected_revision": initial["revision"],
            },
        )
    )

    current = _projection(client, session_id)
    second_window = _open_window(current)
    _data(
        client.post(
            f"/api/v1/sessions/{session_id}/directions",
            json=_bounded_direction(
                request_id="direction-queued-in-second-window",
                revision=current["revision"],
                window_id=second_window["window_id"],
            ),
        )
    )
    _data(
        client.post(
            f"/api/v1/sessions/{session_id}/directions",
            json=_final_fact_direction(
                request_id="direction-rejected-in-second-window",
                revision=current["revision"],
                window_id=second_window["window_id"],
            ),
        )
    )

    evidence = _evidence(client, session_id)
    checks = evidence["completeness"]["scenario_coverage"]["checks"]
    assert checks["accepted_direction_applied"] is True
    assert checks["semantic_direction_rejection"] is True
    assert checks["same_intervention_window"] is False
    assert checks["direction"] is False
    assert evidence["completeness"]["integrity"]["status"] == "valid"
    assert evidence["completeness"]["scenario_coverage"]["status"] == "partial"
