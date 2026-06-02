from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from tools.testing.validate_readiness_manifest import validate_manifest, validate_manifest_file


MANIFEST_PATH = Path("docs/contracts/v0.7-readiness-manifest.json")


def _manifest() -> dict[str, object]:
    return json.loads(MANIFEST_PATH.read_text())


def _write_manifest(tmp_path: Path, manifest: dict[str, object]) -> Path:
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(manifest, indent=2) + "\n")
    return path


def test_manifest_file_passes() -> None:
    assert validate_manifest_file(MANIFEST_PATH) == []


def test_valid_manifest_passes() -> None:
    assert validate_manifest(_manifest()) == []


def test_missing_required_field_fails() -> None:
    manifest = _manifest()
    manifest.pop("manifest_id")

    errors = validate_manifest(manifest)

    assert any("missing required keys" in error and "manifest_id" in error for error in errors)


def test_missing_required_contract_surface_fails() -> None:
    manifest = _manifest()
    contract_surfaces = manifest["contract_surfaces"]
    assert isinstance(contract_surfaces, list)
    manifest["contract_surfaces"] = [
        surface
        for surface in contract_surfaces
        if isinstance(surface, dict)
        and surface.get("path") != "docs/contracts/projection-consumer-contract.md"
    ]

    errors = validate_manifest(manifest)

    assert any("contract_surfaces missing required path" in error for error in errors)


def test_missing_required_schema_surface_fails() -> None:
    manifest = _manifest()
    manifest["schema_surfaces"] = []

    errors = validate_manifest(manifest)

    assert any("schema_surfaces must be a non-empty list" in error for error in errors)


def test_unsupported_readiness_claim_value_fails() -> None:
    manifest = _manifest()
    readiness_claim_values = manifest["readiness_claim_values"]
    assert isinstance(readiness_claim_values, list)
    readiness_claim_values.append("ready")

    errors = validate_manifest(manifest)

    assert any("unsupported value" in error and "ready" in error for error in errors)


def test_pass_like_evidence_status_fails() -> None:
    manifest = _manifest()
    evidence_references = manifest["evidence_references"]
    assert isinstance(evidence_references, list)
    reference = evidence_references[0]
    assert isinstance(reference, dict)
    reference["status"] = "external suite pass"

    errors = validate_manifest(manifest)

    assert any("status is not allowed" in error and "external suite pass" in error for error in errors)


def test_absolute_path_fails() -> None:
    manifest = _manifest()
    contract_surfaces = manifest["contract_surfaces"]
    assert isinstance(contract_surfaces, list)
    surface = contract_surfaces[0]
    assert isinstance(surface, dict)
    surface["path"] = "/SENTINEL_PUBLIC_PATH"

    errors = validate_manifest(manifest)

    assert any("public repository-relative path" in error for error in errors)


def test_parent_traversal_path_fails() -> None:
    manifest = _manifest()
    contract_surfaces = manifest["contract_surfaces"]
    assert isinstance(contract_surfaces, list)
    surface = contract_surfaces[0]
    assert isinstance(surface, dict)
    surface["path"] = "../docs/contracts/external-fixture-runner-contract.md"

    errors = validate_manifest(manifest)

    assert any("public repository-relative path" in error for error in errors)


def test_evidence_reference_without_path_or_command_fails() -> None:
    manifest = _manifest()
    evidence_references = manifest["evidence_references"]
    assert isinstance(evidence_references, list)
    reference = evidence_references[0]
    assert isinstance(reference, dict)
    reference.pop("path")

    errors = validate_manifest(manifest)

    assert any("must include path or command" in error for error in errors)


def test_synthetic_private_detail_marker_fails() -> None:
    manifest = _manifest()
    manifest["compatibility_notes"] = ["Synthetic leak marker: SENTINEL_PRIVATE_PATH."]

    errors = validate_manifest(manifest)

    assert any("synthetic private path marker" in error for error in errors)


def test_evidence_reference_private_command_fails() -> None:
    manifest = _manifest()
    evidence_references = manifest["evidence_references"]
    assert isinstance(evidence_references, list)
    reference = evidence_references[0]
    assert isinstance(reference, dict)
    reference["command"] = "python /Users/alice/private-suite/run.py"

    errors = validate_manifest(manifest)

    assert any("evidence_references[0].command" in error and "local absolute path" in error for error in errors)


def test_evidence_reference_policy_prefixed_private_command_fails() -> None:
    manifest = _manifest()
    evidence_references = manifest["evidence_references"]
    assert isinstance(evidence_references, list)
    reference = evidence_references[0]
    assert isinstance(reference, dict)
    reference["command"] = "Do not include /Users/alice/private-suite/run.py"

    errors = validate_manifest(manifest)

    assert any("evidence_references[0].command" in error and "local absolute path" in error for error in errors)


@pytest.mark.parametrize(
    ("leaked_text", "expected_error"),
    [
        ("Evidence command used /Users/alice/workspace/run.py.", "local absolute path"),
        ("Do not include /Users/alice/workspace/run.py in this manifest.", "local absolute path"),
        ("Runner selected data-testid=submit-button.", "UI selector"),
        ("Runner selected #submit-button.", "UI selector"),
        ("Runner selected .primary-submit.", "UI selector"),
        ("Runner selected button[type=submit].", "UI selector"),
        ("Report kept validation oracle expected output.", "validation oracle"),
        ("Manifest references private transcript text.", "private transcript"),
        ("Manifest retained seed data row.", "seed data"),
        ("Manifest includes event payload {'type': 'external'}.", "event payload"),
    ],
)
def test_manifest_real_private_detail_text_fails(leaked_text: str, expected_error: str) -> None:
    manifest = _manifest()
    manifest["compatibility_notes"] = [leaked_text]

    errors = validate_manifest(manifest)

    assert any(expected_error in error for error in errors)


def test_manifest_allows_redaction_policy_without_concrete_leak() -> None:
    manifest = _manifest()
    manifest["redaction_rules"] = [
        "Do not include UI selectors, hidden reset API details, private fixture paths, validation oracle internals, transcripts, seed data, or non-redacted event payloads.",
        "Use abstract identifiers and public repository-relative paths only.",
    ]

    assert validate_manifest(manifest) == []


def test_readiness_manifest_schema_tightens_expressible_semantics() -> None:
    schema = json.loads(Path("docs/contracts/v0.7-readiness-manifest-schema.json").read_text())
    no_forbidden_ref = {"$ref": "#/$defs/noForbiddenText"}
    no_concrete_ref = {"$ref": "#/$defs/noConcreteLeakText"}

    assert no_forbidden_ref in schema["properties"]["generated_from"]["allOf"]
    assert no_forbidden_ref in schema["properties"]["compatibility_notes"]["items"]["allOf"]
    assert no_concrete_ref in schema["properties"]["redaction_rules"]["items"]["allOf"]
    assert schema["properties"]["readiness_claim_values"]["items"]["enum"] == [
        "contract ready",
        "report format ready",
        "core-side compatibility ready",
        "external suite pass",
        "blocked",
        "skipped",
        "out of scope",
        "projection consumer contract ready",
        "projection report format ready",
        "external consumer pass",
    ]
    evidence_status = schema["properties"]["evidence_references"]["items"]["properties"]["status"]
    assert evidence_status["enum"] == ["contract ready", "report format ready", "blocked", "skipped", "out of scope"]
    evidence_command = schema["properties"]["evidence_references"]["items"]["properties"]["command"]
    assert "not" in evidence_command


def test_cli_returns_zero_for_valid_manifest() -> None:
    result = subprocess.run(
        [sys.executable, "tools/testing/validate_readiness_manifest.py", str(MANIFEST_PATH)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "PASS: validated readiness manifest" in result.stdout


def test_cli_returns_one_for_invalid_manifest(tmp_path: Path) -> None:
    manifest = _manifest()
    manifest["readiness_claim_values"] = ["ready"]
    path = _write_manifest(tmp_path, manifest)

    result = subprocess.run(
        [sys.executable, "tools/testing/validate_readiness_manifest.py", str(path)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1
    assert "FAIL:" in result.stderr
