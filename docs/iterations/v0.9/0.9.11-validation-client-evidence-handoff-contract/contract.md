# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

- `validation_client_evidence_bundle`: a directory exported by a client that
  contains only public, redacted evidence artifacts.
- `evidence_bundle_manifest`: a JSON manifest describing artifact names,
  relative paths, producer identity, schema versions, scenario, status, and
  checker compatibility.
- `display_artifact`: a public artifact that may be shown to a human without
  exposing provider secrets, raw prompts, raw provider responses, private Agent
  memory, hidden context, raw thought, private evaluator data, or external
  seed/oracle content.
- `export_artifact`: a public artifact that may be written into a saved-result
  directory for checker consumption.
- `client_role`: `display_export_only`.
- `evaluator_role`: `worldengine_checker_or_second_agent_review`.
- `provider_owner`: `worldengine`.

## Required Artifact Set

A complete LLM-backed lifecycle handoff should be able to reference these
named artifacts when the scenario requires them:

- `result.json`
- `operation-log.jsonl`
- `provider-live-summary.json`
- `world-creation-summary.json`
- `world-rule-summary.json`
- `rule-parameter-summary.json`
- `event-legality-summary.json`
- `agent-autonomy-summary.json`
- `diff-replay-summary.json`
- `world-lifecycle-summary.json`
- `narrative-projection-summary.json`
- `diagnostic-conversation-summary.json`
- `redaction-scan.json`
- `scorecard-summary.json`
- `second-agent-review.md`
- optional screenshots or public transcript files.

The client may omit artifacts that are not required for the active scenario,
but it must not relabel missing required artifacts as PASS.

## Manifest Requirements

`evidence_bundle_manifest` must include:

- `schema_version`
- `bundle_id`
- `scenario`
- `result_status`
- `client_role`
- `provider_owner`
- `evaluator_role`
- `created_at`
- `artifact_index`
- `redaction_status`
- `checker_contract`
- `unsupported_items`

`artifact_index` entries must include:

- `name`
- `path`
- `required`
- `displayable`
- `exportable`
- `producer`
- `schema_version`
- `redaction_status`

All paths must be relative and stay inside the evidence bundle.

## Compatibility Constraints

- The handoff contract must remain additive and redacted.
- Existing 0.9.10 checker artifact names remain authoritative for saved-result
  validation.
- Client export may copy or bundle public artifacts, but must not transform
  redacted PASS-critical fields into new meanings.
- The client must preserve `pass`, `fail`, `blocked`, and `not_run` status
  values rather than mapping them into UI-only labels.

## Allowed Changes

- This package directory.
- Parent v0.9 route/status/review docs.
- Documentation-only public handoff specs in this repository if needed.

## Forbidden Changes

- No Validation Client repository implementation.
- No WorldEngine backend runtime behavior changes.
- No checker implementation or fixture changes.
- No provider live calls or provider credential handling.
- No frontend implementation.
- No generated-result creation or rewrite.
- No external validation execution.
- No new runtime features under `backend/worldengine/`.

## Boundary Rules

- The client must not own LLM calls, provider keys, provider readiness truth, or
  generated world content.
- The client must not decide PASS. It may display checker status and reviewer
  findings.
- The client must not expose raw prompts, raw provider requests/responses,
  provider traces, authorization headers, API keys, private Agent memory,
  private Agent goals, raw thought, hidden context, private evaluator data, or
  external seed/oracle content.
- The client must not convert narrative projection or diagnostic conversation
  into canonical world events or Agent memory.

## North Star Check

This package helps external validation consume WorldEngine evidence without
turning the engine into an application-specific backend or moving core LLM
behavior into a client.

## Out-of-Scope Follow-ups

- `0.9.12` owns live or explicitly blocked LLM-backed full lifecycle validation
  execution evidence.
- Validation Client implementation belongs to a separate repository or
  explicitly authorized future milestone.
