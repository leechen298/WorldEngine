# Plan

## Objective

Create the full `0.8.5-core-working-state-smoke-evidence` package and prepare
it for documentation/contract review before any evidence commands run.

## Authoritative Inputs Read

- `AGENTS.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.8/CURRENT_STATE.md`
- `docs/iterations/v0.8/GOAL_RUNNER.md`
- `docs/iterations/v0.8/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.8/v0.8-plan.md`
- `docs/iterations/v0.8/0.8.1-minimum-working-state-contract/contract.md`
- `docs/iterations/v0.8/0.8.2-core-observable-surface-boundary/contract.md`
- `docs/iterations/v0.8/0.8.3-generation-runtime-agent-loop-readiness/review.md`
- `docs/iterations/v0.8/0.8.4-external-validation-handoff-contract/contract.md`
- `docs/testing/product-capability-validation-playbook.md`
- `docs/current-implementation.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`

## Documentation Type

Mixed validation package, documentation stage. This package may later run
evidence commands after review authorization, but drafting this package does
not run evidence and does not change implementation files.

## Files To Create Or Update

Create:

- `README.md` / `README.zh.md`
- `intent.md` / `intent.zh.md`
- `contract.md` / `contract.zh.md`
- `technical-design.md` / `technical-design.zh.md`
- `test-plan.md` / `test-plan.zh.md`
- `plan.md` / `plan.zh.md`
- `review.md` / `review.zh.md`

Update parent v0.8 status surfaces to `0.8.5 ready for review` after the
package files exist.

## Files Explicitly Out Of Scope

- runtime, schema, API, frontend, backend test, checker implementation,
  fixture, migration, generated result, external repository, external
  validator code, external application code, and `backend/worldengine/` files
  during documentation drafting.

## Required Package Status Values

Before review:

- package `Status: planned / ready for review`.
- `implementation_authorized: no`.
- `evidence_execution_authorized: no`.
- parent status `in progress / 0.8.5 ready for review`.

After documentation/contract evaluator PASS:

- package may become `ready for evidence execution`.
- `implementation_authorized: no` unless the contract is updated and reviewed.
- `evidence_execution_authorized: yes`, limited to exact `test-plan.md`
  commands.

## Allowed Changes

- Documentation under this package.
- Parent v0.8 route/status/review synchronization.
- After review only: run authorized evidence commands and record evidence.

## Forbidden Changes

- Implementation changes during documentation drafting.
- External validator or external application execution.
- Product-specific validation data.
- Unreviewed result artifacts.
- Overclaiming skipped, blocked, out-of-scope, historical, or documentation
  evidence as PASS.

## Review Gates

1. Create full docs and mirrors.
2. Run documentation shape/status/scope/text guards.
3. Ask a read-only documentation/contract evaluator to check scope, command
   matrix, authorization, non-claims, and handoff compatibility.
4. Fix P1/blocking P2 findings.
5. Record review results and, if approved, bounded evidence execution
   authorization.

## Verification Commands

Documentation stage:

- `git diff --check`
- required child docs and mirrors check.
- parent/child status consistency check.
- changed-file scope guard.
- v0.8 Markdown whitespace check.
- command-matrix and overclaim scans.

Evidence stage after review:

- exact commands listed in `test-plan.md` only.

## Stop Conditions

Stop before evidence execution if:

- the documentation/contract evaluator reports P1 or blocking P2.
- the command matrix does not cover required core surfaces or classify gaps.
- evidence would require private external validation data.
- product code must be changed for validation to pass.
- external validator or external application execution becomes required.

## Handoff After Review

If documentation review passes, hand off to evidence execution for the exact
authorized commands. If evidence later passes or blockers are recorded, hand
off to `0.8.6-v0.8-evidence-and-boundary-audit`.
