# Intent

## Background

0.2.2 defined the structural schema language for recursive worlds by adding
`EntityRef`, `WorldCell`, and `WorldSpec`. 0.2.3 added an event-local
reference layer with `EventRef` and `Event.refs`.

0.2.4 should now provide the first small reference `WorldSpec` fixture so the
schema language has a stable, reviewable data example and future test input.
The fixture is a schema-focused reference data fixture. It is not a runtime
world and not an application implementation.

## User Outcome

Future maintainers should be able to inspect one historical concrete anchor deterministic world spec
and understand the intended shape of a valid recursive `WorldSpec` without
starting the runtime engine, adding a loader, or interpreting application behavior.

## Engineering Outcome

After review approval, implementation should add:

- a single JSON fixture at `backend/data/world_specs/historical concrete fixture path`.
- a focused Python test at `backend/app/tests/test_worldspec_fixture.py`.

The test should read the JSON with `json` and `pathlib`, validate it with
`WorldSpec.model_validate(...)`, and exercise recursive `WorldCell` /
`EntityRef` validation through the existing schema models.

## Why Now

- 0.2.2 created the minimum schema structure.
- 0.2.3 added event-local refs without connecting runtime behavior.
- 0.2.4 can now validate the schema language with a stable fixture.
- v0.3 can later decide how a validated `WorldSpec` is loaded into runtime.
- v0.7 or later roadmap work can turn historical-concrete-fixture ideas into a complete
  historical concrete fixture direction or product-facing projection.

## Non-Goals

- Do not implement code in this documentation stage.
- Do not create the JSON fixture or fixture test yet.
- Do not implement a production WorldSpec loader.
- Do not implement a runtime bridge.
- Do not make historical concrete fixture runnable in 0.2.4.
- Do not add concrete demo runtime, application-specific backend logic, world generation,
  agent memory, pseudo-self, or frontend behavior.
