# Technical Design

Status: review complete

## Current State

WorldEngine currently has a generic `WorldSpec` schema and loader/runtime
bridge, but no world-generation implementation. The relevant current surfaces
are:

- `backend/app/schemas/world_cell.py`: `WorldSpec` contains
  `schema_version`, `id`, optional `label`, `root`, and metadata; `WorldCell`
  contains `id`, optional `label`, `kind`, `entity_refs`, `child_cells`, and
  metadata.
- `backend/app/schemas/entity.py`: `EntityRef` contains non-empty `id` and
  `kind`, optional `label`, and metadata.
- `backend/app/core/worldspec_loader.py`: `load_worldspec` accepts mappings or
  JSON strings/bytes, validates through `WorldSpec`, and returns success or
  loader errors. Current normal failure codes include `unsupported_input`,
  `parse_error`, and `schema_validation_error`, with schema paths represented
  as JSON Pointer-style locations.
- `backend/app/core/runtime_context.py`: `build_runtime_context` derives a
  bounded runtime context from a loaded `WorldSpec`; summaries must not expose
  raw `WorldSpec` or root payloads.
- `backend/app/core/runtime_engine.py`: runtime state, tick behavior, event
  emission, params, callbacks, and optional runtime context are already
  compatibility-sensitive.
- `backend/app/schemas/api.py` and `backend/app/api/app_factory.py`: API
  envelopes and exception handling use `code`, `data`, and `msg` for success
  and `code`, `msg`, optional `data` for errors. Existing HTTP-to-application
  error mapping includes 400 to 10, 401 to 20, 403 to 21, 404 to 24, 409 to
  29, 422 to 30, and 500 to 50.

`0.6.1` changes none of these files.

## Documentation Structure

This package adds a full documentation-only child package:

```text
docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/
├── README.md
├── README.zh.md
├── intent.md
├── intent.zh.md
├── contract.md
├── contract.zh.md
├── technical-design.md
├── technical-design.zh.md
├── test-plan.md
├── test-plan.zh.md
├── plan.md
├── plan.zh.md
├── review.md
└── review.zh.md
```

## Concept Flow

The planned generation contract uses this flow:

```text
WorldGenerationRequest
  -> WorldTemplate and constraints, or validated GenerationPlan
  -> GeneratedWorldSpec with GenerationMetadata and diagnostics
  -> GenerationPreview for bounded inspection
  -> later loader/runtime-readiness checks before runtime use
```

For AI-assisted generation, the flow is deliberately split:

```text
external/user/tool/AI output
  -> untrusted structured GenerationPlan import
  -> validation and diagnostics
  -> later compilation into WorldSpec only after a reviewed package authorizes it
```

Live provider invocation, provider credentials, prompt storage, and hidden
model side effects are not part of this package.

## Planned Field Semantics

Later additive schemas should preserve these semantics:

| Concept | Required semantic groups |
| --- | --- |
| `WorldGenerationRequest` | request identity, one primary input path, constraints, provenance, deterministic seed material when applicable |
| `WorldTemplate` | template identity/version, generic cell patterns, entity-ref slots, metadata defaults, validation constraints |
| `GenerationPlan` | root intent, child-cell entries, entity-ref entries, metadata entries, constraints, provenance |
| `GeneratedWorldSpec` | candidate `WorldSpec`, metadata, diagnostics, validation state |
| `GenerationMetadata` | request/generation identity, template or plan lineage, seed lineage, validation status, diagnostics, timestamps/source clock |
| `GenerationPreview` | bounded summary of ids, counts, metadata keys, validation status, diagnostics |
| `RegenerationRequest` | source generation/request lineage, changed constraints, compatibility expectations |
| diagnostics | stable code, message, optional path, severity, source context |

These are semantic requirements, not implementation schemas in this package.

## Compatibility Strategy

The generated output contract is anchored to existing loader behavior:

- Later generated `WorldSpec` values must validate through `load_worldspec`.
- Loader parse and schema validation errors remain authoritative for invalid
  generated specs, including existing error codes and JSON Pointer-style
  paths.
- Runtime context remains derived through `build_runtime_context`; generation
  metadata must not leak into runtime context unless a later reviewed child
  explicitly defines an additive summary.
- Runtime ticks, event emission, params, archive, Agent Loop, and memory
  behavior remain unchanged until a later reviewed package authorizes any
  additive integration. Tick events and runtime state must not expose raw
  generated specs or root payloads.
- Future generation API responses must use the existing API envelope and
  error shape.

## Affected Surfaces

Affected files are limited to this package directory. This package does not
affect runtime, schemas, services, APIs, frontend, backend tests, fixtures,
migrations, generated outputs, external repositories, or legacy code.

## Anti-Drift Rules

- Treat generation contracts as engine contracts, not demo-world authoring.
- Keep templates generic; placeholder identifiers are allowed only when they
  cannot be mistaken for concrete world content.
- Treat AI-assisted generation as structured plan import and validation, not
  live provider behavior.
- Do not claim generated-world quality from structural validity alone.
- Do not promote historical v0.5 evidence into current v0.6 pass evidence.
- Keep implementation authorization closed until an implementation-bearing
  child records its own reviewed authorization.

## Risks

- Risk: contract terms are later implemented as concrete fixture data.
  Mitigation: forbid concrete content and require focused scope guards.
- Risk: generated output passes shape checks but is overstated as runnable or
  high quality.
  Mitigation: separate structural validity, runtime readiness, preview, and
  quality claims.
- Risk: AI-assisted generation is treated as live provider integration.
  Mitigation: require provider-independent structured plan import first.
- Risk: later API work drifts from existing envelopes.
  Mitigation: make `ApiResponse` / `ApiErrorResponse` compatibility explicit.
