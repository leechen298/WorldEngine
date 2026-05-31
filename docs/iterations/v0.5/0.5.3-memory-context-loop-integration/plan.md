# Plan

Status: review complete

## Files

Create:

- this package's docs and Chinese mirrors.

Modify after authorization:

- `backend/app/schemas/agent_loop.py`
- `backend/app/agent/perception.py`
- `backend/app/api/app_factory.py`
- focused tests under `backend/app/tests/`

Do not touch:

- `backend/worldengine/**`
- frontend files
- public memory API routes
- action adapter semantics
- migrations
- fixtures
- generated result artifacts
- external repositories

## Steps

1. Read `0.5.2` review and memory substrate implementation.
2. Draft package docs and Chinese mirrors.
3. Run documentation checks.
4. Run documentation/contract evaluator.
5. Record `implementation_authorized: yes` only after evaluator pass.
6. Add focused failing test and run TDD red.
7. Implement additive memory context schema/perception/app wiring.
8. Rerun focused tests until green.
9. Run adjacent compatibility tests.
10. Run implementation-scope, code-review, validation-evidence, and closeout
    consistency evaluators.
11. Update review evidence and parent handoff status only after gates pass.

## Stop Conditions

Stop if:

- evaluator reports P1 or blocking P2.
- implementation requires action semantics changes.
- implementation requires public memory APIs or loop request memory selectors.
- code touches `backend/worldengine/**`.
- tests fail outside approved scope.

## Verification

Run the exact commands in `test-plan.md` and record exit status, pass/fail
counts, skipped checks, and rationale in `review.md`.

## Review Update Step

Update `review.md` and `review.zh.md` with changed files, commands run, test
results, compatibility review, scope review, evaluator evidence, unresolved
findings, and final assessment.
