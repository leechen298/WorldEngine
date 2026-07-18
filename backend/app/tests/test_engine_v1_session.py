from __future__ import annotations

import hashlib
import json
from collections import defaultdict, deque
from typing import Any

from app.tests.test_engine_v1_generation import (
    _boot_session,
    _client,
    _data,
    _events,
    _evidence,
    _projection,
)


def _canonical_hash(value: dict[str, Any], algorithm: str) -> str:
    assert algorithm == "sha256-canonical-json-v1"
    normalized = json.dumps(
        value,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return hashlib.sha256(normalized).hexdigest()


def _has_hash_path(
    graph: dict[str, set[str]],
    start_hash: str,
    end_hash: str,
) -> bool:
    pending = deque([start_hash])
    visited = {start_hash}
    while pending:
        current = pending.popleft()
        if current == end_hash:
            return True
        for candidate in graph.get(current, set()):
            if candidate not in visited:
                visited.add(candidate)
                pending.append(candidate)
    return False


def test_ac_02_boot_cites_package_and_initial_state_is_consistent() -> None:
    client = _client()
    package, created = _boot_session(client)
    session_id = created["session_id"]

    session = _data(client.get(f"/api/v1/sessions/{session_id}"))
    canonical_head = session["projection"]
    projection = _projection(client, session_id)
    evidence = _evidence(client, session_id)
    initial_snapshot = evidence["snapshots"][0]

    assert created["projection"]["status"] == "ready"
    assert created["source_package_hash"] == package["package_hash"]
    assert session["source_package_hash"] == package["package_hash"]
    assert evidence["package"]["package_hash"] == package["package_hash"]

    assert canonical_head["tick"] == projection["tick"] == initial_snapshot["tick"] == 0
    assert canonical_head["revision"] == projection["revision"]
    assert canonical_head["revision"] == initial_snapshot["revision"]
    assert canonical_head["state_hash"] == projection["state_hash"]
    assert canonical_head["state_hash"] == initial_snapshot["state_hash"]
    assert evidence["projection"]["state_hash"] == canonical_head["state_hash"]
    assert initial_snapshot["canonical_state"]


def test_ac_03_step_n_advances_exact_ticks_and_consistent_public_heads() -> None:
    client = _client()
    package, session = _boot_session(client)
    session_id = session["session_id"]
    before = _data(client.get(f"/api/v1/sessions/{session_id}"))["projection"]
    before_projection = _projection(client, session_id)

    step_result = _data(
        client.post(
            f"/api/v1/sessions/{session_id}/steps",
            json={
                "request_id": "step-exact-three",
                "step_count": 3,
                "expected_revision": before["revision"],
            },
        )
    )
    after = _data(client.get(f"/api/v1/sessions/{session_id}"))["projection"]
    after_projection = _projection(client, session_id)
    evidence = _evidence(client, session_id)

    assert step_result["request_id"] == "step-exact-three"
    assert step_result["step_count"] == 3
    assert step_result["start_tick"] == before["tick"]
    assert step_result["start_revision"] == before["revision"]
    assert step_result["start_state_hash"] == before["state_hash"]
    assert step_result["end_tick"] == after["tick"]
    assert step_result["end_revision"] == after["revision"]
    assert step_result["end_state_hash"] == after["state_hash"]
    assert step_result["projection"] == after_projection

    assert after["tick"] == before["tick"] + 3
    assert after["world_time_seconds"] == (
        before["world_time_seconds"] + 3 * package["brief"]["step_seconds"]
    )
    assert after["revision"] > before["revision"]
    assert after_projection["event_cursor"] > before_projection["event_cursor"]
    assert after["tick"] == after_projection["tick"]
    assert after["revision"] == after_projection["revision"]
    assert after["state_hash"] == after_projection["state_hash"]

    snapshots = sorted(evidence["snapshots"], key=lambda item: item["tick"])
    assert {0, 1, 2, 3}.issubset({item["tick"] for item in snapshots})
    assert snapshots[-1]["tick"] == after["tick"]
    assert snapshots[-1]["revision"] == after["revision"]
    assert snapshots[-1]["state_hash"] == after["state_hash"]

    events = _events(
        client,
        session_id,
        after_sequence=before_projection["event_cursor"],
    )
    sequences = [event["sequence"] for event in events]
    assert sequences
    assert sequences == sorted(sequences)
    assert all(
        sequence > before_projection["event_cursor"] for sequence in sequences
    )
    assert [event["tick"] for event in events] == sorted(
        event["tick"] for event in events
    )


def test_ac_09_snapshot_and_diff_chain_reproduces_current_hash() -> None:
    client = _client()
    _, session = _boot_session(client)
    session_id = session["session_id"]

    _data(
        client.post(
            f"/api/v1/sessions/{session_id}/steps",
            json={
                "request_id": "step-hash-chain",
                "step_count": 3,
                "expected_revision": session["projection"]["revision"],
            },
        )
    )
    evidence = _evidence(client, session_id)
    projection = _projection(client, session_id)
    snapshots = sorted(
        evidence["snapshots"],
        key=lambda item: (item["revision"], item["tick"]),
    )
    diffs = evidence["diffs"]
    events = evidence["events"]
    algorithm = evidence["state_hash_algorithm"]

    assert snapshots
    assert diffs
    for snapshot in snapshots:
        assert _canonical_hash(snapshot["canonical_state"], algorithm) == snapshot[
            "state_hash"
        ]

    diff_ids = {diff["diff_id"] for diff in diffs}
    assert len(diff_ids) == len(diffs)
    graph: dict[str, set[str]] = defaultdict(set)
    for diff in diffs:
        assert diff["operations"]
        assert diff["state_hash_before"] != diff["state_hash_after"]
        graph[diff["state_hash_before"]].add(diff["state_hash_after"])

    for earlier, later in zip(snapshots, snapshots[1:]):
        if earlier["state_hash"] != later["state_hash"]:
            assert _has_hash_path(
                graph,
                earlier["state_hash"],
                later["state_hash"],
            )

    for event in events:
        refs = event["diff_refs"]
        assert set(refs).issubset(diff_ids)
        if event["status"] == "rejected":
            assert refs == []
        if (
            event["status"] == "accepted"
            and event["state_hash_before"] != event["state_hash_after"]
        ):
            assert refs

    latest = snapshots[-1]
    assert latest["state_hash"] == projection["state_hash"]
    assert latest["revision"] == projection["revision"]
    assert evidence["projection"]["state_hash"] == projection["state_hash"]


def test_sessions_from_the_same_package_keep_isolated_canonical_state() -> None:
    client = _client()
    package, first = _boot_session(client)
    second = _data(
        client.post(
            "/api/v1/sessions",
            json={
                "request_id": "session-create-isolated-second",
                "package_id": package["package_id"],
                "package_hash": package["package_hash"],
            },
        )
    )

    _data(
        client.post(
            f"/api/v1/sessions/{first['session_id']}/steps",
            json={
                "request_id": "step-only-first-session",
                "step_count": 1,
                "expected_revision": first["projection"]["revision"],
            },
        )
    )
    first_after = _projection(client, first["session_id"])
    second_after = _projection(client, second["session_id"])

    assert first_after["tick"] == 1
    assert second_after["tick"] == 0
    assert second_after["revision"] == 0
    assert second_after["variables"] == second["projection"]["variables"]
    assert first_after["state_hash"] != second_after["state_hash"]


def test_session_idempotency_key_reuse_with_different_package_conflicts() -> None:
    client = _client()
    first_package, first_session = _boot_session(client)
    second_package = _data(
        client.post(
            "/api/v1/world-packages",
            json={
                "request_id": "package-for-session-idempotency-conflict",
                "brief": {
                    "seed": "different-session-package-seed",
                    "premise": "A second generic public package.",
                },
            },
        )
    )

    response = client.post(
        "/api/v1/sessions",
        json={
            "request_id": "session-create-default",
            "package_id": second_package["package_id"],
            "package_hash": second_package["package_hash"],
        },
    )
    conflict = _data(response, expected_status=409)

    assert conflict["reason_code"] == "idempotency_key_reused"
    assert len(client.app.state.engine_v1_service._sessions) == 1
    assert _projection(client, first_session["session_id"])["source_package_hash"] == (
        first_package["package_hash"]
    )


def test_evidence_completeness_replays_diffs_and_event_links() -> None:
    client = _client()
    _, session = _boot_session(client)
    session_id = session["session_id"]
    _data(
        client.post(
            f"/api/v1/sessions/{session_id}/steps",
            json={
                "request_id": "step-before-evidence-corruption",
                "step_count": 2,
                "expected_revision": session["projection"]["revision"],
            },
        )
    )
    before = _evidence(client, session_id)
    assert before["completeness"]["checks"]["diff_snapshot_replay"] is True
    assert before["completeness"]["checks"]["event_diff_links"] is True

    record = client.app.state.engine_v1_service._sessions[session_id]
    record.diffs[0].operations[0].after = 999
    record.events[1].diff_refs = []
    corrupted = _evidence(client, session_id)

    assert corrupted["completeness"]["status"] == "incomplete"
    assert corrupted["completeness"]["checks"]["diff_snapshot_replay"] is False
    assert corrupted["completeness"]["checks"]["event_diff_links"] is False


def test_evidence_completeness_requires_experience_to_change_decision() -> None:
    client = _client()
    _, session = _boot_session(client)
    session_id = session["session_id"]
    _data(
        client.post(
            f"/api/v1/sessions/{session_id}/steps",
            json={
                "request_id": "step-before-agent-evidence-corruption",
                "step_count": 2,
                "expected_revision": session["projection"]["revision"],
            },
        )
    )
    before = _evidence(client, session_id)
    assert before["completeness"]["checks"]["agent_causal_chain"] is True
    assert before["completeness"]["checks"]["experience_linked_decision"] is True

    record = client.app.state.engine_v1_service._sessions[session_id]
    later_decision = record.agent_cycles[-1].decision
    later_decision["intent"] = "explore_allowed_action"
    later_decision["decision_mode"] = "initial_policy"
    corrupted = _evidence(client, session_id)

    assert corrupted["completeness"]["status"] == "incomplete"
    assert (
        corrupted["completeness"]["checks"]["experience_linked_decision"]
        is False
    )


def test_step_failure_rolls_back_all_canonical_changes(monkeypatch) -> None:
    client = _client()
    _, session = _boot_session(client)
    session_id = session["session_id"]
    before_projection = _projection(client, session_id)
    before_evidence = _evidence(client, session_id)
    service = client.app.state.engine_v1_service

    def fail_agent_cycle(*_args, **_kwargs) -> None:
        raise RuntimeError("forced atomic-step failure")

    monkeypatch.setattr(service, "_run_agent_cycle", fail_agent_cycle)
    response = client.post(
        f"/api/v1/sessions/{session_id}/steps",
        json={
            "request_id": "step-forced-rollback",
            "step_count": 1,
            "expected_revision": before_projection["revision"],
        },
    )
    failure = _data(response, expected_status=500)

    assert failure["reason_code"] == "atomic_operation_failed"
    assert failure["diagnostic_id"].startswith("diagnostic-")
    assert "forced atomic-step failure" not in response.text
    assert service._diagnostics[-1]["diagnostic_id"] == failure["diagnostic_id"]
    assert service._diagnostics[-1]["redaction_status"] == "safe-metadata-only"
    assert _projection(client, session_id) == before_projection
    after_evidence = _evidence(client, session_id)
    assert after_evidence["events"] == before_evidence["events"]
    assert after_evidence["diffs"] == before_evidence["diffs"]
    assert after_evidence["snapshots"] == before_evidence["snapshots"]
