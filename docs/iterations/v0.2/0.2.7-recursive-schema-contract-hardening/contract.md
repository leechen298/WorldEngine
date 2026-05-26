# Contract

## Public Concepts

- EntityRef: a generic reference to an entity by non-empty `id`, non-empty
  `kind`, optional `label`, and free-form `metadata`.
- WorldCell: a recursive world unit with non-empty `id`, optional `label`,
  literal `kind = "world"`, entity references, child cells, and metadata.
- WorldSpec: a versioned recursive world specification with
  `schema_version = "0.2"`, non-empty `id`, optional `label`, a required root
  WorldCell, and metadata.
- Generic schema contract docs: human-readable contract documents that explain
  schema fields, compatibility expectations, validation boundaries, and
  non-runtime semantics.

## Compatibility Constraints

- Existing runtime behavior must stay unchanged.
- Existing API response shapes must stay unchanged.
- Existing frontend behavior must stay unchanged.
- Existing EventRef / Event.refs compatibility must not be affected.
- Schema changes must be additive unless this package returns to
  documentation review with an explicitly approved breaking-change contract.
- Existing valid EntityRef, WorldCell, and WorldSpec payloads covered by
  current tests must continue to validate.
- Existing invalid generic values covered by current tests must continue to be
  rejected.

## Allowed Changes

- Add `docs/contracts/entity-ref-contract.md`.
- Add `docs/contracts/worldcell-contract.md`.
- Add `docs/contracts/worldspec-contract.md`.
- Update `backend/app/tests/test_world_cell_schema.py` with domain-neutral
  schema tests if coverage gaps remain after reading existing tests.
- Update `backend/app/tests/test_worldspec_schema_smoke.py` with
  domain-neutral schema tests if coverage gaps remain after reading existing
  tests.
- Make additive validation clarifications in `backend/app/schemas/entity.py`
  or `backend/app/schemas/world_cell.py` only if required by the approved
  contract and covered by tests.
- Update this package's `review.md` and `review.zh.md` with actual
  implementation evidence.

## Forbidden Changes

- Do not implement a WorldSpec loader.
- Do not connect WorldSpec to RuntimeEngine.
- Do not modify runtime services, runtime state flow, event log persistence,
  or tick behavior.
- Do not modify API routes or API response shapes.
- Do not modify frontend dashboard files.
- Do not modify fixtures or add fixture data.
- Do not add migrations.
- Do not modify `backend/worldengine/`.
- Do not add concrete external-world names, characters, locations, resources,
  roles, story rules, seed data, UI concepts, or product-specific backend
  logic.
- Do not implement generation, projection, memory, agent loop,
  self-continuity, resolver, or causality behavior.
- Do not create external repositories.

## Acceptance Requirements

- The three contract documents exist and describe field semantics,
  compatibility behavior, validation boundaries, and explicit non-goals.
- Focused schema tests either remain sufficient by documented assessment or
  are updated to cover recursive children, invalid generic values, and
  model_dump / model_validate round trips.
- `make check-backend` passes if schema or test files are changed.
- Focused schema pytest commands pass if schema or test files are changed.
- Documentation checks pass for the package docs and contract docs.
- Review evidence records every command run and does not claim unrun tests as
  passed.
- The changed-file set contains no runtime, API, frontend, fixture, migration,
  or external-repository implementation files.

## North Star Check

This package strengthens reusable recursive world schema contracts. It does
not introduce a concrete world, product-specific backend, or application
surface. Runtime loading and future agent, memory, generation, and projection
work remain out of scope.

## Out-of-Scope Follow-ups

- 0.2.8 hardens EventRef and Event.refs.
- 0.2.9 audits schema, event, external boundary, and legacy boundary
  evidence.
- v0.3 may load validated generic WorldSpec data into runtime context.
- Later milestones may add generation, projection, agent loop, memory, and
  self-continuity.
