# Plan

Status: planned / ready for review

## Ordered Steps

1. Read v0.2 release, evidence, boundary, and compatibility docs.
2. Confirm v0.2 closeout remains final / complete and this validation does not
   reopen implementation.
3. Define repository and documentation checks.
4. Define backend deterministic checks.
5. Define schema smoke and event compatibility checks.
6. Define runtime step, world events, event steps, params, and archive checks.
7. Define API smoke strategy using TestClient or curl.
8. Define E2E framework availability discovery.
9. Define fallback when browser E2E is unavailable.
10. Define release claim validation.
11. Define concrete demo-world regression check.
12. Update review with documentation-only evidence.

## Phase Boundaries

- This package stops after planning.
- `02-e2e-validation-execution/` owns command execution and results.

## Stop Conditions

Stop and record a P2 in review if the plan:

- hardcodes the current branch.
- treats Playwright config as proof that E2E is runnable.
- declares validation results.
- changes implementation scope.

## Review Update Step

The review must list changed files, commands run, commands not run, scope
review, compatibility review, unresolved P1/P2/P3, and final assessment.
