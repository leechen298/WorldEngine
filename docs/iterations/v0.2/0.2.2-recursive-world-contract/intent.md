# Intent

## Problem

WorldEngine has a v0.1 runtime/event scaffold and v0.2 direction documents,
but it does not yet have a reviewed schema contract for recursive world
structure. Without that contract, follow-up work can accidentally jump into
runtime migration, village-specific behavior, loader design, or agent memory
before the minimal world structure is stable.

## Goal

Create the implementation-ready documentation gate for additive Pydantic
schemas that express:

- `EntityRef` as a lightweight reference or declaration entry.
- `WorldCell` as the minimal recursive world unit.
- `WorldSpec` as the minimal top-level container for a recursive world.

The successful end state is a reviewed plan that lets the next implementation
stage add these schemas and focused tests without changing v0.1 runtime
behavior.

## Non-goals

- Do not implement code in this documentation stage.
- Do not migrate `RuntimeEngine` to `WorldCell`.
- Do not implement a WorldSpec loader.
- Do not add the reference WorldSpec fixture.
- Do not implement village runtime or game-specific logic.
- Do not modify the dashboard or frontend.
- Do not implement world generation.
- Do not implement agent memory, agent inner-world, or pseudo-self continuity.
- Do not modify `backend/worldengine/`.
- Do not start 0.2.3 event contract work.

## Why Now

0.2.1 established project direction and iteration governance. 0.2.2 is the
first code package in v0.2 and should define the recursive world structure
before event extensions, reference fixtures, loader work, or runtime bridging.

## North Star Alignment

This package supports recursive world structures by defining how a world can
contain child worlds. It keeps the first village-like surface as a future
projection and avoids turning WorldEngine into a village-specific backend.
