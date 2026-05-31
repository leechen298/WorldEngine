# Plan

Status: review complete

## Objective

Create and review the `0.6.5` generation validation, metadata, and preview
API package, then implement only after `implementation_authorized: yes`.

## Inputs Read

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/README.md`
- `docs/iterations/v0.6/GOAL_RUNNER.md`
- `docs/iterations/v0.6/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.6/v0.6-plan.md`
- `0.6.1` generation contract
- `0.6.2` deterministic generator core contract and review
- `0.6.3` structured plan compiler contract and review
- `0.6.4` plan import boundary contract and review
- `backend/app/schemas/api.py`
- `backend/app/api/app_factory.py`
- `backend/app/api/routes/__init__.py`
- current API envelope compatibility tests
- current generation schemas and core implementation

## Execution Steps

1. Create the seven required package docs and Chinese mirrors.
2. Keep initial status at `planned / ready for review` and
   `implementation_authorized: no`.
3. Run documentation checks.
4. Request documentation/contract evaluator review.
5. After evaluator PASS, record `implementation_authorized: yes` and sync
   parent status surfaces.
6. Implement only the approved preview schema/core/route/test files.
7. Run focused, adjacent, full backend, diff, and scope checks.
8. Request implementation-scope, code-review, validation-evidence, and
   closeout consistency evaluators.
9. If all checks pass, mark `0.6.5` review complete and hand off to `0.6.6`.

## Files To Create Or Update

Documentation stage:

- `docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api/**`
- parent v0.6 status and review files.

Implementation stage after authorization:

- `backend/app/schemas/world_generation.py`
- `backend/app/core/world_generation.py`
- `backend/app/api/routes/world_generation.py`
- `backend/app/api/routes/__init__.py`
- `backend/app/api/app_factory.py`
- `backend/app/tests/test_generation_preview_api.py`
- existing focused generation/API compatibility tests only if needed.
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

## Stop Conditions

- Implementation starts before authorization.
- Documentation/contract evaluator reports P0/P1 or blocking P2.
- Preview API requires changing existing envelopes or shared error handlers.
- Preview requires persistence, frontend UI, runtime loading/readiness,
  regeneration, live AI access, prompts, provider traces, concrete content,
  external validation internals, projection readiness, or
  `backend/worldengine/**`.
- Implementation needs files outside the approved list.
- Focused or regression tests fail and cannot be honestly recorded as passed.

## Handoff

After closeout, `0.6.6-regeneration-and-runtime-readiness-integration`
receives public preview, validation diagnostics, and bounded metadata semantics
for regeneration and runtime-readiness work.
