# Contract

## Public Concepts

- Core boundary cleanup: removal of concrete Demo world anchors from active
  WorldEngine core docs, fixture data, and fixture tests.
- Generic schema smoke fixture: a domain-neutral WorldSpec JSON file used only
  to prove schema validation, recursion, entity references, and round-trip
  behavior.
- External fixture world: a future out-of-repository consumer that validates
  WorldEngine through public contracts without shaping core repository
  internals.
- External validation report: a redacted report format that records external
  validation evidence without storing external world implementation details in
  the core repository.
- Historical iteration artifact: prior iteration documentation that may retain
  concrete Demo language only when explicitly marked as historical context.

## Compatibility Constraints

- Existing runtime behavior must stay compatible.
- Existing API response shapes must stay compatible.
- Existing frontend behavior must stay compatible.
- Existing generic schema contracts must be preserved.
- Schema changes are not required for this package. If any schema cleanup is
  proposed later, it must be additive unless a reviewed contract explicitly
  allows a breaking change.
- WorldCell, WorldSpec, EntityRef, EventRef, and other generic schema names
  must not be removed because of this cleanup.

## Allowed Changes

After this documentation gate is reviewed and approved, implementation may:

- Update `docs/project-north-star.md` and `docs/project-north-star.zh.md` to
  replace concrete Demo world wording with external projection application,
  external validation world, and external fixture world language.
- Update `docs/product-model.md` and `docs/product-model.zh.md` to keep
  WorldEngine positioned as a generic recursive world runtime substrate.
- Update `docs/scope-boundaries.md` and `docs/scope-boundaries.zh.md` to remove
  allowances for concrete Demo fixtures inside the core repository.
- Update `docs/roadmap.md` and `docs/roadmap.zh.md` to remove the v0.7
  superseded concrete fixture direction milestone and replace it with external validation
  readiness / projection consumer readiness.
- Update `AGENTS.md` and `AGENTS.zh.md` to remove concrete demo surface or
  concrete demo surface surface wording from current guidance.
- Update `README.md` and `README.zh.md` to remove references to running a
  superseded concrete fixture direction.
- Update other active core docs if they contain the same concrete Demo anchors,
  including architecture, glossary, release planning, and v0.2 index or plan
  docs.
- Mark `docs/iterations/v0.2/0.2.4-worldspec-reference-fixture/` as a
  historical iteration artifact that no longer defines future direction.
- Delete `backend/data/world_specs/historical concrete fixture path` or replace it with
  `backend/data/world_specs/schema_smoke_world.json`.
- Delete or rewrite `backend/app/tests/test_worldspec_fixture.py` as
  `backend/app/tests/test_worldspec_schema_smoke.py`.
- Add `docs/external-fixture-boundary.md`.
- Add `docs/validation-report-template.md`.
- Reset later roadmap direction to generic engine milestones:
  - v0.2.5: core boundary cleanup and roadmap reset.
  - v0.2.6: iteration workflow and plan reset.
  - v0.3: WorldSpec loader and runtime bridge.
  - v0.3.5: external fixture contract readiness.
  - v0.4: Agent-in-World minimal loop.
  - v0.5: memory and self-continuity substrate.
  - v0.6: world generation v1.
  - v0.7: external validation readiness / projection consumer readiness.
  - v0.8: first external projection application readiness.
- Update this package's `review.md` with implementation evidence during
  closeout.

## Forbidden Changes

- Do not create an external fixture repository.
- Do not create an external validation repository.
- Do not implement a WorldSpec loader.
- Do not implement a runtime bridge.
- Do not implement an Agent loop.
- Do not implement memory or self-continuity.
- Do not implement world generation.
- Do not modify the frontend dashboard.
- Do not modify v0.1 runtime behavior.
- Do not modify API routes or response shapes.
- Do not modify production event log storage.
- Do not modify `backend/worldengine/` runtime behavior.
- Do not delete WorldCell, WorldSpec, EntityRef, EventRef, or other generic
  schema contracts.
- Do not replace historical concrete fixture with another concrete Demo world.
- Do not introduce any new concrete world, role, location, resource, plot rule,
  narrative rule, application UI, seed data, or internal external-validation world
  implementation detail.
- Do not keep active tests or active fixtures coupled to concrete Demo world
  words, entities, locations, resources, or assertions.
- Do not treat historical iteration artifacts as current roadmap direction.

## Active Documentation Anchor Cleanup

Implementation must treat the following as active-doc cleanup candidates:

- `AGENTS.md`
- `AGENTS.zh.md`
- `README.md`
- `README.zh.md`
- `docs/project-north-star.md`
- `docs/project-north-star.zh.md`
- `docs/product-model.md`
- `docs/product-model.zh.md`
- `docs/scope-boundaries.md`
- `docs/scope-boundaries.zh.md`
- `docs/roadmap.md`
- `docs/roadmap.zh.md`
- `docs/architecture.md`
- `docs/architecture.zh.md`
- `docs/glossary.md`
- `docs/glossary.zh.md`
- `docs/releases/v0.2.md`
- `docs/releases/v0.2.zh.md`
- `docs/iterations/v0.2/README.md`
- `docs/iterations/v0.2/README.zh.md`
- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`

The implementer must search for concrete Demo world anchors before editing and
must not assume this list is complete.

## Historical Documentation Rule

Historical iteration packages may retain old wording only if the new 0.2.5
cleanup clearly marks that wording as historical. Historical documents must not
be used as future roadmap authority after this package closes.

## North Star Check

This package strengthens the north star by removing concrete Demo world
semantics from the core repository. It keeps WorldEngine focused on recursive
world generation, runtime, event contracts, agent-in-world behavior, memory,
self-continuity, and projections.

## Out-of-Scope Follow-ups

- External fixture repository creation.
- External validation repository creation.
- Runtime loading of WorldSpec data.
- Runtime bridge from WorldSpec to v0.1 runtime.
- Agent-in-world loop.
- Memory and self-continuity substrate.
- World generation v1.
- User-facing projection application implementation.
