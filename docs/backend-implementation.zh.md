# 后端实现

状态：当前后端地图，覆盖到 v0.5

英文版本：`backend-implementation.md`。

本文描述 v0.5 最终收口后的 active `backend/app/` implementation。在已评审 v0.6
package 落地 world-generation code 前，本文不描述 planned v0.6 implementation。

## 应用组装

入口：

- `backend/app/main.py`
- `backend/app/api/app_factory.py`

`create_app()` 构建 FastAPI app，配置 CORS，创建 process-local runtime services，
注册 exception handlers，并 include routers。

Environment variables：

| Variable | Default | Purpose |
|---|---:|---|
| `APP_HOST` | `0.0.0.0` | 运行 `python app/main.py` 时的 host。 |
| `APP_PORT` | `8000` | 运行 `python app/main.py` 时的 port。 |
| `CORS_ORIGINS` | `http://localhost:5173,http://127.0.0.1:5173` | 允许的 frontend origins。 |
| `WORLD_STEP_SECONDS` | `600` | 每个 runtime step 推进的秒数。 |
| `WORLD_SNAPSHOT_INTERVAL_TICKS` | `10` | Snapshot interval。 |
| `WORLD_SUMMARY_INTERVAL_TICKS` | `20` | Summary interval。 |
| `WORLD_DRYRUN_STEPS` | `20` | Dry-run simulation ticks。 |
| `WORLD_DRYRUN_MAX_AVG_EVENTS_PER_TICK` | `20` | Dry-run event-rate limit。 |
| `WORLD_DRYRUN_MAX_TOTAL_EVENTS` | `500` | Dry-run total event limit。 |
| `WORLD_DRYRUN_MAX_FINAL_COUNTER` | `100000` | Dry-run counter upper bound。 |

App factory 会创建这些 active state/services：

- event log、world state、default world module tree。
- params validators 和 dry-run validator。
- snapshot 和 summary stores。
- process-local agent memory store。
- runtime engine 和 archive service。
- 带 mock provider 的 params agent。
- 包含 perception builder 与 action adapter 的 Agent Loop service。

## API Envelope 和 Errors

Success responses 使用：

```text
{ "code": 0, "data": ..., "msg": "ok" }
```

Error responses 使用：

```text
{ "code": <number>, "msg": "<message>", "data": ... }
```

HTTP errors 在 `app_factory.py` 中 normalize。常见 mappings：

- `400 -> code 10`
- `404 -> code 24`
- `422 -> code 30`
- `500 -> code 50`

## Runtime

Files：

- `backend/app/core/runtime_engine.py`
- `backend/app/core/event_bus.py`
- `backend/app/core/runtime_context.py`
- `backend/app/core/worldspec_loader.py`

`RuntimeEngine` 存储：

- `tick_id`
- `world_time_seconds`
- `step_seconds`
- `updated_at`
- optional inert runtime context

`step()` 追加 `tick.advanced` event，然后运行配置的 world root module。

`InMemoryEventLog` 按插入顺序存储 events，并提供：

- `snapshot()`
- bounded list access。
- newest-first events 的 cursor pagination。
- 按 tick 分组的 event-step pagination。

`worldspec_loader.py` 和 `runtime_context.py` 会校验 generic `WorldSpec` data，
并派生 bounded runtime-context summary。这个 bridge 不会让 loaded `WorldSpec` data
成为活跃递归 runtime state。

## World State 和 Modules

Files：

- `backend/app/world/state.py`
- `backend/app/world/service.py`
- `backend/app/world/module_types.py`
- `backend/app/world/modules/*`

`WorldState` 是 nested params object，提供：

- `get_params()`
- `apply_patch()`
- `set_param()`
- `remove_param()`
- validation override accessors。

Default module tree：

```text
root
├── heartbeat
└── counter
```

`HeartbeatModule` 会 emit `module.tick`，除非 `heartbeat.enabled` 被设为 `false`。

`CounterModule` 会 emit `module.counter`，并按 `counter.increment` 增加内部 counter。
如果 param 缺失或 invalid，则使用 `1`。

`CompositeModule` 运行 child modules，聚合 child summaries，并 emit
`module.aggregate`。

## WorldSpec Schema 和 Loader

Files：

- `backend/app/schemas/entity.py`
- `backend/app/schemas/world_cell.py`
- `backend/app/core/worldspec_loader.py`
- `backend/app/core/runtime_context.py`

`WorldCell` 和 `WorldSpec` 提供 additive recursive-world schema contracts。Loader
接受 mappings、JSON strings 或 JSON bytes，并返回 validated loaded spec 或
structured errors。

Runtime-context bridge 从 loaded spec 派生可审查 metadata，并让 raw `WorldSpec`
payloads 不出现在 runtime step outputs 或 event payloads 中。

## World Params

Files：

- `backend/app/api/routes/world_params.py`
- `backend/app/schemas/params.py`
- `backend/app/world/validation/*`
- `backend/app/world/dry_run.py`

Writable params：

| Path | Type | Notes |
|---|---|---|
| `counter.increment` | int | min `1`, max `1000`; 允许 structured values。 |
| `heartbeat.enabled` | bool | 控制 heartbeat module event emission。 |
| `scene.weather` | string | 作为 world param 存储；当前没有 module 消费它。 |

Reserved prefixes：

- `system`
- `runtime`
- `_internal`

Patch ops：

- `add`
- `set`
- `remove`

应用 params 前，route 会运行：

1. 通过 `ParamValidator` static validation。
2. 通过 `ParamDryRunValidator` dry-run validation。
3. 真实调用 `WorldState.apply_patch()`。
4. 追加 `params.applied` event。

Dry-run validation 会 clone `WorldState`，创建 fresh default module tree，运行 sandbox
`RuntimeEngine`，并检查 total events、average events per tick、final counter value、
duplicate set paths 和 no-effect counter changes 等 metrics。

## Archive

Files：

- `backend/app/world/archive.py`
- `backend/app/world/storage/snapshot_store.py`
- `backend/app/world/storage/summary_store.py`
- `backend/app/schemas/snapshot.py`
- `backend/app/schemas/summary.py`
- `backend/app/api/routes/archive.py`

Archive 是 callback-driven。`ArchiveService.on_tick_completed()` 注册到 runtime
engine。

Snapshots include：

- snapshot id。
- tick id。
- world time。
- created time。
- runtime state。
- params。

Summaries include：

- summary id。
- from/to tick。
- created time。
- text summary。
- total events 和 type counts。

Stores 是 in-memory。

## Params Agent

Files：

- `backend/app/agent/params_agent.py`
- `backend/app/agent/llm_provider.py`
- `backend/app/api/routes/world_agent.py`

Params agent 是 LLM-style patch proposer。它不是 persistent world agent。

Flow：

1. read runtime state。
2. read current params。
3. read recent events。
4. ask provider for JSON patches。
5. parse patch list。
6. run static validation。
7. run dry-run validation。
8. apply patches or retry with error feedback。
9. append `params.applied` 或 `params.proposal_rejected`。

App factory 当前使用 `MockLLMProvider`。

## Agent Loop

Files：

- `backend/app/agent/perception.py`
- `backend/app/agent/action_adapter.py`
- `backend/app/agent/loop_service.py`
- `backend/app/schemas/agent_loop.py`
- `backend/app/api/routes/world_agent.py`

`PerceptionBuilder` 会从以下信息创建 bounded `PerceptionFrame`：

- runtime state。
- current params。
- recent events。
- optional runtime-context summary。
- optional memory context。

`AgentLoopService` 接受 `LoopStepRequest`；当请求没有提供 intent 时使用
deterministic `noop`；然后应用已评审 action boundary，并返回 `LoopStepResponse`。

Supported action types：

- `noop`
- `params.patch`

Unsupported actions 会被 rejected。`params.patch` 使用与 world params 相同的 static
和 dry-run validation path。

## Memory Substrate

Files：

- `backend/app/schemas/agent_memory.py`
- `backend/app/agent/memory.py`
- `backend/app/agent/perception.py`

v0.5 新增：

- `MemoryEvidenceRef`
- `WorkingMemoryRecord`
- `EpisodicMemoryRecord`
- `InMemoryAgentMemoryStore`
- optional `PerceptionFrame.memory_context`

Store 是 process-local 和 generic。它按 `agent_id` 与 `world_id` 归属 records，返回
deep copies，并为 perception 提供 deterministic bounded list access。

当前没有 public memory API、durable persistence、vector store，也没有 automatic
reflection/self-summary/relationship/personality drift behavior。

## Placeholder Ports 和 Legacy Code

`backend/app/infra/ports` 和 `backend/app/infra/sqlite` 包含 placeholder repository
interfaces/adapters。它们不是 runtime、archive 或 memory state 的 active
persistence path。

`backend/worldengine/` 是 legacy code，没有接入 active FastAPI app。
