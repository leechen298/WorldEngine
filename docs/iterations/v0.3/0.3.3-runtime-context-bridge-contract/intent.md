# Intent

## Problem

`0.3.2` gives WorldEngine a minimal loader for validated generic `WorldSpec`
data, but it still does not define how that loaded data may approach runtime
state. Without a reviewed bridge contract, implementation could accidentally
place raw `WorldSpec` data into runtime payloads, reinterpret `WorldCell` as a
runtime module, or break v0.1 tick, event, params, archive, API, or frontend
compatibility.

## Goal

Create a reviewable runtime context bridge contract that defines accepted
input, derived context shape, runtime boundaries, compatibility evidence,
error categories, assumptions, risks, and verification requirements for a
later minimal bridge implementation.

## Non-goals

- Do not implement the runtime context bridge.
- Do not change `RuntimeEngine`.
- Do not connect loaded data to runtime behavior.
- Do not add API routes or response fields.
- Do not emit events or put raw `WorldSpec` into event payloads.
- Do not alter params, archive, persistence, frontend, fixture, migration, or
  legacy behavior.
- Do not map `WorldCell` directly to `WorldModule`.
- Do not implement world generation, Agent-in-World loop, memory,
  self-continuity, projection, story generation, or NPC chat behavior.

## Why Now

v0.3 is the bridge from schema and loader foundations toward runtime context.
The loader must remain data-only, and runtime work must preserve v0.1
compatibility. A contract is needed before `0.3.4` can safely add any optional
runtime context path.

## North Star Alignment

This package supports the north star by preparing a generic route from
structured world specifications toward runtime without narrowing WorldEngine
into a concrete game, demo world, external validation fixture, or product
backend.

## Assumptions

- `0.3.2` loader output or a reviewed equivalent is the only bridge input.
- The initial runtime context can be useful as optional, inert metadata before
  it drives behavior.
- Existing v0.1 runtime state and module behavior remain the compatibility
  baseline for v0.3 bridge work.
- Any future mapping from `WorldCell` to runtime modules requires a separate
  reviewed package.

## Open Risks

- A future bridge implementation may be tempted to expose too much raw
  `WorldSpec` data for convenience.
- Context storage inside `RuntimeEngine` could accidentally change serialized
  runtime responses.
- Metadata copied from `WorldSpec` could gain domain-specific meaning unless
  the implementation keeps it neutral.
- Compatibility evidence for frontend-facing shapes may require broader tests
  than the minimal backend bridge implementation otherwise suggests.
