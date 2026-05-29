# Plan

Status: planned / ready for review

## Ordered Steps

1. Define the autonomous reviewer role.
2. List required inputs.
3. Define commands to run or record as blocked.
4. Define release claim checks.
5. Define API, schema, runtime, and compatibility finding categories.
6. Define concrete demo-world regression checks.
7. Define unsupported-claim handling.
8. Define final recommendation values.
9. Hand off to the execution package.

## Phase Boundaries

- This package defines reviewer instructions.
- `04-codex-autonomous-validation-execution/` owns execution and review
  verification.

## Stop Conditions

Stop and record a P2 if the plan:

- lets the reviewer rely only on summaries.
- allows code changes.
- allows unverified success claims.
- omits P1/P2/P3 classification.
- omits concrete demo-world regression checks.

## Review Update Step

Update `review.md` with the documentation-only scope and final assessment.
