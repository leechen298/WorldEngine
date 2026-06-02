# Plan

## Ordered Execution Steps

1. Read v0.8 parent state and `0.8.0` review.
2. Create this package's seven English documents and seven Chinese mirrors.
3. Define required core slices, claim taxonomy, evidence classes, exclusions,
   and handoff criteria.
4. Update parent route/status surfaces to mark `0.8.1` review complete and
   select `0.8.2`.
5. Run documentation checks from `test-plan.md`.
6. Use read-only evaluator review for contract completeness and overclaim
   risk.
7. Record evidence and final assessment in `review.md`.

## Phase Boundaries

- Phase 1: contract documentation only.
- Phase 2: route/status synchronization only.
- Phase 3: documentation checks and evaluator review only.

No implementation or evidence execution is in scope.

## Stop Conditions

Stop if:

- package docs or mirrors are missing.
- taxonomy allows blocked, skipped, or out-of-scope states to count as pass.
- text implies external validation PASS or product readiness.
- parent and child status surfaces drift.
- evaluator reports P1 or unresolved P2.

## Review Update Step

Update `review.md` and `review.zh.md` with changed files, exact commands,
test results, compatibility review, scope review, unresolved findings, and
final assessment.
