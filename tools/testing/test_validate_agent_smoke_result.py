from __future__ import annotations

import json
import shutil
from pathlib import Path

from tools.testing.validate_agent_smoke_result import validate_result_dir


FIXTURES_DIR = Path(__file__).parent / "fixtures" / "agent-smoke"


def test_valid_basic_runtime_fixture_passes() -> None:
    errors = validate_result_dir(FIXTURES_DIR / "valid-basic-runtime")

    assert errors == []


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
