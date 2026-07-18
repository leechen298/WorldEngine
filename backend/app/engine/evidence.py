from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, Tuple

from app.engine.generation import canonical_hash
from app.engine.models import EngineSessionRecord
from app.schemas.engine_v1 import SnapshotRecord


def canonical_state(record: EngineSessionRecord) -> Dict[str, Any]:
    return {
        "session_id": record.session_id,
        "world_id": record.world_id,
        "source_package_hash": record.package.package_hash,
        "status": record.status,
        "tick": record.tick,
        "world_time_seconds": record.world_time_seconds,
        "revision": record.revision,
        "variables": {key: record.variables[key] for key in sorted(record.variables)},
        "feedback_count": record.feedback_count,
        "agents": {
            key: record.agents[key].model_dump(mode="json")
            for key in sorted(record.agents)
        },
    }


def state_hash(record: EngineSessionRecord) -> str:
    return canonical_hash(canonical_state(record))


def next_event_id(record: EngineSessionRecord) -> str:
    return f"event-{record.session_id}-{len(record.events) + 1:06d}"


def next_diff_id(record: EngineSessionRecord) -> str:
    return f"diff-{record.session_id}-{len(record.diffs) + 1:06d}"


def capture_snapshot(record: EngineSessionRecord) -> SnapshotRecord:
    snapshot = SnapshotRecord(
        snapshot_id=f"snapshot-{record.session_id}-r{record.revision:06d}",
        tick=record.tick,
        revision=record.revision,
        state_hash=state_hash(record),
        canonical_state=deepcopy(canonical_state(record)),
    )
    if not record.snapshots or record.snapshots[-1].revision != snapshot.revision:
        record.snapshots.append(snapshot)
    return snapshot


def _read_public_path(state: Dict[str, Any], path: str) -> Any:
    current: Any = state
    for part in path.strip("/").split("/"):
        if not isinstance(current, dict) or part not in current:
            raise KeyError(path)
        current = current[part]
    return current


def _write_public_path(state: Dict[str, Any], path: str, value: Any) -> None:
    parts = path.strip("/").split("/")
    current: Any = state
    for part in parts[:-1]:
        if not isinstance(current, dict) or part not in current:
            raise KeyError(path)
        current = current[part]
    if not isinstance(current, dict) or parts[-1] not in current:
        raise KeyError(path)
    current[parts[-1]] = deepcopy(value)


def _event_diff_links_are_valid(record: EngineSessionRecord) -> bool:
    event_ids = [event.event_id for event in record.events]
    diff_ids = [diff.diff_id for diff in record.diffs]
    if len(event_ids) != len(set(event_ids)) or len(diff_ids) != len(set(diff_ids)):
        return False
    if [event.sequence for event in record.events] != list(
        range(1, len(record.events) + 1)
    ):
        return False

    events_by_id = {event.event_id: event for event in record.events}
    diffs_by_id = {diff.diff_id: diff for diff in record.diffs}
    referenced_diffs: list[str] = []
    for event in record.events:
        if event.status == "rejected" and event.diff_refs:
            return False
        if event.state_hash_before != event.state_hash_after and not event.diff_refs:
            return False
        for diff_ref in event.diff_refs:
            diff = diffs_by_id.get(diff_ref)
            if diff is None:
                return False
            if (
                diff.event_ref != event.event_id
                or diff.request_id != event.request_id
                or diff.tick != event.tick
                or diff.revision != event.revision
                or diff.state_hash_before != event.state_hash_before
                or diff.state_hash_after != event.state_hash_after
            ):
                return False
            referenced_diffs.append(diff_ref)

    if len(referenced_diffs) != len(set(referenced_diffs)):
        return False
    if set(referenced_diffs) != set(diff_ids):
        return False
    return all(diff.event_ref in events_by_id for diff in record.diffs)


def _diff_and_snapshot_replay_is_valid(record: EngineSessionRecord) -> bool:
    if not record.snapshots:
        return False
    initial = record.snapshots[0]
    if initial.revision != 0:
        return False

    replayed = deepcopy(initial.canonical_state)
    if canonical_hash(replayed) != initial.state_hash:
        return False
    replayed_heads: Dict[int, Tuple[str, Dict[str, Any]]] = {
        initial.revision: (initial.state_hash, deepcopy(replayed))
    }

    try:
        for diff in record.diffs:
            if canonical_hash(replayed) != diff.state_hash_before:
                return False
            if not diff.operations:
                return False
            for operation in diff.operations:
                if _read_public_path(replayed, operation.path) != operation.before:
                    return False
                _write_public_path(replayed, operation.path, operation.after)
            if canonical_hash(replayed) != diff.state_hash_after:
                return False
            if replayed.get("revision") != diff.revision:
                return False
            replayed_heads[diff.revision] = (
                diff.state_hash_after,
                deepcopy(replayed),
            )
    except (KeyError, TypeError, ValueError):
        return False

    current_state = canonical_state(record)
    if replayed != current_state or canonical_hash(replayed) != state_hash(record):
        return False

    snapshot_ids = [snapshot.snapshot_id for snapshot in record.snapshots]
    if len(snapshot_ids) != len(set(snapshot_ids)):
        return False
    for snapshot in record.snapshots:
        head = replayed_heads.get(snapshot.revision)
        if head is None:
            return False
        if canonical_hash(snapshot.canonical_state) != snapshot.state_hash:
            return False
        if head != (snapshot.state_hash, snapshot.canonical_state):
            return False
    return True


def _agent_causality_is_valid(record: EngineSessionRecord) -> Tuple[bool, bool, bool]:
    if not record.agent_cycles:
        return True, False, False

    events_by_id = {event.event_id: event for event in record.events}
    diffs_by_id = {diff.diff_id: diff for diff in record.diffs}
    prior_experiences: Dict[str, Dict[str, Any]] = {}
    baseline_decisions: Dict[str, Tuple[Any, Any]] = {}
    experience_changed_decision = False
    feedback_influenced_decision = False

    for cycle in record.agent_cycles:
        if not all(
            (
                cycle.perception,
                cycle.decision,
                cycle.action_request,
                cycle.rule_judgment,
                cycle.action_result,
            )
        ):
            return False, False, False
        if not cycle.event_refs or any(
            event_ref not in events_by_id for event_ref in cycle.event_refs
        ):
            return False, False, False
        if any(diff_ref not in diffs_by_id for diff_ref in cycle.diff_refs):
            return False, False, False
        result_event_ref = cycle.action_result.get("event_ref")
        if result_event_ref not in cycle.event_refs:
            return False, False, False
        result_event = events_by_id[result_event_ref]

        used_ids = [item.ref_id for item in cycle.experience_refs_used]
        decision_ref_ids = cycle.decision.get("experience_ref_ids", [])
        if used_ids != decision_ref_ids:
            return False, False, False
        perceived_experiences = cycle.perception.get("experience_refs")
        if not isinstance(perceived_experiences, list) or used_ids != [
            item.get("ref_id")
            for item in perceived_experiences
            if isinstance(item, dict)
        ]:
            return False, False, False

        action_target = cycle.action_request.get("target_ref")
        action_amount = cycle.action_request.get("amount")
        visible_variables = cycle.perception.get("visible_variables")
        feedback_count = cycle.perception.get("feedback_count")
        influence_factors = cycle.decision.get("influence_factors")
        if (
            not isinstance(action_target, str)
            or not isinstance(action_amount, int)
            or not isinstance(visible_variables, dict)
            or action_target not in visible_variables
            or not isinstance(feedback_count, int)
            or feedback_count < 0
            or not isinstance(influence_factors, list)
            or cycle.decision.get("target_ref") != action_target
            or cycle.decision.get("visible_value")
            != visible_variables[action_target]
            or cycle.decision.get("selected_amount") != action_amount
            or cycle.decision.get("feedback_count") != feedback_count
            or cycle.perception.get("state_hash") != result_event.state_hash_before
        ):
            return False, False, False

        expected_factors = ["current_variables"]
        if used_ids:
            expected_factors.append("experience")
        if feedback_count:
            expected_factors.append("feedback_count")
        if influence_factors != expected_factors:
            return False, False, False

        if feedback_count and used_ids:
            expected_intent = "adapt_to_feedback_with_experience"
            expected_mode = "feedback_adjusted_experience_policy"
        elif feedback_count:
            expected_intent = "adapt_to_feedback"
            expected_mode = "feedback_adjusted_policy"
        elif used_ids:
            expected_intent = "repeat_rule_accepted_action"
            expected_mode = "experience_guided_policy"
        else:
            expected_intent = "explore_allowed_action"
            expected_mode = "initial_policy"
        if (
            cycle.decision.get("intent") != expected_intent
            or cycle.decision.get("decision_mode") != expected_mode
        ):
            return False, False, False

        if used_ids:
            for experience in cycle.experience_refs_used:
                source = prior_experiences.get(experience.ref_id)
                if source != experience.model_dump(mode="json"):
                    return False, False, False
                if experience.source_tick >= cycle.tick:
                    return False, False, False
            baseline = baseline_decisions.get(cycle.agent_id)
            current = (
                cycle.decision.get("intent"),
                cycle.decision.get("decision_mode"),
            )
            if baseline is not None and current != baseline:
                experience_changed_decision = True
        else:
            baseline_decisions.setdefault(
                cycle.agent_id,
                (
                    cycle.decision.get("intent"),
                    cycle.decision.get("decision_mode"),
                ),
            )

        if feedback_count:
            prior_feedback_count = sum(
                event.event_type == "client.feedback.accepted"
                and event.status == "accepted"
                and event.sequence < result_event.sequence
                for event in record.events
            )
            if prior_feedback_count < feedback_count:
                return False, False, False
            feedback_influenced_decision = True

        new_experience = cycle.action_result.get("experience_ref")
        if new_experience is not None:
            if (
                not isinstance(new_experience, dict)
                or new_experience.get("ref_id") != result_event_ref
                or new_experience.get("source_tick") != cycle.tick
                or new_experience.get("target_ref") != action_target
                or new_experience.get("amount") != action_amount
            ):
                return False, False, False
            prior_experiences[result_event_ref] = deepcopy(new_experience)

    return True, experience_changed_decision, feedback_influenced_decision


def _direction_evidence_is_valid(
    record: EngineSessionRecord,
) -> Tuple[bool, bool, bool, bool]:
    events_by_id = {event.event_id: event for event in record.events}
    diffs_by_id = {diff.diff_id: diff for diff in record.diffs}
    applied_acceptances = []
    valid_rejections = []

    for decision in record.direction_decisions:
        submission_event = events_by_id.get(decision.event_ref)
        if submission_event is None or submission_event.request_id != decision.request_id:
            return False, False, False, False

        if decision.status == "accepted":
            if (
                submission_event.event_type != "direction.accepted"
                or submission_event.status != "accepted"
                or submission_event.diff_refs
                or decision.application_status == "not_applicable"
            ):
                return False, False, False, False
        elif decision.status in {"rejected", "conflict"}:
            if (
                submission_event.event_type != "direction.rejected"
                or submission_event.status != "rejected"
                or submission_event.diff_refs
                or decision.queued
                or decision.application_status != "not_applicable"
                or decision.application_event_refs
                or decision.applied_diff_refs
            ):
                return False, False, False, False
            if decision.reason_code == "direct_final_fact_forbidden":
                valid_rejections.append(decision)
            continue
        else:
            return False, False, False, False

        application_events = [
            events_by_id.get(event_ref) for event_ref in decision.application_event_refs
        ]
        if any(
            event is None or event.request_id != decision.request_id
            for event in application_events
        ):
            return False, False, False, False

        if decision.application_status == "queued":
            if (
                not decision.queued
                or decision.application_reason_code is not None
                or decision.application_event_refs
                or decision.applied_diff_refs
            ):
                return False, False, False, False
            continue

        if decision.queued or not application_events:
            return False, False, False, False

        if decision.application_status == "applied":
            if (
                decision.application_reason_code != "direction_applied"
                or not decision.applied_diff_refs
                or any(
                    event.event_type != "direction.applied"
                    or event.status != "accepted"
                    for event in application_events
                )
            ):
                return False, False, False, False
            application_diff_refs = [
                diff_ref for event in application_events for diff_ref in event.diff_refs
            ]
            if application_diff_refs != decision.applied_diff_refs or any(
                diff_ref not in diffs_by_id
                or diffs_by_id[diff_ref].event_ref not in decision.application_event_refs
                for diff_ref in decision.applied_diff_refs
            ):
                return False, False, False, False
            applied_acceptances.append(decision)
            continue

        if decision.application_status == "application_rejected":
            if (
                decision.application_reason_code
                != "direction_target_range_violation"
                or decision.applied_diff_refs
                or any(
                    event.event_type != "direction.application_rejected"
                    or event.status != "rejected"
                    or event.diff_refs
                    for event in application_events
                )
            ):
                return False, False, False, False
            continue

        return False, False, False, False

    same_window = any(
        accepted_item.window_id == rejected_item.window_id
        for accepted_item in applied_acceptances
        for rejected_item in valid_rejections
    )
    return True, bool(applied_acceptances), bool(valid_rejections), same_window


def _request_correlations_are_valid(record: EngineSessionRecord) -> bool:
    events_by_id = {event.event_id: event for event in record.events}
    diffs_by_id = {diff.diff_id: diff for diff in record.diffs}
    keys: set[Tuple[str, str]] = set()

    for correlation in record.request_correlations:
        operation_id = correlation.get("operation_id")
        request_id = correlation.get("request_id")
        event_refs = correlation.get("event_refs")
        diff_refs = correlation.get("diff_refs")
        key = (operation_id, request_id)
        if (
            not isinstance(operation_id, str)
            or not isinstance(request_id, str)
            or key in keys
            or not isinstance(event_refs, list)
            or not event_refs
            or not isinstance(diff_refs, list)
            or any(event_ref not in events_by_id for event_ref in event_refs)
            or any(diff_ref not in diffs_by_id for diff_ref in diff_refs)
        ):
            return False
        keys.add(key)

        correlated_events = [events_by_id[event_ref] for event_ref in event_refs]
        if [event.sequence for event in correlated_events] != sorted(
            event.sequence for event in correlated_events
        ):
            return False
        correlated_diff_refs = [
            diff_ref for event in correlated_events for diff_ref in event.diff_refs
        ]
        last_event = correlated_events[-1]
        if (
            correlated_diff_refs != diff_refs
            or correlation.get("tick") != last_event.tick
            or correlation.get("revision") != last_event.revision
            or correlation.get("state_hash") != last_event.state_hash_after
        ):
            return False

    correlations_by_key = {
        (item["operation_id"], item["request_id"]): item
        for item in record.request_correlations
    }
    for decision in record.direction_decisions:
        correlation = correlations_by_key.get(("directions.submit", decision.request_id))
        if correlation is None or (
            correlation.get("status") != decision.status
            or correlation.get("application_status") != decision.application_status
            or correlation.get("event_refs")
            != [decision.event_ref, *decision.application_event_refs]
            or correlation.get("diff_refs") != decision.applied_diff_refs
        ):
            return False
    return True


def _accepted_event_with_diff(record: EngineSessionRecord, event_type: str) -> bool:
    return any(
        event.event_type == event_type
        and event.status == "accepted"
        and bool(event.diff_refs)
        for event in record.events
    )


def evidence_integrity_checks(record: EngineSessionRecord) -> Dict[str, bool]:
    agent_chain, _, _ = _agent_causality_is_valid(record)
    direction_chain, _, _, _ = _direction_evidence_is_valid(record)
    last_snapshot_matches = bool(record.snapshots) and (
        record.snapshots[-1].state_hash == state_hash(record)
        and record.snapshots[-1].revision == record.revision
    )
    return {
        "event_diff_links": _event_diff_links_are_valid(record),
        "diff_snapshot_replay": _diff_and_snapshot_replay_is_valid(record),
        "agent_causal_links": agent_chain,
        "direction_causal_links": direction_chain,
        "request_correlations": _request_correlations_are_valid(record),
        "projection_snapshot_consistent": last_snapshot_matches,
    }


def evidence_scenario_coverage_checks(record: EngineSessionRecord) -> Dict[str, bool]:
    agent_chain, experience_changed, feedback_influenced = (
        _agent_causality_is_valid(record)
    )
    direction_chain, accepted_applied, semantic_rejection, same_window = (
        _direction_evidence_is_valid(record)
    )
    return {
        "action": _accepted_event_with_diff(record, "client.action.accepted"),
        "feedback": _accepted_event_with_diff(record, "client.feedback.accepted"),
        "agent": bool(record.agent_cycles) and agent_chain,
        "direction": (
            direction_chain
            and accepted_applied
            and semantic_rejection
            and same_window
        ),
        "agent_experience": agent_chain and experience_changed,
        "agent_feedback_influence": agent_chain and feedback_influenced,
        "accepted_direction_applied": direction_chain and accepted_applied,
        "semantic_direction_rejection": direction_chain and semantic_rejection,
        "same_intervention_window": direction_chain and same_window,
    }
