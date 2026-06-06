# Plan

Chinese mirror: `plan.zh.md`.

## Objective

Close v0.9 as a reviewed BLOCKED release candidate based on current evidence.

## Authoritative Inputs

- `docs/iterations/v0.9/CURRENT_STATE.md`
- `docs/iterations/v0.9/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.9/v0.9-plan.md`
- `docs/iterations/v0.9/review.md`
- `docs/testing/results/2026-06-06-llm-backed-lifecycle-validation.md`
- `test-results/agent-autonomous/20260606T142210+0800-llm-backed-full-lifecycle/result.json`

## Steps

1. Create the 0.9.13 package document set.
2. Update parent route/status docs to `final / blocked` after review.
3. Revalidate package completeness and saved-result evidence.
4. Run whitespace/status consistency checks.
5. Request read-only evaluator review before final closeout.

## Stop Conditions

- Any parent doc claims provider live PASS, external validation PASS, product
  readiness, or LLM-backed full lifecycle PASS.
- Any required package file or mirror is missing.
- The saved BLOCKED result no longer validates.
- A read-only evaluator finds blocking P1/P2.
