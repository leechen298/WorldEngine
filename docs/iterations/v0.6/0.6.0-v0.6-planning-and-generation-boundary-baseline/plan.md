# Plan

Status: planned / ready for review

## Files

Create:

- `docs/iterations/v0.6/README.md`
- `docs/iterations/v0.6/README.zh.md`
- `docs/iterations/v0.6/v0.6-plan.md`
- `docs/iterations/v0.6/v0.6-plan.zh.md`
- `docs/iterations/v0.6/GOAL_RUNNER.md`
- `docs/iterations/v0.6/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/CURRENT_STATE.zh.md`
- `docs/iterations/v0.6/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.6/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.6/review.md`
- `docs/iterations/v0.6/review.zh.md`
- all English and Chinese files under
  `docs/iterations/v0.6/0.6.0-v0.6-planning-and-generation-boundary-baseline/`.

Modify:

- none outside `docs/iterations/v0.6/**`.

Do not touch:

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- migrations or alembic files
- fixtures or generated results
- external repositories
- existing testing documentation changes already present in the worktree

## Ordered Execution Steps

1. Read repository guidance, project direction, roadmap, iteration standards,
   v0.5 final closeout, and current WorldSpec/runtime-context code.
2. Draft v0.6 parent campaign docs and package sequence.
3. Draft `0.6.0` package docs and Chinese mirrors.
4. Keep all status values at `planned / ready for review` and
   `implementation_authorized: no`.
5. Run documentation checks from `test-plan.md`.
6. Update parent and child `review.md` / `review.zh.md` with actual command
   evidence.
7. Leave implementation authorization closed and hand off for documentation
   review.

## Phase Boundaries

- Documentation drafting may create only `docs/iterations/v0.6/**`.
- Documentation review may update review evidence and status only when checks
  and evaluator evidence support it.
- Implementation may start only in a later child package after review records
  `implementation_authorized: yes`.

## Stop Conditions

Stop and record a blocker if:

- any required file or mirror is missing.
- v0.6 planning requires concrete world content, private validation internals,
  or application-specific backend behavior.
- a command fails and cannot be fixed inside documentation scope.
- implementation files would need to change during `0.6.0`.
- evaluator evidence is required for a stronger status claim but unavailable.

## Review Update Step

After verification, update `review.md` and `review.zh.md` with:

- changed files.
- exact commands run.
- exact results.
- compatibility review.
- scope review.
- evaluator status.
- unresolved P1/P2/P3 findings.
- final assessment.

## Verification

Use the exact documentation checks and scope guard in `test-plan.md`.
