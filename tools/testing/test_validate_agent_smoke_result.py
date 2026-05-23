from __future__ import annotations

import json
import shutil
from pathlib import Path

from tools.testing.agent_smoke_evidence import build_api_summary_from_state
from tools.testing.validate_agent_smoke_result import validate_result_dir


FIXTURES_DIR = Path(__file__).parent / "fixtures" / "agent-smoke"


def test_valid_basic_runtime_fixture_passes() -> None:
    errors = validate_result_dir(FIXTURES_DIR / "valid-basic-runtime")

    assert errors == []


def test_valid_params_flow_fixture_passes() -> None:
    errors = validate_result_dir(FIXTURES_DIR / "valid-params-flow")

    assert errors == []


def test_valid_invalid_param_fixture_passes() -> None:
    errors = validate_result_dir(FIXTURES_DIR / "valid-invalid-param")

    assert errors == []


def test_evidence_helper_builds_params_flow_summary() -> None:
    summary = build_api_summary_from_state(
        scenario="dashboard-params-flow",
        baseline={
            "health_status": "ok",
            "runtime": {"tick_id": 4},
            "world_params": {},
        },
        health={"status": "ok"},
        runtime={"tick_id": 5},
        params={"counter": {"increment": {"value": 2, "type": "number"}}},
        events=[
            {
                "tick_id": 5,
                "type": "module.counter",
                "payload": {"increment": 2, "counter": 2},
            }
        ],
    )

    assert summary["scenario"] == "dashboard-params-flow"
    assert summary["param_path"] == "counter.increment"
    assert summary["observed_value"] == 2
    assert summary["counter_event_increment"] == 2


def test_evidence_helper_builds_invalid_param_summary(tmp_path: Path) -> None:
    operation_log = tmp_path / "operation-log.jsonl"
    operation_log.write_text(
        json.dumps({"seq": 1, "type": "ui", "target": "world-params-error", "action": "read"})
        + "\n"
    )

    summary = build_api_summary_from_state(
        scenario="dashboard-invalid-param",
        baseline={
            "health_status": "ok",
            "runtime": {"tick_id": 4},
            "world_params": {"counter": {"increment": {"value": 1, "type": "number"}}},
        },
        health={"status": "ok"},
        runtime={"tick_id": 4},
        params={"counter": {"increment": {"value": 1, "type": "number"}}},
        events=[],
        operation_log_path=operation_log,
    )

    assert summary["scenario"] == "dashboard-invalid-param"
    assert summary["invalid_path"] == "system.secret"
    assert summary["params_unchanged"] is True
    assert summary["ui_error_seen"] is True


def test_agent_verdict_fixture_fails() -> None:
    errors = validate_result_dir(FIXTURES_DIR / "invalid-agent-verdict")

    assert any("verdict_source" in error for error in errors)


def test_missing_required_artifact_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "missing-console-log"
    shutil.copytree(FIXTURES_DIR / "valid-basic-runtime", result_dir)
    (result_dir / "console.log").unlink()

    errors = validate_result_dir(result_dir)

    assert any("console.log" in error for error in errors)


def test_empty_commands_fail(tmp_path: Path) -> None:
    result_dir = tmp_path / "empty-commands"
    shutil.copytree(FIXTURES_DIR / "valid-basic-runtime", result_dir)
    result_json = result_dir / "result.json"
    result_json.write_text(
        result_json.read_text().replace(
            '"commands": [',
            '"commands": [], "commands_original": [',
        )
    )

    errors = validate_result_dir(result_dir)

    assert any("commands" in error for error in errors)


def test_non_zero_command_exit_code_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "failed-command"
    shutil.copytree(FIXTURES_DIR / "valid-basic-runtime", result_dir)
    result_json = result_dir / "result.json"
    result = json.loads(result_json.read_text())
    result["commands"][0]["exit_code"] = 1
    result_json.write_text(json.dumps(result, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("commands[0].exit_code must be 0" in error for error in errors)


def test_empty_assertions_fail(tmp_path: Path) -> None:
    result_dir = tmp_path / "empty-assertions"
    shutil.copytree(FIXTURES_DIR / "valid-basic-runtime", result_dir)
    result_json = result_dir / "result.json"
    result_json.write_text(
        result_json.read_text().replace(
            '"assertions": [',
            '"assertions": [], "assertions_original": [',
        )
    )

    errors = validate_result_dir(result_dir)

    assert any("assertions" in error for error in errors)


def test_unsupported_scenario_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "unsupported-scenario"
    shutil.copytree(FIXTURES_DIR / "valid-basic-runtime", result_dir)
    result_json = result_dir / "result.json"
    result = json.loads(result_json.read_text())
    result["scenario"] = "dashboard-archive-summary"
    result_json.write_text(json.dumps(result, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("supported scenarios" in error and "dashboard-basic-runtime" in error for error in errors)


def test_missing_required_ui_target_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "missing-ui-target"
    shutil.copytree(FIXTURES_DIR / "valid-params-flow", result_dir)
    operation_log = result_dir / "operation-log.jsonl"
    operations = [
        json.loads(line)
        for line in operation_log.read_text().splitlines()
        if "runtime-step-button" not in line
    ]
    operation_log.write_text("\n".join(json.dumps(operation) for operation in operations) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("runtime-step-button" in error for error in errors)


def test_result_and_api_summary_scenario_mismatch_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "scenario-mismatch"
    shutil.copytree(FIXTURES_DIR / "valid-params-flow", result_dir)
    api_summary_path = result_dir / "api-summary.json"
    api_summary = json.loads(api_summary_path.read_text())
    api_summary["scenario"] = "dashboard-basic-runtime"
    api_summary_path.write_text(json.dumps(api_summary, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("scenario must match" in error for error in errors)


def test_missing_checker_evidence_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "missing-checker-evidence"
    shutil.copytree(FIXTURES_DIR / "valid-params-flow", result_dir)
    api_summary_path = result_dir / "api-summary.json"
    api_summary = json.loads(api_summary_path.read_text())
    api_summary.pop("counter_event_increment")
    api_summary_path.write_text(json.dumps(api_summary, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("counter_event_increment" in error for error in errors)


def test_incorrect_params_flow_evidence_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "incorrect-params-flow"
    shutil.copytree(FIXTURES_DIR / "valid-params-flow", result_dir)
    api_summary_path = result_dir / "api-summary.json"
    api_summary = json.loads(api_summary_path.read_text())
    api_summary["observed_value"] = 3
    api_summary["counter_event_increment"] = 3
    api_summary_path.write_text(json.dumps(api_summary, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("observed_value" in error for error in errors)
    assert any("counter_event_increment" in error for error in errors)


def test_incorrect_invalid_param_unchanged_evidence_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "incorrect-invalid-param"
    shutil.copytree(FIXTURES_DIR / "valid-invalid-param", result_dir)
    api_summary_path = result_dir / "api-summary.json"
    api_summary = json.loads(api_summary_path.read_text())
    api_summary["params_unchanged"] = False
    api_summary["after_params"] = {"system": {"secret": {"value": "blocked", "type": "string"}}}
    api_summary_path.write_text(json.dumps(api_summary, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("params_unchanged" in error for error in errors)


def test_assertion_without_evidence_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "missing-evidence"
    shutil.copytree(FIXTURES_DIR / "valid-basic-runtime", result_dir)
    result_json = result_dir / "result.json"
    result_json.write_text(
        result_json.read_text().replace(
            '"evidence": {',
            '"evidence_missing": {',
            1,
        )
    )

    errors = validate_result_dir(result_dir)

    assert any("evidence" in error for error in errors)


def test_missing_operation_log_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "missing-operation-log"
    shutil.copytree(FIXTURES_DIR / "valid-basic-runtime", result_dir)
    result_json = result_dir / "result.json"
    result = json.loads(result_json.read_text())
    result["artifacts"]["operation_log"] = "operation-log.jsonl"
    result_json.write_text(json.dumps(result, indent=2) + "\n")
    (result_dir / "operation-log.jsonl").unlink()

    errors = validate_result_dir(result_dir)

    assert any("operation_log" in error or "operation-log.jsonl" in error for error in errors)


def test_empty_operation_log_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "empty-operation-log"
    shutil.copytree(FIXTURES_DIR / "valid-basic-runtime", result_dir)
    (result_dir / "operation-log.jsonl").write_text("")

    errors = validate_result_dir(result_dir)

    assert any("operation-log.jsonl" in error and "at least one" in error for error in errors)


def test_operation_log_rejects_direct_api_operations(tmp_path: Path) -> None:
    result_dir = tmp_path / "api-operation"
    shutil.copytree(FIXTURES_DIR / "valid-basic-runtime", result_dir)
    result_json = result_dir / "result.json"
    result = json.loads(result_json.read_text())
    result["artifacts"]["operation_log"] = "operation-log.jsonl"
    result_json.write_text(json.dumps(result, indent=2) + "\n")
    (result_dir / "operation-log.jsonl").write_text(
        json.dumps(
            {
                "seq": 1,
                "type": "api",
                "method": "GET",
                "target": "/runtime/state",
                "summary": "Direct API reads are not allowed as agent operations.",
            }
        )
        + "\n"
    )

    errors = validate_result_dir(result_dir)

    assert any("direct API" in error or "type must be ui or cli" in error for error in errors)


def test_operation_log_non_zero_cli_exit_code_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "failed-cli-operation"
    shutil.copytree(FIXTURES_DIR / "valid-basic-runtime", result_dir)
    operation_log = result_dir / "operation-log.jsonl"
    operations = [json.loads(line) for line in operation_log.read_text().splitlines()]
    operations[0]["exit_code"] = 1
    operation_log.write_text("\n".join(json.dumps(operation) for operation in operations) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("operation-log.jsonl line 1.exit_code must be 0" in error for error in errors)


def test_absolute_artifact_path_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "absolute-artifact"
    shutil.copytree(FIXTURES_DIR / "valid-basic-runtime", result_dir)
    result_json = result_dir / "result.json"
    result = json.loads(result_json.read_text())
    result["artifacts"]["console_log"] = str(result_dir / "console.log")
    result_json.write_text(json.dumps(result, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("console_log must stay inside result directory" in error for error in errors)


def test_parent_directory_artifact_path_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "parent-artifact"
    shutil.copytree(FIXTURES_DIR / "valid-basic-runtime", result_dir)
    result_json = result_dir / "result.json"
    result = json.loads(result_json.read_text())
    result["artifacts"]["console_log"] = "../console.log"
    result_json.write_text(json.dumps(result, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("console_log must stay inside result directory" in error for error in errors)
