from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_KEYS = {
    "manifest_id",
    "manifest_version",
    "engine_reference",
    "generated_from",
    "contract_surfaces",
    "schema_surfaces",
    "template_surfaces",
    "capability_areas",
    "readiness_claim_values",
    "evidence_references",
    "compatibility_notes",
    "redaction_rules",
}
REQUIRED_PUBLIC_PATHS = {
    "docs/contracts/external-fixture-runner-contract.md",
    "docs/contracts/external-validation-readiness-contract.md",
    "docs/contracts/projection-consumer-contract.md",
    "docs/testing/external-validation-report-schema.json",
    "docs/validation-report-template.md",
    "tools/testing/validate_external_validation_report.py",
    "docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/review.md",
    "docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/review.md",
}
REQUIRED_CONTRACT_PATHS = {
    "docs/contracts/external-fixture-runner-contract.md",
    "docs/contracts/external-validation-readiness-contract.md",
    "docs/contracts/projection-consumer-contract.md",
}
REQUIRED_SCHEMA_PATHS = {"docs/testing/external-validation-report-schema.json"}
REQUIRED_TEMPLATE_PATHS = {"docs/validation-report-template.md"}
ALLOWED_TAXONOMY_VALUES = {
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
}
ALLOWED_EVIDENCE_STATUSES = {
    "contract ready",
    "report format ready",
    "blocked",
    "skipped",
    "out of scope",
}
FORBIDDEN_MARKERS = {
    "SENTINEL_PRIVATE_PATH": "synthetic private path marker",
    "SENTINEL_UI_SELECTOR": "synthetic UI selector marker",
    "SENTINEL_HIDDEN_RESET_API": "synthetic hidden reset API marker",
    "SENTINEL_ORACLE_INTERNAL": "synthetic validation oracle marker",
    "SENTINEL_SEED_DATA": "synthetic seed data marker",
    "SENTINEL_PRIVATE_TRANSCRIPT": "synthetic private transcript marker",
    "SENTINEL_EXTERNAL_EVENT_PAYLOAD": "synthetic external event payload marker",
}


def _load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text())
    except FileNotFoundError:
        errors.append(f"Missing manifest file: {path}")
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


def _validate_public_path(path_value: Any, field_name: str, errors: list[str]) -> None:
    if not _is_non_empty_string(path_value):
        errors.append(f"{field_name} must be a non-empty string")
        return

    raw_path = Path(path_value)
    if raw_path.is_absolute() or ".." in raw_path.parts:
        errors.append(f"{field_name} must be a public repository-relative path: {path_value}")
        return

    if not raw_path.exists():
        errors.append(f"{field_name} does not exist: {path_value}")


def _validate_surface_list(
    manifest: dict[str, Any],
    key: str,
    required_paths: set[str],
    all_paths: set[str],
    errors: list[str],
) -> None:
    surfaces = manifest.get(key)
    if not isinstance(surfaces, list) or not surfaces:
        errors.append(f"{key} must be a non-empty list")
        return

    seen_paths: set[str] = set()
    for index, surface in enumerate(surfaces):
        if not isinstance(surface, dict):
            errors.append(f"{key}[{index}] must be an object")
            continue
        for field in ["id", "path", "status", "capability_area"]:
            if not _is_non_empty_string(surface.get(field)):
                errors.append(f"{key}[{index}].{field} must be a non-empty string")
        status = surface.get("status")
        if isinstance(status, str) and status not in ALLOWED_EVIDENCE_STATUSES:
            errors.append(f"{key}[{index}].status is not allowed for manifest evidence: {status}")
        path = surface.get("path")
        _validate_public_path(path, f"{key}[{index}].path", errors)
        if isinstance(path, str):
            seen_paths.add(path)
            all_paths.add(path)

    missing_paths = sorted(required_paths - seen_paths)
    if missing_paths:
        errors.append(f"{key} missing required path(s): {', '.join(missing_paths)}")


def _validate_capability_areas(manifest: dict[str, Any], errors: list[str]) -> None:
    areas = manifest.get("capability_areas")
    if not isinstance(areas, list) or not areas:
        errors.append("capability_areas must be a non-empty list")
        return

    for index, area in enumerate(areas):
        if not isinstance(area, dict):
            errors.append(f"capability_areas[{index}] must be an object")
            continue
        for field in ["id", "label", "summary"]:
            if not _is_non_empty_string(area.get(field)):
                errors.append(f"capability_areas[{index}].{field} must be a non-empty string")


def _validate_claim_values(manifest: dict[str, Any], errors: list[str]) -> None:
    values = manifest.get("readiness_claim_values")
    if not isinstance(values, list) or not values:
        errors.append("readiness_claim_values must be a non-empty list")
        return

    unknown = sorted(value for value in values if value not in ALLOWED_TAXONOMY_VALUES)
    if unknown:
        errors.append(f"readiness_claim_values contains unsupported value(s): {', '.join(unknown)}")


def _validate_evidence_references(manifest: dict[str, Any], all_paths: set[str], errors: list[str]) -> None:
    references = manifest.get("evidence_references")
    if not isinstance(references, list) or not references:
        errors.append("evidence_references must be a non-empty list")
        return

    for index, reference in enumerate(references):
        if not isinstance(reference, dict):
            errors.append(f"evidence_references[{index}] must be an object")
            continue
        for field in ["id", "status", "summary"]:
            if not _is_non_empty_string(reference.get(field)):
                errors.append(f"evidence_references[{index}].{field} must be a non-empty string")

        status = reference.get("status")
        if isinstance(status, str) and status not in ALLOWED_EVIDENCE_STATUSES:
            errors.append(f"evidence_references[{index}].status is not allowed for this manifest: {status}")

        path = reference.get("path")
        command = reference.get("command")
        if path is None and command is None:
            errors.append(f"evidence_references[{index}] must include path or command")
        if path is not None:
            _validate_public_path(path, f"evidence_references[{index}].path", errors)
            if isinstance(path, str):
                all_paths.add(path)
        if command is not None and not _is_non_empty_string(command):
            errors.append(f"evidence_references[{index}].command must be a non-empty string")

    missing_paths = sorted(REQUIRED_PUBLIC_PATHS - all_paths)
    if missing_paths:
        errors.append(f"manifest missing required public path(s): {', '.join(missing_paths)}")


def _validate_string_list(manifest: dict[str, Any], key: str, errors: list[str]) -> None:
    values = manifest.get(key)
    if not isinstance(values, list) or not values:
        errors.append(f"{key} must be a non-empty list")
        return
    for index, value in enumerate(values):
        if not _is_non_empty_string(value):
            errors.append(f"{key}[{index}] must be a non-empty string")


def _scan_for_forbidden_markers(manifest: dict[str, Any], errors: list[str]) -> None:
    for value in _iter_strings(manifest):
        for marker, description in FORBIDDEN_MARKERS.items():
            if marker in value:
                errors.append(f"manifest contains forbidden private-detail marker: {description}")


def validate_manifest(manifest: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(manifest, dict):
        return ["manifest must be a JSON object"]

    missing_keys = sorted(REQUIRED_KEYS - set(manifest))
    if missing_keys:
        errors.append(f"manifest missing required keys: {', '.join(missing_keys)}")

    for key in ["manifest_id", "manifest_version", "generated_from"]:
        if key in manifest and not _is_non_empty_string(manifest.get(key)):
            errors.append(f"{key} must be a non-empty string")

    engine_reference = manifest.get("engine_reference")
    if not isinstance(engine_reference, dict):
        errors.append("engine_reference must be an object")
    else:
        for field in ["version", "source"]:
            if not _is_non_empty_string(engine_reference.get(field)):
                errors.append(f"engine_reference.{field} must be a non-empty string")

    all_paths: set[str] = set()
    _validate_surface_list(manifest, "contract_surfaces", REQUIRED_CONTRACT_PATHS, all_paths, errors)
    _validate_surface_list(manifest, "schema_surfaces", REQUIRED_SCHEMA_PATHS, all_paths, errors)
    _validate_surface_list(manifest, "template_surfaces", REQUIRED_TEMPLATE_PATHS, all_paths, errors)
    _validate_capability_areas(manifest, errors)
    _validate_claim_values(manifest, errors)
    _validate_evidence_references(manifest, all_paths, errors)
    _validate_string_list(manifest, "compatibility_notes", errors)
    _validate_string_list(manifest, "redaction_rules", errors)
    _scan_for_forbidden_markers(manifest, errors)
    return errors


def validate_manifest_file(path: Path | str) -> list[str]:
    errors: list[str] = []
    manifest = _load_json(Path(path), errors)
    if errors:
        return errors
    return validate_manifest(manifest)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate_readiness_manifest.py MANIFEST_JSON", file=sys.stderr)
        return 2

    errors = validate_manifest_file(argv[1])
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(f"PASS: validated readiness manifest at {argv[1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
