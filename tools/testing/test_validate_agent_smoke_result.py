from __future__ import annotations

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
