# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

- `llm_backed_validation_run`: a bounded execution of the documented suite.
- `live_provider_smoke`: a WorldEngine-owned provider call with redacted public
  evidence.
- `validation_result_status`: `pass`, `fail`, `blocked`, or `not_run`.
- `durable_result_summary`: a Markdown record under `docs/testing/results/`.
- `second_agent_review`: read-only evidence review that can block PASS.

## Allowed Changes After Review

- result summaries under `docs/testing/results/`.
- raw ignored result artifacts under `test-results/agent-autonomous/**`.
- this package docs and parent v0.9 route/review docs.

## Execution Authorization After Review

After documentation/contract review passes, this package may authorize:

- starting required local services if already configured.
- running documented basic and LLM-backed validation flows.
- making WorldEngine-owned live provider calls only through documented
  validation commands and only when credentials are already environment-owned.
- running saved-result checker and scorecard commands.
- requesting second-Agent read-only review.
- writing durable result summaries.

## Forbidden Changes

- No code changes to make a failing run pass.
- No generated-result rewrite to force PASS.
- No checker, fixture, or schema changes.
- No Validation Client implementation.
- No frontend implementation.
- No provider credential creation, display, or storage.
- No external validation PASS claim without checker/scorecard/second-Agent
  evidence.
- No raw prompt, raw provider request/response, provider trace, API key,
  authorization header, private Agent memory, private Agent goal, raw thought,
  hidden context, private evaluator data, or seed/oracle evidence.
- No new runtime features under `backend/worldengine/`.

## Required Evidence

A PASS result requires:

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
- `validation-client-evidence-bundle.json` or an explicitly mapped
  `manifest.json`/`evidence_bundle_manifest`
- `redaction-scan.json`
- `scorecard-summary.json`
- `second-agent-review.md`
- checker output proving saved-result validity.

## Stop Rules

Stop and classify when:

- provider cost, quota, rate limit, or network constraints block reliable
  validation.
- no WorldEngine-owned live provider call path exists.
- required artifacts are missing and cannot be regenerated from the same run.
- redaction scan finds a blocking leak.
- checker support is missing for a claimed PASS.
- Agent action is client-scripted or direct user direction mutates final world
  facts.

## Handoff

On PASS or classified FAIL/BLOCKED/NOT_RUN, hand off to
`0.9.13-v0.9-release-candidate-and-closeout`.
