# Technical Design

## Overview

0.2.5 is a boundary reset. The implementation should make the core repository
domain-neutral again while preserving generic recursive-world schema language.

The implementation stage has two work surfaces:

- active documentation cleanup.
- fixture and test cleanup.

No runtime behavior, API behavior, frontend behavior, loader behavior, Agent
behavior, memory behavior, or generation behavior changes are included.

## Active Documentation Cleanup

Replace concrete Demo world language in active docs with generic consumer
language:

- replace concrete demo surface wording with external projection application.
- replace superseded concrete fixture direction wording with external validation world or
  external fixture world.
- replace validation interface wording with external validation consumer.
- keep the point that external consumers validate WorldEngine through public
  contracts.
- keep the point that concrete Demo worlds must not live in or shape the core
  repository.

The cleanup should preserve existing English and Chinese mirrors where they
exist. If an active English doc is changed and a `.zh.md` mirror exists, update
the mirror in the same implementation pass.

## Fixture Strategy

Remove the concrete fixture:

- delete `backend/data/world_specs/historical concrete fixture path`; or
- replace it with `backend/data/world_specs/schema_smoke_world.json`.

If replacement is chosen, the new fixture must be domain-neutral. Use generic
identifiers and labels such as:

- `schema-smoke-world`
- `Schema Smoke World`
- `root`
- `child-a`
- `child-b`
- `entity-a`

The fixture must not encode a concrete Demo world, role, location, resource,
plot rule, narrative rule, schedule, inventory, or UI concept.

## Test Strategy

Replace the concrete fixture test:

- delete or rewrite `backend/app/tests/test_worldspec_fixture.py`.
- create `backend/app/tests/test_worldspec_schema_smoke.py` if a new file name
  is clearer.

The schema smoke test may directly read JSON with `json` and `pathlib`. It must
not implement a production WorldSpec loader.

The test should verify only generic schema behavior:

- `WorldSpec.model_validate(...)` accepts the fixture dictionary.
- `schema_version` is `"0.2"`.
- `root` exists and is a `WorldCell`.
- `root.kind` is `"world"`.
- `root.child_cells` supports recursive child worlds.
- nested child cells validate recursively.
- `EntityRef` supports generic entity references through `entity_refs`.
- `model_dump()` followed by `WorldSpec.model_validate(...)` round-trips.

The test must not assert concrete Demo semantics. The active test file must not
contain these terms:

- `historical concrete anchor`
- `concrete demo`
- `Concrete demo`
- `historical concrete anchor`
- `historical-child-cell`
- `historical area`
- `historical-nested-entity`
- `historical actor`

## External Fixture Boundary Documentation

Add `docs/external-fixture-boundary.md` during implementation. It should define
the core-repository boundary for future external fixtures:

- external fixtures consume public WorldEngine schemas, APIs, CLI commands, or
  validation contracts.
- external fixtures must not require core repository knowledge of their world
  entities, locations, resources, story rules, or UI.
- the core repository may store redacted evidence, contract examples, and
  validation report formats.
- the core repository must not store external fixture seed data or internal
  validation world implementation details.

## Validation Report Template

Add `docs/validation-report-template.md` during implementation. It should
capture redacted validation evidence without embedding external world details:

- validation target name or redacted identifier.
- WorldEngine version or commit.
- public contract exercised.
- commands or runner invocation.
- pass/fail result.
- redacted evidence summary.
- compatibility notes.
- unresolved findings.

The template must not require external-world seed data, concrete entity names,
locations, resources, plot rules, or internal validation implementation files.

## Roadmap Reset

Update active roadmap docs to remove the superseded concrete fixture direction direction and
use generic engine milestones:

- v0.2.5: core boundary cleanup and roadmap reset.
- v0.2.6: iteration workflow and plan reset.
- v0.3: WorldSpec loader and runtime bridge, loading generic WorldSpec only.
- v0.3.5: external fixture contract readiness, defining how external runners
  call the main repository without creating those repositories.
- v0.4: Agent-in-World minimal loop with perception, action intent, validated
  action result, and event consequence.
- v0.5: memory and self-continuity substrate.
- v0.6: world generation v1.
- v0.7: external validation readiness / projection consumer readiness.
- v0.8: first external projection application readiness.

## Compatibility

The implementation must preserve generic schema compatibility. It may remove
or replace concrete fixture data and concrete fixture assertions, but it must
not remove or narrow WorldSpec, WorldCell, EntityRef, or EventRef.

Runtime, API, frontend, and legacy backend behavior must remain unchanged.
