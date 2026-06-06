# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Current State

`tools/testing/validate_agent_autonomous_result.py` currently validates saved
autonomous result directories for dashboard scenarios and the basic
`worldengine-full-lifecycle-autonomous` scenario. It checks result metadata,
relative artifact paths, operation-log structure, score item PASS status,
scorecard summary, basic public evidence redaction markers, and a
`world-lifecycle-summary.json` shape for the basic full lifecycle scenario.

`docs/testing/agent-autonomous/result-schema.json` only enumerates the current
basic autonomous scenarios. The LLM-backed scenario docs and artifact contract
are still `planned / checker-extension-required`.

## Contract Alignment and Invariants

- The checker remains a saved-result checker. It must not start services,
  mutate product state, call providers, or rewrite result artifacts.
- Existing scenarios keep their current PASS-only success semantics.
- LLM-backed scenarios get explicit status classification and stricter PASS
  checks.
- Redaction checks must scan both artifact payloads and artifact names/field
  names, with documented safe exceptions only.
- Full lifecycle PASS must require both deterministic checker/scorecard PASS
  and second-Agent review clean status.

## Proposed Implementation

1. Add LLM-backed scenario constants, scenario-specific required artifact maps,
   allowed statuses, and taxonomy maps.
2. Split status validation so existing scenarios still require `status=pass`,
   while LLM-backed scenarios may be `pass`, `fail`, `blocked`, or `not_run`.
3. Add JSON loaders for LLM-backed summary artifacts:
   - `provider-live-summary.json`
   - `world-creation-summary.json`
   - `world-rule-summary.json`
   - `rule-parameter-summary.json`
   - `event-legality-summary.json`
   - `agent-autonomy-summary.json`
   - `diff-replay-summary.json`
   - `world-lifecycle-summary.json`
   - `redaction-scan.json`
   - `scorecard-summary.json`
4. Add scenario-specific validators for PASS-critical fields. These validators
   should reject PASS when required public signals are missing or contradict
   the artifact contract.
5. Add blocked/not-run classification checks: `blocked` and `not_run` require
   non-empty `failures` or `unverified_items` with scenario taxonomy, and must
   not be described as PASS.
6. Add fixture directories for at least:
   - valid or blocked provider live smoke result.
   - valid LLM-backed world creation result.
   - valid rule parameter evolution result.
   - valid rule-compliant event generation result.
   - valid Agent persistent autonomy result.
   - valid full lifecycle result.
   - invalid redaction leak.
   - invalid missing critical artifact.
   - invalid full lifecycle missing second-Agent review.
   - invalid PASS with blocked scorecard item.
7. Update `result-schema.json` and documentation statuses to reflect checker
   support after implementation evidence exists.

## Affected Surfaces

- `tools/testing/validate_agent_autonomous_result.py`
- `tools/testing/test_validate_agent_autonomous_result.py`
- `tools/testing/fixtures/agent-autonomous/**`
- `docs/testing/agent-autonomous/result-schema.json`
- LLM-backed testing docs and this package docs.

## Data Model / Schema Changes

`result.json` remains additive. Existing fields stay required. LLM-backed
scenarios add support for non-PASS status values and scenario-specific artifact
requirements.

Summary artifacts use the documented fields in
`llm-backed-artifact-contract.md`. PASS requires their redaction booleans and
critical evidence fields to match the scorecard.

## Runtime / Service Design

No runtime or service code is changed. The checker reads files from a saved
result directory and emits validation errors. It is intentionally detached from
live provider execution.

## Compatibility

Existing fixtures and `make validate-agent-autonomous-fixtures` must still
pass. Existing failures must still fail. New LLM-backed fixtures must not make
older dashboard result directories invalid.

## Risks

- Overly weak checker rules could rubber-stamp missing LLM-backed evidence.
  Scenario-specific PASS-critical checks and negative fixtures cover this.
- Overly broad redaction scanning could reject safe field labels. Safe
  exceptions must be explicit and tested.
- Allowing `blocked` and `not_run` could blur PASS. The checker must preserve a
  clear distinction: only `pass` with all critical items passing can be PASS.
