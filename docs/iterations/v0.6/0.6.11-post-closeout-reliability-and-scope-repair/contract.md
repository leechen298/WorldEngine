# Contract

Status: review complete

implementation_authorized: yes

## Public Concepts

This package does not add public concepts. It repairs existing v0.6 generation
reliability and evidence consistency:

- failed generation ids and seed digests must preserve valid seed material even
  when an unrelated non-JSON metadata or constraints value makes the full
  request payload non-canonical.
- imported-plan preview must fail through the public preview API when redacted
  provenance still contains sensitive metadata keys.
- clean-pass evidence requires a reviewed package-specific scope guard, not the
  documentation-only `0.6.10` contract.

## Allowed Changes

- `docs/iterations/v0.6/0.6.11-post-closeout-reliability-and-scope-repair/**`
- `backend/app/core/world_generation.py`
- `backend/app/tests/test_deterministic_world_generation.py`
- `backend/app/tests/test_structured_generation_plan_compiler.py`
- `backend/app/tests/test_generation_preview_api.py`
- `backend/app/tests/test_plan_import_boundary.py`
- `frontend/src/components/GenerationPanel.vue`
- `frontend/src/components/GenerationPanel.test.ts`
- `frontend/e2e/dashboard-generation.spec.ts`
- `docs/backend-implementation.md`
- `docs/backend-implementation.zh.md`
- `docs/current-implementation.md`
- `docs/current-implementation.zh.md`
- `docs/frontend-implementation.md`
- `docs/frontend-implementation.zh.md`
- `docs/iterations/v0.6/README.md`
- `docs/iterations/v0.6/README.zh.md`
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/CURRENT_STATE.zh.md`
- `docs/iterations/v0.6/review.md`
- `docs/iterations/v0.6/review.zh.md`
- `docs/testing/results/2026-06-01-v0.6-reliability-validation.md`

## Forbidden Changes

- `backend/worldengine/**`
- `backend/app/alembic/**`
- `backend/migrations/**`
- `test-results/**`
- external repositories.
- new public routes, new schemas, migrations, persistence, live provider
  integration, concrete world content, private validation oracle details,
  projection application code, or v0.7/v0.8 scope.
- root README or roadmap status sync unless a later review explicitly requires
  it.

## Compatibility Requirements

- Existing v0.6 template, plan, import, preview, regeneration, runtime-readiness,
  dashboard, and E2E behavior remains additive and backward compatible.
- Failed generation id/digest values may change only for failed requests whose
  full canonical payload previously collapsed through a fallback path.
- No pass claim may be made for live Agent smoke, full autonomous runner,
  external validation readiness, projection readiness, live provider behavior,
  generation quality, or product readiness.

## Out-Of-Scope Follow-Ups

- v0.7 owns external validation readiness.
- v0.8 owns external projection application readiness.
- Future generation-quality evaluation requires its own reviewed package.
