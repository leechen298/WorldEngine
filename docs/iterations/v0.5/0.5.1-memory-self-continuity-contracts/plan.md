# Plan

Status: review complete

## Files

Create:

- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/README.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/README.zh.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/intent.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/intent.zh.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/contract.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/contract.zh.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/technical-design.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/technical-design.zh.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/test-plan.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/test-plan.zh.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/plan.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/plan.zh.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/review.md`
- `docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/review.zh.md`

Modify after verification:

- parent v0.5 status files only as needed for accurate handoff.

Do not touch:

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- tests
- fixtures
- migrations
- generated result artifacts
- external repositories

## Steps

1. Read required project and v0.5 campaign documents.
2. Read the `0.5.0` review evidence and handoff.
3. Draft the English package documents.
4. Draft semantically equivalent Chinese mirrors.
5. Run the documentation and scope checks in `test-plan.md`.
6. Run a read-only documentation/contract evaluator.
7. Fix any P1/P2 within documentation scope.
8. Update `review.md` and `review.zh.md` with exact evidence.
9. Mark the package review complete only if checks and evaluator evidence pass.
10. Hand off to `0.5.2-working-and-episodic-memory-substrate`.

## Stop Conditions

Stop and record a blocker if:

- required package docs or mirrors are missing.
- implementation files need changes.
- any concept requires behavior to be meaningful.
- a required evaluator checkpoint is unavailable.
- an evaluator reports P1 or blocking P2.
- historical v0.4 evidence is being treated as current v0.5 pass evidence.

## Verification

Run the exact commands in `test-plan.md`.

## Review Update Step

After verification, update `review.md` and `review.zh.md` with:

- changed files.
- commands run and exit status.
- test results and not-run rationale.
- compatibility review.
- scope review.
- subagent/evaluator findings.
- unresolved P1/P2/P3.
- final assessment.
