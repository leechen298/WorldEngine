# Contract

Status: final / closeout complete

implementation_authorized: no

## Scope

This package is documentation-only final closeout. It may update final v0.6
status surfaces and roadmap status only after current-session final evidence
and closeout consistency review pass.

## Allowed Files

- Files under `docs/iterations/v0.6/0.6.10-v0.6-final-closeout/`
- Parent v0.6 status/review documents:
  - `docs/iterations/v0.6/README.md`
  - `docs/iterations/v0.6/README.zh.md`
  - `docs/iterations/v0.6/CURRENT_STATE.md`
  - `docs/iterations/v0.6/CURRENT_STATE.zh.md`
  - `docs/iterations/v0.6/GOAL_RUNNER.md`
  - `docs/iterations/v0.6/GOAL_RUNNER.zh.md`
  - `docs/iterations/v0.6/CAMPAIGN_PLAN.md`
  - `docs/iterations/v0.6/CAMPAIGN_PLAN.zh.md`
  - `docs/iterations/v0.6/v0.6-plan.md`
  - `docs/iterations/v0.6/v0.6-plan.zh.md`
  - `docs/iterations/v0.6/review.md`
  - `docs/iterations/v0.6/review.zh.md`
- `docs/roadmap.md` and `docs/roadmap.zh.md`, only for status synchronization
  after final evidence passes.
- root `README.md` and `README.zh.md`, only for final status, capability, and
  evidence synchronization after final evidence passes.

## Forbidden Files

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- migrations, fixtures, generated output, external repositories, concrete
  world content, and product demo files.

## Final Claims Allowed

If all final checks pass, v0.6 may claim:

- reviewed World Generation v1 contracts, schema/core, deterministic template
  generation, structured plan compilation, plan import boundaries,
  preview/regeneration/readiness API, dashboard preview, and E2E smoke are
  complete for v0.6;
- current-session final backend regression, frontend unit/build, and E2E smoke
  commands passed;
- v0.6 final closeout complete.

## Claims Not Allowed

Final closeout must not claim:

- v0.7 external validation readiness;
- v0.8 projection readiness;
- product readiness across all WorldEngine surfaces;
- Agent smoke or autonomous runner pass;
- subjective generation quality approval;
- live provider integration;
- concrete world/story/map/character content readiness.

## Review Gate

This package may be marked final only after:

- `0.6.9` is review complete;
- final verification commands pass;
- final closeout records are updated with exact results;
- status consistency checks pass;
- a closeout consistency evaluator reports no P1/P2 finding.
