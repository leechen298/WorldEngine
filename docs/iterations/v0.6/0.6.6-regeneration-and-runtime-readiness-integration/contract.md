# Contract

Status: review complete

implementation_authorized: yes

## Public Concepts

- `GenerationLineage`: bounded metadata connecting a parent generation request
  or generation id to a regenerated output.
- `GenerationRegenerationRequest`: API-facing request that reuses a reviewed
  `GenerationPreviewRequest`, applies bounded override seed/constraints, and
  records why regeneration is being requested.
- `GenerationRegenerationResult`: response containing lineage, regenerated
  preview, runtime-readiness result, and deterministic diagnostics.
- `RuntimeReadinessRequest`: API-facing request carrying a candidate
  `WorldSpec` and source label for loader/context checks.
- `RuntimeReadinessResult`: bounded result showing loader success, runtime
  context bridge success, optional bounded runtime context summary, diagnostics,
  and `does_not_mutate_runtime: true`.

## API Contract

Implementation may extend the existing generation router with:

```text
POST /world/generation/regenerate
POST /world/generation/runtime-readiness
```

Both routes must return `ApiResponse[...]` on accepted request shapes and must
use the existing `ApiErrorResponse` validation handler for malformed request
payloads. Generation, regeneration, loader, or runtime-context validation
failures should return HTTP 200 with failed status and diagnostics.

## Allowed Changes

Documentation stage:

- create and update this package under `docs/iterations/v0.6/`.
- update parent v0.6 status surfaces only for current child state and
  evidence.
- record subagent/evaluator evidence.

Implementation stage, only after `implementation_authorized: yes`:

- update `backend/app/schemas/world_generation.py`.
- update `backend/app/core/world_generation.py`.
- update `backend/app/api/routes/world_generation.py`.
- add focused tests:
  - `backend/app/tests/test_generation_regeneration_api.py`
- update existing focused compatibility tests only where needed:
  - `backend/app/tests/test_generation_preview_api.py`
  - `backend/app/tests/test_worldspec_loader.py`
  - `backend/app/tests/test_runtime_context_bridge.py`
  - `backend/app/tests/test_runtime_step.py`
  - existing generation schema/compiler/import tests if directly affected.
- update this package `review.md` / `review.zh.md`.
- update parent v0.6 status surfaces only for current child state and
  evidence.

`backend/app/api/routes/__init__.py` and `backend/app/api/app_factory.py` are
not expected to change because `0.6.5` already included the generation router.
If implementation requires touching them, stop and return to documentation
review.

## Forbidden Changes

- Do not change `RuntimeEngine.step`, tick/time semantics, event emission
  semantics, or existing runtime route response shapes.
- Do not automatically install, persist, or activate generated specs in the
  live runtime.
- Do not add persistence/repository modules, migrations, fixtures, generated
  output files, external repositories, or `backend/worldengine/**`.
- Do not add frontend UI, dashboard workflow, E2E, external validation runner,
  projection app behavior, live provider calls, network calls, prompt
  execution, provider traces, private oracle details, or concrete world
  content.
- Do not expose raw `WorldSpec` payloads or root payloads in runtime events or
  readiness summaries.
- Do not claim runtime readiness beyond loader/context bridge readiness.

## Compatibility Requirements

- Existing generation preview API remains compatible.
- Existing API envelopes remain compatible.
- Existing `worldspec_loader`, `runtime_context`, and `RuntimeEngine` behavior
  remain compatible.
- Runtime-context summaries remain bounded.
- Readiness checks are inert and do not mutate runtime state.

## Authorization Criteria

This package may record `implementation_authorized: yes` only after:

- all package docs and Chinese mirrors exist.
- documentation/contract evaluator reports PASS with no P0/P1 and no blocking
  unresolved P2.
- contract/design/test-plan/plan explicitly forbid runtime mutation,
  tick/event semantic changes, persistence/migrations, frontend UI, external
  validation/projection behavior, live AI/provider behavior, concrete content,
  and `backend/worldengine/**`.
- planned tests cover regeneration success/failure, deterministic lineage,
  readiness success/failure, bounded context summary, no raw `WorldSpec` in
  runtime events, existing preview compatibility, runtime bridge compatibility,
  full backend regression, and scope guard.

## Out-of-Scope Follow-ups

- `0.6.7`: dashboard preview and E2E smoke.
- v0.7 external validation readiness.
- v0.8 projection application readiness.
