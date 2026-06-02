from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


REQUIRED_KEYS = {
    "report_id",
    "engine_reference",
    "public_contract_surface",
    "external_suite_id",
    "redacted_target_id",
    "capability_area",
    "scenario_id",
    "high_level_goal",
    "status",
    "observed_public_behavior",
    "redacted_evidence_summary",
    "compatibility_notes",
    "unresolved_findings",
    "redaction_confirmed",
    "forbidden_detail_review",
    "scope_review",
}
REQUIRED_TEXT_KEYS = {
    "report_id",
    "engine_reference",
    "public_contract_surface",
    "external_suite_id",
    "redacted_target_id",
    "capability_area",
    "scenario_id",
    "high_level_goal",
    "observed_public_behavior",
    "redacted_evidence_summary",
    "compatibility_notes",
}
ALLOWED_STATUSES = {"pass", "fail", "blocked", "skipped", "out_of_scope"}
NON_PASS_STATUSES_REQUIRING_REASON = {"fail", "blocked", "skipped", "out_of_scope"}
FORBIDDEN_DETAIL_KEYS = {
    "concrete_external_world_name",
    "character_name",
    "location_name",
    "story_rule",
    "seed_data",
    "private_transcript",
    "ui_selector",
    "hidden_reset_api_detail",
    "private_fixture_path",
    "validation_oracle_internal",
    "non_redacted_external_event_payload",
}
SCOPE_REVIEW_KEYS = {
    "public_contract_exercised",
    "core_repository_behavior_affected",
    "external_consumer_detail_redacted",
    "follow_up_required_in_worldengine_core",
}
ALLOWED_FINDING_SEVERITIES = {"P1", "P2", "P3"}
RESOLVED_FINDING_STATUSES = {"accepted", "resolved"}

REDACTION_RISK_PATTERNS = {
    "SENTINEL_PRIVATE_PATH": "synthetic private path marker",
    "SENTINEL_UI_SELECTOR": "synthetic UI selector marker",
    "SENTINEL_HIDDEN_RESET_API": "synthetic hidden reset API marker",
    "SENTINEL_ORACLE_INTERNAL": "synthetic validation oracle marker",
    "SENTINEL_SEED_DATA": "synthetic seed data marker",
    "SENTINEL_PRIVATE_TRANSCRIPT": "synthetic private transcript marker",
    "SENTINEL_EXTERNAL_EVENT_PAYLOAD": "synthetic external event payload marker",
}
PRIVATE_PATH_RE = re.compile(r"(/Users/|/home/|file:///).*(fixture|private|oracle|validation)", re.IGNORECASE)


def _load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text())
    except FileNotFoundError:
        errors.append(f"Missing report file: {path}")
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON in {path}: {exc}")
    return None


def _is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _iter_strings(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        strings: list[str] = []
        for item in value.values():
            strings.extend(_iter_strings(item))
        return strings
    if isinstance(value, list):
        strings = []
        for item in value:
            strings.extend(_iter_strings(item))
        return strings
    return []


def _validate_required_fields(report: dict[str, Any], errors: list[str]) -> None:
    missing_keys = sorted(REQUIRED_KEYS - set(report))
    if missing_keys:
        errors.append(f"report missing required keys: {', '.join(missing_keys)}")

    for key in sorted(REQUIRED_TEXT_KEYS):
        if key in report and not _is_non_empty_string(report.get(key)):
            errors.append(f"{key} must be a non-empty string")


def _validate_status(report: dict[str, Any], errors: list[str]) -> None:
    status = report.get("status")
    if status not in ALLOWED_STATUSES:
        allowed = ", ".join(sorted(ALLOWED_STATUSES))
        errors.append(f"status must be one of: {allowed}")
        return

    if status in NON_PASS_STATUSES_REQUIRING_REASON and not _is_non_empty_string(report.get("status_reason")):
        errors.append(f"status_reason is required when status is {status}")


def _validate_redaction(report: dict[str, Any], errors: list[str]) -> None:
    if report.get("redaction_confirmed") is not True:
        errors.append("redaction_confirmed must be true")

    review = report.get("forbidden_detail_review")
    if not isinstance(review, dict):
        errors.append("forbidden_detail_review must be an object")
        return

    missing_keys = sorted(FORBIDDEN_DETAIL_KEYS - set(review))
    if missing_keys:
        errors.append(f"forbidden_detail_review missing required keys: {', '.join(missing_keys)}")

    for key in sorted(FORBIDDEN_DETAIL_KEYS & set(review)):
        value = review.get(key)
        if not isinstance(value, bool):
            errors.append(f"forbidden_detail_review.{key} must be a boolean")
        elif value is not False:
            errors.append(f"forbidden_detail_review.{key} must be false for a redacted report")


def _validate_findings(report: dict[str, Any], errors: list[str]) -> None:
    findings = report.get("unresolved_findings")
    if not isinstance(findings, list):
        errors.append("unresolved_findings must be a list")
        return

    for index, finding in enumerate(findings):
        if not isinstance(finding, dict):
            errors.append(f"unresolved_findings[{index}] must be an object")
            continue

        severity = finding.get("severity")
        if severity not in ALLOWED_FINDING_SEVERITIES:
            errors.append(f"unresolved_findings[{index}].severity must be P1, P2, or P3")
        if not _is_non_empty_string(finding.get("summary")):
            errors.append(f"unresolved_findings[{index}].summary must be a non-empty string")

        status = finding.get("status")
        if not _is_non_empty_string(status):
            errors.append(f"unresolved_findings[{index}].status must be a non-empty string")

        if report.get("status") == "pass" and severity in {"P1", "P2"} and status not in RESOLVED_FINDING_STATUSES:
            errors.append(f"pass report cannot contain unresolved {severity} finding at unresolved_findings[{index}]")


def _validate_scope_review(report: dict[str, Any], errors: list[str]) -> None:
    scope_review = report.get("scope_review")
    if not isinstance(scope_review, dict):
        errors.append("scope_review must be an object")
        return

    missing_keys = sorted(SCOPE_REVIEW_KEYS - set(scope_review))
    if missing_keys:
        errors.append(f"scope_review missing required keys: {', '.join(missing_keys)}")

    if not _is_non_empty_string(scope_review.get("public_contract_exercised")):
        errors.append("scope_review.public_contract_exercised must be a non-empty string")

    for key in sorted(SCOPE_REVIEW_KEYS - {"public_contract_exercised"}):
        if key in scope_review and not isinstance(scope_review.get(key), bool):
            errors.append(f"scope_review.{key} must be a boolean")

    if scope_review.get("external_consumer_detail_redacted") is not True:
        errors.append("scope_review.external_consumer_detail_redacted must be true")

    if scope_review.get("follow_up_required_in_worldengine_core") is True and not _is_non_empty_string(
        scope_review.get("follow_up_summary")
    ):
        errors.append("scope_review.follow_up_summary is required when core follow-up is required")


def _validate_status_semantics(report: dict[str, Any], errors: list[str]) -> None:
    if report.get("status") != "pass":
        return

    if not _is_non_empty_string(report.get("observed_public_behavior")):
        errors.append("pass report requires observed_public_behavior")
    if not _is_non_empty_string(report.get("redacted_evidence_summary")):
        errors.append("pass report requires redacted_evidence_summary")


def _scan_for_redaction_risks(report: dict[str, Any], errors: list[str]) -> None:
    for value in _iter_strings(report):
        for pattern, description in REDACTION_RISK_PATTERNS.items():
            if pattern in value:
                errors.append(f"report contains forbidden leaked detail marker: {description}")
        if PRIVATE_PATH_RE.search(value):
            errors.append("report contains a private path-like leaked detail")


def validate_report(report: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(report, dict):
        return ["report must be a JSON object"]

    _validate_required_fields(report, errors)
    _validate_status(report, errors)
    _validate_redaction(report, errors)
    _validate_findings(report, errors)
    _validate_scope_review(report, errors)
    _validate_status_semantics(report, errors)
    _scan_for_redaction_risks(report, errors)
    return errors


def validate_report_file(path: Path | str) -> list[str]:
    errors: list[str] = []
    report = _load_json(Path(path), errors)
    if errors:
        return errors
    return validate_report(report)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate_external_validation_report.py REPORT_JSON", file=sys.stderr)
        return 2

    errors = validate_report_file(argv[1])
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(f"PASS: validated external validation report at {argv[1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
