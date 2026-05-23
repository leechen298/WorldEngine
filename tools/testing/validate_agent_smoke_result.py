from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_KEYS = {
    "scenario",
    "status",
    "verdict_source",
    "agent_summary",
    "commands",
    "artifacts",
    "assertions",
    "failures",
}


def _load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text())
    except FileNotFoundError:
        errors.append(f"Missing required file: {path.name}")
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON in {path.name}: {exc}")
    return None


def _is_non_empty_evidence(value: Any) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return bool(value)
    if isinstance(value, dict):
        return bool(value)
    return value is not None


def _validate_artifact_path(result_dir: Path, artifact_name: str, relative_path: Any, errors: list[str]) -> None:
    if not isinstance(relative_path, str) or not relative_path.strip():
        errors.append(f"Artifact {artifact_name} must be a non-empty relative path")
        return

    path = result_dir / relative_path
    if not path.exists():
        errors.append(f"Missing required artifact {artifact_name}: {relative_path}")
        return
    if path.is_file() and path.stat().st_size == 0:
        errors.append(f"Artifact {artifact_name} is empty: {relative_path}")


def _validate_artifacts(result_dir: Path, result: dict[str, Any], errors: list[str]) -> None:
    artifacts = result.get("artifacts")
    if not isinstance(artifacts, dict):
        errors.append("artifacts must be an object")
        return

    _validate_artifact_path(result_dir, "transcript", artifacts.get("transcript"), errors)
    _validate_artifact_path(result_dir, "console_log", artifacts.get("console_log"), errors)
    _validate_artifact_path(result_dir, "api_summary", artifacts.get("api_summary"), errors)

    screenshots = artifacts.get("screenshots")
    if not isinstance(screenshots, list) or not screenshots:
        errors.append("artifacts.screenshots must contain at least one path")
        return

    for index, screenshot in enumerate(screenshots):
        _validate_artifact_path(result_dir, f"screenshots[{index}]", screenshot, errors)


def _validate_commands(result: dict[str, Any], errors: list[str]) -> None:
    commands = result.get("commands")
    if not isinstance(commands, list) or not commands:
        errors.append("commands must contain at least one command record")
        return

    for index, command in enumerate(commands):
        if not isinstance(command, dict):
            errors.append(f"commands[{index}] must be an object")
            continue
        if not isinstance(command.get("command"), str) or not command["command"].strip():
            errors.append(f"commands[{index}].command must be a non-empty string")
        if not isinstance(command.get("exit_code"), int):
            errors.append(f"commands[{index}].exit_code must be an integer")


def _validate_assertions(result: dict[str, Any], errors: list[str]) -> None:
    assertions = result.get("assertions")
    if not isinstance(assertions, list) or not assertions:
        errors.append("assertions must contain at least one assertion")
        return

    for index, assertion in enumerate(assertions):
        if not isinstance(assertion, dict):
            errors.append(f"assertions[{index}] must be an object")
            continue
        if not isinstance(assertion.get("name"), str) or not assertion["name"].strip():
            errors.append(f"assertions[{index}].name must be a non-empty string")
        if assertion.get("status") != "pass":
            errors.append(f"assertions[{index}].status must be pass")
        if not _is_non_empty_evidence(assertion.get("evidence")):
            errors.append(f"assertions[{index}].evidence is required")


def _validate_api_summary(result_dir: Path, result: dict[str, Any], errors: list[str]) -> None:
    artifacts = result.get("artifacts")
    if not isinstance(artifacts, dict):
        return
    api_summary_path = artifacts.get("api_summary")
    if not isinstance(api_summary_path, str) or not api_summary_path.strip():
        return

    api_summary = _load_json(result_dir / api_summary_path, errors)
    if not isinstance(api_summary, dict):
        errors.append("api-summary.json must contain an object")
        return

    if result.get("scenario") != "dashboard-basic-runtime":
        return

    if api_summary.get("health_status") != "ok":
        errors.append("api-summary.json health_status must be ok")

    before_tick = api_summary.get("before_tick")
    after_tick = api_summary.get("after_tick")
    if not isinstance(before_tick, int) or not isinstance(after_tick, int):
        errors.append("api-summary.json before_tick and after_tick must be integers")
        return
    if after_tick != before_tick + 1:
        errors.append(
            "api-summary.json must prove after_tick equals before_tick + 1 "
            f"(got {before_tick} -> {after_tick})"
        )


def validate_result_dir(result_dir: Path | str) -> list[str]:
    result_dir = Path(result_dir)
    errors: list[str] = []

    if not result_dir.exists() or not result_dir.is_dir():
        return [f"Result directory does not exist: {result_dir}"]

    raw_result = _load_json(result_dir / "result.json", errors)
    if not isinstance(raw_result, dict):
        errors.append("result.json must contain an object")
        return errors

    missing_keys = sorted(REQUIRED_KEYS - set(raw_result))
    if missing_keys:
        errors.append(f"result.json missing required keys: {', '.join(missing_keys)}")

    if raw_result.get("status") != "pass":
        errors.append("status must be pass for a successful agent smoke result")
    if raw_result.get("verdict_source") != "deterministic_checker":
        errors.append("verdict_source must be deterministic_checker, not agent")
    if not isinstance(raw_result.get("agent_summary"), str) or not raw_result["agent_summary"].strip():
        errors.append("agent_summary must be a non-empty string")
    if not isinstance(raw_result.get("failures"), list):
        errors.append("failures must be a list")
    elif raw_result["failures"]:
        errors.append("failures must be empty when status is pass")

    _validate_commands(raw_result, errors)
    _validate_assertions(raw_result, errors)
    _validate_artifacts(result_dir, raw_result, errors)
    _validate_api_summary(result_dir, raw_result, errors)

    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate_agent_smoke_result.py RESULT_DIR", file=sys.stderr)
        return 2

    errors = validate_result_dir(argv[1])
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(f"PASS: validated agent smoke result at {argv[1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
