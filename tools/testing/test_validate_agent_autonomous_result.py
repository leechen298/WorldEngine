from __future__ import annotations

import json
import shutil
from pathlib import Path

from tools.testing.validate_agent_autonomous_result import validate_result_dir


FIXTURES_DIR = Path(__file__).parent / "fixtures" / "agent-autonomous"


def test_valid_basic_runtime_fixture_passes() -> None:
    assert validate_result_dir(FIXTURES_DIR / "valid-dashboard-basic-runtime") == []


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
