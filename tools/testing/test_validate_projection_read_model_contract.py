from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from tools.testing.validate_projection_read_model_contract import (
    validate_projection_read_model_contract,
    validate_projection_read_model_contract_file,
)


CONTRACT_PATH = Path("docs/contracts/projection-read-model-schema.json")


def _contract() -> dict[str, object]:
    return json.loads(CONTRACT_PATH.read_text())


def _write_contract(tmp_path: Path, contract: dict[str, object]) -> Path:
    path = tmp_path / "projection-read-model-contract.json"
    path.write_text(json.dumps(contract, indent=2) + "\n")
    return path


def _families(contract: dict[str, object]) -> dict[str, object]:
    families = contract["read_model_families"]
    assert isinstance(families, dict)
    return families


def _family(contract: dict[str, object], family_id: str) -> dict[str, object]:
    family = _families(contract)[family_id]
    assert isinstance(family, dict)
    return family


def test_contract_file_passes() -> None:
    assert validate_projection_read_model_contract_file(CONTRACT_PATH) == []


def test_valid_contract_passes() -> None:
    assert validate_projection_read_model_contract(_contract()) == []


def test_missing_required_key_fails() -> None:
    contract = _contract()
    contract.pop("contract_id")

    errors = validate_projection_read_model_contract(contract)

    assert any("missing required keys" in error and "contract_id" in error for error in errors)


def test_unsupported_top_level_capability_fails() -> None:
    contract = _contract()
    contract["write_api"] = {"enabled": True}

    errors = validate_projection_read_model_contract(contract)

    assert any("unsupported top-level keys" in error and "write_api" in error for error in errors)


def test_missing_required_family_fails() -> None:
    contract = _contract()
    _families(contract).pop("memory_context_summary")

    errors = validate_projection_read_model_contract(contract)

    assert any("missing required family" in error and "memory_context_summary" in error for error in errors)


def test_unsupported_extra_family_fails() -> None:
    contract = _contract()
    _families(contract)["projection_app_write_api"] = {
        "id": "projection_app_write_api",
        "version": "0.7.4",
        "read_only": True,
        "allowed_fields": ["status"],
        "redaction_notes": ["Synthetic unsupported family."],
        "no_write_capability": True,
    }

    errors = validate_projection_read_model_contract(contract)

    assert any("unsupported family" in error and "projection_app_write_api" in error for error in errors)


def test_family_id_mismatch_fails() -> None:
    contract = _contract()
    _family(contract, "runtime_summary")["id"] = "event_timeline_summary"

    errors = validate_projection_read_model_contract(contract)

    assert any("id must equal runtime_summary" in error for error in errors)


def test_non_read_only_family_fails() -> None:
    contract = _contract()
    _family(contract, "runtime_summary")["read_only"] = False

    errors = validate_projection_read_model_contract(contract)

    assert any("runtime_summary.read_only must be true" in error for error in errors)


def test_family_with_write_capability_fails() -> None:
    contract = _contract()
    _family(contract, "agent_loop_summary")["no_write_capability"] = False

    errors = validate_projection_read_model_contract(contract)

    assert any("agent_loop_summary.no_write_capability must be true" in error for error in errors)


def test_forbidden_capability_field_fails() -> None:
    contract = _contract()
    _family(contract, "runtime_summary")["reset_api"] = "/reset"

    errors = validate_projection_read_model_contract(contract)

    assert any("reset_api is a forbidden capability field" in error for error in errors)


def test_unsafe_allowed_field_fails() -> None:
    contract = _contract()
    allowed_fields = _family(contract, "runtime_summary")["allowed_fields"]
    assert isinstance(allowed_fields, list)
    allowed_fields.append("write_api_url")

    errors = validate_projection_read_model_contract(contract)

    assert any("exposes forbidden term" in error and "write" in error for error in errors)


def test_unbounded_allowed_field_fails() -> None:
    contract = _contract()
    allowed_fields = _family(contract, "event_timeline_summary")["allowed_fields"]
    assert isinstance(allowed_fields, list)
    allowed_fields.append("payload")

    errors = validate_projection_read_model_contract(contract)

    assert any("not a public bounded field" in error and "payload" in error for error in errors)


@pytest.mark.parametrize(
    "field_name",
    [
        "private_application_state_summary",
        "application_state_summary",
        "private_state_summary",
    ],
)
def test_private_application_state_allowed_field_fails(field_name: str) -> None:
    contract = _contract()
    allowed_fields = _family(contract, "readiness_manifest_summary")["allowed_fields"]
    assert isinstance(allowed_fields, list)
    allowed_fields.append(field_name)

    errors = validate_projection_read_model_contract(contract)

    assert any("exposes forbidden term" in error and field_name in error for error in errors)


def test_missing_required_forbidden_capability_fails() -> None:
    contract = _contract()
    capabilities = contract["forbidden_capabilities"]
    assert isinstance(capabilities, list)
    capabilities.remove("private_runner_hook")

    errors = validate_projection_read_model_contract(contract)

    assert any("missing required exclusion" in error and "private_runner_hook" in error for error in errors)


def test_absolute_source_contract_path_fails() -> None:
    contract = _contract()
    contract["source_contract"] = "/tmp/projection-consumer-contract.md"

    errors = validate_projection_read_model_contract(contract)

    assert any("public repository-relative path" in error for error in errors)


def test_synthetic_private_detail_marker_fails() -> None:
    contract = _contract()
    redaction_rules = contract["redaction_rules"]
    assert isinstance(redaction_rules, list)
    redaction_rules.append("Synthetic leak marker: SENTINEL_RAW_MEMORY.")

    errors = validate_projection_read_model_contract(contract)

    assert any("synthetic raw memory marker" in error for error in errors)


def test_prompt_trace_marker_fails() -> None:
    contract = _contract()
    compatibility_notes = contract["compatibility_notes"]
    assert isinstance(compatibility_notes, list)
    compatibility_notes.append("Synthetic leak marker: SENTINEL_PROMPT_TRACE.")

    errors = validate_projection_read_model_contract(contract)

    assert any("synthetic prompt trace marker" in error for error in errors)


def test_cli_returns_zero_for_valid_contract() -> None:
    result = subprocess.run(
        [sys.executable, "tools/testing/validate_projection_read_model_contract.py", str(CONTRACT_PATH)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "PASS: validated projection read model contract" in result.stdout


def test_cli_returns_one_for_invalid_contract(tmp_path: Path) -> None:
    contract = _contract()
    _family(contract, "runtime_summary")["read_only"] = False
    path = _write_contract(tmp_path, contract)

    result = subprocess.run(
        [sys.executable, "tools/testing/validate_projection_read_model_contract.py", str(path)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1
    assert "FAIL:" in result.stderr
