# Plan

Status: planned / ready for review

## Objective

Prepare a documentation-only audit package for reviewed v0.8 evidence and
boundaries before release-candidate packaging.

## Authoritative Inputs

- `AGENTS.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.8/CURRENT_STATE.md`
- `docs/iterations/v0.8/GOAL_RUNNER.md`
- `docs/iterations/v0.8/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.8/v0.8-plan.md`
- `docs/iterations/v0.8/review.md`
- `docs/iterations/v0.8/0.8.0-v0.8-planning-and-v0.7-handoff-baseline/review.md`
- `docs/iterations/v0.8/0.8.1-minimum-working-state-contract/review.md`
- `docs/iterations/v0.8/0.8.2-core-observable-surface-boundary/review.md`
- `docs/iterations/v0.8/0.8.3-generation-runtime-agent-loop-readiness/review.md`
- `docs/iterations/v0.8/0.8.4-external-validation-handoff-contract/review.md`
- `docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/review.md`
- `docs/testing/results/2026-06-02-v0.7-code-review.md`
- `docs/testing/results/2026-06-02-v0.7-overall-validation.md`

## Steps

1. Create the full `0.8.6` package document set and Chinese mirrors.
2. Create `audit-report.md` and `audit-report.zh.md` templates.
3. Sync parent v0.8 status to ready-for-review.
4. Run documentation checks and scope/status guards.
5. Request read-only documentation/contract review.
6. If review passes, authorize documentation-only audit execution.
7. Fill audit report and package review from authorized audit checks.
8. Request validation/closeout review before handing off to `0.8.7`.

## Stop Conditions

- Stop if required input reviews are missing.
- Stop if any evidence reference cannot be located during audit execution.
- Stop if the audit needs runtime, API, frontend, test, checker, fixture,
  migration, generated-result, external repo, external validator/app, or
  `backend/worldengine/` changes.
- Stop if any P1 or blocking P2 would be hidden or converted into PASS.
- Stop if audit language implies final v0.8 readiness, product readiness, or
  external validation PASS.

## Current Stage

Documentation stage only. Audit execution, implementation, and evidence
execution remain unauthorized until review.
