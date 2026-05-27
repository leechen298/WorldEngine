# Intent

## Problem

`0.3.2` implemented the generic `WorldSpec` loader, and `0.3.3` defined the
runtime context bridge contract. Runtime still has no reviewed path for
holding loaded world context. Without a narrow implementation package,
bridge work could accidentally change tick behavior, expose raw `WorldSpec`
data, reinterpret `WorldCell` as `WorldModule`, or widen into generation,
Agent, memory, projection, or product-specific behavior.

## Goal

Implement a minimal optional runtime context bridge that accepts only
successful loader output or a reviewed equivalent, derives bounded inert
context, and preserves existing runtime and public behavior by default.

## Non-goals

- Do not migrate `RuntimeEngine` to `WorldCell`.
- Do not make context affect `RuntimeEngine.step()`, `world_time_seconds`,
  module execution, events, params, archive snapshots, or API responses.
- Do not add new API routes or frontend behavior.
- Do not persist runtime context.
- Do not modify schemas or migrations.
- Do not create fixtures or concrete world data.
- Do not implement world generation, Agent-in-World loop, memory,
  self-continuity, projection, story generation, or NPC chat behavior.
- Do not modify legacy `backend/worldengine/` runtime code.

## Why Now

v0.3 exists to bridge validated generic `WorldSpec` data toward runtime
without losing v0.1 compatibility. This package is the minimal implementation
step after the loader and bridge contracts have been reviewed.

## North Star Alignment

The bridge supports WorldEngine as a generic recursive world runtime
substrate by letting validated world specification data become inspectable
runtime context. It avoids demo-specific logic and keeps future Agent,
memory, generation, and projection behavior for later milestones.

## Assumptions

- `LoadedWorldSpec` from `backend/app/core/worldspec_loader.py` is the normal
  bridge input.
- Runtime context is useful first as inert metadata and diagnostics.
- Existing `RuntimeEngine` constructor calls must continue to work without
  passing context.
- The existing default module tree remains authoritative for v0.3 runtime
  behavior.
- Any API exposure of context requires a later reviewed package unless this
  package review explicitly approves an additive diagnostic path.

## Open Risks

- Adding context storage to `RuntimeEngine` could accidentally leak into
  serialized runtime responses.
- Tests may under-cover frontend-facing response compatibility if only unit
  tests are run.
- Error normalization could duplicate loader validation responsibility.
- Metadata copied into context could become domain-specific unless tests and
  review keep it neutral.
