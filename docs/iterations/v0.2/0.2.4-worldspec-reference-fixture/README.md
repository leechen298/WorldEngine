# 0.2.4 WorldSpec Reference Fixture

Status: ready for implementation

Type: code

## Goal

Create the documentation gate for the first reference WorldSpec fixture.
0.2.4 is the first verifiable world sample, not the first runnable world.

After review approval, this package may add a small deterministic
`tiny_village.world.json` fixture and focused validation tests that prove the
fixture conforms to the 0.2.2 `WorldSpec`, `WorldCell`, and `EntityRef` schema
language.

## Documents

- [x] `README.md`
- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

Chinese mirror documents are included as `.zh.md` files and must remain
synchronized with the English package documents.

## Status Checklist

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [x] Documentation gate approved
- [x] Ready for implementation
- [ ] Implementation complete
- [ ] Tests/evidence complete
- [ ] Review complete

## Implementation Boundary

The documentation gate has been reviewed and approved. The implementation
stage is limited to:

- `backend/data/world_specs/tiny_village.world.json`
- `backend/app/tests/test_worldspec_fixture.py`
- this package's `review.md` and `review.zh.md` during closeout

The documentation stage must not create the fixture or test file.

No schema implementation, production WorldSpec loader, runtime bridge,
RuntimeEngine behavior, event log storage, module, API route, frontend,
`backend/worldengine/`, village runtime, game-specific backend logic, world
generation, agent memory, pseudo-self, persistence/restart logic, or 0.2.5
work is included in this package.
