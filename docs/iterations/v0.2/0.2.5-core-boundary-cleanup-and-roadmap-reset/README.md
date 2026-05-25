# 0.2.5 Core Boundary Cleanup And Roadmap Reset

Status: review complete

Type: mixed

## Goal

Remove concrete Demo world anchors from WorldEngine core planning and prepare
the follow-up cleanup that keeps the repository focused on a generic recursive
world runtime substrate.

This package exists because previous v0.2 work introduced Tiny Village,
village-like game, and reference village wording as fixture or validation
language. That wording is now risky because it can cause future coding agents
to treat WorldEngine as a Demo game backend instead of a general engine.

0.2.5 will reset that boundary by documenting the later cleanup of active
project direction, roadmap language, fixture data, and fixture tests. It will
also reserve public interfaces for future external fixture worlds and external
validation consumers without creating those repositories in this package.

## Scope

This documentation-planning pass creates only this iteration package. It does
not modify active roadmap, north star, scope, README, AGENTS, runtime, schema,
API, frontend, tests, fixtures, or release files.

The implementation stage for this package may later:

- remove Tiny Village, village-like game, and reference village anchors from
  active project direction documents.
- replace concrete Demo world fixture data with a domain-neutral schema smoke
  fixture.
- replace concrete fixture tests with generic WorldSpec schema smoke tests.
- add core-repository docs for external fixture boundaries and redacted
  validation reports.
- reset v0.3 and later roadmap language around generic engine consumers.

The implementation stage must not create an external fixture repository,
external validation repository, concrete Demo world, game UI, runtime bridge,
WorldSpec loader, Agent loop, memory substrate, or world generation system.

## Documents

- [x] `README.md`
- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

## Status Checklist

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [x] Documentation gate approved
- [x] Ready for implementation
- [x] Implementation complete
- [x] Tests/evidence complete
- [x] Review complete

## Roadmap Reset Summary

The proposed roadmap direction after this package is:

- v0.2.5: core boundary cleanup and roadmap reset.
- v0.2.6: generic WorldSpec / WorldCell schema foundation closeout.
- v0.3: WorldSpec loader and runtime bridge for generic WorldSpec data only.
- v0.3.5: external fixture contract readiness.
- v0.4: Agent-in-World minimal loop.
- v0.5: memory and self-continuity substrate.
- v0.6: world generation v1.
- v0.7: external validation readiness / projection consumer readiness.
- v0.8: first external projection application readiness.

Concrete Demo worlds remain outside the WorldEngine core repository and should
consume the engine through public contracts.
