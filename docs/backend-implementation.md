# Backend Implementation

Status: current backend map through v0.5

This document describes the active `backend/app/` implementation after the
v0.5 final closeout. It does not describe planned v0.6 world-generation code
until a reviewed v0.6 package lands that implementation.

Chinese mirror: `backend-implementation.zh.md`.

## Application Assembly

Entry points:

- `backend/app/main.py`
- `backend/app/api/app_factory.py`

`create_app()` builds a FastAPI app, configures CORS, creates process-local
runtime services, registers exception handlers, and includes routers.

Environment variables:

| Variable | Default | Purpose |
|---|---:|---|
| `APP_HOST` | `0.0.0.0` | Host when running `python app/main.py`. |
| `APP_PORT` | `8000` | Port when running `python app/main.py`. |
| `CORS_ORIGINS` | `http://localhost:5173,http://127.0.0.1:5173` | Allowed frontend origins. |
| `WORLD_STEP_SECONDS` | `600` | Seconds advanced by each runtime step. |
| `WORLD_SNAPSHOT_INTERVAL_TICKS` | `10` | Snapshot interval. |
| `WORLD_SUMMARY_INTERVAL_TICKS` | `20` | Summary interval. |
| `WORLD_DRYRUN_STEPS` | `20` | Dry-run simulation ticks. |
| `WORLD_DRYRUN_MAX_AVG_EVENTS_PER_TICK` | `20` | Dry-run event-rate limit. |
| `WORLD_DRYRUN_MAX_TOTAL_EVENTS` | `500` | Dry-run total event limit. |
| `WORLD_DRYRUN_MAX_FINAL_COUNTER` | `100000` | Dry-run counter upper bound. |

The app factory creates these active state/services:

- event log, world state, default world module tree.
- params validators and dry-run validator.
- snapshot and summary stores.
- process-local agent memory store.
- runtime engine and archive service.
- params agent with mock provider.
- Agent Loop service with perception builder and action adapter.

## API Envelope and Errors

Success responses use:

```text
{ "code": 0, "data": ..., "msg": "ok" }
```

Error responses use:

```text
{ "code": <number>, "msg": "<message>", "data": ... }
```

HTTP errors are normalized in `app_factory.py`. Common mappings include:

- `400 -> code 10`
- `404 -> code 24`
- `422 -> code 30`
- `500 -> code 50`

## Runtime

Files:

- `backend/app/core/runtime_engine.py`
- `backend/app/core/event_bus.py`
- `backend/app/core/runtime_context.py`
- `backend/app/core/worldspec_loader.py`

`RuntimeEngine` stores:

- `tick_id`
- `world_time_seconds`
- `step_seconds`
- `updated_at`
- optional inert runtime context

`step()` appends a `tick.advanced` event and then runs the configured world
root module.

`InMemoryEventLog` stores events in insertion order and provides:

- `snapshot()`
- bounded list access.
- cursor pagination over newest-first events.
- grouped event-step pagination by tick.

`worldspec_loader.py` and `runtime_context.py` validate generic `WorldSpec`
data and derive a bounded runtime-context summary. This bridge does not make
loaded `WorldSpec` data execute as active recursive runtime state.

## World State and Modules

Files:

- `backend/app/world/state.py`
- `backend/app/world/service.py`
- `backend/app/world/module_types.py`
- `backend/app/world/modules/*`

`WorldState` is a nested params object with:

- `get_params()`
- `apply_patch()`
- `set_param()`
- `remove_param()`
- validation override accessors.

The default module tree is:

```text
root
├── heartbeat
└── counter
```

`HeartbeatModule` emits `module.tick` unless `heartbeat.enabled` is set to
`false`.

`CounterModule` emits `module.counter` and increments an internal counter by
`counter.increment`. If the param is missing or invalid, it uses `1`.

`CompositeModule` runs child modules, aggregates child summaries, and emits
`module.aggregate`.

## WorldSpec Schema And Loader

Files:

- `backend/app/schemas/entity.py`
- `backend/app/schemas/world_cell.py`
- `backend/app/core/worldspec_loader.py`
- `backend/app/core/runtime_context.py`

`WorldCell` and `WorldSpec` provide additive recursive-world schema contracts.
The loader accepts mappings, JSON strings, or JSON bytes and returns either a
validated loaded spec or structured errors.

The runtime-context bridge derives inspectable metadata from a loaded spec and
keeps raw `WorldSpec` payloads out of runtime step outputs and event payloads.

## World Params

Files:

- `backend/app/api/routes/world_params.py`
- `backend/app/schemas/params.py`
- `backend/app/world/validation/*`
- `backend/app/world/dry_run.py`

Writable params:

| Path | Type | Notes |
|---|---|---|
| `counter.increment` | int | min `1`, max `1000`; structured values allowed. |
| `heartbeat.enabled` | bool | controls heartbeat module event emission. |
| `scene.weather` | string | stored as world param; no current module consumes it. |

Reserved prefixes:

- `system`
- `runtime`
- `_internal`

Patch ops:

- `add`
- `set`
- `remove`

Before applying params, the route runs:

1. static validation through `ParamValidator`.
2. dry-run validation through `ParamDryRunValidator`.
3. real `WorldState.apply_patch()`.
4. `params.applied` event append.

Dry-run validation clones `WorldState`, creates a fresh default module tree,
runs a sandbox `RuntimeEngine`, and checks metrics such as total events,
average events per tick, final counter value, duplicate set paths, and
no-effect counter changes.

## Archive

Files:

- `backend/app/world/archive.py`
- `backend/app/world/storage/snapshot_store.py`
- `backend/app/world/storage/summary_store.py`
- `backend/app/schemas/snapshot.py`
- `backend/app/schemas/summary.py`
- `backend/app/api/routes/archive.py`

Archive is callback-driven. `ArchiveService.on_tick_completed()` is registered
on the runtime engine.

Snapshots include:

- snapshot id.
- tick id.
- world time.
- created time.
- runtime state.
- params.

Summaries include:

- summary id.
- from/to tick.
- created time.
- text summary.
- total events and type counts.

Stores are in-memory.

## Params Agent

Files:

- `backend/app/agent/params_agent.py`
- `backend/app/agent/llm_provider.py`
- `backend/app/api/routes/world_agent.py`

The params agent is an LLM-style patch proposer. It is not a persistent world
agent.

Flow:

1. read runtime state.
2. read current params.
3. read recent events.
4. ask provider for JSON patches.
5. parse patch list.
6. run static validation.
7. run dry-run validation.
8. apply patches or retry with error feedback.
9. append `params.applied` or `params.proposal_rejected`.

The app factory currently uses `MockLLMProvider`.

## Agent Loop

Files:

- `backend/app/agent/perception.py`
- `backend/app/agent/action_adapter.py`
- `backend/app/agent/loop_service.py`
- `backend/app/schemas/agent_loop.py`
- `backend/app/api/routes/world_agent.py`

`PerceptionBuilder` creates a bounded `PerceptionFrame` from:

- runtime state.
- current params.
- recent events.
- optional runtime-context summary.
- optional memory context.

`AgentLoopService` accepts `LoopStepRequest`, uses a deterministic `noop` when
no intent is supplied, applies the reviewed action boundary, and returns
`LoopStepResponse`.

Supported action types:

- `noop`
- `params.patch`

Unsupported actions are rejected. `params.patch` uses the same static and
dry-run validation path as world params.

## Memory Substrate

Files:

- `backend/app/schemas/agent_memory.py`
- `backend/app/agent/memory.py`
- `backend/app/agent/perception.py`

v0.5 adds:

- `MemoryEvidenceRef`
- `WorkingMemoryRecord`
- `EpisodicMemoryRecord`
- `InMemoryAgentMemoryStore`
- optional `PerceptionFrame.memory_context`

The store is process-local and generic. It scopes records by `agent_id` and
`world_id`, returns deep copies, and provides deterministic bounded list access
for perception.

There is no public memory API, no durable persistence, no vector store, and no
automatic reflection/self-summary/relationship/personality drift behavior.

## Placeholder Ports and Legacy Code

`backend/app/infra/ports` and `backend/app/infra/sqlite` contain placeholder
repository interfaces/adapters. They are not the active persistence path for
runtime, archive, or memory state.

`backend/worldengine/` is legacy code and is not wired into the active FastAPI
app.
