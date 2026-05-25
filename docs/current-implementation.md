# Current Implementation

Status: v0.1 implementation map

This document summarizes what is implemented in the current `v0.1` branch. It
describes current code, not planned v0.2 behavior.

## Summary

v0.1 is a runtime scaffold with a backend, dashboard, in-memory runtime state,
event timeline, world params flow, dry-run validation, archive summaries, and a
params-oriented agent endpoint.

v0.1 is not yet a recursive world engine. It does not implement WorldCell,
WorldSpec loading, world generation, agent memory, or pseudo-self continuity.

## Active Paths

- `backend/app/` - active backend.
- `frontend/src/` - active dashboard.
- `docs/` - project, release, iteration, and implementation docs.
- `backend/worldengine/` - legacy path; not used by the active app.

## Runtime Model

The active backend is assembled in `backend/app/api/app_factory.py`.

At app startup, the factory creates in-memory singletons on `app.state`:

- `InMemoryEventLog`
- `WorldState`
- default world module tree
- `ParamValidator`
- `ParamDryRunValidator`
- `InMemorySnapshotStore`
- `InMemorySummaryStore`
- `RuntimeEngine`
- `ArchiveService`
- `ParamsAgent`

The runtime loop is manual. A caller posts to `/runtime/step`, and
`RuntimeEngine.step()`:

1. increments `tick_id`.
2. advances `world_time_seconds` by `step_seconds`.
3. appends a `tick.advanced` event.
4. runs the default world module tree.
5. appends module events.
6. calls archive callbacks.
7. returns the current runtime state.

## Current World Model

The world model in v0.1 is parameter-driven and module-driven:

- `WorldState` stores a nested params dictionary.
- `ParamRegistry.default()` defines writable paths.
- `WorldModule` instances receive `TickContext` and emit events.
- the default module tree contains:
  - `root.heartbeat`
  - `root.counter`

This is not yet a WorldCell or WorldSpec model.

## Current Agent Model

The current implemented agent path is `ParamsAgent`. It is a params proposal
and validation loop, not an agent-in-world cognition model.

`ParamsAgent`:

- builds prompts from runtime state, current params, recent events, and a goal.
- calls an `LLMProvider` protocol.
- parses proposed patches.
- validates patches through static validation.
- validates patches through dry-run simulation.
- applies valid patches to `WorldState`.
- appends `params.applied` or `params.proposal_rejected` events.

The default app factory wires a `MockLLMProvider`, so v0.1 does not require a
real provider to start.

## Current Archive Model

`ArchiveService` is registered as a runtime step callback.

It creates:

- snapshots every `WORLD_SNAPSHOT_INTERVAL_TICKS` ticks, default `10`.
- summaries every `WORLD_SUMMARY_INTERVAL_TICKS` ticks, default `20`.

Snapshots store runtime state and params. Summaries count event types and write
a small text summary from events in the interval.

Storage is in-memory.

## Current Dashboard

The frontend is a Vue 3 + TypeScript dashboard. It loads:

- backend health.
- runtime state.
- grouped event steps.
- current world params.
- latest summary.

It exposes:

- a runtime step button.
- timeline pagination and expanded event details.
- manual world param patch form.
- params-agent auto-tune form.
- placeholder agent state panel.
- latest summary panel.

## Current API Surfaces

See `docs/api-reference-v0.1.md` for endpoint-level details.

High-level groups:

- health: `/health`
- runtime: `/runtime/state`, `/runtime/step`
- timeline: `/world/events`, `/world/event-steps`
- params: `/world/params`, `/world/params/apply`
- params agent: `/world/agent/params/propose-and-apply`
- archive: `/world/snapshots`, `/world/summaries`

## Current Verification

See `docs/testing/v0.1-test-map.md` and
`docs/testing/results/2026-05-23-v0.1-closeout.md`.

Latest recorded closeout results:

- backend: `63 passed`.
- frontend unit tests: `24 passed`.
- frontend production build: passed with a chunk-size warning.

## Known Implementation Limits

- Runtime state is process-local and in-memory.
- Event log is in-memory.
- Snapshot and summary stores are in-memory.
- World and agent schemas are placeholders.
- Event schema has only minimal fields.
- No WorldCell or WorldSpec exists yet.
- No world generation exists yet.
- No agent perception/action/memory loop exists yet.
- No external projection application consumer exists yet.
