# Technical Design

Status: review complete

## Design Boundary

`0.6.3` extends the existing generation module rather than introducing a
public API or runtime pathway. The compiler operates on structured plan data,
validates it, and returns the same generation result pattern used by `0.6.2`.

No route, frontend, persistence, runtime tick, Agent/memory, fixture, or
legacy `backend/worldengine/` surface is part of this design.

## Planned Schema Additions

`backend/app/schemas/world_generation.py` may add:

- `PlanCell`: recursive structured cell plan with generic `id`, optional
  `label`, `entity_refs`, `child_cells`, and `metadata`.
- `GenerationPlan`: plan `id`, `version`, root `PlanCell`, optional metadata,
  and constraints.
- `PlanGenerationRequest`: request id, plan, optional seed material, and
  request-level constraints.
- additive metadata fields such as `source_kind`, `plan_id`, and
  `plan_version`, while preserving current template-generation behavior.

The implementation must not change `WorldSpec`, `WorldCell`, or `EntityRef`.

## Planned Core Additions

`backend/app/core/world_generation.py` may add:

- `validate_generation_plan(plan, request_constraints=None)`.
- `generate_worldspec_from_plan(request)`.
- private helpers that share deterministic digest and JSON canonicalization
  behavior with template generation.

The compiler maps `PlanCell` to `WorldCell` without hidden rule execution. It
should reuse or parallel `0.6.2` diagnostics for duplicate cell ids, duplicate
entity refs, child-count bounds, entity-kind allowlists, unsupported versions,
and unsupported seed/material values.

## Determinism

The seed digest must include request id, normalized plan data, request
constraints, and seed material. Unsupported non-JSON values, non-finite
floats, tuples, sets, objects, or non-string dict keys must fail with stable
diagnostics rather than being coerced into output.

## Compatibility

Valid compiler output must pass current `WorldSpec` schema, loader, and
runtime-context bridge tests. Existing template generation must remain
deterministic and compatible.

## Failure Model

Invalid plans return a failed generation result with diagnostics and no
`WorldSpec`. Diagnostics use stable machine-readable codes and JSON
Pointer-style paths into the plan input.

## Out Of Scope

- AI-assisted import or provider behavior.
- Prompt execution or free-form prose parsing.
- API, frontend, E2E, persistence, migrations, external validation,
  projection, runtime tick/event, Agent/memory, and regeneration behavior.
