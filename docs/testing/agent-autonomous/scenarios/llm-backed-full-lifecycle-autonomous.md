# LLM-backed Full Lifecycle Autonomous Validation

Status: saved-result-checker-supported / live evidence not run

Parent plan: `docs/testing/llm-backed-lifecycle-validation-plan.md`.

## Goal

Prove the complete LLM-backed lifecycle: provider live smoke, LLM-backed world
creation, rule-driven evolution, rule-compliant events, persistent Agent
autonomy evidence, evidence export, checker PASS, and second-Agent read-only
review.

## Required Operations

- Run `provider-live-smoke-deepseek` or consume an accepted same-session
  provider live smoke prerequisite.
- Create an LLM-backed world from a basic user premise.
- Advance ticks until rule-driven parameter evolution, events, snapshots, and
  diffs are visible.
- Submit at least one external environmental direction and validate legality.
- Observe multi-round Agent autonomy evidence.
- Export evidence bundle from the Validation Client.
- Run WorldEngine checker or scorecard over the result directory.
- Run second-Agent read-only evidence review.

## Forbidden Operations

- UI smoke is treated as full lifecycle PASS.
- Provider readiness is treated as live call proof.
- Deterministic generic world output is treated as LLM-backed.
- Direct API calls are recorded as Agent operation-log operations.
- Client scripts Agent actions.
- User direction is written directly as final state.
- Raw prompt, raw response, API key, private memory, raw thought, or hidden
  context appears in evidence.

## Required Artifacts

- `result.json`
- `operation-log.jsonl`
- `transcript.md`
- `console.log`
- screenshots
- `api-summary.json`
- `provider-live-summary.json`
- `world-creation-summary.json`
- `world-rule-summary.json`
- `rule-parameter-summary.json`
- `event-legality-summary.json`
- `agent-autonomy-summary.json`
- `diff-replay-summary.json`
- `world-lifecycle-summary.json`
- `validation-client-evidence-bundle.json`
- `scorecard-summary.json`
- `second-agent-review.md`

## PASS Source

PASS requires WorldEngine checker or scorecard PASS for all critical items plus
second-Agent read-only review with no blocking P1 or P2 issue.

## FAIL Taxonomy

- `provider`
- `world_creation`
- `world_evolution`
- `event_legality`
- `agent_autonomy`
- `redaction`
- `client_evidence`
- `checker_gap`

## Redaction Requirements

All component scenario redaction requirements apply. Any leak of API key,
authorization header, raw prompt, raw response, provider trace, private
memory, private goal, raw thought, raw chain-of-thought, or hidden context is
immediate FAIL.
