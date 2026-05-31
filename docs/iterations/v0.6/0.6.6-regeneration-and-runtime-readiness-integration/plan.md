# Plan

Status: review complete

## Objective

Create and review the `0.6.6` regeneration and runtime-readiness package, then
implement only after `implementation_authorized: yes`.

## Inputs Read

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/v0.6-plan.md`
- `0.6.5` generation preview API contract and review
- `backend/app/core/worldspec_loader.py`
- `backend/app/core/runtime_context.py`
- `backend/app/core/runtime_engine.py`
- `backend/app/tests/test_worldspec_loader.py`
- `backend/app/tests/test_runtime_context_bridge.py`
- `backend/app/tests/test_runtime_step.py`

## Execution Steps

1. Create the seven required package docs and Chinese mirrors.
2. Keep initial status at `planned / ready for review` and
   `implementation_authorized: no`.
3. Run documentation checks.
4. Request documentation/contract evaluator review.
5. After evaluator PASS, record `implementation_authorized: yes` and sync
   parent status surfaces.
6. Implement only the approved regeneration/readiness schema/core/route/test
   files.
7. Run focused, full backend, diff, and scope checks.
8. Request implementation-scope, code-review, validation-evidence, and
   closeout consistency evaluators.
9. If all checks pass, mark `0.6.6` review complete and hand off to `0.6.7`.

## Files To Create Or Update

Documentation stage:

- `docs/iterations/v0.6/0.6.6-regeneration-and-runtime-readiness-integration/**`
- parent v0.6 status and review files.

Implementation stage after authorization:

- `backend/app/schemas/world_generation.py`
- `backend/app/core/world_generation.py`
- `backend/app/api/routes/world_generation.py`
- `backend/app/tests/test_generation_regeneration_api.py`
- existing focused compatibility tests only if needed.
- this package review files and parent status surfaces.

## Files Explicitly Out Of Scope

- `frontend/**`
- `backend/worldengine/**`
- persistence/repository modules.
- migrations.
- fixtures.
- generated output artifacts.
- external repositories.
- provider SDKs, prompt libraries, network clients, or background workers.
- `backend/app/api/app_factory.py` and `backend/app/api/routes/__init__.py`
  unless documentation review is reopened.

## Stop Conditions

- Implementation starts before authorization.
- Regeneration requires persistence or durable history.
- Readiness checks mutate live runtime state.
- Runtime readiness becomes full runtime migration.
- `RuntimeEngine.step` or event payload semantics must change.
- Raw `WorldSpec` data leaks into runtime events or readiness summaries.
- Implementation needs files outside the approved list.

## Handoff

After closeout, `0.6.7-dashboard-generation-preview-and-e2e-smoke` receives
stable regeneration/readiness API semantics for dashboard preview work.
