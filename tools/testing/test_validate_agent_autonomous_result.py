from __future__ import annotations

import json
import shutil
from pathlib import Path

from tools.testing.validate_agent_autonomous_result import validate_result_dir


FIXTURES_DIR = Path(__file__).parent / "fixtures" / "agent-autonomous"


def _write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n")


def _write_valid_full_lifecycle_result(result_dir: Path) -> None:
    result_dir.mkdir(parents=True, exist_ok=True)
    (result_dir / "screenshots").mkdir()
    (result_dir / "screenshots" / "runtime-console.png").write_bytes(b"placeholder image")
    (result_dir / "transcript.md").write_text("# Transcript\n\nObserved full lifecycle evidence.\n")
    (result_dir / "console.log").write_text("no client errors\n")
    (result_dir / "operation-log.jsonl").write_text(
        "\n".join(
            [
                json.dumps({"seq": 1, "type": "ui", "target": "dashboard", "action": "open"}),
                json.dumps({"seq": 2, "type": "ui", "target": "world-create-form", "action": "fill"}),
                json.dumps(
                    {
                        "seq": 3,
                        "type": "ui",
                        "target": "worldengine-session-create-button",
                        "action": "click",
                    }
                ),
                json.dumps({"seq": 4, "type": "ui", "target": "runtime-run-button", "action": "click"}),
                json.dumps({"seq": 5, "type": "ui", "target": "runtime-tick-counter", "action": "observe"}),
                json.dumps({"seq": 6, "type": "ui", "target": "agent-life-log", "action": "observe"}),
                json.dumps({"seq": 7, "type": "ui", "target": "director-guidance-input", "action": "fill"}),
                json.dumps({"seq": 8, "type": "ui", "target": "evidence-download-button", "action": "click"}),
                json.dumps(
                    {
                        "seq": 9,
                        "type": "cli",
                        "command": "make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/latest",
                        "exit_code": 0,
                        "summary": "Ran deterministic autonomous scorecard checker.",
                    }
                ),
            ]
        )
        + "\n"
    )
    _write_json(
        result_dir / "api-summary.json",
        {
            "status": "pass",
            "worldengine_public_calls": [
                {"method": "GET", "path": "/manifest", "status_code": 200},
                {"method": "POST", "path": "/worlds", "status_code": 200},
                {"method": "POST", "path": "/worlds/{world_id}/director-guidance", "status_code": 200},
            ],
            "private_trace_included": False,
        },
    )
    _write_json(
        result_dir / "world-lifecycle-summary.json",
        {
            "scenario": "worldengine-full-lifecycle-autonomous",
            "world_creation": {
                "status": "pass",
                "world_id": "world-generic-001",
                "public_initial_state_observed": True,
                "visualization_observed": True,
            },
            "runtime_progression": {
                "status": "pass",
                "tick_start": 0,
                "tick_end": 8,
                "events_observed": 12,
                "snapshots_observed": 2,
            },
            "agent_autonomy": {
                "status": "pass",
                "agent_actions_observed": 4,
                "unique_action_types": ["observe", "move"],
                "client_scripted_actions": False,
                "worldengine_evidence_observed": True,
            },
            "external_direction": {
                "status": "pass",
                "director_guidance_observed": True,
                "direct_agent_private_state_mutation": False,
            },
            "evidence_integrity": {
                "status": "pass",
                "operation_log_entries": 9,
                "api_trace_entries": 3,
                "redaction_scan_passed": True,
            },
        },
    )
    _write_json(
        result_dir / "scorecard-summary.json",
        {
            "scenario": "worldengine-full-lifecycle-autonomous",
            "status": "pass",
            "verdict_source": "scorecard_checker",
        },
    )
    _write_json(
        result_dir / "result.json",
        {
            "scenario": "worldengine-full-lifecycle-autonomous",
            "goal": "Validate WorldEngine can create, run, and evidence an autonomous-agent world lifecycle.",
            "mode": "scorecard_autonomous",
            "status": "pass",
            "verdict_source": "scorecard_checker",
            "score_items": [
                {"name": "world_created", "status": "pass", "evidence": "world-lifecycle-summary.json"},
                {"name": "runtime_progressed", "status": "pass", "evidence": "world-lifecycle-summary.json"},
                {"name": "agent_autonomy_observed", "status": "pass", "evidence": "world-lifecycle-summary.json"},
                {"name": "external_direction_bounded", "status": "pass", "evidence": "world-lifecycle-summary.json"},
            ],
            "required_artifacts": [
                "transcript",
                "console_log",
                "scorecard_summary",
                "operation_log",
                "api_summary",
                "world_lifecycle_summary",
                "screenshots",
            ],
            "artifacts": {
                "transcript": "transcript.md",
                "console_log": "console.log",
                "scorecard_summary": "scorecard-summary.json",
                "operation_log": "operation-log.jsonl",
                "api_summary": "api-summary.json",
                "world_lifecycle_summary": "world-lifecycle-summary.json",
                "screenshots": ["screenshots/runtime-console.png"],
            },
            "operation_log": "operation-log.jsonl",
            "unverified_items": [],
            "failures": [],
        },
    )


def _clean_redaction() -> dict:
    return {
        "api_keys_included": False,
        "authorization_headers_included": False,
        "raw_prompts_included": False,
        "raw_provider_requests_included": False,
        "raw_provider_responses_included": False,
        "provider_traces_included": False,
        "private_agent_memory_included": False,
        "private_agent_goals_included": False,
        "raw_thought_included": False,
        "hidden_context_included": False,
        "private_evaluator_data_included": False,
        "external_world_seed_included": False,
        "external_world_oracle_included": False,
    }


def _summary(scenario: str, **fields: object) -> dict:
    payload = {
        "schema_version": "0.9.10",
        "scenario": scenario,
        "status": "pass",
        "source": "fixture",
        "created_at": "2026-06-06T00:00:00Z",
        "redaction": _clean_redaction(),
        "evidence_refs": ["operation-log.jsonl"],
        "failures": [],
    }
    payload.update(fields)
    return payload


def _write_base_llm_result(result_dir: Path, scenario: str, artifact_payloads: dict[str, dict | str]) -> None:
    result_dir.mkdir(parents=True, exist_ok=True)
    (result_dir / "operation-log.jsonl").write_text(
        json.dumps({"seq": 1, "type": "cli", "command": "make validate-agent-autonomous-result RESULT_DIR=fixture", "exit_code": 0})
        + "\n"
    )
    (result_dir / "transcript.md").write_text("# Transcript\n\nStructured LLM-backed evidence fixture.\n")
    (result_dir / "console.log").write_text("fixture only\n")
    _write_json(result_dir / "redaction-scan.json", {"scenario": scenario, "status": "pass", "redaction": _clean_redaction()})
    _write_json(result_dir / "scorecard-summary.json", {"scenario": scenario, "status": "pass", "verdict_source": "scorecard_checker"})

    artifacts = {
        "operation_log": "operation-log.jsonl",
        "transcript": "transcript.md",
        "console_log": "console.log",
        "redaction_scan": "redaction-scan.json",
        "scorecard_summary": "scorecard-summary.json",
    }
    for name, payload in artifact_payloads.items():
        filename = f"{name.replace('_', '-')}.json" if isinstance(payload, dict) else str(payload)
        artifacts[name] = filename
        if isinstance(payload, dict):
            _write_json(result_dir / filename, payload)

    _write_json(
        result_dir / "result.json",
        {
            "scenario": scenario,
            "goal": f"Validate {scenario}.",
            "mode": "llm_backed_scorecard",
            "status": "pass",
            "verdict_source": "scorecard_checker",
            "score_items": [{"name": "redaction_clean", "status": "pass", "evidence": "redaction-scan.json"}],
            "required_artifacts": list(artifacts),
            "artifacts": artifacts,
            "operation_log": "operation-log.jsonl",
            "unverified_items": [],
            "failures": [],
        },
    )


def _write_valid_llm_full_lifecycle_result(result_dir: Path) -> None:
    scenario = "llm-backed-full-lifecycle-autonomous"
    payloads = {
        "provider_live_summary": _summary(
            scenario,
            provider_class="deepseek",
            model_label="deepseek-chat",
            call_attempted=True,
            call_status="success",
            worldengine_owned_call=True,
        ),
        "world_creation_summary": _summary(
            scenario,
            llm_backed=True,
            deterministic_generic_fallback_detected=False,
            world_id="world-llm-001",
        ),
        "world_rule_summary": _summary(
            scenario,
            parameters=[{"name": "temperature"}],
            evolution_rules=[{"id": "rule.temperature"}],
            event_legality_rules=[{"id": "event.weather"}],
        ),
        "rule_parameter_summary": _summary(
            scenario,
            changed_parameters=[{"name": "temperature", "rule_ref": "rule.temperature"}],
            unexplained_changes=[],
            fixed_counter_only_detected=False,
        ),
        "event_legality_summary": _summary(
            scenario,
            rule_adjudications=[{"rule_ref": "event.weather", "status": "accepted"}],
            direct_final_state_mutation_detected=False,
        ),
        "agent_autonomy_summary": _summary(
            scenario,
            decision_moments=["tick-1", "tick-2"],
            client_scripted_action_detected=False,
            single_event_only_detected=False,
        ),
        "diff_replay_summary": _summary(scenario, replay_supported=True),
        "world_lifecycle_summary": _summary(scenario, lifecycle_complete=True),
    }
    _write_base_llm_result(result_dir, scenario, payloads)
    (result_dir / "second-agent-review.md").write_text(
        "# Second-Agent Review\n\nFinal review verdict: pass\n\nNo blocking findings.\n"
    )
    result = json.loads((result_dir / "result.json").read_text())
    result["artifacts"]["second_agent_review"] = "second-agent-review.md"
    result["required_artifacts"].append("second_agent_review")
    result["score_items"] = [
        {"name": name, "status": "pass", "evidence": "scorecard-summary.json"}
        for name in [
            "provider_live_smoke",
            "world_creation_llm_backed",
            "world_rules_generated",
            "parameter_evolution_rule_linked",
            "event_legality_enforced",
            "agent_persistent_autonomy",
            "diff_replay_available",
            "redaction_clean",
            "client_evidence_complete",
            "second_agent_review_clean",
        ]
    ]
    _write_json(result_dir / "result.json", result)


def test_valid_basic_runtime_fixture_passes() -> None:
    assert validate_result_dir(FIXTURES_DIR / "valid-dashboard-basic-runtime") == []


def test_valid_worldengine_full_lifecycle_fixture_passes() -> None:
    assert validate_result_dir(FIXTURES_DIR / "valid-worldengine-full-lifecycle") == []


def test_valid_llm_provider_live_smoke_fixture_passes() -> None:
    assert validate_result_dir(FIXTURES_DIR / "valid-provider-live-smoke-deepseek") == []


def test_agent_verdict_fixture_fails() -> None:
    errors = validate_result_dir(FIXTURES_DIR / "invalid-agent-verdict")

    assert any("verdict_source" in error for error in errors)


def test_direct_api_operation_fails() -> None:
    errors = validate_result_dir(FIXTURES_DIR / "invalid-direct-api-operation")

    assert any("direct API" in error or "type must be ui or cli" in error for error in errors)


def test_cli_nonzero_exit_fails() -> None:
    errors = validate_result_dir(FIXTURES_DIR / "invalid-cli-nonzero-exit")

    assert any("exit_code must be 0" in error for error in errors)


def test_unresolved_p1_item_fails() -> None:
    errors = validate_result_dir(FIXTURES_DIR / "invalid-unverified-p1")

    assert any("unresolved P1" in error for error in errors)


def test_failed_score_item_fails() -> None:
    errors = validate_result_dir(FIXTURES_DIR / "invalid-failed-score-item")

    assert any("score_items" in error and "status must be pass" in error for error in errors)


def test_missing_required_artifact_fails() -> None:
    errors = validate_result_dir(FIXTURES_DIR / "invalid-missing-artifact")

    assert any("Missing required artifact" in error for error in errors)


def test_invalid_llm_redaction_leak_fixture_fails() -> None:
    errors = validate_result_dir(FIXTURES_DIR / "invalid-llm-redaction-leak")

    assert any("redaction flags must all be false" in error for error in errors)


def test_scenario_required_ui_target_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "missing-ui-target"
    shutil.copytree(FIXTURES_DIR / "valid-dashboard-basic-runtime", result_dir)
    operation_log = result_dir / "operation-log.jsonl"
    operations = [
        json.loads(line)
        for line in operation_log.read_text().splitlines()
        if "runtime-step-button" not in line
    ]
    operation_log.write_text("\n".join(json.dumps(operation) for operation in operations) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("runtime-step-button" in error for error in errors)


def test_scorecard_summary_mismatch_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "scorecard-mismatch"
    shutil.copytree(FIXTURES_DIR / "valid-dashboard-basic-runtime", result_dir)
    summary_path = result_dir / "scorecard-summary.json"
    summary = json.loads(summary_path.read_text())
    summary["scenario"] = "autonomous-dashboard-params-flow"
    summary_path.write_text(json.dumps(summary, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("scorecard-summary.json scenario must match" in error for error in errors)


def test_valid_full_world_lifecycle_result_passes(tmp_path: Path) -> None:
    result_dir = tmp_path / "valid-full-lifecycle"
    _write_valid_full_lifecycle_result(result_dir)

    assert validate_result_dir(result_dir) == []


def test_full_world_lifecycle_missing_agent_actions_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "missing-agent-actions"
    _write_valid_full_lifecycle_result(result_dir)
    summary_path = result_dir / "world-lifecycle-summary.json"
    summary = json.loads(summary_path.read_text())
    summary["agent_autonomy"]["agent_actions_observed"] = 0
    summary_path.write_text(json.dumps(summary, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("agent_autonomy.agent_actions_observed" in error for error in errors)


def test_full_world_lifecycle_client_scripted_agent_actions_fail(tmp_path: Path) -> None:
    result_dir = tmp_path / "client-scripted-actions"
    _write_valid_full_lifecycle_result(result_dir)
    summary_path = result_dir / "world-lifecycle-summary.json"
    summary = json.loads(summary_path.read_text())
    summary["agent_autonomy"]["client_scripted_actions"] = True
    summary_path.write_text(json.dumps(summary, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("agent_autonomy.client_scripted_actions" in error for error in errors)


def test_full_world_lifecycle_non_advancing_runtime_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "non-advancing-runtime"
    _write_valid_full_lifecycle_result(result_dir)
    summary_path = result_dir / "world-lifecycle-summary.json"
    summary = json.loads(summary_path.read_text())
    summary["runtime_progression"]["tick_end"] = summary["runtime_progression"]["tick_start"]
    summary_path.write_text(json.dumps(summary, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("runtime_progression.tick_end" in error for error in errors)


def test_full_world_lifecycle_failed_redaction_scan_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "failed-redaction-scan"
    _write_valid_full_lifecycle_result(result_dir)
    summary_path = result_dir / "world-lifecycle-summary.json"
    summary = json.loads(summary_path.read_text())
    summary["evidence_integrity"]["redaction_scan_passed"] = False
    summary_path.write_text(json.dumps(summary, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("evidence_integrity.redaction_scan_passed" in error for error in errors)


def test_full_world_lifecycle_cli_curl_disguised_direct_api_call_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "cli-disguised-direct-api"
    _write_valid_full_lifecycle_result(result_dir)
    operation_log = result_dir / "operation-log.jsonl"
    operations = [
        json.loads(line)
        for line in operation_log.read_text().splitlines()
        if line.strip()
    ]
    operations.append(
        {
            "seq": len(operations) + 1,
            "type": "cli",
            "command": "curl -s http://127.0.0.1:8000/worlds",
            "exit_code": 0,
            "summary": "Direct public API call disguised as CLI evidence.",
        }
    )
    operation_log.write_text("\n".join(json.dumps(operation) for operation in operations) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("direct public API calls must be recorded in api-summary.json" in error for error in errors)


def test_full_world_lifecycle_cli_python_disguised_direct_api_call_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "cli-python-disguised-direct-api"
    _write_valid_full_lifecycle_result(result_dir)
    operation_log = result_dir / "operation-log.jsonl"
    operations = [
        json.loads(line)
        for line in operation_log.read_text().splitlines()
        if line.strip()
    ]
    operations.append(
        {
            "seq": len(operations) + 1,
            "type": "cli",
            "command": (
                "python -c \"import requests; "
                "requests.get('http://127.0.0.1:8000/runtime/state')\""
            ),
            "exit_code": 0,
            "summary": "Direct runtime API call disguised as CLI evidence.",
        }
    )
    operation_log.write_text("\n".join(json.dumps(operation) for operation in operations) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("direct public API calls must be recorded in api-summary.json" in error for error in errors)


def test_full_world_lifecycle_cli_described_direct_api_call_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "cli-described-direct-api"
    _write_valid_full_lifecycle_result(result_dir)
    operation_log = result_dir / "operation-log.jsonl"
    operations = [
        json.loads(line)
        for line in operation_log.read_text().splitlines()
        if line.strip()
    ]
    operations.append(
        {
            "seq": len(operations) + 1,
            "type": "cli",
            "command": "POST /runtime/step repeated through WorldEngine public API",
            "exit_code": 0,
            "summary": "Direct runtime API call disguised as CLI evidence.",
        }
    )
    operation_log.write_text("\n".join(json.dumps(operation) for operation in operations) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("direct public API calls must be recorded in api-summary.json" in error for error in errors)


def test_full_world_lifecycle_public_evidence_phrase_marker_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "public-evidence-phrase-marker"
    _write_valid_full_lifecycle_result(result_dir)
    api_summary_path = result_dir / "api-summary.json"
    api_summary = json.loads(api_summary_path.read_text())
    api_summary["worldengine_public_calls"][0]["response_summary"] = {
        "public_explanation": "no Agent private memory was changed"
    }
    api_summary_path.write_text(json.dumps(api_summary, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("api-summary.json contains forbidden public evidence marker" in error for error in errors)


def test_full_world_lifecycle_public_provider_metadata_passes(tmp_path: Path) -> None:
    result_dir = tmp_path / "public-provider-metadata"
    _write_valid_full_lifecycle_result(result_dir)
    api_summary_path = result_dir / "api-summary.json"
    api_summary = json.loads(api_summary_path.read_text())
    api_summary["worldengine_public_calls"][0]["public_summary"] = {
        "provider": {
            "provider_class": "unconfigured",
            "provider_readiness": "not_configured",
            "credential_source_class": "none",
            "model_label": "unconfigured",
        }
    }
    api_summary_path.write_text(json.dumps(api_summary, indent=2) + "\n")

    assert validate_result_dir(result_dir) == []


def test_full_world_lifecycle_public_credential_field_still_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "public-credential-field"
    _write_valid_full_lifecycle_result(result_dir)
    api_summary_path = result_dir / "api-summary.json"
    api_summary = json.loads(api_summary_path.read_text())
    api_summary["worldengine_public_calls"][0]["public_summary"] = {
        "provider": {
            "credential": "none",
        }
    }
    api_summary_path.write_text(json.dumps(api_summary, indent=2) + "\n")

    errors = validate_result_dir(result_dir)

    assert any("api-summary.json contains forbidden public evidence marker" in error for error in errors)


def test_valid_llm_backed_full_lifecycle_result_passes(tmp_path: Path) -> None:
    result_dir = tmp_path / "valid-llm-full-lifecycle"
    _write_valid_llm_full_lifecycle_result(result_dir)

    assert validate_result_dir(result_dir) == []


def test_llm_backed_result_allows_honest_blocked_status(tmp_path: Path) -> None:
    result_dir = tmp_path / "blocked-provider-smoke"
    scenario = "provider-live-smoke-deepseek"
    _write_base_llm_result(
        result_dir,
        scenario,
        {
            "provider_live_summary": _summary(
                scenario,
                status="blocked",
                call_attempted=False,
                call_status="not_run",
                worldengine_owned_call=True,
            )
        },
    )
    result = json.loads((result_dir / "result.json").read_text())
    result["status"] = "blocked"
    result["score_items"] = [{"name": "provider_live_smoke", "status": "blocked", "evidence": "provider-live-summary.json"}]
    result["failures"] = [{"taxonomy": "provider", "message": "provider credentials unavailable"}]
    _write_json(result_dir / "result.json", result)
    scorecard = json.loads((result_dir / "scorecard-summary.json").read_text())
    scorecard["status"] = "blocked"
    _write_json(result_dir / "scorecard-summary.json", scorecard)

    assert validate_result_dir(result_dir) == []


def test_public_result_schema_allows_non_pass_failures() -> None:
    schema = json.loads(Path("docs/testing/agent-autonomous/result-schema.json").read_text())

    failures_schema = schema["properties"]["failures"]

    assert failures_schema["type"] == "array"
    assert "maxItems" not in failures_schema


def test_public_result_schema_rejects_pass_failures() -> None:
    schema = json.loads(Path("docs/testing/agent-autonomous/result-schema.json").read_text())

    pass_condition = schema["allOf"][0]

    assert pass_condition["if"]["properties"]["status"]["const"] == "pass"
    assert pass_condition["then"]["properties"]["failures"]["maxItems"] == 0


def test_llm_backed_result_allows_honest_fail_status(tmp_path: Path) -> None:
    result_dir = tmp_path / "failed-provider-smoke"
    scenario = "provider-live-smoke-deepseek"
    _write_base_llm_result(
        result_dir,
        scenario,
        {
            "provider_live_summary": _summary(
                scenario,
                status="fail",
                call_attempted=True,
                call_status="error",
                worldengine_owned_call=True,
            )
        },
    )
    result = json.loads((result_dir / "result.json").read_text())
    result["status"] = "fail"
    result["score_items"] = [{"name": "provider_live_smoke", "status": "fail", "evidence": "provider-live-summary.json"}]
    result["failures"] = [{"taxonomy": "provider", "message": "provider returned an error"}]
    _write_json(result_dir / "result.json", result)
    scorecard = json.loads((result_dir / "scorecard-summary.json").read_text())
    scorecard["status"] = "fail"
    _write_json(result_dir / "scorecard-summary.json", scorecard)

    assert validate_result_dir(result_dir) == []


def test_llm_backed_result_allows_honest_not_run_status(tmp_path: Path) -> None:
    result_dir = tmp_path / "not-run-provider-smoke"
    scenario = "provider-live-smoke-deepseek"
    _write_base_llm_result(
        result_dir,
        scenario,
        {
            "provider_live_summary": _summary(
                scenario,
                status="not_run",
                call_attempted=False,
                call_status="not_run",
                worldengine_owned_call=True,
            )
        },
    )
    result = json.loads((result_dir / "result.json").read_text())
    result["status"] = "not_run"
    result["score_items"] = [{"name": "provider_live_smoke", "status": "not_run", "evidence": "provider-live-summary.json"}]
    result["unverified_items"] = [
        {"severity": "P3", "status": "accepted", "resolved": True, "message": "scenario not executed"}
    ]
    _write_json(result_dir / "result.json", result)
    scorecard = json.loads((result_dir / "scorecard-summary.json").read_text())
    scorecard["status"] = "not_run"
    _write_json(result_dir / "scorecard-summary.json", scorecard)

    assert validate_result_dir(result_dir) == []


def test_llm_backed_world_creation_generic_fallback_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "generic-fallback"
    scenario = "llm-backed-world-creation"
    _write_base_llm_result(
        result_dir,
        scenario,
        {
            "world_creation_summary": _summary(
                scenario,
                llm_backed=True,
                deterministic_generic_fallback_detected=True,
            ),
            "world_rule_summary": _summary(
                scenario,
                parameters=[{"name": "temperature"}],
                evolution_rules=[{"id": "rule.temperature"}],
                event_legality_rules=[{"id": "event.weather"}],
            ),
        },
    )

    errors = validate_result_dir(result_dir)

    assert any("deterministic_generic_fallback_detected" in error for error in errors)


def test_llm_backed_rule_parameter_unexplained_change_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "rule-parameter-unexplained"
    scenario = "world-rule-parameter-evolution"
    _write_base_llm_result(
        result_dir,
        scenario,
        {
            "rule_parameter_summary": _summary(
                scenario,
                changed_parameters=[{"name": "temperature", "rule_ref": "rule.temperature"}],
                unexplained_changes=[{"name": "humidity"}],
                fixed_counter_only_detected=False,
            ),
            "diff_replay_summary": _summary(scenario, replay_supported=True),
        },
    )

    errors = validate_result_dir(result_dir)

    assert any("unexplained_changes must be empty" in error for error in errors)


def test_llm_backed_rule_parameter_fixed_counter_only_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "rule-parameter-fixed-counter"
    scenario = "world-rule-parameter-evolution"
    _write_base_llm_result(
        result_dir,
        scenario,
        {
            "rule_parameter_summary": _summary(
                scenario,
                changed_parameters=[{"name": "temperature", "rule_ref": "rule.temperature"}],
                unexplained_changes=[],
                fixed_counter_only_detected=True,
            ),
            "diff_replay_summary": _summary(scenario, replay_supported=True),
        },
    )

    errors = validate_result_dir(result_dir)

    assert any("fixed_counter_only_detected must be false" in error for error in errors)


def test_llm_backed_event_legality_direct_final_state_mutation_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "event-direct-final-state"
    scenario = "rule-compliant-event-generation"
    _write_base_llm_result(
        result_dir,
        scenario,
        {
            "event_legality_summary": _summary(
                scenario,
                rule_adjudications=[{"rule_ref": "event.weather", "status": "accepted"}],
                direct_final_state_mutation_detected=True,
            )
        },
    )

    errors = validate_result_dir(result_dir)

    assert any("direct_final_state_mutation_detected must be false" in error for error in errors)


def test_llm_backed_agent_persistent_single_event_only_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "agent-single-event"
    scenario = "agent-persistent-autonomy-evidence"
    _write_base_llm_result(
        result_dir,
        scenario,
        {
            "agent_autonomy_summary": _summary(
                scenario,
                decision_moments=["tick-1"],
                client_scripted_action_detected=False,
                single_event_only_detected=True,
            )
        },
    )

    errors = validate_result_dir(result_dir)

    assert any("decision_moments must contain at least two entries" in error for error in errors)
    assert any("single_event_only_detected must be false" in error for error in errors)


def test_llm_backed_agent_persistent_client_scripted_action_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "agent-client-scripted"
    scenario = "agent-persistent-autonomy-evidence"
    _write_base_llm_result(
        result_dir,
        scenario,
        {
            "agent_autonomy_summary": _summary(
                scenario,
                decision_moments=["tick-1", "tick-2"],
                client_scripted_action_detected=True,
                single_event_only_detected=False,
            )
        },
    )

    errors = validate_result_dir(result_dir)

    assert any("client_scripted_action_detected must be false" in error for error in errors)


def test_llm_backed_redaction_leak_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "redaction-leak"
    _write_valid_llm_full_lifecycle_result(result_dir)
    scan = json.loads((result_dir / "redaction-scan.json").read_text())
    scan["redaction"]["raw_provider_responses_included"] = True
    _write_json(result_dir / "redaction-scan.json", scan)

    errors = validate_result_dir(result_dir)

    assert any("redaction flags must all be false" in error for error in errors)


def test_llm_backed_redaction_private_evaluator_marker_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "private-evaluator-marker"
    _write_valid_llm_full_lifecycle_result(result_dir)
    scan = json.loads((result_dir / "redaction-scan.json").read_text())
    scan["public_note"] = "private evaluator data included"
    _write_json(result_dir / "redaction-scan.json", scan)

    errors = validate_result_dir(result_dir)

    assert any("private evaluator" in error or "evaluator data" in error for error in errors)


def test_llm_backed_redaction_external_seed_oracle_marker_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "external-seed-oracle-marker"
    _write_valid_llm_full_lifecycle_result(result_dir)
    scan = json.loads((result_dir / "redaction-scan.json").read_text())
    scan["public_note"] = "external world seed and oracle content were retained"
    _write_json(result_dir / "redaction-scan.json", scan)

    errors = validate_result_dir(result_dir)

    assert any("external world seed" in error or "oracle content" in error for error in errors)


def test_llm_backed_full_lifecycle_missing_second_agent_review_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "missing-second-agent-review"
    _write_valid_llm_full_lifecycle_result(result_dir)
    result = json.loads((result_dir / "result.json").read_text())
    result["required_artifacts"].remove("second_agent_review")
    result["artifacts"].pop("second_agent_review")
    _write_json(result_dir / "result.json", result)

    errors = validate_result_dir(result_dir)

    assert any("second_agent_review" in error for error in errors)


def test_llm_backed_full_lifecycle_missing_critical_score_item_fails(tmp_path: Path) -> None:
    result_dir = tmp_path / "missing-critical-score-item"
    _write_valid_llm_full_lifecycle_result(result_dir)
    result = json.loads((result_dir / "result.json").read_text())
    result["score_items"] = [
        item for item in result["score_items"] if item["name"] != "provider_live_smoke"
    ]
    _write_json(result_dir / "result.json", result)

    errors = validate_result_dir(result_dir)

    assert any("provider_live_smoke" in error for error in errors)
