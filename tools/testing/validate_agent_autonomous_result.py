from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_KEYS = {
    "scenario",
    "goal",
    "mode",
    "status",
    "verdict_source",
    "score_items",
    "required_artifacts",
    "artifacts",
    "operation_log",
    "unverified_items",
    "failures",
}
SUPPORTED_SCENARIOS = {
    "autonomous-dashboard-basic-runtime",
    "autonomous-dashboard-params-flow",
    "autonomous-dashboard-invalid-param",
    "autonomous-dashboard-agent-autotune",
    "autonomous-dashboard-timeline-investigation",
}
ALLOWED_VERDICT_SOURCES = {"scorecard_checker", "deterministic_checker"}
REQUIRED_UI_TARGETS = {
    "autonomous-dashboard-basic-runtime": {
        "dashboard",
        "runtime-tick-id",
        "runtime-step-button",
    },
    "autonomous-dashboard-params-flow": {
        "dashboard",
        "world-params-path-input",
        "world-params-type-select",
        "world-params-value-input",
        "world-params-apply-button",
        "runtime-step-button",
    },
    "autonomous-dashboard-invalid-param": {
        "dashboard",
        "world-params-path-input",
        "world-params-value-input",
        "world-params-apply-button",
        "world-params-error",
    },
    "autonomous-dashboard-agent-autotune": {
        "dashboard",
        "world-agent-goal-input",
        "world-agent-autotune-button",
        "world-agent-success",
        "world-agent-patches",
    },
    "autonomous-dashboard-timeline-investigation": {
        "dashboard",
        "runtime-step-button",
        "timeline-panel",
        "timeline-row",
        "timeline-row-expand",
    },
}


def _load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text())
    except FileNotFoundError:
        errors.append(f"Missing required file: {path.name}")
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON in {path.name}: {exc}")
    return None


def _validate_relative_artifact_path(
    result_dir: Path,
    artifact_name: str,
    relative_path: Any,
    errors: list[str],
) -> None:
    if not isinstance(relative_path, str) or not relative_path.strip():
        errors.append(f"Artifact {artifact_name} must be a non-empty relative path")
        return

    raw_path = Path(relative_path)
    if raw_path.is_absolute() or ".." in raw_path.parts:
        errors.append(f"Artifact {artifact_name} must stay inside result directory: {relative_path}")
        return

    path = result_dir / relative_path
    if not path.exists():
        errors.append(f"Missing required artifact {artifact_name}: {relative_path}")
        return
    if path.is_file() and path.stat().st_size == 0:
        errors.append(f"Artifact {artifact_name} is empty: {relative_path}")


def _validate_artifacts(result_dir: Path, result: dict[str, Any], errors: list[str]) -> None:
    artifacts = result.get("artifacts")
    required_artifacts = result.get("required_artifacts")
    if not isinstance(artifacts, dict):
        errors.append("artifacts must be an object")
        return
    if not isinstance(required_artifacts, list) or not required_artifacts:
        errors.append("required_artifacts must be a non-empty list")
        return

    for artifact_name in required_artifacts:
        if not isinstance(artifact_name, str) or not artifact_name.strip():
            errors.append("required_artifacts entries must be non-empty strings")
            continue
        if artifact_name == "screenshots":
            screenshots = artifacts.get("screenshots")
            if not isinstance(screenshots, list) or not screenshots:
                errors.append("artifacts.screenshots must contain at least one path")
                continue
            for index, screenshot in enumerate(screenshots):
                _validate_relative_artifact_path(result_dir, f"screenshots[{index}]", screenshot, errors)
            continue
        _validate_relative_artifact_path(result_dir, artifact_name, artifacts.get(artifact_name), errors)

    operation_log = result.get("operation_log")
    artifacts_operation_log = artifacts.get("operation_log")
    if operation_log != artifacts_operation_log:
        errors.append("operation_log must match artifacts.operation_log")


def _validate_operation_log(result_dir: Path, result: dict[str, Any], errors: list[str]) -> set[str]:
    operation_log = result.get("operation_log")
    if not isinstance(operation_log, str) or not operation_log.strip():
        errors.append("operation_log must be a non-empty relative path")
        return set()

    path = result_dir / operation_log
    try:
        lines = path.read_text().splitlines()
    except FileNotFoundError:
        return set()

    non_empty_lines = [line for line in lines if line.strip()]
    if not non_empty_lines:
        errors.append("operation-log.jsonl must contain at least one operation record")
        return set()

    ui_targets: set[str] = set()
    previous_seq = 0
    for index, line in enumerate(non_empty_lines, start=1):
        try:
            operation = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"operation-log.jsonl line {index} must be valid JSON: {exc}")
            continue
        if not isinstance(operation, dict):
            errors.append(f"operation-log.jsonl line {index} must be an object")
            continue

        seq = operation.get("seq")
        if not isinstance(seq, int):
            errors.append(f"operation-log.jsonl line {index}.seq must be an integer")
        elif seq <= previous_seq:
            errors.append(f"operation-log.jsonl line {index}.seq must increase")
        else:
            previous_seq = seq

        operation_type = operation.get("type")
        if operation_type not in {"ui", "cli"}:
            errors.append(
                f"operation-log.jsonl line {index} type must be ui or cli; "
                "direct API operations are not allowed"
            )
            continue

        if operation_type == "ui":
            target = operation.get("target")
            if not isinstance(target, str) or not target.strip():
                errors.append(f"operation-log.jsonl line {index}.target must be a non-empty string")
            else:
                ui_targets.add(target)
            if not isinstance(operation.get("action"), str) or not operation["action"].strip():
                errors.append(f"operation-log.jsonl line {index}.action must be a non-empty string")

        if operation_type == "cli":
            if not isinstance(operation.get("command"), str) or not operation["command"].strip():
                errors.append(f"operation-log.jsonl line {index}.command must be a non-empty string")
            exit_code = operation.get("exit_code")
            if not isinstance(exit_code, int):
                errors.append(f"operation-log.jsonl line {index}.exit_code must be an integer")
            elif exit_code != 0:
                errors.append(f"operation-log.jsonl line {index}.exit_code must be 0")

    return ui_targets


def _validate_required_ui_targets(result: dict[str, Any], ui_targets: set[str], errors: list[str]) -> None:
    scenario = result.get("scenario")
    if scenario not in REQUIRED_UI_TARGETS:
        return
    missing = sorted(REQUIRED_UI_TARGETS[scenario] - ui_targets)
    if missing:
        errors.append(f"operation-log.jsonl missing required UI target(s) for {scenario}: {', '.join(missing)}")


def _validate_score_items(result: dict[str, Any], errors: list[str]) -> None:
    score_items = result.get("score_items")
    if not isinstance(score_items, list) or not score_items:
        errors.append("score_items must contain at least one item")
        return

    for index, item in enumerate(score_items):
        if not isinstance(item, dict):
            errors.append(f"score_items[{index}] must be an object")
            continue
        if not isinstance(item.get("name"), str) or not item["name"].strip():
            errors.append(f"score_items[{index}].name must be a non-empty string")
        if item.get("status") != "pass":
            errors.append(f"score_items[{index}].status must be pass")
        evidence = item.get("evidence")
        if evidence is None or evidence == "" or evidence == [] or evidence == {}:
            errors.append(f"score_items[{index}].evidence is required")


def _validate_unverified_items(result: dict[str, Any], errors: list[str]) -> None:
    unverified_items = result.get("unverified_items")
    if not isinstance(unverified_items, list):
        errors.append("unverified_items must be a list")
        return

    for index, item in enumerate(unverified_items):
        if not isinstance(item, dict):
            errors.append(f"unverified_items[{index}] must be an object")
            continue
        severity = item.get("severity")
        status = item.get("status")
        resolved = item.get("resolved")
        if severity == "P1" and status not in {"resolved", "accepted"} and resolved is not True:
            errors.append(f"unverified_items[{index}] contains unresolved P1 item")


def _validate_scorecard_summary(result_dir: Path, result: dict[str, Any], errors: list[str]) -> None:
    artifacts = result.get("artifacts")
    if not isinstance(artifacts, dict):
        return
    summary_path = artifacts.get("scorecard_summary")
    if not isinstance(summary_path, str) or not summary_path.strip():
        errors.append("artifacts.scorecard_summary is required")
        return

    summary = _load_json(result_dir / summary_path, errors)
    if not isinstance(summary, dict):
        errors.append("scorecard-summary.json must contain an object")
        return
    if summary.get("scenario") != result.get("scenario"):
        errors.append("scorecard-summary.json scenario must match result.json scenario")
    if summary.get("status") != "pass":
        errors.append("scorecard-summary.json status must be pass")
    if summary.get("verdict_source") not in ALLOWED_VERDICT_SOURCES:
        errors.append("scorecard-summary.json verdict_source is invalid")


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

    scenario = raw_result.get("scenario")
    if scenario not in SUPPORTED_SCENARIOS:
        supported = ", ".join(sorted(SUPPORTED_SCENARIOS))
        errors.append(f"scenario must be one of supported scenarios: {supported}")
    if raw_result.get("status") != "pass":
        errors.append("status must be pass for a successful autonomous result")
    verdict_source = raw_result.get("verdict_source")
    if verdict_source not in ALLOWED_VERDICT_SOURCES:
        errors.append(
            "verdict_source must be deterministic_checker or scorecard_checker, "
            f"not {verdict_source}"
        )
    if not isinstance(raw_result.get("goal"), str) or not raw_result["goal"].strip():
        errors.append("goal must be a non-empty string")
    if not isinstance(raw_result.get("mode"), str) or not raw_result["mode"].strip():
        errors.append("mode must be a non-empty string")
    if not isinstance(raw_result.get("failures"), list):
        errors.append("failures must be a list")
    elif raw_result["failures"]:
        errors.append("failures must be empty when status is pass")

    _validate_artifacts(result_dir, raw_result, errors)
    ui_targets = _validate_operation_log(result_dir, raw_result, errors)
    _validate_required_ui_targets(raw_result, ui_targets, errors)
    _validate_score_items(raw_result, errors)
    _validate_unverified_items(raw_result, errors)
    _validate_scorecard_summary(result_dir, raw_result, errors)

    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate_agent_autonomous_result.py RESULT_DIR", file=sys.stderr)
        return 2

    errors = validate_result_dir(argv[1])
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(f"PASS: validated agent autonomous result at {argv[1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
