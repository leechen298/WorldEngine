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


def _agent_causality_is_valid(record: EngineSessionRecord) -> Tuple[bool, bool]:
    if not record.agent_cycles:
        return False, False

    events_by_id = {event.event_id: event for event in record.events}
    diffs_by_id = {diff.diff_id: diff for diff in record.diffs}
    prior_experiences: Dict[str, Dict[str, Any]] = {}
    baseline_decisions: Dict[str, Tuple[Any, Any]] = {}
    experience_changed_decision = False

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
            return False, False
        if not cycle.event_refs or any(
            event_ref not in events_by_id for event_ref in cycle.event_refs
        ):
            return False, False
        if any(diff_ref not in diffs_by_id for diff_ref in cycle.diff_refs):
            return False, False
        result_event_ref = cycle.action_result.get("event_ref")
        if result_event_ref not in cycle.event_refs:
            return False, False

        used_ids = [item.ref_id for item in cycle.experience_refs_used]
        decision_ref_ids = cycle.decision.get("experience_ref_ids", [])
        if used_ids != decision_ref_ids:
            return False, False
        if used_ids:
            for experience in cycle.experience_refs_used:
                source = prior_experiences.get(experience.ref_id)
                if source != experience.model_dump(mode="json"):
                    return False, False
                if experience.source_tick >= cycle.tick:
                    return False, False
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

        new_experience = cycle.action_result.get("experience_ref")
        if new_experience is not None:
            if (
                not isinstance(new_experience, dict)
                or new_experience.get("ref_id") != result_event_ref
                or new_experience.get("source_tick") != cycle.tick
            ):
                return False, False
            prior_experiences[result_event_ref] = deepcopy(new_experience)

    return True, experience_changed_decision


def _direction_evidence_is_valid(
    record: EngineSessionRecord,
) -> Tuple[bool, bool, bool]:
    events_by_id = {event.event_id: event for event in record.events}
    diffs_by_id = {diff.diff_id: diff for diff in record.diffs}
    accepted = [item for item in record.direction_decisions if item.status == "accepted"]
    rejected = [
        item
        for item in record.direction_decisions
        if item.status == "rejected"
        and item.reason_code == "direct_final_fact_forbidden"
    ]

    applied_acceptances = []
    for decision in accepted:
        acceptance_event = events_by_id.get(decision.event_ref)
        if (
            acceptance_event is None
            or acceptance_event.event_type != "direction.accepted"
            or acceptance_event.status != "accepted"
            or acceptance_event.request_id != decision.request_id
            or acceptance_event.diff_refs
        ):
            continue
        if not decision.application_event_refs or not decision.applied_diff_refs:
            continue
        application_events = [
            events_by_id.get(event_ref)
            for event_ref in decision.application_event_refs
        ]
        if any(
            event is None
            or event.event_type != "direction.applied"
            or event.status != "accepted"
            or event.request_id != decision.request_id
            for event in application_events
        ):
            continue
        if any(
            diff_ref not in diffs_by_id
            or diffs_by_id[diff_ref].event_ref
            not in decision.application_event_refs
            for diff_ref in decision.applied_diff_refs
        ):
            continue
        applied_acceptances.append(decision)

    valid_rejections = []
    for decision in rejected:
        event = events_by_id.get(decision.event_ref)
        if (
            event is not None
            and event.event_type == "direction.rejected"
            and event.status == "rejected"
            and event.request_id == decision.request_id
            and not event.diff_refs
            and not decision.applied_diff_refs
            and not decision.application_event_refs
        ):
            valid_rejections.append(decision)

    same_window = any(
        accepted_item.window_id == rejected_item.window_id
        for accepted_item in applied_acceptances
        for rejected_item in valid_rejections
    )
    return bool(applied_acceptances), bool(valid_rejections), same_window


def evidence_integrity_checks(record: EngineSessionRecord) -> Dict[str, bool]:
    agent_chain, experience_changed = _agent_causality_is_valid(record)
    accepted_applied, semantic_rejection, same_window = (
        _direction_evidence_is_valid(record)
    )
    last_snapshot_matches = bool(record.snapshots) and (
        record.snapshots[-1].state_hash == state_hash(record)
        and record.snapshots[-1].revision == record.revision
    )
    return {
        "event_diff_links": _event_diff_links_are_valid(record),
        "diff_snapshot_replay": _diff_and_snapshot_replay_is_valid(record),
        "agent_causal_chain": agent_chain,
        "experience_linked_decision": experience_changed,
        "accepted_direction_applied": accepted_applied,
        "semantic_direction_rejection": semantic_rejection,
        "same_intervention_window": same_window,
        "projection_snapshot_consistent": last_snapshot_matches,
    }
