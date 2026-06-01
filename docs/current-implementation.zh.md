# 当前实现

状态：当前实现地图，覆盖到 v0.6

英文版本：`current-implementation.md`。

本文总结 v0.6 最终收口以及 0.6.11 post-closeout reliability/scope repair 后的 active
implementation。

## 摘要

WorldEngine 当前包含 FastAPI backend、Vue dashboard、process-local runtime
state、event timeline、world params flow、dry-run validation、archive summaries、
params-oriented agent endpoint、request-scoped Agent Loop、generic WorldSpec
loader/runtime-context bridge、第一层 process-local memory substrate，以及 v0.6
World Generation v1。Memory substrate 用于 Agent Loop perception 中的 bounded
memory context。

当前实现仍不是完整的递归世界引擎。它不会把递归 `WorldCell` 结构作为活跃运行时
状态运行，不声明 external validation 或 projection readiness，不会 durable
persistence memory，不暴露 public memory APIs，不运行 automatic reflection 或
self-summary behavior，不通过 relationship 或 personality drift 修改 actions，也不提供
external projection applications。

## 活跃路径

- `backend/app/` - active backend。
- `frontend/src/` - active dashboard。
- `docs/` - project、release、iteration、validation 和 implementation docs。
- `backend/worldengine/` - legacy pre-v0.1 path；active app 不使用它。

## 运行时模型

Active backend 在 `backend/app/api/app_factory.py` 中组装。

App startup 时，factory 会在 `app.state` 上创建 process-local services：

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

World generation 当前是 stateless、request-scoped 的能力。它通过 schema/core
helpers 和 API routes 暴露，不作为 persistent generation service 存在于 `app.state`。

Runtime loop 是手动的。调用方 POST `/runtime/step`，`RuntimeEngine.step()` 会：

1. 递增 `tick_id`。
2. 按 `step_seconds` 推进 `world_time_seconds`。
3. 追加 `tick.advanced` event。
4. 运行 default world module tree。
5. 追加 module events。
6. 调用 archive callbacks。
7. 返回 current runtime state。

`RuntimeEngine` 也可以携带由 loaded generic `WorldSpec` 派生出的可选 inert
runtime-context summary。当前 runtime 仍不会把 loaded `WorldSpec` data 作为活跃递归
世界状态执行。

## 当前世界模型

活跃 runtime world model 仍是 parameter-driven 和 module-driven：

- `WorldState` 存储 nested params dictionary。
- `ParamRegistry.default()` 定义 writable params paths。
- `WorldModule` 接收 `TickContext` 并 emit events。
- default module tree 包含 `root.heartbeat` 和 `root.counter`。

Generic recursive-world schema support 已通过 `WorldCell`、`WorldSpec` schema
validation，以及 loader/runtime-context bridge helpers 存在。该能力是兼容性和交接
基座；生成的 `WorldSpec` payload 可以被 validate 和 preview，但不会作为活跃递归
runtime state 执行。

## 当前 World Generation 模型

v0.6 在 `backend/app/core/world_generation.py` 和
`backend/app/schemas/world_generation.py` 下新增 generic World Generation v1。

它可以：

- 定义 generic world-generation request、template、plan、validation、
  provenance、preview、regeneration 和 runtime-readiness schemas。
- 校验 generic templates 和 structured generation plans。
- 从已评审 templates 生成 deterministic generic `WorldSpec` data。
- 将 structured generation plans compile 为可检查的 `WorldSpec` material。
- 只以 structured data 和 redacted provenance 导入 AI-assisted plans。
- 在 import boundary 拒绝 prompt/provider/secret/oracle fields 以及 `access_token`、
  `apiKey`、`providerTrace` 等 secret-bearing aliases，同时允许 redacted token usage
  metrics。
- 在 `/world/generation` 下暴露 preview、regeneration 和 runtime-readiness APIs。

它不会调用 live providers、执行 prompts、持久化 generated worlds、把 generated worlds
作为 active runtime state 运行、批准 subjective generation quality，也不声明 external
validation-world 或 projection-application readiness。

## 当前 Agent 模型

当前 agent implementation 有两条路径。

`ParamsAgent` 是 LLM-style params proposal 与 validation loop。它会：

- 从 runtime state、current params、recent events 和 goal 构造 prompts。
- 调用 `LLMProvider` protocol。
- 解析 proposed patches。
- 通过 static validation 校验 patches。
- 通过 dry-run simulation 校验 patches。
- 将 valid patches 应用到 `WorldState`。
- 追加 `params.applied` 或 `params.proposal_rejected` events。

`AgentLoopService` 执行一次 request-scoped Agent-in-World loop step。它会：

- 从 runtime state、world params、recent events、可选 runtime-context summary 和
  可选 memory context 构建 bounded `PerceptionFrame`。
- 接受显式 `ActionIntent`，或使用 deterministic `noop` intent。
- 只应用已评审的 `noop` 和 `params.patch` action boundary。
- 返回包含 perception、intent 和 action result evidence 的 `LoopStepResponse`。

v0.5 memory work 不改变 action semantics。Memory context 只是 perception 的
read-only input，不是隐藏 action side effect。

## 当前 Memory 模型

v0.5 新增了 generic process-local memory substrate：

- `MemoryEvidenceRef`
- `WorkingMemoryRecord`
- `EpisodicMemoryRecord`
- `InMemoryAgentMemoryStore`
- `PerceptionFrame` 上的 `MemoryContextSummary`

Working 和 episodic records 是通用结构，按 `agent_id` 和 `world_id` 归属，并带有
可审查 provenance。In-memory store 返回 deep copies，使用 deterministic bounded
ordering，并已接入 default app，使 perception 可以包含 bounded read-only memory
context。

当前实现没有 public memory read/write API、durable persistence、vector retrieval、
automatic reflection、self-summary generation、relationship behavior，也没有
personality drift action modifier。

## 当前归档模型

`ArchiveService` 注册为 runtime step callback。

它会创建：

- 每 `WORLD_SNAPSHOT_INTERVAL_TICKS` ticks 创建 snapshots，默认 `10`。
- 每 `WORLD_SUMMARY_INTERVAL_TICKS` ticks 创建 summaries，默认 `20`。

Snapshots 存储 runtime state 和 params。Summaries 统计 event types，并根据 interval
内的 events 写入简短 text summary。Storage 是 process-local 和 in-memory。

## 当前 Dashboard

Frontend 是 Vue 3 + TypeScript dashboard。它加载：

- backend health。
- runtime state。
- grouped event steps。
- current world params。
- latest summary。

它提供：

- runtime step button。
- timeline pagination 和 expanded event details。
- manual world param patch form。
- params-agent auto-tune form。
- E2E 覆盖的 agent loop baseline interactions。
- latest summary panel。
- generation preview form，展示 validation、diagnostics 和 runtime-readiness result。

Dashboard 不暴露 product memory management、projection application readiness、
external validation UI、live-provider generation 或 generation quality approval。

## 当前 API surfaces

`docs/api-reference-v0.5.md` 是 generation 之前的 API baseline；legacy v0.1
reference 见 `docs/api-reference-v0.1.md`。v0.6 generation API 行为记录在 v0.6
iteration package evidence 中。

High-level groups：

- health：`/health`
- runtime：`/runtime/state`, `/runtime/step`
- timeline：`/world/events`, `/world/event-steps`
- params：`/world/params`, `/world/params/apply`
- params agent：`/world/agent/params/propose-and-apply`
- agent loop：`/world/agent/loop/step`
- archive：`/world/snapshots`, `/world/summaries`
- generation：`/world/generation/preview`, `/world/generation/regenerate`,
  `/world/generation/runtime-readiness`

v0.6 没有 public memory API。

## 当前验证

当前 v0.6 closeout evidence 记录在：

- `docs/iterations/v0.6/review.md`
- `docs/iterations/v0.6/0.6.10-v0.6-final-closeout/final-closeout.md`
- `docs/iterations/v0.6/0.6.11-post-closeout-reliability-and-scope-repair/review.md`
- `docs/testing/results/2026-06-01-v0.6-reliability-validation.md`

关键已记录 v0.6 和 post-review repair 结果包括：

- focused backend/API 0.6.11 repair suite：`59 passed`。
- full backend regression：`233 passed`。
- frontend unit suite：`36 passed`。
- frontend production build：通过，仅有既有 Vite chunk-size warning。
- full E2E：`17 passed`。
- 0.6.11 package-specific changed-file scope guard：`out_of_scope=0`。
- forbidden implementation sentinel：`backend/worldengine`、`backend/app/alembic`、
  `backend/migrations` 和 `test-results` 无输出。
- saved Agent smoke checker：既有 saved result PASS。
- minimal autonomous saved-result checker：既有 saved result PASS。
- closeout consistency evaluator：PASS。

v0.6 明确不声明 external validation readiness、projection readiness、full product
readiness、新 live Agent smoke、full autonomous runner、live provider 或
generation-quality pass。

早期 v0.5 closeout 和 validation evidence 记录在：

- `docs/releases/v0.5.md`
- `docs/iterations/v0.5/0.5.7-v0.5-final-closeout/final-closeout.md`
- `docs/testing/results/2026-05-31-v0.5-overall-validation.md`

关键已记录结果包括：

- focused backend memory substrate：`7 passed`。
- focused perception and loop API：`16 passed`。
- focused backend memory/loop/action compatibility：`33 passed`。
- full backend regression：`145 passed`。
- frontend unit baseline：`28 passed`。
- frontend production build：通过，仅有既有 Vite chunk-size warning。
- focused Agent Loop E2E：`9 passed`。
- full E2E：`15 passed`。
- Agent smoke saved-result checker：PASS。
- minimal autonomous saved-result checker：PASS。

这些是已记录的 evidence artifacts。本次文档更新不重新运行这些完整验证流程。

## 已知实现限制

- Runtime state 是 process-local 和 in-memory。
- Event log 是 in-memory。
- Snapshot、summary 和 memory stores 都是 in-memory。
- Loaded `WorldSpec` data 可以提供 inert runtime context，但不会作为活跃递归世界状态执行。
- World generation 已实现为 deterministic request/preview/import boundaries，不是
  active recursive runtime execution 或 persistent generated world storage。
- Runtime、archive 或 memory state 均没有 durable persistence 或 migrations。
- 没有 public memory API。
- 没有 vector retrieval、automatic reflection、self-summary generation、
  relationship behavior 或 personality drift action modifier。
- 不声明 external validation readiness、projection application readiness、full product
  readiness、Agent smoke/autonomous coverage、live-provider behavior 或
  generation-quality pass。
