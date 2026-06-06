from __future__ import annotations

import json
import re
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
    "worldengine-full-lifecycle-autonomous",
    "provider-live-smoke-deepseek",
    "llm-backed-world-creation",
    "world-rule-parameter-evolution",
    "rule-compliant-event-generation",
    "agent-persistent-autonomy-evidence",
    "llm-backed-full-lifecycle-autonomous",
}
ALLOWED_VERDICT_SOURCES = {"scorecard_checker", "deterministic_checker"}
FULL_WORLD_LIFECYCLE_SCENARIO = "worldengine-full-lifecycle-autonomous"
LLM_BACKED_SCENARIOS = {
    "provider-live-smoke-deepseek",
    "llm-backed-world-creation",
    "world-rule-parameter-evolution",
    "rule-compliant-event-generation",
    "agent-persistent-autonomy-evidence",
    "llm-backed-full-lifecycle-autonomous",
}
LLM_ALLOWED_STATUSES = {"pass", "fail", "blocked", "not_run"}
LLM_REQUIRED_ARTIFACTS = {
    "provider-live-smoke-deepseek": {"provider_live_summary", "redaction_scan", "scorecard_summary"},
    "llm-backed-world-creation": {
        "world_creation_summary",
        "world_rule_summary",
        "redaction_scan",
        "scorecard_summary",
    },
    "world-rule-parameter-evolution": {
        "rule_parameter_summary",
        "diff_replay_summary",
        "redaction_scan",
        "scorecard_summary",
    },
    "rule-compliant-event-generation": {"event_legality_summary", "redaction_scan", "scorecard_summary"},
    "agent-persistent-autonomy-evidence": {"agent_autonomy_summary", "redaction_scan", "scorecard_summary"},
    "llm-backed-full-lifecycle-autonomous": {
        "provider_live_summary",
        "world_creation_summary",
        "world_rule_summary",
        "rule_parameter_summary",
        "event_legality_summary",
        "agent_autonomy_summary",
        "diff_replay_summary",
        "world_lifecycle_summary",
        "redaction_scan",
        "scorecard_summary",
        "second_agent_review",
    },
}
LLM_FULL_LIFECYCLE_CRITICAL_ITEMS = {
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
}
FORBIDDEN_PUBLIC_EVIDENCE_MARKERS = {
    "api_key",
    "apikey",
    "authorization",
    "credential",
    "hidden context",
    "hidden_context",
    "external world seed",
    "external-world seed",
    "external_world_seed",
    "oracle content",
    "oracle_content",
    "authorization header",
    "private goal",
    "private memory",
    "private evaluator",
    "private_evaluator",
    "evaluator data",
    "evaluator_data",
    "private prompt",
    "private_prompt",
    "provider secret",
    "provider_secret",
    "provider trace",
    "raw request",
    "raw_request",
    "raw prompt",
    "raw_prompt",
    "raw response",
    "raw_response",
    "raw provider request",
    "raw_provider_request",
    "raw provider response",
    "raw_provider_response",
    "raw thought",
    "raw_thought",
    "chain-of-thought",
    "relationship internals",
    "self_state",
    "source_path",
}
SAFE_PUBLIC_EVIDENCE_FIELD_NAMES = {
    "api_keys_included",
    "authorization_headers_included",
    "credential_source_class",
    "hidden_context_included",
    "external_world_seed_included",
    "external_world_oracle_included",
    "private_agent_goals_included",
    "private_agent_memory_included",
    "private_evaluator_data_included",
    "provider_traces_included",
    "raw_prompts_included",
    "raw_provider_requests_included",
    "raw_provider_responses_included",
    "raw_thought_included",
}
PUBLIC_API_CLI_PATTERN = re.compile(
    r"\b(get|post|put|patch|delete)\s+/(manifest|openapi\.json|world|worlds|runtime|archive)\b"
)
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
    FULL_WORLD_LIFECYCLE_SCENARIO: {
        "dashboard",
        "world-create-form",
        "worldengine-session-create-button",
        "runtime-run-button",
        "runtime-tick-counter",
        "agent-life-log",
        "director-guidance-input",
        "evidence-download-button",
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
            command = operation.get("command")
            if not isinstance(command, str) or not command.strip():
                errors.append(f"operation-log.jsonl line {index}.command must be a non-empty string")
            elif result.get("scenario") == FULL_WORLD_LIFECYCLE_SCENARIO:
                lowered_command = command.lower()
                if (
                    "http://" in lowered_command
                    or "https://" in lowered_command
                    or "worldengine public api" in lowered_command
                    or PUBLIC_API_CLI_PATTERN.search(lowered_command)
                ):
                    errors.append(
                        f"operation-log.jsonl line {index} direct public API calls must be "
                        "recorded in api-summary.json, not CLI operations"
                    )
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

    scenario = result.get("scenario")
    result_status = result.get("status")
    for index, item in enumerate(score_items):
        if not isinstance(item, dict):
            errors.append(f"score_items[{index}] must be an object")
            continue
        if not isinstance(item.get("name"), str) or not item["name"].strip():
            errors.append(f"score_items[{index}].name must be a non-empty string")
        status = item.get("status")
        if scenario in LLM_BACKED_SCENARIOS:
            if status not in LLM_ALLOWED_STATUSES:
                errors.append(f"score_items[{index}].status must be pass, fail, blocked, or not_run")
            elif result_status == "pass" and status != "pass":
                errors.append(f"score_items[{index}].status must be pass when result status is pass")
        elif status != "pass":
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
    if result.get("scenario") in LLM_BACKED_SCENARIOS:
        if summary.get("status") not in LLM_ALLOWED_STATUSES:
            errors.append("scorecard-summary.json status must be pass, fail, blocked, or not_run")
        elif result.get("status") == "pass" and summary.get("status") != "pass":
            errors.append("scorecard-summary.json status must be pass when result status is pass")
    elif summary.get("status") != "pass":
        errors.append("scorecard-summary.json status must be pass")
    if summary.get("verdict_source") not in ALLOWED_VERDICT_SOURCES:
        errors.append("scorecard-summary.json verdict_source is invalid")


def _redaction_flags_are_clean(redaction: Any) -> bool:
    if not isinstance(redaction, dict):
        return False
    return all(value is False for value in redaction.values())


def _validate_redaction_scan(result_dir: Path, artifacts: dict[str, Any], errors: list[str]) -> None:
    scan = _artifact_json(result_dir, artifacts, "redaction_scan", errors)
    if not isinstance(scan, dict):
        errors.append("redaction-scan.json must contain an object")
        return
    if scan.get("status") != "pass":
        errors.append("redaction-scan.json status must be pass")
    redaction = scan.get("redaction")
    if not _redaction_flags_are_clean(redaction):
        errors.append("redaction-scan.json redaction flags must all be false for PASS-capable evidence")
    _validate_public_evidence_redaction(scan, "redaction-scan.json", errors)


def _validate_summary_status(summary: dict[str, Any], artifact_name: str, result: dict[str, Any], errors: list[str]) -> None:
    status = summary.get("status")
    if status not in LLM_ALLOWED_STATUSES:
        errors.append(f"{artifact_name} status must be pass, fail, blocked, or not_run")
    elif result.get("status") == "pass" and status != "pass":
        errors.append(f"{artifact_name} status must be pass when result status is pass")
    if "redaction" in summary and not _redaction_flags_are_clean(summary.get("redaction")):
        errors.append(f"{artifact_name} redaction flags must all be false for PASS-capable evidence")
    _validate_public_evidence_redaction(summary, artifact_name, errors)


def _validate_second_agent_review(result_dir: Path, artifacts: dict[str, Any], errors: list[str]) -> None:
    review_path = artifacts.get("second_agent_review")
    if not isinstance(review_path, str) or not review_path.strip():
        errors.append("artifacts.second_agent_review is required")
        return
    path = result_dir / review_path
    try:
        review = path.read_text().lower()
    except FileNotFoundError:
        return
    if "final review verdict: pass" not in review and "final verdict: pass" not in review:
        errors.append("second-agent-review.md must record a PASS final review verdict")
    if "blocking p1" in review or "blocking p2" in review:
        errors.append("second-agent-review.md must not contain blocking P1/P2 findings")


def _validate_llm_backed_artifacts(result_dir: Path, result: dict[str, Any], errors: list[str]) -> None:
    scenario = result.get("scenario")
    if scenario not in LLM_BACKED_SCENARIOS:
        return
    artifacts = result.get("artifacts")
    if not isinstance(artifacts, dict):
        return

    expected = LLM_REQUIRED_ARTIFACTS[scenario]
    missing = sorted(name for name in expected if name not in artifacts)
    if missing:
        errors.append(f"artifacts missing LLM-backed required artifact(s): {', '.join(missing)}")
        return

    _validate_redaction_scan(result_dir, artifacts, errors)

    provider = _artifact_json(result_dir, artifacts, "provider_live_summary", errors) if "provider_live_summary" in expected else None
    if isinstance(provider, dict):
        _validate_summary_status(provider, "provider-live-summary.json", result, errors)
        if result.get("status") == "pass":
            if provider.get("call_attempted") is not True:
                errors.append("provider-live-summary.json call_attempted must be true for PASS")
            if provider.get("call_status") != "success":
                errors.append("provider-live-summary.json call_status must be success for PASS")
            if provider.get("worldengine_owned_call") is not True:
                errors.append("provider-live-summary.json worldengine_owned_call must be true for PASS")

    world_creation = _artifact_json(result_dir, artifacts, "world_creation_summary", errors) if "world_creation_summary" in expected else None
    if isinstance(world_creation, dict):
        _validate_summary_status(world_creation, "world-creation-summary.json", result, errors)
        if result.get("status") == "pass":
            if world_creation.get("llm_backed") is not True:
                errors.append("world-creation-summary.json llm_backed must be true for PASS")
            if world_creation.get("deterministic_generic_fallback_detected") is not False:
                errors.append("world-creation-summary.json deterministic_generic_fallback_detected must be false for PASS")

    world_rule = _artifact_json(result_dir, artifacts, "world_rule_summary", errors) if "world_rule_summary" in expected else None
    if isinstance(world_rule, dict):
        _validate_summary_status(world_rule, "world-rule-summary.json", result, errors)
        if result.get("status") == "pass":
            for field in ("parameters", "evolution_rules", "event_legality_rules"):
                if not world_rule.get(field):
                    errors.append(f"world-rule-summary.json {field} must be non-empty for PASS")

    rule_parameter = _artifact_json(result_dir, artifacts, "rule_parameter_summary", errors) if "rule_parameter_summary" in expected else None
    if isinstance(rule_parameter, dict):
        _validate_summary_status(rule_parameter, "rule-parameter-summary.json", result, errors)
        if result.get("status") == "pass":
            if not rule_parameter.get("changed_parameters"):
                errors.append("rule-parameter-summary.json changed_parameters must be non-empty for PASS")
            if rule_parameter.get("unexplained_changes"):
                errors.append("rule-parameter-summary.json unexplained_changes must be empty for PASS")
            if rule_parameter.get("fixed_counter_only_detected") is not False:
                errors.append("rule-parameter-summary.json fixed_counter_only_detected must be false for PASS")

    event_legality = _artifact_json(result_dir, artifacts, "event_legality_summary", errors) if "event_legality_summary" in expected else None
    if isinstance(event_legality, dict):
        _validate_summary_status(event_legality, "event-legality-summary.json", result, errors)
        if result.get("status") == "pass":
            if not event_legality.get("rule_adjudications"):
                errors.append("event-legality-summary.json rule_adjudications must be non-empty for PASS")
            if event_legality.get("direct_final_state_mutation_detected") is not False:
                errors.append("event-legality-summary.json direct_final_state_mutation_detected must be false for PASS")

    agent_autonomy = _artifact_json(result_dir, artifacts, "agent_autonomy_summary", errors) if "agent_autonomy_summary" in expected else None
    if isinstance(agent_autonomy, dict):
        _validate_summary_status(agent_autonomy, "agent-autonomy-summary.json", result, errors)
        if result.get("status") == "pass":
            if not isinstance(agent_autonomy.get("decision_moments"), list) or len(agent_autonomy["decision_moments"]) < 2:
                errors.append("agent-autonomy-summary.json decision_moments must contain at least two entries for PASS")
            if agent_autonomy.get("client_scripted_action_detected") is not False:
                errors.append("agent-autonomy-summary.json client_scripted_action_detected must be false for PASS")
            if agent_autonomy.get("single_event_only_detected") is not False:
                errors.append("agent-autonomy-summary.json single_event_only_detected must be false for PASS")

    diff_replay = _artifact_json(result_dir, artifacts, "diff_replay_summary", errors) if "diff_replay_summary" in expected else None
    if isinstance(diff_replay, dict):
        _validate_summary_status(diff_replay, "diff-replay-summary.json", result, errors)
        if result.get("status") == "pass" and diff_replay.get("replay_supported") is not True:
            errors.append("diff-replay-summary.json replay_supported must be true for PASS")

    lifecycle = _artifact_json(result_dir, artifacts, "world_lifecycle_summary", errors) if "world_lifecycle_summary" in expected else None
    if isinstance(lifecycle, dict):
        _validate_summary_status(lifecycle, "world-lifecycle-summary.json", result, errors)

    if scenario == "llm-backed-full-lifecycle-autonomous" and result.get("status") == "pass":
        score_names = {
            item.get("name")
            for item in result.get("score_items", [])
            if isinstance(item, dict) and item.get("status") == "pass"
        }
        missing_items = sorted(LLM_FULL_LIFECYCLE_CRITICAL_ITEMS - score_names)
        if missing_items:
            errors.append(f"missing critical LLM-backed score item(s): {', '.join(missing_items)}")
        _validate_second_agent_review(result_dir, artifacts, errors)


def _artifact_json(result_dir: Path, artifacts: dict[str, Any], name: str, errors: list[str]) -> Any:
    relative_path = artifacts.get(name)
    if not isinstance(relative_path, str) or not relative_path.strip():
        errors.append(f"artifacts.{name} is required")
        return None
    return _load_json(result_dir / relative_path, errors)


def _section(summary: dict[str, Any], name: str, errors: list[str]) -> dict[str, Any]:
    raw_section = summary.get(name)
    if not isinstance(raw_section, dict):
        errors.append(f"world-lifecycle-summary.json {name} must be an object")
        return {}
    if raw_section.get("status") != "pass":
        errors.append(f"world-lifecycle-summary.json {name}.status must be pass")
    return raw_section


def _require_true(section: dict[str, Any], section_name: str, field: str, errors: list[str]) -> None:
    if section.get(field) is not True:
        errors.append(f"world-lifecycle-summary.json {section_name}.{field} must be true")


def _require_false(section: dict[str, Any], section_name: str, field: str, errors: list[str]) -> None:
    if section.get(field) is not False:
        errors.append(f"world-lifecycle-summary.json {section_name}.{field} must be false")


def _require_positive_int(section: dict[str, Any], section_name: str, field: str, errors: list[str]) -> None:
    value = section.get(field)
    if not isinstance(value, int) or value <= 0:
        errors.append(f"world-lifecycle-summary.json {section_name}.{field} must be a positive integer")


def _collect_forbidden_public_evidence_markers(payload: Any) -> set[str]:
    leaked: set[str] = set()

    def scan_text(value: str) -> None:
        lowered = value.lower()
        leaked.update(marker for marker in FORBIDDEN_PUBLIC_EVIDENCE_MARKERS if marker in lowered)

    def scan_node(node: Any) -> None:
        if isinstance(node, dict):
            for key, value in node.items():
                key_text = str(key)
                if key_text.lower() not in SAFE_PUBLIC_EVIDENCE_FIELD_NAMES:
                    scan_text(key_text)
                scan_node(value)
            return
        if isinstance(node, list):
            for item in node:
                scan_node(item)
            return
        if isinstance(node, str):
            scan_text(node)

    scan_node(payload)
    return leaked


def _validate_public_evidence_redaction(payload: Any, artifact_name: str, errors: list[str]) -> None:
    leaked = sorted(_collect_forbidden_public_evidence_markers(payload))
    if leaked:
        errors.append(f"{artifact_name} contains forbidden public evidence marker(s): {', '.join(leaked)}")


def _validate_world_lifecycle_artifacts(result_dir: Path, result: dict[str, Any], errors: list[str]) -> None:
    if result.get("scenario") != FULL_WORLD_LIFECYCLE_SCENARIO:
        return

    artifacts = result.get("artifacts")
    if not isinstance(artifacts, dict):
        return

    api_summary = _artifact_json(result_dir, artifacts, "api_summary", errors)
    if isinstance(api_summary, dict):
        if api_summary.get("status") != "pass":
            errors.append("api-summary.json status must be pass")
        if api_summary.get("private_trace_included") is not False:
            errors.append("api-summary.json private_trace_included must be false")
        public_calls = api_summary.get("worldengine_public_calls")
        if not isinstance(public_calls, list) or not public_calls:
            errors.append("api-summary.json worldengine_public_calls must be a non-empty list")
        elif not any(call.get("path") == "/worlds" and call.get("method") == "POST" for call in public_calls if isinstance(call, dict)):
            errors.append("api-summary.json must include POST /worlds public evidence")
        _validate_public_evidence_redaction(api_summary, "api-summary.json", errors)

    lifecycle = _artifact_json(result_dir, artifacts, "world_lifecycle_summary", errors)
    if not isinstance(lifecycle, dict):
        errors.append("world-lifecycle-summary.json must contain an object")
        return
    if lifecycle.get("scenario") != FULL_WORLD_LIFECYCLE_SCENARIO:
        errors.append("world-lifecycle-summary.json scenario must match result.json scenario")
    _validate_public_evidence_redaction(lifecycle, "world-lifecycle-summary.json", errors)

    world_creation = _section(lifecycle, "world_creation", errors)
    if not isinstance(world_creation.get("world_id"), str) or not world_creation["world_id"].strip():
        errors.append("world-lifecycle-summary.json world_creation.world_id must be a non-empty string")
    _require_true(world_creation, "world_creation", "public_initial_state_observed", errors)
    _require_true(world_creation, "world_creation", "visualization_observed", errors)

    runtime_progression = _section(lifecycle, "runtime_progression", errors)
    tick_start = runtime_progression.get("tick_start")
    tick_end = runtime_progression.get("tick_end")
    if not isinstance(tick_start, int) or not isinstance(tick_end, int) or tick_end <= tick_start:
        errors.append("world-lifecycle-summary.json runtime_progression.tick_end must be greater than tick_start")
    _require_positive_int(runtime_progression, "runtime_progression", "events_observed", errors)
    _require_positive_int(runtime_progression, "runtime_progression", "snapshots_observed", errors)

    agent_autonomy = _section(lifecycle, "agent_autonomy", errors)
    _require_positive_int(agent_autonomy, "agent_autonomy", "agent_actions_observed", errors)
    action_types = agent_autonomy.get("unique_action_types")
    if not isinstance(action_types, list) or not action_types:
        errors.append("world-lifecycle-summary.json agent_autonomy.unique_action_types must be a non-empty list")
    _require_false(agent_autonomy, "agent_autonomy", "client_scripted_actions", errors)
    _require_true(agent_autonomy, "agent_autonomy", "worldengine_evidence_observed", errors)

    external_direction = _section(lifecycle, "external_direction", errors)
    _require_true(external_direction, "external_direction", "director_guidance_observed", errors)
    _require_false(external_direction, "external_direction", "direct_agent_private_state_mutation", errors)

    evidence_integrity = _section(lifecycle, "evidence_integrity", errors)
    _require_positive_int(evidence_integrity, "evidence_integrity", "operation_log_entries", errors)
    _require_positive_int(evidence_integrity, "evidence_integrity", "api_trace_entries", errors)
    _require_true(evidence_integrity, "evidence_integrity", "redaction_scan_passed", errors)


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
    if scenario in LLM_BACKED_SCENARIOS:
        status = raw_result.get("status")
        if status not in LLM_ALLOWED_STATUSES:
            errors.append("status must be pass, fail, blocked, or not_run for LLM-backed scenarios")
        elif status != "pass" and not raw_result.get("failures") and not raw_result.get("unverified_items"):
            errors.append("non-pass LLM-backed results must include failures or unverified_items")
    elif raw_result.get("status") != "pass":
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
    elif raw_result["failures"] and (scenario not in LLM_BACKED_SCENARIOS or raw_result.get("status") == "pass"):
        errors.append("failures must be empty when status is pass")

    _validate_artifacts(result_dir, raw_result, errors)
    ui_targets = _validate_operation_log(result_dir, raw_result, errors)
    _validate_required_ui_targets(raw_result, ui_targets, errors)
    _validate_score_items(raw_result, errors)
    _validate_unverified_items(raw_result, errors)
    _validate_scorecard_summary(result_dir, raw_result, errors)
    _validate_world_lifecycle_artifacts(result_dir, raw_result, errors)
    _validate_llm_backed_artifacts(result_dir, raw_result, errors)

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
