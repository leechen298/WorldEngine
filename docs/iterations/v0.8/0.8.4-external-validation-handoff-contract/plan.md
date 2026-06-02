# Plan

## Objective

Create the full `0.8.4-external-validation-handoff-contract` documentation
package and prepare it for read-only documentation/contract review.

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
- `docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/contract.md`
- `docs/iterations/v0.7/0.7.3-contract-bundle-and-readiness-manifest/contract.md`
- `docs/iterations/v0.7/0.7.4-projection-consumer-read-model-contracts/contract.md`
- `docs/iterations/v0.7/0.7.9-v07-cr-checker-schema-repair/review.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/current-implementation.md`
- `docs/glossary.md`

## Documentation Type

Documentation-only package with full mixed-package shape because it defines
evidence rules, status taxonomy, compatibility boundaries, and future
automation-consumption vocabulary.

## Files To Create Or Update

Create:

- `README.md` / `README.zh.md`
- `intent.md` / `intent.zh.md`
- `contract.md` / `contract.zh.md`
- `technical-design.md` / `technical-design.zh.md`
- `test-plan.md` / `test-plan.zh.md`
- `plan.md` / `plan.zh.md`
- `review.md` / `review.zh.md`

Update parent v0.8 status surfaces only:

- `docs/iterations/v0.8/README.md`
- `docs/iterations/v0.8/README.zh.md`
- `docs/iterations/v0.8/v0.8-plan.md`
- `docs/iterations/v0.8/v0.8-plan.zh.md`
- `docs/iterations/v0.8/GOAL_RUNNER.md`
- `docs/iterations/v0.8/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.8/CURRENT_STATE.md`
- `docs/iterations/v0.8/CURRENT_STATE.zh.md`
- `docs/iterations/v0.8/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.8/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.8/review.md`
- `docs/iterations/v0.8/review.zh.md`

## Files Explicitly Out Of Scope

- runtime, schema, API, frontend, backend test, checker implementation,
  fixture, migration, generated result, external repository, external
  validator code, external application code, and `backend/worldengine/` files.
- `docs/contracts/`, `tools/testing/`, and report/template files.

## Required Package Status Values

Before review:

- package `Status: planned / ready for review`.
- `implementation_authorized: no`.
- `evidence_execution_authorized: no`.
- parent route `documentation-review-needed`.

After evaluator PASS and final docs checks:

- package `Status: review complete`.
- parent status `in progress / 0.8.5 child selected`.
- `0.8.5-core-working-state-smoke-evidence: selected / child docs not created`.
- implementation and evidence execution authorization remain `no`.

## Allowed Changes

- Documentation under this package.
- Parent v0.8 route/status/review synchronization.

## Forbidden Changes

- Any implementation or test changes.
- Any external validator or external application content.
- Any private scenario, oracle, selector, transcript, screenshot, private path,
  provider trace, prompt, secret, concrete world, product data, reset/write API,
  persistence, migration, or `backend/worldengine/` work.

## Review Gates

1. Run documentation shape, status, scope, text, and formatting checks.
2. Ask a read-only documentation/contract evaluator to review 0.8.4.
3. Fix any P1 or blocking P2.
4. Record evaluator evidence and final commands in `review.md`.
5. Advance parent route only if checks and evaluator review pass.

## Verification Commands

- `git diff --check`
- required child docs and mirrors check.
- v0.8 parent/child status consistency check.
- changed-file scope guard.
- v0.8 Markdown whitespace check.
- forbidden old-status/pending-claim scan.
- 0.8.4 handoff private-detail and overclaim text scan.

## Open Questions Or Assumptions

- This package is documentation-only. Schema/checker/template implementation,
  if needed, belongs in a later reviewed package.
- `external_validation` may be named as a future evidence class but is not
  accepted as current PASS evidence.

## Stop Conditions

Stop if:

- the handoff contract needs concrete external validation content.
- implementation files become necessary.
- private validator details are required.
- current-session evidence would be needed for a PASS claim.
- parent and child status surfaces cannot be kept consistent.

## Handoff After Review

After review, hand off to `0.8.5-core-working-state-smoke-evidence` for
core-side smoke/evidence package creation. Do not run that evidence from this
package.
