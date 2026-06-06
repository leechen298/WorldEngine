# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

- `v0.9_closeout_status`: `pass`, `blocked`, or `deferred`.
- `release_candidate_summary`: the parent evidence assessment for v0.9.
- `classified_blocker`: an unresolved gap with taxonomy, evidence, and next
  route.

## Allowed Changes

- this package docs.
- parent v0.9 route/status/review docs.
- durable closeout summary references under existing documentation paths.

## Forbidden Changes

- No backend, frontend, API, schema, checker, fixture, migration, or
  Validation Client implementation changes.
- No live provider calls.
- No new evidence execution.
- No generated-result rewrites to force PASS.
- No product readiness, external validation PASS, or LLM-backed lifecycle PASS
  claim unless current evidence proves it.

## Required Evidence

- 0.9.12 result summary:
  `docs/testing/results/2026-06-06-llm-backed-lifecycle-validation.md`
- 0.9.12 result directory:
  `test-results/agent-autonomous/20260606T142210+0800-llm-backed-full-lifecycle`
- parent and child review docs for `0.9.1` through `0.9.12`.
- status consistency checks after closeout edits.

## Exit Criteria

v0.9 may close as BLOCKED when the closeout docs:

- identify the blocking taxonomy.
- reference checker-valid evidence.
- keep implementation and provider authorization closed.
- avoid product readiness and external validation PASS claims.
- route future work to a narrower repair or future-version plan.
