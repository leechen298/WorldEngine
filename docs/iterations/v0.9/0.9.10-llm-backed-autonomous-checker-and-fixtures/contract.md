# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

- `LLM_BACKED_SCENARIOS`: the six LLM-backed autonomous scenario names:
  `provider-live-smoke-deepseek`, `llm-backed-world-creation`,
  `world-rule-parameter-evolution`, `rule-compliant-event-generation`,
  `agent-persistent-autonomy-evidence`, and
  `llm-backed-full-lifecycle-autonomous`.
- `llm_backed_result_status`: scenario status values `pass`, `fail`,
  `blocked`, and `not_run`.
- `llm_backed_artifact_summary`: required public JSON artifacts described by
  `docs/testing/agent-autonomous/llm-backed-artifact-contract.md`.
- `llm_backed_scorecard_item`: deterministic critical items from
  `docs/testing/agent-autonomous/llm-backed-scorecard.md`.
- `redaction_scan`: public evidence that forbidden markers are absent.
- `second_agent_review_status`: read-only review result for full lifecycle
  PASS gating.

## Compatibility Constraints

- Existing saved-result checker behavior for dashboard scenarios and
  `worldengine-full-lifecycle-autonomous` must remain compatible.
- Existing fixture commands must still work:
  `make validate-agent-autonomous-result RESULT_DIR=<dir>` and
  `make validate-agent-autonomous-fixtures`.
- Result schema extensions must be additive. Existing valid basic fixtures must
  not require LLM-backed artifacts.
- LLM-backed scenarios may be accepted as `blocked` or `not_run` when required
  public artifacts honestly classify missing provider/evidence prerequisites.
- A `pass` result must be stricter than `blocked` or `not_run`; missing
  critical artifacts, redaction leaks, failed critical items, or missing
  second-Agent review must prevent PASS.

## Allowed Changes

- `tools/testing/validate_agent_autonomous_result.py`
- `tools/testing/test_validate_agent_autonomous_result.py`
- `tools/testing/fixtures/agent-autonomous/**`
- `docs/testing/agent-autonomous/result-schema.json`
- LLM-backed autonomous testing docs under `docs/testing/agent-autonomous/**`
- this package directory and parent v0.9 routing/review docs.

## Forbidden Changes

- No WorldEngine product runtime behavior changes.
- No provider live calls or provider credential handling.
- No frontend UI implementation.
- No Validation Client repository implementation.
- No generated-result rewrites to force PASS.
- No concrete external validation world seed data in this repository.
- No new runtime features under `backend/worldengine/`.
- No changes to `backend/app/**`. The intended implementation scope is
  `tools/testing` plus docs and fixtures.

## Required Checker Semantics

- Extend supported scenarios to include the six LLM-backed scenario names.
- Permit `status` values `pass`, `fail`, `blocked`, and `not_run` for
  LLM-backed scenarios, while preserving the existing successful-result
  behavior for older scenarios.
- Require every declared `required_artifacts` entry to exist and stay inside
  the result directory.
- Validate scenario-specific required artifact names from the artifact
  contract.
- Reject PASS when `redaction` or `redaction-scan.json` includes API keys,
  authorization headers, raw prompts, raw provider requests, raw provider
  responses, provider traces, private Agent memory, private Agent goals, raw
  thought, raw chain-of-thought, hidden context, private evaluator data, or
  concrete external-world seed/oracle content.
- Reject PASS when scorecard critical items are absent, non-pass, unsupported,
  or lack public evidence.
- For `llm-backed-full-lifecycle-autonomous`, require all component summaries,
  `scorecard-summary.json`, and `second-agent-review.md` with no blocking P1/P2
  finding before PASS.
- Classify missing checker support or missing required evidence as
  `checker_gap`, `client_evidence`, or the scenario-specific taxonomy, not PASS.

## North Star Check

This package makes public evidence machine-checkable. It does not add
application-specific backend behavior, concrete worlds, product UI, or hidden
LLM truth.

## Out-of-Scope Follow-ups

- `0.9.11` owns Validation Client evidence handoff contracts.
- `0.9.12` owns live or blocked LLM-backed full lifecycle execution evidence.
- Future packages may add stricter semantic checks after real result artifacts
  expose more public structure.
