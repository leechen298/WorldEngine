from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_KEYS = {
    "contract_id",
    "contract_version",
    "source_contract",
    "read_model_families",
    "forbidden_capabilities",
    "redaction_rules",
    "compatibility_notes",
}
REQUIRED_FAMILIES = {
    "runtime_summary",
    "event_timeline_summary",
    "agent_loop_summary",
    "memory_context_summary",
    "generation_readiness_summary",
    "readiness_manifest_summary",
    "redacted_report_summary",
}
REQUIRED_FORBIDDEN_CAPABILITIES = {
    "write_api",
    "reset_api",
    "persistence",
    "migration",
    "private_runner_hook",
    "product_ui",
    "projection_app_behavior",
    "consumer_specific_backend_behavior",
    "raw_memory_export",
    "prompt_trace_export",
    "private_transcript_export",
    "event_payload_export",
}
ALLOWED_FIELD_SUFFIXES = (
    "_id",
    "_ids",
    "_ref",
    "_refs",
    "_status",
    "_summary",
    "_summaries",
    "_counts",
    "_range",
    "_version",
    "_confirmed",
    "_reasons",
    "_claims",
)
ALLOWED_LITERAL_FIELDS = {"status", "summary", "summarized_events", "finding_counts"}
FORBIDDEN_ALLOWED_FIELD_TERMS = {
    "write",
    "reset",
    "persist",
    "migration",
    "private_runner",
    "product_ui",
    "projection_app",
    "raw_memory",
    "prompt",
    "trace",
    "transcript",
    "event_payload",
    "secret",
    "selector",
    "oracle",
    "seed",
    "map",
    "character",
    "location",
    "story_rule",
    "fixture_path",
}
FORBIDDEN_FAMILY_KEY_TERMS = {
    "write",
    "reset",
    "persist",
    "migration",
    "private_runner",
    "product_ui",
    "projection_app",
}
FORBIDDEN_MARKERS = {
    "SENTINEL_WRITE_API": "synthetic write API marker",
    "SENTINEL_RESET_API": "synthetic reset API marker",
    "SENTINEL_PRIVATE_RUNNER_HOOK": "synthetic private runner marker",
    "SENTINEL_RAW_MEMORY": "synthetic raw memory marker",
    "SENTINEL_PROMPT_TRACE": "synthetic prompt trace marker",
    "SENTINEL_PRIVATE_TRANSCRIPT": "synthetic private transcript marker",
    "SENTINEL_EXTERNAL_EVENT_PAYLOAD": "synthetic external event payload marker",
    "SENTINEL_UI_SELECTOR": "synthetic UI selector marker",
    "SENTINEL_PROVIDER_SECRET": "synthetic provider secret marker",
    "SENTINEL_SEED_DATA": "synthetic seed data marker",
    "SENTINEL_CONCRETE_WORLD": "synthetic concrete world marker",
}


def _load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text())
    except FileNotFoundError:
        errors.append(f"Missing projection read model contract file: {path}")
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


def _validate_string_list(contract: dict[str, Any], key: str, errors: list[str]) -> None:
    values = contract.get(key)
    if not isinstance(values, list) or not values:
        errors.append(f"{key} must be a non-empty list")
        return
    for index, value in enumerate(values):
        if not _is_non_empty_string(value):
            errors.append(f"{key}[{index}] must be a non-empty string")


def _field_is_public_bounded(field_name: str) -> bool:
    return field_name in ALLOWED_LITERAL_FIELDS or field_name.endswith(ALLOWED_FIELD_SUFFIXES)


def _validate_allowed_fields(family_id: str, family: dict[str, Any], errors: list[str]) -> None:
    allowed_fields = family.get("allowed_fields")
    if not isinstance(allowed_fields, list) or not allowed_fields:
        errors.append(f"read_model_families.{family_id}.allowed_fields must be a non-empty list")
        return

    for index, field_name in enumerate(allowed_fields):
        if not _is_non_empty_string(field_name):
            errors.append(f"read_model_families.{family_id}.allowed_fields[{index}] must be a non-empty string")
            continue

        normalized = field_name.strip().lower()
        if not _field_is_public_bounded(normalized):
            errors.append(
                f"read_model_families.{family_id}.allowed_fields[{index}] is not a public bounded field: {field_name}"
            )

        matched_terms = sorted(term for term in FORBIDDEN_ALLOWED_FIELD_TERMS if term in normalized)
        if matched_terms:
            errors.append(
                f"read_model_families.{family_id}.allowed_fields[{index}] exposes forbidden term(s): "
                + ", ".join(matched_terms)
            )


def _validate_family(family_key: str, family: Any, errors: list[str]) -> None:
    if not isinstance(family, dict):
        errors.append(f"read_model_families.{family_key} must be an object")
        return

    for key in family:
        normalized_key = key.lower()
        matched_terms = sorted(term for term in FORBIDDEN_FAMILY_KEY_TERMS if term in normalized_key)
        if matched_terms and key not in {"no_write_capability"}:
            errors.append(
                f"read_model_families.{family_key}.{key} is a forbidden capability field: "
                + ", ".join(matched_terms)
            )

    if family.get("id") != family_key:
        errors.append(f"read_model_families.{family_key}.id must equal {family_key}")
    if not _is_non_empty_string(family.get("version")):
        errors.append(f"read_model_families.{family_key}.version must be a non-empty string")
    if family.get("read_only") is not True:
        errors.append(f"read_model_families.{family_key}.read_only must be true")
    if family.get("no_write_capability") is not True:
        errors.append(f"read_model_families.{family_key}.no_write_capability must be true")

    _validate_allowed_fields(family_key, family, errors)

    redaction_notes = family.get("redaction_notes")
    if not isinstance(redaction_notes, list) or not redaction_notes:
        errors.append(f"read_model_families.{family_key}.redaction_notes must be a non-empty list")
    else:
        for index, note in enumerate(redaction_notes):
            if not _is_non_empty_string(note):
                errors.append(f"read_model_families.{family_key}.redaction_notes[{index}] must be a non-empty string")


def _validate_families(contract: dict[str, Any], errors: list[str]) -> None:
    families = contract.get("read_model_families")
    if not isinstance(families, dict) or not families:
        errors.append("read_model_families must be a non-empty object")
        return

    missing_families = sorted(REQUIRED_FAMILIES - set(families))
    if missing_families:
        errors.append(f"read_model_families missing required family/families: {', '.join(missing_families)}")

    extra_families = sorted(set(families) - REQUIRED_FAMILIES)
    if extra_families:
        errors.append(f"read_model_families contains unsupported family/families: {', '.join(extra_families)}")

    for family_key, family in families.items():
        if not _is_non_empty_string(family_key):
            errors.append("read_model_families keys must be non-empty strings")
            continue
        _validate_family(family_key, family, errors)


def _validate_forbidden_capabilities(contract: dict[str, Any], errors: list[str]) -> None:
    capabilities = contract.get("forbidden_capabilities")
    if not isinstance(capabilities, list) or not capabilities:
        errors.append("forbidden_capabilities must be a non-empty list")
        return

    for index, capability in enumerate(capabilities):
        if not _is_non_empty_string(capability):
            errors.append(f"forbidden_capabilities[{index}] must be a non-empty string")

    capability_set = {capability for capability in capabilities if isinstance(capability, str)}
    missing = sorted(REQUIRED_FORBIDDEN_CAPABILITIES - capability_set)
    if missing:
        errors.append(f"forbidden_capabilities missing required exclusion(s): {', '.join(missing)}")


def _scan_for_forbidden_markers(contract: dict[str, Any], errors: list[str]) -> None:
    for value in _iter_strings(contract):
        for marker, description in FORBIDDEN_MARKERS.items():
            if marker in value:
                errors.append(f"projection read model contract contains forbidden marker: {description}")


def validate_projection_read_model_contract(contract: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(contract, dict):
        return ["projection read model contract must be a JSON object"]

    missing_keys = sorted(REQUIRED_KEYS - set(contract))
    if missing_keys:
        errors.append(f"projection read model contract missing required keys: {', '.join(missing_keys)}")

    extra_keys = sorted(set(contract) - REQUIRED_KEYS)
    if extra_keys:
        errors.append(f"projection read model contract contains unsupported top-level keys: {', '.join(extra_keys)}")

    for key in ["contract_id", "contract_version"]:
        if key in contract and not _is_non_empty_string(contract.get(key)):
            errors.append(f"{key} must be a non-empty string")

    if "source_contract" in contract:
        _validate_public_path(contract.get("source_contract"), "source_contract", errors)

    _validate_families(contract, errors)
    _validate_forbidden_capabilities(contract, errors)
    _validate_string_list(contract, "redaction_rules", errors)
    _validate_string_list(contract, "compatibility_notes", errors)
    _scan_for_forbidden_markers(contract, errors)
    return errors


def validate_projection_read_model_contract_file(path: Path | str) -> list[str]:
    errors: list[str] = []
    contract = _load_json(Path(path), errors)
    if errors:
        return errors
    return validate_projection_read_model_contract(contract)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate_projection_read_model_contract.py CONTRACT_JSON", file=sys.stderr)
        return 2

    errors = validate_projection_read_model_contract_file(argv[1])
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(f"PASS: validated projection read model contract at {argv[1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
