# Plan

## Ordered Execution Steps

1. Read governing documents:
   - `AGENTS.md`
   - `docs/iterations/AGENTS.md`
   - `docs/project-north-star.md`
   - `docs/product-model.md`
   - `docs/scope-boundaries.md`
   - `docs/roadmap.md`
   - `docs/iterations/v0.9/README.md`
   - `docs/iterations/v0.9/GOAL_RUNNER.md`
   - `docs/iterations/v0.9/CURRENT_STATE.md`
   - `docs/iterations/v0.9/CAMPAIGN_PLAN.md`
   - `docs/iterations/v0.9/v0.9-plan.md`
   - `docs/iterations/v0.9/review.md`
2. Confirm the active route points to
   `0.9.0-v0.9-planning-and-v0.8-handoff-baseline-documentation-package-needed`.
3. Dispatch read-only subagents/evaluators for v0.9 gate and scope review.
4. Create the `0.9.0` package document set and Chinese mirrors.
5. Synchronize parent v0.9 status surfaces:
   - mark `0.9.0` as `review complete`.
   - select `0.9.1-provider-live-smoke-and-redaction-boundary` as
     documentation-package-needed.
   - keep implementation, evidence execution, provider live-call, audit, and
     external validation authorization closed.
6. Run documentation checks from `test-plan.md`.
7. Reconcile subagent/evaluator findings against source files and command
   evidence.
8. Update `review.md` with changed files, commands, test results,
   compatibility review, scope review, findings, and final assessment.
9. Stop before implementation. Hand off to `0.9.1` documentation-package
   creation.

## Phase Boundaries

Documentation phase:

- May create or update the package documents and parent v0.9 status surfaces.
- May run documentation consistency checks.
- May use read-only subagents/evaluators.

Implementation phase:

- Not authorized in this package.
- Must not start until a future implementation-bearing child package has a
  reviewed contract, technical design, test plan, plan, and `review.md`
  authorization.

Evidence execution phase:

- Not authorized in this package.
- Provider live calls and checker-backed LLM-backed evidence wait for future
  package authorization.

## Stop Conditions

Stop if:

- required `0.9.0` package docs or mirrors are missing.
- parent status surfaces conflict about active child, route, or authorization.
- any runtime, schema, API, frontend, backend test, checker, fixture,
  migration, generated result, external repository, Validation Client,
  provider configuration, or `backend/worldengine/` implementation file would
  be modified.
- a live provider call or evidence execution would be needed.
- subagent/evaluator reports a P0/P1 or blocking P2 that cannot be fixed
  inside this documentation-only scope.
- v0.8 handoff evidence is described as v0.9 PASS evidence.
- LLM-backed testing docs are described as current PASS-capable coverage.
- provider secrets, raw prompts, raw responses, raw traces, private Agent
  memory, raw thought, chain-of-thought, or hidden context would be exposed.

## Review Update Step

Before closeout, update this package `review.md` and mirrors with:

- changed files.
- commands run.
- test results.
- subagent/evaluator evidence.
- compatibility review.
- scope review.
- unresolved findings.
- final assessment and handoff route.
