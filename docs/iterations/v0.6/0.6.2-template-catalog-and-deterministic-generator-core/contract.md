# Contract

Status: review complete

implementation_authorized: yes

## Public Concepts

This package implements only the deterministic subset of the `0.6.1`
generation contract.

- `WorldTemplate`: backend schema describing a generic template id, version,
  root template cell, entity reference slots, metadata defaults, and
  constraints.
- `TemplateCell`: backend schema for generic cell ids, optional generic labels,
  entity refs, child cells, and metadata.
- `GenerationDiagnostic`: stable diagnostic code, severity, message, optional
  path, and source context for template validation and generation failures.
- `GenerationMetadata`: generation id, request id, template id/version,
  deterministic seed digest, validation status, diagnostics count, and lineage
  fields needed by later packages.
- `TemplateGenerationRequest`: request wrapper for template, seed material, and
  constraints.
- `TemplateGenerationResult`: generated `WorldSpec` plus metadata and
  diagnostics, or diagnostics without a generated spec on failure.

## Allowed Changes

Documentation stage:

- create and update this package under `docs/iterations/v0.6/`.
- record documentation/contract evaluator evidence.

Implementation stage, only after `implementation_authorized: yes`:

- create `backend/app/schemas/world_generation.py`.
- create `backend/app/core/world_generation.py`.
- create focused tests:
  - `backend/app/tests/test_world_generation_schema.py`
  - `backend/app/tests/test_template_catalog.py`
  - `backend/app/tests/test_deterministic_world_generation.py`
- update this package `review.md` / `review.zh.md`.
- update parent v0.6 status surfaces only for current child state and evidence.

## Forbidden Changes

- Do not modify `backend/app/schemas/world_cell.py`,
  `backend/app/schemas/entity.py`, `backend/app/core/worldspec_loader.py`,
  `backend/app/core/runtime_context.py`, or
  `backend/app/core/runtime_engine.py` unless a design gap is found and the
  package is returned to documentation review first.
- Do not modify `backend/app/api/**`, `backend/app/schemas/api.py`,
  `frontend/**`, `backend/app/agent/**`, persistence/repository modules,
  archive, params, migrations, fixtures, generated result files, external
  repositories, or `backend/worldengine/**`.
- Do not add public generation API routes, structured-plan compiler behavior,
  AI-assisted plan import, metadata/preview API, regeneration behavior,
  dashboard UI, E2E behavior, external validation readiness, projection
  readiness, live external AI-provider calls, durable persistence, or
  migrations.
- Do not add concrete demo-world names, maps, characters, locations,
  resources, story rules, private validation oracle details, generated seed
  data, or application-specific backend behavior.
- Do not claim generated worlds are runnable beyond loader/runtime-context
  compatibility evidence in this package.

## Implementation Requirements

- Generated output must validate against the current `WorldSpec` schema with
  `schema_version == "0.2"`.
- Generation must be deterministic for the same template, request id,
  constraints, and seed material.
- Different seed material may change reviewed deterministic ids/metadata, but
  must preserve schema validity.
- Diagnostics must be deterministic and include stable code, severity, message,
  optional JSON Pointer-style path, and optional source context.
- Invalid templates must return diagnostics rather than mutate input or depend
  on hidden state.
- Template inputs and generated outputs must remain generic and inspectable.
- The generator must not call external services, read environment secrets, use
  wall-clock time for output identity, or persist generated data.

## Compatibility Requirements

- Existing `WorldSpec`, `WorldCell`, and `EntityRef` invariants remain
  unchanged.
- Existing loader error codes and JSON Pointer path behavior remain unchanged.
- Runtime-context summaries remain bounded and must not expose raw `WorldSpec`
  or root payloads.
- Runtime tick/event behavior remains unchanged.
- Existing API routes and envelopes remain unchanged.
- Existing v0.4 Agent Loop and v0.5 memory surfaces remain unchanged.
- Historical v0.5 evidence remains handoff context only.

## Authorization Criteria

This package may record `implementation_authorized: yes` only after:

- all package docs and Chinese mirrors exist.
- `contract.md`, `technical-design.md`, `test-plan.md`, and `plan.md` are
  reviewed.
- documentation/contract evaluator reports PASS with no P0/P1 and no blocking
  unresolved P2.
- review evidence confirms this package reads and follows `0.6.1`.
- changed-file scope for future implementation is limited to the allowed files
  in this contract.
- planned tests cover deterministic output, invalid template diagnostics,
  generated `WorldSpec` loader compatibility, and adjacent runtime-context
  compatibility.

## North Star Check

This package advances world generation as a generic engine capability. It does
not turn the repository into a demo backend, does not store concrete world
content, and keeps generated worlds compatible with the existing engine spine.

## Out-of-Scope Follow-ups

- `0.6.3`: structured generation plan compiler.
- `0.6.4`: AI-assisted plan import.
- `0.6.5`: backend API, validation, metadata, and preview API.
- `0.6.6`: regeneration and runtime-readiness integration.
- `0.6.7`: dashboard preview and E2E smoke.
- v0.7 external validation readiness.
- v0.8 projection application readiness.
