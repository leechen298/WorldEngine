# Contract

Status: review complete

implementation_authorized: yes

## Public Concepts

This package defines the structured-plan subset of the `0.6.1` generation
contract and extends the `0.6.2` deterministic generator surface additively.

- `GenerationPlan`: normalized, provider-independent data that describes a
  candidate `WorldSpec` structure and constraints.
- `PlanCell`: a plan entry for one world cell, including generic id, optional
  label, entity references, child cells, and metadata.
- `PlanGenerationRequest`: request wrapper carrying request id, a
  `GenerationPlan`, optional deterministic seed material, and optional
  request-level constraints.
- Plan compiler diagnostics: deterministic `GenerationDiagnostic` records for
  unsupported plan versions, duplicate ids, duplicate entity references,
  invalid bounds, disallowed entity kinds, non-JSON seed/material values, and
  malformed plan metadata.
- Plan generation metadata: existing generation metadata extended additively
  so plan-generated output records plan id/version and source kind while
  preserving template-generation metadata behavior.

## Allowed Changes

Documentation stage:

- create and update this package under `docs/iterations/v0.6/`.
- update parent v0.6 status surfaces only for current child state and evidence.
- record subagent/evaluator evidence.

Implementation stage, only after `implementation_authorized: yes`:

- update `backend/app/schemas/world_generation.py`.
- update `backend/app/core/world_generation.py`.
- add focused tests:
  - `backend/app/tests/test_generation_plan_schema.py`
  - `backend/app/tests/test_structured_generation_plan_compiler.py`
- update existing focused generation tests only where needed to verify
  compatibility:
  - `backend/app/tests/test_world_generation_schema.py`
  - `backend/app/tests/test_deterministic_world_generation.py`
- update this package `review.md` / `review.zh.md`.
- update parent v0.6 status surfaces only for current child state and evidence.

If implementation needs a new core module instead of extending
`backend/app/core/world_generation.py`, stop and return to documentation
review before adding that path.

## Forbidden Changes

- Do not modify `backend/app/api/**`, `backend/app/schemas/api.py`,
  `frontend/**`, persistence/repository modules, migrations, fixtures,
  generated output files, external repositories, or `backend/worldengine/**`.
- Do not modify `backend/app/core/runtime_context.py`,
  `backend/app/core/runtime_engine.py`, `backend/app/core/worldspec_loader.py`,
  `backend/app/schemas/world_cell.py`, or `backend/app/schemas/entity.py`
  unless a design gap is found and this package returns to documentation
  review first.
- Do not add public generation API routes, AI-assisted plan import, live
  provider calls, preview API, regeneration behavior, dashboard UI, E2E
  behavior, external validation readiness, projection readiness, durable
  persistence, or migrations.
- Do not accept free-form prompt text as executable generation behavior.
- Do not read environment secrets, use wall-clock/random identity for output,
  or persist generated data.
- Do not add concrete demo-world names, maps, characters, locations,
  resources, story rules, private validation oracle details, generated seed
  data, or application-specific backend behavior.

## Implementation Requirements

- Plan compilation must be deterministic for the same plan, request id,
  constraints, and seed material.
- Generated output must validate against the current `WorldSpec` schema with
  `schema_version == "0.2"`.
- The compiler must return diagnostics rather than mutating input or depending
  on hidden state.
- Diagnostics must include stable code, severity, message, optional JSON
  Pointer-style path, and source context.
- Strict JSON seed/material canonicalization from `0.6.2` must remain
  applicable to plan compilation.
- Plan-generated output must remain generic and inspectable.
- Template-generation behavior from `0.6.2` must remain compatible.

## Compatibility Requirements

- Existing `WorldSpec`, `WorldCell`, and `EntityRef` invariants remain
  unchanged.
- Existing loader error codes and JSON Pointer path behavior remain unchanged.
- Existing runtime-context summaries remain bounded and unchanged.
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
- review evidence confirms this package reads and follows `0.6.1` and
  `0.6.2`.
- changed-file scope for future implementation is limited to the allowed files
  in this contract.
- planned tests cover valid plan compilation, invalid diagnostics, duplicate
  ids/refs, constraint violations, unsupported plan version, non-JSON
  seed/material, no input mutation, loader compatibility, and template
  generator compatibility.

## North Star Check

This package advances generic world generation as a structured engine
capability. It does not turn WorldEngine into a demo backend and does not add
application-specific generation behavior.

## Out-of-Scope Follow-ups

- `0.6.4`: AI-assisted plan import.
- `0.6.5`: backend API, validation, metadata, and preview API.
- `0.6.6`: regeneration and runtime-readiness integration.
- `0.6.7`: dashboard preview and E2E smoke.
- v0.7 external validation readiness.
- v0.8 projection application readiness.
