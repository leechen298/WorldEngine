# Plan

## Phase 1: Documentation Cleanup

1. Re-read the active direction docs and this package contract before editing.
2. Search for concrete Demo world anchors:

   ```bash
   rg -n "tiny|village|Village|Tiny|workshop|square|notice-board|reference village|village-like" AGENTS.md AGENTS.zh.md README.md README.zh.md docs backend/app/tests backend/data
   ```

3. Update `docs/project-north-star.md` and `docs/project-north-star.zh.md` to
   remove first concrete Demo surface wording and use external projection
   application / external validation world language.
4. Update `docs/product-model.md` and `docs/product-model.zh.md` to keep the
   product model generic and remove first concrete product surface wording.
5. Update `docs/scope-boundaries.md` and `docs/scope-boundaries.zh.md` to
   remove permission for concrete Demo fixtures inside the core repository.
6. Update `docs/roadmap.md` and `docs/roadmap.zh.md` with the reset roadmap:
   v0.2.5 boundary cleanup, v0.2.6 generic schema foundation closeout, v0.3
   generic WorldSpec loader/runtime bridge, v0.3.5 external fixture contract
   readiness, v0.4 Agent-in-World loop, v0.5 memory/self-continuity, v0.6 world
   generation, v0.7 external validation/projection readiness, and v0.8 first
   external projection application readiness.
7. Update `AGENTS.md` and `AGENTS.zh.md` to remove first concrete Demo surface
   guidance from active agent instructions.
8. Update `README.md` and `README.zh.md` to remove reference world runtime
   wording from current capability limitations.
9. Update other active docs found by the search, including architecture,
   glossary, release planning, and v0.2 index or plan docs when they contain
   active concrete Demo world direction.
10. Add `docs/external-fixture-boundary.md`.
11. Add `docs/validation-report-template.md`.
12. Mark `docs/iterations/v0.2/0.2.4-worldspec-reference-fixture/` as a
   historical iteration artifact that no longer defines future roadmap
   direction.

## Phase 2: Code And Test Cleanup

1. Delete `backend/data/world_specs/tiny_village.world.json` or replace it with
   `backend/data/world_specs/schema_smoke_world.json`.
2. Delete or rewrite `backend/app/tests/test_worldspec_fixture.py` as a generic
   schema smoke test, preferably `backend/app/tests/test_worldspec_schema_smoke.py`.
3. Ensure the generic schema smoke test verifies:
   - `WorldSpec.model_validate(...)`.
   - `schema_version == "0.2"`.
   - root `WorldCell` existence.
   - recursive `child_cells`.
   - generic `EntityRef` support.
   - `model_dump()` / `model_validate(...)` round-trip.
4. Ensure the active test file does not contain concrete Demo terms:
   `tiny`, `village`, `Village`, `Tiny`, `workshop`, `square`,
   `notice-board`, or `villager`.
5. Run the implementation-stage verification commands from `test-plan.md`.
6. Update this package's `review.md` with changed files, exact commands run,
   test results, compatibility review, scope review, unresolved findings, and
   final assessment.

## Phase Boundary

Phase 1 and Phase 2 may be implemented in one reviewed implementation stage
after this package is approved, but the implementer must keep the edits scoped
to this contract. Do not start loader, runtime bridge, Agent loop, memory,
world generation, frontend, external repository, or new concrete Demo world
work.
