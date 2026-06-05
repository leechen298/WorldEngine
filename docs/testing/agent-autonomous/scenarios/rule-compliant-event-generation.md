# Rule-compliant Event Generation

Status: planned / checker-extension-required

Parent plan: `docs/testing/llm-backed-lifecycle-validation-plan.md`.

## Goal

Prove random events and user-directed external guidance are constrained by
world rules and cannot directly force illegal final outcomes.

## Required Operations

- Run a world with public event legality rules.
- Capture at least one WorldEngine-generated or selected random event.
- Submit at least one natural-language external direction that describes a
  risk, pressure, or environmental tendency rather than a final outcome.
- Verify WorldEngine accepts, rejects, delays, transforms, or resolves the
  direction according to public rules.
- Capture legality summaries plus resulting diffs or snapshots.

## Forbidden Operations

- User direction directly kills, heals, teleports, rewrites, or otherwise
  forces an Agent final state without rule adjudication.
- Validation Client creates authoritative events.
- Impossible events pass without legality status.
- Raw prompt or raw provider response is used as public proof.

## Required Artifacts

- `result.json`
- `operation-log.jsonl`
- `api-summary.json`
- `event-legality-summary.json`
- event artifacts
- snapshot artifacts
- diff artifacts
- `redaction-scan.json`
- `scorecard-summary.json` or checker output

## PASS Source

PASS requires checker or scorecard output showing external direction affected
only external events or environment and WorldEngine decided final outcomes
through public rules.

## FAIL Taxonomy

- `event_legality`
- `world_evolution`
- `agent_autonomy`
- `redaction`
- `client_evidence`
- `checker_gap`

## Redaction Requirements

Public legality summaries, event ids, rule references, and public outcomes are
allowed. Private Agent memory, private goals, hidden context, raw thought, raw
prompt, and raw response are forbidden.
