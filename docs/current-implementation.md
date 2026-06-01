# Current Implementation

Status: current implementation map through v0.6

This document summarizes the active implementation after the v0.6 final
closeout and the 0.6.11 post-closeout reliability/scope repair.

Chinese mirror: `current-implementation.zh.md`.

## Summary

WorldEngine currently provides a FastAPI backend, Vue dashboard, process-local
runtime state, event timeline, world params flow, dry-run validation, archive
summaries, a params-oriented agent endpoint, a request-scoped Agent Loop, a
generic WorldSpec loader/runtime-context bridge, the first process-local memory
substrate for bounded Agent Loop perception context, and v0.6 World Generation
v1.

The active implementation is still not a complete recursive world engine. It
does not run recursive `WorldCell` structures as active runtime state, claim
external validation or projection readiness, persist memory durably, expose
public memory APIs, run automatic reflection or self-summary behavior, modify
actions through relationship or personality drift, or provide external
projection applications.

## Active Paths

- `backend/app/` - active backend.
- `frontend/src/` - active dashboard.
- `docs/` - project, release, iteration, validation, and implementation docs.
- `backend/worldengine/` - legacy pre-v0.1 path; not used by the active app.

## Runtime Model

The active backend is assembled in `backend/app/api/app_factory.py`.

At app startup, the factory creates process-local services on `app.state`:

- `InMemoryEventLog`
- `WorldState`
- default world module tree
- `ParamValidator`
- `ParamDryRunValidator`
- `InMemorySnapshotStore`
- `InMemorySummaryStore`
- `InMemoryAgentMemoryStore`
- `RuntimeEngine`
- `ArchiveService`
- `ParamsAgent`
- `AgentLoopService`

World generation is currently stateless and request-scoped. It is exposed
through schema/core helpers and API routes, not through a persistent generation
service on `app.state`.

The runtime loop is manual. A caller posts to `/runtime/step`, and
`RuntimeEngine.step()`:

1. increments `tick_id`.
2. advances `world_time_seconds` by `step_seconds`.
3. appends a `tick.advanced` event.
4. runs the default world module tree.
5. appends module events.
6. calls archive callbacks.
7. returns the current runtime state.

`RuntimeEngine` may also carry an optional inert runtime-context summary derived
from a loaded generic `WorldSpec`. The current runtime still does not execute
loaded `WorldSpec` data as active recursive world state.

## Current World Model

The active runtime world model is still parameter-driven and module-driven:

- `WorldState` stores a nested params dictionary.
- `ParamRegistry.default()` defines writable params paths.
- `WorldModule` instances receive `TickContext` and emit events.
- the default module tree contains `root.heartbeat` and `root.counter`.

Generic recursive-world schema support exists through `WorldCell` and
`WorldSpec` schema validation plus loader/runtime-context bridge helpers. That
support is a compatibility and handoff substrate; generated `WorldSpec` payloads
can be validated and previewed, but they are not executed as active recursive
runtime state.

## Current World Generation Model

v0.6 adds generic World Generation v1 under `backend/app/core/world_generation.py`
and `backend/app/schemas/world_generation.py`.

It can:

- define generic world-generation request, template, plan, validation,
  provenance, preview, regeneration, and runtime-readiness schemas.
- validate generic templates and structured generation plans.
- generate deterministic generic `WorldSpec` data from reviewed templates.
- compile structured generation plans into inspectable `WorldSpec` material.
- import AI-assisted plans only as structured data with redacted provenance.
- reject prompt/provider/secret/oracle fields and secret-bearing aliases such
  as `access_token`, `apiKey`, and `providerTrace` at the import boundary while
  allowing redacted token usage metrics.
- expose preview, regeneration, and runtime-readiness APIs under
  `/world/generation`.

It does not call live providers, execute prompts, persist generated worlds, run
generated worlds as active runtime state, approve subjective generation quality,
or claim external validation-world or projection-application readiness.

## Current Agent Model

The active agent implementation has two paths.

`ParamsAgent` is an LLM-style params proposal and validation loop. It:

- builds prompts from runtime state, current params, recent events, and a goal.
- calls an `LLMProvider` protocol.
- parses proposed patches.
- validates patches through static validation.
- validates patches through dry-run simulation.
- applies valid patches to `WorldState`.
- appends `params.applied` or `params.proposal_rejected` events.

`AgentLoopService` runs one request-scoped Agent-in-World loop step. It:

- builds a bounded `PerceptionFrame` from runtime state, world params, recent
  events, optional runtime-context summary, and optional memory context.
- accepts an explicit `ActionIntent` or uses a deterministic `noop` intent.
- applies only the reviewed `noop` and `params.patch` action boundary.
- returns `LoopStepResponse` with perception, intent, and action result
  evidence.

Action semantics are unchanged by v0.5 memory work. Memory context is read-only
input to perception, not a hidden action side effect.

## Current Memory Model

v0.5 added a generic process-local memory substrate:

- `MemoryEvidenceRef`
- `WorkingMemoryRecord`
- `EpisodicMemoryRecord`
- `InMemoryAgentMemoryStore`
- `MemoryContextSummary` on `PerceptionFrame`

Working and episodic records are generic, scoped by `agent_id` and `world_id`,
and carry inspectable provenance. The in-memory store returns deep copies,
applies deterministic bounded ordering, and is wired into the default app so
perception can include bounded read-only memory context.

There is no public memory read/write API, no durable persistence, no vector
retrieval, no automatic reflection, no self-summary generation, no relationship
behavior, and no personality drift action modifier in the current
implementation.

## Current Archive Model

`ArchiveService` is registered as a runtime step callback.

It creates:

- snapshots every `WORLD_SNAPSHOT_INTERVAL_TICKS` ticks, default `10`.
- summaries every `WORLD_SUMMARY_INTERVAL_TICKS` ticks, default `20`.

Snapshots store runtime state and params. Summaries count event types and write
a small text summary from events in the interval. Storage is process-local and
in-memory.

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
- agent loop baseline interactions covered by E2E.
- latest summary panel.
- generation preview form with validation, diagnostics, and runtime-readiness
  result display.

The dashboard does not expose product memory management, projection application
readiness, external validation UI, live-provider generation, or generation
quality approval.

## Current API Surfaces

See `docs/api-reference-v0.5.md` for the pre-generation API baseline and
`docs/api-reference-v0.1.md` for the legacy v0.1 reference. v0.6 generation API
behavior is recorded in the v0.6 iteration package evidence.

High-level groups:

- health: `/health`
- runtime: `/runtime/state`, `/runtime/step`
- timeline: `/world/events`, `/world/event-steps`
- params: `/world/params`, `/world/params/apply`
- params agent: `/world/agent/params/propose-and-apply`
- agent loop: `/world/agent/loop/step`
- archive: `/world/snapshots`, `/world/summaries`
- generation: `/world/generation/preview`,
  `/world/generation/regenerate`, `/world/generation/runtime-readiness`

No public memory API exists in v0.6.

## Current Verification

Current v0.6 closeout evidence is recorded in:

- `docs/iterations/v0.6/review.md`
- `docs/iterations/v0.6/0.6.10-v0.6-final-closeout/final-closeout.md`
- `docs/iterations/v0.6/0.6.11-post-closeout-reliability-and-scope-repair/review.md`
- `docs/testing/results/2026-06-01-v0.6-reliability-validation.md`

Key recorded v0.6 and post-review repair results include:

- focused backend/API 0.6.11 repair suite: `59 passed`.
- full backend regression: `233 passed`.
- frontend unit suite: `36 passed`.
- frontend production build: passed with an existing Vite chunk-size warning.
- full E2E: `17 passed`.
- 0.6.11 package-specific changed-file scope guard: `out_of_scope=0`.
- forbidden implementation sentinel: no output for `backend/worldengine`,
  `backend/app/alembic`, `backend/migrations`, and `test-results`.
- saved Agent smoke checker: PASS for the existing saved result.
- minimal autonomous saved-result checker: PASS for the existing saved result.
- closeout consistency evaluator: PASS.

v0.6 deliberately does not claim external validation readiness, projection
readiness, full product readiness, new live Agent smoke, full autonomous runner,
live provider, or generation-quality pass.

Earlier v0.5 closeout and validation evidence is recorded in:

- `docs/releases/v0.5.md`
- `docs/iterations/v0.5/0.5.7-v0.5-final-closeout/final-closeout.md`
- `docs/testing/results/2026-05-31-v0.5-overall-validation.md`

Key recorded results include:

- focused backend memory substrate: `7 passed`.
- focused perception and loop API: `16 passed`.
- focused backend memory/loop/action compatibility: `33 passed`.
- full backend regression: `145 passed`.
- frontend unit baseline: `28 passed`.
- frontend production build: passed with an existing Vite chunk-size warning.
- focused Agent Loop E2E: `9 passed`.
- full E2E: `15 passed`.
- Agent smoke saved-result checker: PASS.
- minimal autonomous saved-result checker: PASS.

These are recorded evidence artifacts. This document update does not rerun those
full validation flows.

## Known Implementation Limits

- Runtime state is process-local and in-memory.
- Event log is in-memory.
- Snapshot, summary, and memory stores are in-memory.
- Loaded `WorldSpec` data can inform inert runtime context but is not executed
  as active recursive world state.
- World generation is implemented as deterministic request/preview/import
  boundaries, not as active recursive runtime execution or persistent generated
  world storage.
- No durable persistence or migrations are present for runtime, archive, or
  memory state.
- No public memory API exists.
- No vector retrieval, automatic reflection, self-summary generation,
  relationship behavior, or personality drift action modifier exists.
- No external validation readiness, projection application readiness, full
  product readiness, Agent smoke/autonomous coverage, live-provider behavior, or
  generation-quality pass is claimed.
