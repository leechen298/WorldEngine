# Complete Product Validation Evidence Contract

Status: planned evidence contract

Chinese mirror: `evidence-contract.zh.md`.

## Purpose

This contract defines the minimum artifacts and redaction expectations for
complete WorldEngine product validation. A future checker may implement these
requirements, but this document is already the documentation-level contract.

## Standard Result Directory

Recommended result directory:

```text
test-results/product-validation/<timestamp>-complete-product-validation/
```

Recommended files:

```text
result.json
coverage-matrix.json
command-matrix.md
operation-log.jsonl
api-summary.json
console.log
transcript.md
redaction-scan.json
second-agent-review.md
artifacts/
raw/
```

If an LLM-backed autonomous run is included, its dedicated result directory
should be:

```text
test-results/agent-autonomous/<timestamp>-llm-backed-full-lifecycle/
```

## `result.json`

Minimum fields:

- `scenario`.
- `goal`.
- `mode`.
- `status`.
- `verdict`.
- `verdict_source`.
- `scope`.
- `started_at`.
- `completed_at`.
- `required_artifacts`.
- `artifacts`.
- `coverage_summary`.
- `failures`.
- `unresolved_findings`.
- `redaction`.

`verdict_source` must be one of:

- `command_matrix`.
- `deterministic_checker`.
- `scorecard_checker`.
- `saved_result_checker`.
- `second_agent_review`.
- `mixed_current_session_evidence`.

## `coverage-matrix.json`

Every CPV row from `coverage-map.md` must be represented.

Minimum row fields:

- `id`.
- `capability_area`.
- `scope_status`: `in_scope`, `out_of_scope`, or `future_scope`.
- `validation_status`: `pass`, `fail`, `blocked`, `skipped`, or `not_run`.
- `evidence_source`.
- `commands_or_checkers`.
- `artifacts`.
- `unresolved_findings`.
- `notes`.

## `command-matrix.md`

Record every command or checker used as evidence:

- command.
- working directory.
- environment assumptions.
- start/end time or approximate duration.
- exit code.
- pass/fail count when reported.
- artifact path.
- whether the command can support PASS or only supporting evidence.

## `operation-log.jsonl`

Operation logs are required for Agent-operated flows.

Allowed Agent operation types:

- `ui`.
- `cli`.

Direct HTTP/API calls must not be recorded as Agent operations. Public API
evidence belongs in `api-summary.json`, `api-log.jsonl`, or checker artifacts.

Each line should include:

- `timestamp`.
- `actor`.
- `operation_type`.
- `target`.
- `summary`.
- `status`.
- `artifact_refs`.

Forbidden:

- API keys.
- authorization headers.
- raw request bodies containing prompts or secrets.
- raw provider responses.
- private Agent memory, goals, thought, or hidden context.

## `api-summary.json`

API summaries may include:

- public endpoint.
- method.
- status code.
- public request category.
- public response category.
- latency.
- artifact reference.
- redaction flags.

They must not include:

- raw authorization headers.
- API key values.
- raw prompts.
- raw provider responses.
- private state payloads.

## Redaction Scan

`redaction-scan.json` should record:

- `passed`.
- `scanner_version` or `scanner_source`.
- checked artifact list.
- forbidden marker classes.
- findings by severity.
- whether any finding blocks PASS.

Forbidden marker classes include:

- provider credentials.
- authorization headers.
- raw prompts.
- raw provider requests or responses.
- provider traces.
- local private paths.
- hidden reset APIs.
- UI selector leakage when it reveals private validation logic.
- private evaluator or oracle data.
- private Agent memory, goals, identity, relationships, self-state, raw
  thought, raw chain-of-thought, or hidden context.
- concrete external validation world seed data in core evidence.

## LLM-backed Artifact Summaries

When LLM-backed lifecycle is in scope, the evidence bundle should include:

- `provider-live-summary.json`.
- `world-creation-summary.json`.
- `world-rule-summary.json`.
- `rule-parameter-summary.json`.
- `event-legality-summary.json`.
- `agent-autonomy-summary.json`.
- `diff-replay-summary.json`.
- `scorecard-summary.json`.

These files are specified in
`docs/testing/agent-autonomous/llm-backed-artifact-contract.md` when that
document exists.

## Durable Result Summary

After a run, write a durable summary under:

```text
docs/testing/results/YYYY-MM-DD-complete-product-validation.md
docs/testing/results/YYYY-MM-DD-complete-product-validation.zh.md
```

Use `result-template.md` and `result-template.zh.md`.
