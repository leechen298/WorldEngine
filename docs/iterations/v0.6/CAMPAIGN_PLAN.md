# Campaign Plan

Status: planned / ready for review

## Objective

Run v0.6 as a review-gated `/goal` campaign that defines and implements World
Generation v1 without turning WorldEngine into an application-specific backend
or storing concrete world content in the core repository.

## Authoritative Inputs Read For 0.6.0

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.5/README.md`
- `docs/iterations/v0.5/CURRENT_STATE.md`
- `docs/iterations/v0.5/GOAL_RUNNER.md`
- `docs/iterations/v0.5/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.5/v0.5-plan.md`
- `docs/iterations/v0.5/0.5.7-v0.5-final-closeout/final-closeout.md`
- `docs/iterations/v0.5/0.5.7-v0.5-final-closeout/review.md`
- `backend/app/schemas/world_cell.py`
- `backend/app/core/worldspec_loader.py`
- `backend/app/core/runtime_context.py`
- `backend/app/core/runtime_engine.py`
- `backend/app/api/app_factory.py`
- `backend/app/tests/test_worldspec_loader.py`
- `backend/app/tests/test_runtime_context_bridge.py`

## Campaign Rules

- The active child package is the only implementation scope.
- `0.6.0` is documentation-only and must not modify implementation files.
- Implementation authorization starts as no for every child.
- Mixed/code packages must complete documentation review before implementation.
- Historical v0.5 evidence is handoff context only.
- Current-session command evidence is required before v0.6 generation,
  runtime, API, frontend, E2E, build, Agent smoke, autonomous validation,
  generation-quality, or release claims.
- Chinese mirrors must preserve status, type, goal, scope, forbidden changes,
  compatibility requirements, findings, and final assessment semantics.

## Planned Child Sequence

1. `0.6.0-v0.6-planning-and-generation-boundary-baseline`
2. `0.6.1-world-generation-contracts-and-template-semantics`
3. `0.6.2-template-catalog-and-deterministic-generator-core`
4. `0.6.3-structured-generation-plan-compiler`
5. `0.6.4-ai-assisted-generation-boundary-and-plan-import`
6. `0.6.5-generation-validation-metadata-and-preview-api`
7. `0.6.6-regeneration-and-runtime-readiness-integration`
8. `0.6.7-dashboard-generation-preview-and-e2e-smoke`
9. `0.6.8-v0.6-evidence-and-compatibility-audit`
10. `0.6.9-v0.6-release-candidate-bundle`
11. `0.6.10-v0.6-final-closeout`

## Cross-Child Handoff Rules

- `0.6.0` hands off reviewed campaign structure and generation boundaries to
  `0.6.1`.
- `0.6.1` hands off public generation concepts, schema semantics, and
  authorization criteria to `0.6.2`.
- `0.6.2` hands off deterministic template generation evidence to `0.6.3`.
- `0.6.3` hands off structured-plan compiler evidence to `0.6.4`.
- `0.6.4` hands off AI-assisted plan-import boundaries to `0.6.5`.
- `0.6.5` hands off backend/API validation, metadata, and preview evidence to
  `0.6.6`.
- `0.6.6` hands off regeneration and runtime-readiness evidence to `0.6.7`.
- `0.6.7` hands off dashboard preview and E2E smoke evidence to audit.
- `0.6.8` hands off evidence and compatibility review to release candidate.
- `0.6.9` hands off release-candidate findings to final closeout.
- `0.6.10` may mark final status only after evidence consistency and review
  gates pass.

## Campaign Exit Criteria

v0.6 may be marked `final / closeout complete` only when:

- all active child packages are review complete or explicitly deferred by
  contract.
- implementation-bearing children record current-session command evidence.
- compatibility review confirms v0.5 loop/memory surfaces and v0.3
  `WorldSpec` loader/runtime-context bridge remain compatible or only
  additively changed by reviewed contracts.
- scope review confirms no concrete demo-world, external validation internal,
  application-specific backend behavior, migration, projection app, live
  external AI-provider dependency, or `backend/worldengine/` work slipped in.
- generated `WorldSpec` data is validated through reviewed loader and
  runtime-readiness checks.
- unresolved findings are classified and no P1/P2 remains without explicit
  accepted rationale.

## Stop Conditions

Stop before implementation or closeout if:

- active package docs are missing required files or mirrors.
- a required evaluator checkpoint is unavailable or reports blocking P1/P2.
- implementation touches files outside the active package contract.
- verification commands fail and the package cannot honestly record pass
  evidence.
- generated examples require concrete demo-world content inside this repo.
- status surfaces drift between README, current state, plan, review, and
  closeout docs.
