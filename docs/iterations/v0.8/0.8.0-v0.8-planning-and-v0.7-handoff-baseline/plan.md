# Plan

## Ordered Execution Steps

1. Read root and iteration governance documents.
2. Read v0.8 parent `README.md`, `CURRENT_STATE.md`, `GOAL_RUNNER.md`,
   `CAMPAIGN_PLAN.md`, `v0.8-plan.md`, and `review.md`.
3. Read current v0.7 `CURRENT_STATE.md` and v0.7 overall validation result to
   confirm handoff status.
4. Create the `0.8.0` child package document set and Chinese mirrors.
5. Update parent v0.8 route/status surfaces to record `0.8.0` review complete
   and `0.8.1` selected / child docs not created.
6. Run documentation checks from `test-plan.md`.
7. Use read-only subagent/evaluator review for v0.7 handoff drift and
   `0.8.0` package completeness.
8. Record changed files, commands, test results, compatibility review, scope
   review, unresolved findings, and final assessment in `review.md`.

## Phase Boundaries

- Phase 1: documentation review and handoff synchronization only.
- Phase 2: documentation checks and evaluator review only.
- Phase 3: handoff to `0.8.1` only after no unresolved P1/P2 remains.

No implementation, evidence execution, backend test, frontend test, E2E,
Agent smoke, autonomous run, external validation run, or runtime smoke belongs
to this package.

## Stop Conditions

Stop if:

- v0.7 handoff evidence cannot be verified from current files.
- required `0.8.0` package docs or mirrors are missing.
- parent and child status surfaces disagree.
- scope guard reports non-`docs/iterations/v0.8/**` changes.
- stale v0.7 unresolved-blocker wording remains in active v0.8 docs.
- an evaluator reports P1 or unresolved P2.
- any text claims v0.8 pass evidence that was not run in this session.

## Review Update Step

After checks and evaluator results, update `review.md` and `review.zh.md` with
the exact commands, pass/fail outputs, compatibility review, scope review,
unresolved findings, and final assessment.
