# LLM-backed Lifecycle Suite Execution

Status: planned runbook / checker-extension-required

Parent plan: `docs/testing/llm-backed-lifecycle-validation-plan.md`.

## Purpose

This is the execution entry point for a future LLM-backed autonomous lifecycle
validation run. It is not executable until the required WorldEngine behavior,
Validation Client evidence fields, and checker support exist.

## Required Reading

- `docs/testing/llm-backed-lifecycle-validation-plan.md`
- `docs/testing/agent-autonomous/scenarios/provider-live-smoke-deepseek.md`
- `docs/testing/agent-autonomous/scenarios/llm-backed-world-creation.md`
- `docs/testing/agent-autonomous/scenarios/world-rule-parameter-evolution.md`
- `docs/testing/agent-autonomous/scenarios/rule-compliant-event-generation.md`
- `docs/testing/agent-autonomous/scenarios/agent-persistent-autonomy-evidence.md`
- `docs/testing/agent-autonomous/scenarios/llm-backed-full-lifecycle-autonomous.md`
- `docs/testing/agent-autonomous/llm-backed-scorecard.md`
- `docs/testing/agent-autonomous/llm-backed-artifact-contract.md`
- `docs/testing/agent-autonomous/second-agent-review-protocol.md`

## Preconditions

- WorldEngine owns provider configuration and provider calls.
- DeepSeek key is available through WorldEngine environment variables.
- Validation Client does not store, show, or forward provider keys.
- A WorldEngine-owned live provider smoke call path exists.
- WorldEngine can generate public LLM-backed world state and rules.
- WorldEngine can evolve parameters and events according to rules.
- WorldEngine can expose public Agent continuity evidence.
- Validation Client can export required evidence artifacts.
- Checker or scorecard support exists for the scenario.

## Execution Sequence

1. Preflight and budget check.
2. Start WorldEngine and Validation Client.
3. Run `provider-live-smoke-deepseek`.
4. Run `llm-backed-world-creation`.
5. Run `world-rule-parameter-evolution`.
6. Run `rule-compliant-event-generation`.
7. Run `agent-persistent-autonomy-evidence`.
8. Export result directory using `llm-backed-result-template.md`.
9. Run checker or scorecard.
10. Run second-Agent read-only review.
11. Write durable result summary under `docs/testing/results/`.

## Stop Rules

Stop and classify FAIL if:

- provider live call cannot be attempted through WorldEngine.
- deterministic generic world output is the only available creation path.
- user direction directly mutates final world state.
- Agent action is client-scripted.
- required artifacts are missing.
- redaction scan finds a blocking leak.
- checker support is missing for the claimed PASS.
- budget, quota, rate limit, or network constraints prevent reliable provider
  validation.

## FAIL Taxonomy

Use one or more:

- `provider`
- `world_creation`
- `world_evolution`
- `event_legality`
- `agent_autonomy`
- `redaction`
- `client_evidence`
- `checker_gap`
