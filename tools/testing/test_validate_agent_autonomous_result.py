from __future__ import annotations

import json
import shutil
from pathlib import Path

from tools.testing.validate_agent_autonomous_result import validate_result_dir


FIXTURES_DIR = Path(__file__).parent / "fixtures" / "agent-autonomous"


def _write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n")


def _write_valid_full_lifecycle_result(result_dir: Path) -> None:
    result_dir.mkdir(parents=True, exist_ok=True)
    (result_dir / "screenshots").mkdir()
    (result_dir / "screenshots" / "runtime-console.png").write_bytes(b"placeholder image")
    (result_dir / "transcript.md").write_text("# Transcript\n\nObserved full lifecycle evidence.\n")
    (result_dir / "console.log").write_text("no client errors\n")
    (result_dir / "operation-log.jsonl").write_text(
        "\n".join(
            [
                json.dumps({"seq": 1, "type": "ui", "target": "dashboard", "action": "open"}),
                json.dumps({"seq": 2, "type": "ui", "target": "world-create-form", "action": "fill"}),
                json.dumps(
                    {
                        "seq": 3,
                        "type": "ui",
                        "target": "worldengine-session-create-button",
                        "action": "click",
                    }
                ),
                json.dumps({"seq": 4, "type": "ui", "target": "runtime-run-button", "action": "click"}),
                json.dumps({"seq": 5, "type": "ui", "target": "runtime-tick-counter", "action": "observe"}),
                json.dumps({"seq": 6, "type": "ui", "target": "agent-life-log", "action": "observe"}),
                json.dumps({"seq": 7, "type": "ui", "target": "director-guidance-input", "action": "fill"}),
                json.dumps({"seq": 8, "type": "ui", "target": "evidence-download-button", "action": "click"}),
                json.dumps(
                    {
                        "seq": 9,
                        "type": "cli",
                        "command": "make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/latest",
                        "exit_code": 0,
                        "summary": "Ran deterministic autonomous scorecard checker.",
                    }
                ),
            ]
        )
        + "\n"
    )
    _write_json(
        result_dir / "api-summary.json",
        {
            "status": "pass",
            "worldengine_public_calls": [
                {"method": "GET", "path": "/manifest", "status_code": 200},
                {"method": "POST", "path": "/worlds", "status_code": 200},
                {"method": "POST", "path": "/worlds/{world_id}/director-guidance", "status_code": 200},
            ],
            "private_trace_included": False,
        },
    )
    _write_json(
        result_dir / "world-lifecycle-summary.json",
        {
            "scenario": "worldengine-full-lifecycle-autonomous",
            "world_creation": {
                "status": "pass",
                "world_id": "world-generic-001",
                "public_initial_state_observed": True,
                "visualization_observed": True,
            },
            "runtime_progression": {
                "status": "pass",
                "tick_start": 0,
                "tick_end": 8,
                "events_observed": 12,
                "snapshots_observed": 2,
            },
            "agent_autonomy": {
                "status": "pass",
                "agent_actions_observed": 4,
                "unique_action_types": ["observe", "move"],
                "client_scripted_actions": False,
                "worldengine_evidence_observed": True,
            },
            "external_direction": {
                "status": "pass",
                "director_guidance_observed": True,
                "direct_agent_private_state_mutation": False,
            },
            "evidence_integrity": {
                "status": "pass",
                "operation_log_entries": 9,
                "api_trace_entries": 3,
                "redaction_scan_passed": True,
            },
        },
    )
    _write_json(
        result_dir / "scorecard-summary.json",
        {
            "scenario": "worldengine-full-lifecycle-autonomous",
            "status": "pass",
            "verdict_source": "scorecard_checker",
        },
    )
    _write_json(
        result_dir / "result.json",
        {
            "scenario": "worldengine-full-lifecycle-autonomous",
            "goal": "Validate WorldEngine can create, run, and evidence an autonomous-agent world lifecycle.",
            "mode": "scorecard_autonomous",
            "status": "pass",
            "verdict_source": "scorecard_checker",
            "score_items": [
                {"name": "world_created", "status": "pass", "evidence": "world-lifecycle-summary.json"},
                {"name": "runtime_progressed", "status": "pass", "evidence": "world-lifecycle-summary.json"},
                {"name": "agent_autonomy_observed", "status": "pass", "evidence": "world-lifecycle-summary.json"},
                {"name": "external_direction_bounded", "status": "pass", "evidence": "world-lifecycle-summary.json"},
            ],
            "required_artifacts": [
                "transcript",
                "console_log",
                "scorecard_summary",
                "operation_log",
                "api_summary",
                "world_lifecycle_summary",
                "screenshots",
            ],
            "artifacts": {
                "transcript": "transcript.md",
                "console_log": "console.log",
                "scorecard_summary": "scorecard-summary.json",
                "operation_log": "operation-log.jsonl",
                "api_summary": "api-summary.json",
                "world_lifecycle_summary": "world-lifecycle-summary.json",
                "screenshots": ["screenshots/runtime-console.png"],
            },
            "operation_log": "operation-log.jsonl",
            "unverified_items": [],
            "failures": [],
        },
    )


def test_valid_basic_runtime_fixture_passes() -> None:
    assert validate_result_dir(FIXTURES_DIR / "valid-dashboard-basic-runtime") == []


def test_valid_worldengine_full_lifecycle_fixture_passes() -> None:
    assert validate_result_dir(FIXTURES_DIR / "valid-worldengine-full-lifecycle") == []


def test_agent_verdict_fixture_fails() -> None:
    errors = validate_result_dir(FIXTURES_DIR / "invalid-agent-verdict")

    assert any("verdict_source" in error for error in errors)


def test_direct_api_operation_fails() -> None:
    errors = validate_result_dir(FIXTURES_DIR / "invalid-direct-api-operation")

    assert any("direct API" in error or "type must be ui or cli" in error for error in errors)


def test_cli_nonzero_exit_fails() -> None:
    errors = validate_result_dir(FIXTURES_DIR / "invalid-cli-nonzero-exit")

    assert any("exit_code must be 0" in error for error in errors)


def test_unresolved_p1_item_fails() -> None:
    errors = validate_result_dir(FIXTURES_DIR / "invalid-unverified-p1")

    assert any("unresolved P1" in error for error in errors)


def test_failed_score_item_fails() -> None:
    errors = validate_result_dir(FIXTURES_DIR / "invalid-failed-score-item")

    assert any("score_items" in error and "status must be pass" in error for error in errors)


def test_missing_required_artifact_fails() -> None:
    errors = validate_result_dir(FIXTURES_DIR / "invalid-missing-artifact")

    assert any("Missing required artifact" in error for error in errors)


def test_scenario_required_ui_target_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "missing-ui-target"
    shutil.copytree(FIXTURES_DIR / "valid-dashboard-basic-runtime", result_dir)
    operation_log = result_dir / "operation-log.jsonl"
    operations = [
        json.loads(line)
        for line in operation_log.read_text().splitlines()
        if "runtime-step-button" not in line
    ]
    operation_log.write_text("\n".join(json.dumps(operation) for operation in operations) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("runtime-step-button" in error for error in errors)


def test_scorecard_summary_mismatch_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "scorecard-mismatch"
    shutil.copytree(FIXTURES_DIR / "valid-dashboard-basic-runtime", result_dir)
    summary_path = result_dir / "scorecard-summary.json"
    summary = json.loads(summary_path.read_text())
    summary["scenario"] = "autonomous-dashboard-params-flow"
    summary_path.write_text(json.dumps(summary, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("scorecard-summary.json scenario must match" in error for error in errors)


def test_valid_full_world_lifecycle_result_passes(tmp_path: Path) -> None:
    result_dir = tmp_path / "valid-full-lifecycle"
    _write_valid_full_lifecycle_result(result_dir)

    assert validate_result_dir(result_dir) == []


def test_full_world_lifecycle_missing_agent_actions_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "missing-agent-actions"
    _write_valid_full_lifecycle_result(result_dir)
    summary_path = result_dir / "world-lifecycle-summary.json"
    summary = json.loads(summary_path.read_text())
    summary["agent_autonomy"]["agent_actions_observed"] = 0
    summary_path.write_text(json.dumps(summary, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("agent_autonomy.agent_actions_observed" in error for error in errors)


def test_full_world_lifecycle_client_scripted_agent_actions_fail(tmp_path: Path) -> None:
    result_dir = tmp_path / "client-scripted-actions"
    _write_valid_full_lifecycle_result(result_dir)
    summary_path = result_dir / "world-lifecycle-summary.json"
    summary = json.loads(summary_path.read_text())
    summary["agent_autonomy"]["client_scripted_actions"] = True
    summary_path.write_text(json.dumps(summary, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("agent_autonomy.client_scripted_actions" in error for error in errors)


def test_full_world_lifecycle_non_advancing_runtime_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "non-advancing-runtime"
    _write_valid_full_lifecycle_result(result_dir)
    summary_path = result_dir / "world-lifecycle-summary.json"
    summary = json.loads(summary_path.read_text())
    summary["runtime_progression"]["tick_end"] = summary["runtime_progression"]["tick_start"]
    summary_path.write_text(json.dumps(summary, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("runtime_progression.tick_end" in error for error in errors)


def test_full_world_lifecycle_failed_redaction_scan_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "failed-redaction-scan"
    _write_valid_full_lifecycle_result(result_dir)
    summary_path = result_dir / "world-lifecycle-summary.json"
    summary = json.loads(summary_path.read_text())
    summary["evidence_integrity"]["redaction_scan_passed"] = False
    summary_path.write_text(json.dumps(summary, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("evidence_integrity.redaction_scan_passed" in error for error in errors)


def test_full_world_lifecycle_cli_curl_disguised_direct_api_call_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "cli-disguised-direct-api"
    _write_valid_full_lifecycle_result(result_dir)
    operation_log = result_dir / "operation-log.jsonl"
    operations = [
        json.loads(line)
        for line in operation_log.read_text().splitlines()
        if line.strip()
    ]
    operations.append(
        {
            "seq": len(operations) + 1,
            "type": "cli",
            "command": "curl -s http://127.0.0.1:8000/worlds",
            "exit_code": 0,
            "summary": "Direct public API call disguised as CLI evidence.",
        }
    )
    operation_log.write_text("\n".join(json.dumps(operation) for operation in operations) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("direct public API calls must be recorded in api-summary.json" in error for error in errors)


def test_full_world_lifecycle_cli_python_disguised_direct_api_call_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "cli-python-disguised-direct-api"
    _write_valid_full_lifecycle_result(result_dir)
    operation_log = result_dir / "operation-log.jsonl"
    operations = [
        json.loads(line)
        for line in operation_log.read_text().splitlines()
        if line.strip()
    ]
    operations.append(
        {
            "seq": len(operations) + 1,
            "type": "cli",
            "command": (
                "python -c \"import requests; "
                "requests.get('http://127.0.0.1:8000/runtime/state')\""
            ),
            "exit_code": 0,
            "summary": "Direct runtime API call disguised as CLI evidence.",
        }
    )
    operation_log.write_text("\n".join(json.dumps(operation) for operation in operations) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("direct public API calls must be recorded in api-summary.json" in error for error in errors)


def test_full_world_lifecycle_cli_described_direct_api_call_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "cli-described-direct-api"
    _write_valid_full_lifecycle_result(result_dir)
    operation_log = result_dir / "operation-log.jsonl"
    operations = [
        json.loads(line)
        for line in operation_log.read_text().splitlines()
        if line.strip()
    ]
    operations.append(
        {
            "seq": len(operations) + 1,
            "type": "cli",
            "command": "POST /runtime/step repeated through WorldEngine public API",
            "exit_code": 0,
            "summary": "Direct runtime API call disguised as CLI evidence.",
        }
    )
    operation_log.write_text("\n".join(json.dumps(operation) for operation in operations) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("direct public API calls must be recorded in api-summary.json" in error for error in errors)


def test_full_world_lifecycle_public_evidence_phrase_marker_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "public-evidence-phrase-marker"
    _write_valid_full_lifecycle_result(result_dir)
    api_summary_path = result_dir / "api-summary.json"
    api_summary = json.loads(api_summary_path.read_text())
    api_summary["worldengine_public_calls"][0]["response_summary"] = {
        "public_explanation": "no Agent private memory was changed"
    }
    api_summary_path.write_text(json.dumps(api_summary, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("api-summary.json contains forbidden public evidence marker" in error for error in errors)
