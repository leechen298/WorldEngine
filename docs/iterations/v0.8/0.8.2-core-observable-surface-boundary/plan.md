# Plan

## Ordered Execution Steps

1. Read v0.8 parent state, `0.8.0` review, and `0.8.1` review.
2. Read v0.7 projection/read-model and external-validation readiness
   contracts plus current implementation/API maps.
3. Create this package's seven English documents and seven Chinese mirrors.
4. Define observable surface families, public source boundaries, allowed
   summary classes, forbidden exposure, and implementation authorization
   criteria.
5. Update parent route/status surfaces to mark `0.8.2` review complete and
   select `0.8.3`.
6. Run documentation checks from `test-plan.md`.
7. Use read-only evaluator review for boundary completeness and leakage risk.
8. Record evidence and final assessment in `review.md`.

## Phase Boundaries

- Phase 1: observable boundary documentation only.
- Phase 2: parent route/status synchronization only.
- Phase 3: documentation checks and evaluator review only.

No implementation, checker, schema, API, frontend, or evidence execution is in
scope.

## Stop Conditions

Stop if:

- package docs or mirrors are missing.
- the boundary requires concrete validator identity, private paths, UI
  selectors, app data, or consumer-specific backend behavior.
- text implies implemented API/readiness PASS.
- parent and child status surfaces drift.
- evaluator reports P1 or unresolved P2.

## Review Update Step

Update `review.md` and `review.zh.md` with changed files, exact commands,
test results, compatibility review, scope review, unresolved findings, and
final assessment.
