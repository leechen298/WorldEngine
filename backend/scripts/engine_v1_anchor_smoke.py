from __future__ import annotations

import argparse
import json
import socket
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict

import httpx


def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def _wait_for_health(client: httpx.Client, timeout_seconds: float = 20.0) -> None:
    deadline = time.monotonic() + timeout_seconds
    while time.monotonic() < deadline:
        try:
            response = client.get("/health")
            if response.status_code == 200:
                return
        except httpx.HTTPError:
            pass
        time.sleep(0.1)
    raise RuntimeError("WorldEngine did not become healthy before the smoke timeout")


def _data(response: httpx.Response) -> Dict[str, Any]:
    response.raise_for_status()
    payload = response.json()
    if payload.get("code") != 0:
        raise RuntimeError(f"WorldEngine request failed: {payload}")
    return payload["data"]


def _path(operations: Dict[str, Dict[str, Any]], operation_id: str, **values: str) -> str:
    path = operations[operation_id]["path"]
    for key, value in values.items():
        path = path.replace("{" + key + "}", value)
    return path


def run_smoke(port: int) -> Dict[str, Any]:
    backend_root = Path(__file__).resolve().parents[1]
    command = [
        sys.executable,
        "-m",
        "uvicorn",
        "app.main:app",
        "--host",
        "127.0.0.1",
        "--port",
        str(port),
    ]
    process = subprocess.Popen(
        command,
        cwd=backend_root,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )
    base_url = f"http://127.0.0.1:{port}"
    try:
        with httpx.Client(base_url=base_url, timeout=10.0, trust_env=False) as client:
            _wait_for_health(client)
            manifest = _data(client.get("/api/v1/capabilities"))
            operations = {
                item["operation_id"]: item for item in manifest["operations"]
            }

            brief = {
                "seed": "smoke-seed-v1",
                "premise": "A bounded generic runtime for public protocol verification",
                "state_variables": [
                    {
                        "key": "anchor_signal",
                        "initial": 0,
                        "minimum": -20,
                        "maximum": 20,
                        "step": 1,
                    }
                ],
            }
            package = _data(
                client.post(
                    _path(operations, "world_packages.create"),
                    json={
                        "request_id": "smoke-package",
                        "brief": brief,
                    },
                )
            )
            repeated_package = _data(
                client.post(
                    _path(operations, "world_packages.create"),
                    json={
                        "request_id": "smoke-package-repeat",
                        "brief": brief,
                    },
                )
            )
            session = _data(
                client.post(
                    _path(operations, "sessions.create"),
                    json={
                        "request_id": "smoke-session",
                        "package_id": package["package_id"],
                        "package_hash": package["package_hash"],
                    },
                )
            )
            session_id = session["session_id"]
            projection = session["projection"]
            window_id = projection["active_intervention_window"]["window_id"]

            accepted_direction = _data(
                client.post(
                    _path(operations, "directions.submit", session_id=session_id),
                    json={
                        "request_id": "smoke-direction-accepted",
                        "window_id": window_id,
                        "expected_revision": projection["revision"],
                        "kind": "bounded_pressure",
                        "target_ref": "anchor_signal",
                        "summary": "Apply bounded public pressure",
                        "magnitude": 1,
                    },
                )
            )
            rejected_direction = _data(
                client.post(
                    _path(operations, "directions.submit", session_id=session_id),
                    json={
                        "request_id": "smoke-direction-rejected",
                        "window_id": window_id,
                        "expected_revision": projection["revision"],
                        "kind": "direct_final_fact",
                        "target_ref": "anchor_signal",
                        "summary": "Assign a final canonical value",
                        "final_value": 10,
                    },
                )
            )
            stepped = _data(
                client.post(
                    _path(operations, "sessions.step", session_id=session_id),
                    json={
                        "request_id": "smoke-step",
                        "step_count": 2,
                        "expected_revision": projection["revision"],
                    },
                )
            )
            projection = stepped["projection"]
            action_id = projection["allowed_actions"][0]
            action = _data(
                client.post(
                    _path(operations, "actions.submit", session_id=session_id),
                    json={
                        "request_id": "smoke-action",
                        "expected_revision": projection["revision"],
                        "action_id": action_id,
                        "target_ref": "anchor_signal",
                        "amount": 1,
                    },
                )
            )
            feedback = _data(
                client.post(
                    _path(operations, "feedback.submit", session_id=session_id),
                    json={
                        "request_id": "smoke-feedback",
                        "expected_revision": action["projection"]["revision"],
                        "feedback_type": "local_outcome_observed",
                        "summary": "Client observed the accepted public outcome",
                        "related_event_ref": action["event_ref"],
                    },
                )
            )
            event_page = _data(
                client.get(
                    _path(operations, "events.poll", session_id=session_id),
                    params={"after_sequence": 0, "limit": 200},
                )
            )
            evidence = _data(
                client.get(
                    _path(operations, "evidence.export", session_id=session_id)
                )
            )
            public_agents = evidence["projection"]["agents"]
            event_items = event_page["items"]
            direction_evidence = next(
                (
                    item
                    for item in evidence["direction_decisions"]
                    if item["request_id"] == accepted_direction["request_id"]
                ),
                None,
            )
            agent_cycles = evidence["agent_cycles"]
            required_operation_ids = {
                "world_packages.create",
                "sessions.create",
                "sessions.step",
                "directions.submit",
                "actions.submit",
                "feedback.submit",
                "events.poll",
                "evidence.export",
            }
            checks = {
                "manifest_discovery": required_operation_ids.issubset(operations),
                "deterministic_package": (
                    package["readiness"]["status"] == "ready"
                    and package["package_hash"] == repeated_package["package_hash"]
                ),
                "session_source_hash": (
                    session["source_package_hash"] == package["package_hash"]
                ),
                "same_window_direction_pair": (
                    accepted_direction["status"] == "accepted"
                    and accepted_direction["window_id"] == window_id
                    and rejected_direction["status"] == "rejected"
                    and rejected_direction["reason_code"]
                    == "direct_final_fact_forbidden"
                    and rejected_direction["window_id"] == window_id
                    and not rejected_direction["applied_diff_refs"]
                ),
                "direction_applied_later": (
                    direction_evidence is not None
                    and bool(direction_evidence["application_event_refs"])
                    and bool(direction_evidence["applied_diff_refs"])
                ),
                "exact_step": (
                    stepped["start_tick"] == 0
                    and stepped["end_tick"] == 2
                    and stepped["step_count"] == 2
                ),
                "agent_causal_chain": (
                    bool(public_agents)
                    and public_agents[0]["cycle_count"] >= 2
                    and len(agent_cycles) >= 2
                    and bool(agent_cycles[-1]["experience_refs_used"])
                    and bool(agent_cycles[-1]["perception"])
                    and bool(agent_cycles[-1]["decision"])
                    and bool(agent_cycles[-1]["action_request"])
                    and bool(agent_cycles[-1]["rule_judgment"])
                    and bool(agent_cycles[-1]["action_result"])
                ),
                "action_accepted": (
                    action["status"] == "accepted"
                    and action["reason_code"] == "action_rule_accepted"
                    and bool(action["applied_diff_refs"])
                ),
                "feedback_accepted": (
                    feedback["status"] == "accepted"
                    and feedback["reason_code"] == "feedback_accepted"
                    and bool(feedback["applied_diff_refs"])
                    and feedback["projection"]["feedback_count"] == 1
                ),
                "event_poll_complete": (
                    bool(event_items)
                    and event_page["has_more"] is False
                    and event_page["next_sequence"]
                    == evidence["projection"]["event_cursor"]
                ),
                "evidence_complete": (
                    evidence["completeness"]["status"] == "complete"
                    and all(evidence["completeness"]["checks"].values())
                ),
            }
            classification = (
                "WORLDENGINE_SIDE_ANCHOR_PASS"
                if all(checks.values())
                else "WORLDENGINE_SIDE_ANCHOR_INCOMPLETE"
            )
            return {
                "classification": classification,
                "complete_v0_13_claimed": False,
                "checks": checks,
                "missing_checks": [
                    name for name, passed in checks.items() if not passed
                ],
                "engine_build": manifest["engine_build"],
                "instance_id": manifest["instance_id"],
                "package_id": package["package_id"],
                "package_hash": package["package_hash"],
                "session_id": session_id,
                "window_id": window_id,
                "accepted_direction_request_id": accepted_direction["request_id"],
                "rejected_direction_request_id": rejected_direction["request_id"],
                "action_request_id": action["request_id"],
                "feedback_request_id": feedback["request_id"],
                "agent_id": public_agents[0]["agent_id"] if public_agents else None,
                "agent_cycle_count": (
                    public_agents[0]["cycle_count"] if public_agents else 0
                ),
                "polled_event_count": len(event_items),
                "event_cursor": event_page["next_sequence"],
                "tick": evidence["projection"]["tick"],
                "revision": evidence["projection"]["revision"],
                "state_hash": evidence["projection"]["state_hash"],
                "evidence_status": evidence["completeness"]["status"],
            }
    finally:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the WorldEngine v1 anchor smoke")
    parser.add_argument("--port", type=int, default=0)
    args = parser.parse_args()
    result = run_smoke(args.port or _free_port())
    print(json.dumps(result, ensure_ascii=True, sort_keys=True))
    return 0 if result["classification"] == "WORLDENGINE_SIDE_ANCHOR_PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
