# Contract

## Public Concepts

- EventRef: a generic event-local structured reference with required
  non-empty `id`, required non-empty `kind`, optional `role`, and free-form
  `metadata`.
- Event.refs: an optional list of EventRef objects on Event. Omitted refs
  validate as an empty list.
- Event-local reference semantics: refs annotate an event payload with
  structured references. In v0.2 they do not prove referential integrity,
  causality, runtime existence, memory linkage, projection visibility, or
  action consequences.
- EventRef contract doc: a human-readable contract document that explains
  field semantics, compatibility expectations, validation boundaries, and
  explicit non-goals.

## Compatibility Constraints

- `Event.refs` remains optional and defaults to `[]`.
- Existing Event dictionaries without refs must continue to validate.
- Existing Event dictionaries with valid refs must continue to validate.
- EventRef must continue to reject empty `id` and empty `kind`.
- Existing payload behavior, event storage shape, runtime behavior, API
  response shapes, frontend behavior, fixtures, migrations, and legacy
  `backend/worldengine/` behavior must stay unchanged.
- Schema changes must be additive unless this package returns to
  documentation review with an explicitly approved breaking-change contract.

## Allowed Changes

- Add `docs/contracts/event-ref-contract.md`.
- Update `backend/app/tests/test_event_schema_compat.py` with domain-neutral
  compatibility tests if coverage gaps remain after reading existing tests.
- Make additive validation clarifications in `backend/app/schemas/event.py`
  only if required by the approved contract and covered by tests.
- Update this package's `review.md` and `review.zh.md` with actual
  implementation evidence.

## Forbidden Changes

- Do not implement a referential integrity resolver.
- Do not implement a timeline causality engine.
- Do not bind EventRef or Event.refs to live WorldCell runtime state.
- Do not implement Agent action consequence logic.
- Do not implement memory, self-continuity, projection, generation, or
  WorldSpec loading behavior.
- Do not modify runtime services, runtime state flow, event log persistence,
  tick behavior, API routes, API response shapes, or frontend files.
- Do not modify fixtures or add fixture data.
- Do not add migrations.
- Do not modify `backend/worldengine/`.
- Do not add concrete external-world names, characters, locations, resources,
  roles, story rules, seed data, UI concepts, or product-specific backend
  logic.
- Do not create external repositories.

## Acceptance Requirements

- `docs/contracts/event-ref-contract.md` exists and describes field
  semantics, compatibility behavior, validation boundaries, event-local
  semantics, and explicit non-goals.
- Focused event schema tests either remain sufficient by documented
  assessment or are updated to cover optional refs, refs with role and
  metadata, empty `id` / `kind` rejection, default metadata, model dump /
  validate round trips, and nested EventPage / EventStepPage validation.
- Existing Event dictionaries without refs continue to validate.
- `make check-backend` passes if schema or test files are changed.
- Focused event schema pytest commands pass if schema or test files are
  changed.
- Documentation checks pass for the package docs and contract docs.
- Review evidence records every command run and does not claim unrun tests as
  passed.
- The changed-file set contains no runtime, API, frontend, fixture,
  migration, or external-repository implementation files.

## North Star Check

This package strengthens the event contract that future runtime, agent,
memory, and projection systems can consume. It does not introduce a concrete
world, product-specific backend, application surface, resolver, or causality
runtime.

## Out-of-Scope Follow-ups

- 0.2.9 audits schema, event, external boundary, and legacy boundary
  evidence.
- v0.3 may load validated generic WorldSpec data into runtime context.
- Later milestones may add event causality, action consequences, projection,
  memory, agent loop, and self-continuity.
