# Plan

Status: review complete

## Files

Create:

- `backend/app/schemas/agent_memory.py`
- `backend/app/agent/memory.py`
- `backend/app/tests/test_agent_memory_substrate.py`
- package docs and mirrors under this directory.

Modify:

- parent v0.5 status/review surfaces only for accurate handoff.

Do not touch:

- `backend/worldengine/**`
- frontend files
- API routes
- app factory wiring
- migrations
- fixtures
- generated result artifacts
- external repositories

## Steps

1. Read required project, v0.5, and `0.5.1` contract docs.
2. Draft complete package docs and Chinese mirrors.
3. Run documentation checks.
4. Run documentation/contract evaluator.
5. If evaluator reports no P1/blocking P2, record
   `implementation_authorized: yes` in `review.md`.
6. Add focused backend tests first.
7. Run focused tests and record the expected red failure.
8. Add minimal schema and in-memory store code.
9. Rerun focused tests until green.
10. Run adjacent compatibility tests.
11. Run implementation-scope evaluator.
12. Run code-review evaluator.
13. Run validation-evidence evaluator.
14. Update review evidence and closeout status only after checks pass.

## Stop Conditions

Stop if:

- required docs or mirrors are missing.
- documentation/contract evaluator reports P1 or blocking P2.
- implementation requires API routes, loop integration, app factory wiring, or
  persistence.
- a code change touches `backend/worldengine/**`.
- action semantics would need to change.
- tests fail and cannot be fixed inside the approved scope.

## Verification

Run the exact commands in `test-plan.md` and record exit status, pass/fail
counts, skipped checks, and rationale in `review.md`.

## Review Update Step

Update `review.md` and `review.zh.md` with changed files, commands run, test
results, compatibility review, scope review, subagent/evaluator evidence,
unresolved findings, and final assessment.
