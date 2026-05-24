# Plan

Status: ready for review

## Documentation Stage

1. Create the 0.2.4 package directory under `docs/iterations/v0.2/`.
2. Draft the English seven-file package:
   `README.md`, `intent.md`, `contract.md`, `technical-design.md`,
   `test-plan.md`, `plan.md`, and `review.md`.
3. Draft synchronized Chinese `.zh.md` mirrors.
4. Update the v0.2 README and plan documents so 0.2.4 moves from `planned`
   to `ready for review`.
5. Run documentation-stage verification commands and record evidence in
   `review.md` and `review.zh.md`.
6. Stop before implementation.

## Review Gate

Review must confirm:

- The fixture is described as the first verifiable world sample, not the first
  runnable world.
- The implementation boundary is limited to
  `backend/data/world_specs/tiny_village.world.json`,
  `backend/app/tests/test_worldspec_fixture.py`, and this package's closeout
  review files.
- The fixture contract uses the existing 0.2.2 `WorldSpec`, `WorldCell`, and
  `EntityRef` schema language.
- Test-only JSON reading is allowed, but production WorldSpec loader work is
  forbidden.
- 0.2.4 is not marked as ready for implementation, implementation complete,
  or review complete.

## Implementation Stage After Approval

After review approval only:

1. Add `backend/data/world_specs/tiny_village.world.json`.
2. Add `backend/app/tests/test_worldspec_fixture.py`.
3. Run the focused fixture test.
4. Run the broader backend app test suite.
5. Run the documented import/validation smoke command.
6. Update `review.md` and `review.zh.md` with implementation-stage evidence.

## Stop Conditions

Stop and return to documentation review if implementation reveals any need to:

- modify `EntityRef`, `WorldCell`, `WorldSpec`, or `Event` schema contracts.
- add a WorldSpec loader or runtime bridge.
- connect the fixture to `RuntimeEngine`.
- add API route, frontend, event log, module, generator, persistence, or
  `backend/worldengine/` behavior.
- add village runtime, game-specific backend logic, world generation, agent
  memory, pseudo-self, or agent behavior loops.
- start 0.2.5.
