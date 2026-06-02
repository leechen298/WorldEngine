from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from tools.testing.validate_external_validation_report import validate_report, validate_report_file


def _report(status: str = "pass") -> dict[str, object]:
    report: dict[str, object] = {
        "report_id": "external-report-001",
        "engine_reference": "commit-redacted-001",
        "public_contract_surface": "docs/contracts/external-validation-readiness-contract.md",
        "external_suite_id": "external-suite-001",
        "redacted_target_id": "target-redacted-001",
        "capability_area": "contract-surface-001",
        "scenario_id": "scenario-001",
        "high_level_goal": "Validate public behavior through a redacted contract surface.",
        "status": status,
        "observed_public_behavior": "The public contract surface responded as described.",
        "redacted_evidence_summary": "Only abstract identifiers and public behavior are retained.",
        "compatibility_notes": "No runtime, API, frontend, or persistence behavior changed.",
        "unresolved_findings": [],
        "redaction_confirmed": True,
        "forbidden_detail_review": {
            "concrete_external_world_name": False,
            "character_name": False,
            "location_name": False,
            "story_rule": False,
            "seed_data": False,
            "private_transcript": False,
            "ui_selector": False,
            "hidden_reset_api_detail": False,
            "private_fixture_path": False,
            "validation_oracle_internal": False,
            "non_redacted_external_event_payload": False,
        },
        "scope_review": {
            "public_contract_exercised": "external-validation-readiness-contract",
            "core_repository_behavior_affected": False,
            "external_consumer_detail_redacted": True,
            "follow_up_required_in_worldengine_core": False,
        },
    }
    if status != "pass":
        report["status_reason"] = f"{status} is recorded with an explicit non-pass reason."
    return report


def _write_report(tmp_path: Path, report: dict[str, object]) -> Path:
    path = tmp_path / "report.json"
    path.write_text(json.dumps(report, indent=2) + "\n")
    return path


def test_valid_pass_report_passes() -> None:
    assert validate_report(_report()) == []


def test_missing_required_field_fails() -> None:
    report = _report()
    report.pop("report_id")

    errors = validate_report(report)

    assert any("missing required keys" in error and "report_id" in error for error in errors)


def test_unsupported_status_fails() -> None:
    report = _report("unknown")

    errors = validate_report(report)

    assert any("status must be one of" in error for error in errors)


def test_redaction_confirmation_required() -> None:
    report = _report()
    report["redaction_confirmed"] = False

    errors = validate_report(report)

    assert any("redaction_confirmed must be true" in error for error in errors)


def test_pass_report_rejects_unresolved_p1_or_p2() -> None:
    report = _report()
    report["unresolved_findings"] = [
        {"severity": "P2", "summary": "Needs current-session evidence.", "status": "open"}
    ]

    errors = validate_report(report)

    assert any("pass report cannot contain unresolved P2" in error for error in errors)


def test_pass_report_rejects_deferred_p1_or_p2() -> None:
    report = _report()
    report["unresolved_findings"] = [
        {"severity": "P2", "summary": "Deferred evidence cannot support pass.", "status": "deferred"}
    ]

    errors = validate_report(report)

    assert any("pass report cannot contain unresolved P2" in error for error in errors)


def test_blocked_requires_reason() -> None:
    report = _report("blocked")
    report.pop("status_reason")

    errors = validate_report(report)

    assert any("status_reason is required when status is blocked" in error for error in errors)


def test_non_pass_statuses_pass_when_reasoned_and_redacted() -> None:
    for status in ["fail", "blocked", "skipped", "out_of_scope"]:
        assert validate_report(_report(status)) == []


def test_forbidden_detail_review_flag_fails() -> None:
    report = _report()
    forbidden_detail_review = report["forbidden_detail_review"]
    assert isinstance(forbidden_detail_review, dict)
    forbidden_detail_review["ui_selector"] = True

    errors = validate_report(report)

    assert any("forbidden_detail_review.ui_selector must be false" in error for error in errors)


def test_scope_review_requires_redaction_confirmation() -> None:
    report = _report()
    scope_review = report["scope_review"]
    assert isinstance(scope_review, dict)
    scope_review["external_consumer_detail_redacted"] = False

    errors = validate_report(report)

    assert any("scope_review.external_consumer_detail_redacted must be true" in error for error in errors)


def test_follow_up_summary_required_when_core_follow_up_is_required() -> None:
    report = _report()
    scope_review = report["scope_review"]
    assert isinstance(scope_review, dict)
    scope_review["follow_up_required_in_worldengine_core"] = True

    errors = validate_report(report)

    assert any("follow_up_summary is required" in error for error in errors)


def test_synthetic_private_path_marker_fails() -> None:
    report = _report()
    report["redacted_evidence_summary"] = "Synthetic leak marker: SENTINEL_PRIVATE_PATH."

    errors = validate_report(report)

    assert any("synthetic private path marker" in error for error in errors)


def test_synthetic_ui_selector_marker_fails() -> None:
    report = _report()
    report["redacted_evidence_summary"] = "Synthetic leak marker: SENTINEL_UI_SELECTOR."

    errors = validate_report(report)

    assert any("synthetic UI selector marker" in error for error in errors)


def test_synthetic_hidden_reset_marker_fails() -> None:
    report = _report()
    report["redacted_evidence_summary"] = "Synthetic leak marker: SENTINEL_HIDDEN_RESET_API."

    errors = validate_report(report)

    assert any("synthetic hidden reset API marker" in error for error in errors)


def test_synthetic_oracle_marker_fails() -> None:
    report = _report()
    report["redacted_evidence_summary"] = "Synthetic leak marker: SENTINEL_ORACLE_INTERNAL."

    errors = validate_report(report)

    assert any("synthetic validation oracle marker" in error for error in errors)


def test_synthetic_seed_marker_fails() -> None:
    report = _report()
    report["redacted_evidence_summary"] = "Synthetic leak marker: SENTINEL_SEED_DATA."

    errors = validate_report(report)

    assert any("synthetic seed data marker" in error for error in errors)


def test_synthetic_transcript_marker_fails() -> None:
    report = _report()
    report["redacted_evidence_summary"] = "Synthetic leak marker: SENTINEL_PRIVATE_TRANSCRIPT."

    errors = validate_report(report)

    assert any("synthetic private transcript marker" in error for error in errors)


def test_synthetic_event_payload_marker_fails() -> None:
    report = _report()
    report["redacted_evidence_summary"] = "Synthetic leak marker: SENTINEL_EXTERNAL_EVENT_PAYLOAD."

    errors = validate_report(report)

    assert any("synthetic external event payload marker" in error for error in errors)


def test_validate_report_file_passes(tmp_path: Path) -> None:
    path = _write_report(tmp_path, _report())

    assert validate_report_file(path) == []


def test_cli_returns_zero_for_valid_report(tmp_path: Path) -> None:
    path = _write_report(tmp_path, _report())

    result = subprocess.run(
        [sys.executable, "tools/testing/validate_external_validation_report.py", str(path)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "PASS: validated external validation report" in result.stdout


def test_cli_returns_one_for_invalid_report(tmp_path: Path) -> None:
    report = _report()
    report["redaction_confirmed"] = False
    path = _write_report(tmp_path, report)

    result = subprocess.run(
        [sys.executable, "tools/testing/validate_external_validation_report.py", str(path)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1
    assert "FAIL: redaction_confirmed must be true" in result.stderr
