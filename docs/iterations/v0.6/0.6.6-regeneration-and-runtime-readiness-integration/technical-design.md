# Technical Design

Status: review complete

## Design Boundary

`0.6.6` adds deterministic regeneration and readiness checks around the
existing generation preview service. It does not add a runtime loader,
activate generated specs, persist regeneration history, or change
`RuntimeEngine.step`.

## Planned Schema Additions

`backend/app/schemas/world_generation.py` may add:

- `GenerationLineage`
- `GenerationRegenerationRequest`
- `GenerationRegenerationResult`
- `RuntimeReadinessRequest`
- `RuntimeReadinessResult`

All request models should reject unexpected fields. Lineage and readiness
metadata must be JSON-compatible and bounded.

## Planned Core Additions

`backend/app/core/world_generation.py` may add:

- `regenerate_world(request: GenerationRegenerationRequest)`.
- `check_runtime_readiness(request: RuntimeReadinessRequest)`.

Regeneration should reuse `preview_generation` with explicit override seed or
constraints, then attach deterministic lineage. Runtime readiness should call
`load_worldspec`, then `build_runtime_context`, then
`summarize_runtime_context` on success.

## Planned API Routes

Extend the existing `backend/app/api/routes/world_generation.py` router:

```text
POST /world/generation/regenerate
POST /world/generation/runtime-readiness
```

No new router export or app-factory wiring is expected.

## Runtime Readiness Semantics

Runtime readiness means:

- candidate `WorldSpec` validates through the existing loader.
- loaded spec can produce a bounded runtime context summary.
- no live runtime state is changed.
- no raw `WorldSpec`, root payload, or generated content is emitted into tick
  events.

It does not mean full runtime migration, product readiness, external
validation readiness, projection readiness, or quality approval.

## Determinism And Safety

Regeneration lineage must be deterministic from request data. No wall-clock
time, random id, network call, provider SDK, prompt execution, persistence, or
background job may participate in results.

## Compatibility

Existing preview, loader, runtime-context, runtime-step, event, Agent/memory,
archive, params, frontend, and `backend/worldengine/` behavior remain
unchanged.
