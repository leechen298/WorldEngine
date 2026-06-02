# Plan

Status: documentation-stage plan

## Objective

Create a complete `0.8.7-v0.8-release-candidate-bundle` document package and
prepare it for read-only review.

## Authoritative Inputs Read

- `AGENTS.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.8/GOAL_RUNNER.md`
- `docs/iterations/v0.8/v0.8-plan.md`
- `docs/iterations/v0.8/0.8.6-v0.8-evidence-and-boundary-audit/audit-report.md`
- `docs/iterations/v0.8/0.8.6-v0.8-evidence-and-boundary-audit/review.md`

## Documentation Type

Documentation-only release-candidate package. Because it changes release
status, evidence rules, package sequencing, and automation-consumption
contracts, the package includes `technical-design.md` and `test-plan.md`.

## Files To Create Or Update

Create:

- `README.md` and `README.zh.md`
- `intent.md` and `intent.zh.md`
- `contract.md` and `contract.zh.md`
- `technical-design.md` and `technical-design.zh.md`
- `test-plan.md` and `test-plan.zh.md`
- `plan.md` and `plan.zh.md`
- `review.md` and `review.zh.md`
- `release-candidate-summary.md` and `release-candidate-summary.zh.md`

Update parent v0.8 status surfaces only to record this package as ready for
review.

## Out Of Scope

- Runtime, schema, API, frontend, backend tests, checker implementation,
  fixtures, migrations, generated results, external repositories, external
  validator implementation, external app implementation, deployment, and
  `backend/worldengine/`.
- New validation execution.
- Final v0.8 closeout.

## Execution Steps

1. Create the package directory and all required docs.
2. Draft release-candidate summary with bounded evidence references.
3. Update parent status surfaces to `0.8.7 ready for review`.
4. Run documentation checks from `test-plan.md`.
5. Request/read documentation evaluator feedback before any review-complete
   status.
6. If review passes, update this package review and parent route according to
   evaluator recommendation.

## Stop Conditions

Stop if evidence references are missing, status surfaces drift, private
details appear, any summary claim implies final release, or any P1/P2 finding
blocks release-candidate review.
