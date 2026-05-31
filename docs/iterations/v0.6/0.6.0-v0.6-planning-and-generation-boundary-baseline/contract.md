# Contract

Status: review complete

## Public Concepts

- `v0.6 World Generation v1`: the version boundary for generic, inspectable
  generation of valid `WorldSpec` data.
- `WorldGenerationRequest`: a future request boundary that may carry a generic
  template id, structured generation plan, constraints, and provenance.
- `WorldTemplate`: a generic, reusable generation shape that must not encode
  concrete demo-world content.
- `GenerationPlan`: structured input that can be validated and compiled into a
  `WorldSpec`.
- `AI-assisted generation`: provider-independent import of structured plans
  that may have been produced by an AI system; live provider calls are not
  implied by this package.
- `GenerationMetadata`: inspectable provenance, diagnostics, template/plan
  lineage, validation status, and regeneration lineage.
- `GenerationPreview`: bounded generated output summary suitable for review
  before runtime use.
- `RegenerationRequest`: a future request that revises a prior generation
  request or output through explicit lineage and constraints.

## Capability Split

| Capability | This package | First implementation candidate |
| --- | --- | --- |
| Generation boundary | define campaign and scope | no code |
| Generation contracts | plan only | `0.6.1` docs |
| Template generator | plan only | `0.6.2` |
| Structured plan compiler | plan only | `0.6.3` |
| AI-assisted plan import | plan only | `0.6.4` |
| Metadata and preview API | plan only | `0.6.5` |
| Regeneration/readiness | plan only | `0.6.6` |
| Dashboard preview | plan only | `0.6.7` |

## Compatibility Requirements

- Existing v0.5 memory/loop schemas and APIs remain unchanged in `0.6.0`.
- Existing v0.3 `WorldSpec` loader and runtime-context bridge remain
  unchanged.
- `WorldSpec`, `WorldCell`, `EntityRef`, `load_worldspec`,
  `build_runtime_context`, and `RuntimeEngine` tick/time behavior are
  compatibility-sensitive.
- Existing API envelope/error shape, event routes, params behavior, archive
  behavior, and optional event reference behavior remain unchanged.
- Future schema changes must be additive unless a later reviewed child
  explicitly allows a breaking change.
- v0.5 command evidence is handoff evidence only, not current v0.6 pass
  evidence.

## Allowed Changes

- Create `docs/iterations/v0.6/**` documentation.
- Create parent campaign files, child package files, Chinese mirrors, review
  evidence, and package sequencing.
- Name planned future implementation paths without creating them:
  - `backend/app/schemas/world_generation.py`
  - `backend/app/world/generation.py` or equivalent approved path
  - `backend/app/api/routes/world_generation.py`
  - `backend/app/tests/test_world_generation_*.py`
  - `frontend/src/components/GenerationPanel.vue`
- Record evaluator status and review findings.

## Forbidden Changes

- Do not modify runtime, schema, API, frontend, backend test, fixture,
  migration, generated result, external repository, or `backend/worldengine/`
  implementation files.
- Do not create planned future implementation paths in this package.
- Do not add generation store behavior, public generation APIs, preview UI,
  regeneration behavior, runtime-readiness behavior, durable persistence,
  migrations, or tests.
- Do not add concrete world names, maps, characters, locations, resources,
  story rules, seed data, UI-specific app behavior, private validation oracle
  details, external validation readiness, projection app readiness, live
  AI-provider calls, or application-specific backend logic.

## North Star Check

This package aligns with the north star by preparing world generation as a
generic engine capability. It keeps application surfaces as consumers, does not
store concrete world content, and does not replace recursive world architecture
with product-specific state.

## Out-of-Scope Follow-ups

- `0.6.1`: public generation contracts and template semantics.
- `0.6.2`: deterministic template generator core.
- `0.6.3`: structured generation plan compiler.
- `0.6.4`: AI-assisted structured plan import boundary.
- `0.6.5`: generation validation, metadata, and preview API.
- `0.6.6`: regeneration and runtime-readiness integration.
- `0.6.7`: dashboard generation preview and E2E smoke.
- v0.7 external validation readiness and v0.8 projection application
  readiness.
