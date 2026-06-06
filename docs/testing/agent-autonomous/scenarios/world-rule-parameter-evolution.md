# World Rule Parameter Evolution

Status: saved-result-checker-supported / live evidence not run

Parent plan: `docs/testing/llm-backed-lifecycle-validation-plan.md`.

## Goal

Prove generated world parameters evolve across ticks according to WorldEngine
rules, not static counters or hard-coded mock behavior.

## Required Operations

- Start from an LLM-backed world with public parameters and rules.
- Advance multiple ticks.
- Capture parameter diffs, events, snapshots, and replay references.
- Verify material parameter changes have public rule references or public
  legality explanations.

## Forbidden Operations

- Static counter-only tick progression is reported as rule evolution.
- Direct mutation without rule evidence is reported as valid.
- Validation Client calculates authoritative world parameter changes.
- Hidden implementation details are exported as proof.

## Required Artifacts

- `result.json`
- `operation-log.jsonl`
- `api-summary.json`
- `rule-parameter-summary.json`
- `world-lifecycle-summary.json`
- `diff-replay-summary.json`
- event artifacts
- snapshot artifacts
- `redaction-scan.json`
- `scorecard-summary.json` or checker output

## PASS Source

PASS requires checker or scorecard output showing rule-linked parameter changes
across ticks.

## FAIL Taxonomy

- `world_evolution`
- `world_creation`
- `redaction`
- `client_evidence`
- `checker_gap`

## Redaction Requirements

Public rule ids, public explanations, parameter names, values, and diffs are
allowed. Private provider traces, raw prompt text, raw response text, and
hidden reasoning are forbidden.
