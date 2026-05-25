# Current Implementation

Status: v0.1 implementation map

英文版本：`current-implementation.md`。

本文档总结当前 `v0.1` 分支已经实现的内容。它描述 current code，不描述 planned v0.2 behavior。

## Summary

v0.1 是 runtime scaffold，包含 backend、dashboard、in-memory runtime state、event timeline、
world params flow、dry-run validation、archive summaries 和 params-oriented agent endpoint。

v0.1 还不是 recursive world engine。它没有实现 WorldCell、WorldSpec loading、world generation、
Agent memory 或 pseudo-self continuity。

## Active Paths

- `backend/app/` - active backend。
- `frontend/src/` - active dashboard。
- `docs/` - project、release、iteration 和 implementation docs。
- `backend/worldengine/` - legacy path；active app 不使用它。

## Runtime Model

Active backend 在 `backend/app/api/app_factory.py` 中组装。

App startup 时，factory 会在 `app.state` 上创建 in-memory singletons：

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

Runtime loop 是手动的。调用方 POST `/runtime/step`，`RuntimeEngine.step()` 会：

1. increment `tick_id`。
2. 按 `step_seconds` 推进 `world_time_seconds`。
3. 追加 `tick.advanced` event。
4. 运行 default world module tree。
5. 追加 module events。
6. 调用 archive callbacks。
7. 返回 current runtime state。

## Current World Model

v0.1 的 world model 是 parameter-driven 和 module-driven：

- `WorldState` 存储 nested params dictionary。
- `ParamRegistry.default()` 定义 writable paths。
- `WorldModule` 接收 `TickContext` 并 emit events。
- default module tree 包含：
  - `root.heartbeat`
  - `root.counter`

这还不是 WorldCell 或 WorldSpec model。

## Current Agent Model

当前实现的 agent path 是 `ParamsAgent`。它是 params proposal 与 validation loop，不是
agent-in-world cognition model。

`ParamsAgent`：

- 从 runtime state、current params、recent events 和 goal 构造 prompts。
- 调用 `LLMProvider` protocol。
- 解析 proposed patches。
- 通过 static validation 校验 patches。
- 通过 dry-run simulation 校验 patches。
- 将 valid patches 应用到 `WorldState`。
- 追加 `params.applied` 或 `params.proposal_rejected` events。

默认 app factory 使用 `MockLLMProvider`，所以 v0.1 启动不需要真实 provider。

## Current Archive Model

`ArchiveService` 注册为 runtime step callback。

它会创建：

- 每 `WORLD_SNAPSHOT_INTERVAL_TICKS` ticks 创建 snapshots，默认 `10`。
- 每 `WORLD_SUMMARY_INTERVAL_TICKS` ticks 创建 summaries，默认 `20`。

Snapshots 存储 runtime state 和 params。Summaries 统计 event types，并根据 interval 内的 events
写入简短 text summary。

Storage 是 in-memory。

## Current Dashboard

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
- placeholder agent state panel。
- latest summary panel。

## Current API Surfaces

Endpoint 级别细节见 `docs/api-reference-v0.1.md`。

High-level groups：

- health: `/health`
- runtime: `/runtime/state`, `/runtime/step`
- timeline: `/world/events`, `/world/event-steps`
- params: `/world/params`, `/world/params/apply`
- params agent: `/world/agent/params/propose-and-apply`
- archive: `/world/snapshots`, `/world/summaries`

## Current Verification

见 `docs/testing/v0.1-test-map.md` 和
`docs/testing/results/2026-05-23-v0.1-closeout.md`。

最新记录的 closeout results：

- backend: `63 passed`。
- frontend unit tests: `24 passed`。
- frontend production build: passed with a chunk-size warning。

## Known Implementation Limits

- Runtime state 是 process-local 和 in-memory。
- Event log 是 in-memory。
- Snapshot 和 summary stores 是 in-memory。
- World 和 Agent schemas 仍是 placeholders。
- Event schema 只有 minimal fields。
- 还没有 WorldCell 或 WorldSpec。
- 还没有 world generation。
- 还没有 Agent perception/action/memory loop。
- 还没有 external projection application consumer。
