# Legacy Boundary

状态：v0.2 compatibility boundary

本文定义 0.2.10 后仓库路径的 active、legacy、placeholder、documentation-only
和 future bridge 边界。本文不改变 runtime behavior。

## 状态说明

- `active`：当前 v0.1 runtime 或 dashboard 正在使用的路径。
- `legacy`：保留但未接入 active app 的代码。
- `placeholder`：已存在的结构性接口或 adapter，但不是 active persistence 或
  runtime path。
- `documentation`：contracts、process、implementation maps 和 review evidence。
- `future`：只能通过后续 reviewed package 执行。

## 边界表

| Surface | Status | Evidence | Boundary |
|---|---|---|---|
| `backend/app/` | active | `AGENTS.md`, `docs/current-implementation.md`, `docs/backend-implementation.md` | Active FastAPI backend，包括 runtime scaffold、event log、world params flow、archive service、params-agent scaffold、schemas 和 API routes。除非后续 contract 另有说明，新 runtime features 应进入此路径。 |
| `frontend/` | active | `AGENTS.md`, `docs/current-implementation.md` | Active Vue dashboard。v0.2.10 不改变 dashboard behavior。 |
| `docs/` | documentation | iteration standard, contracts, implementation maps, review evidence | 项目方向、current implementation descriptions、contracts、release drafts 和 package evidence 的来源。Documentation 可以描述边界，但除非有 command evidence 支撑，不单独证明 runtime behavior。 |
| `backend/app/infra/ports` 和 `backend/app/infra/sqlite` | placeholder | `docs/backend-implementation.md` | Repository interfaces 和 SQLite adapters 已存在，但 v0.1 runtime state、events、snapshots 和 summaries 仍是 in-memory。没有 reviewed implementation package 前，不应把这些 adapters 视为 active persistence。 |
| `backend/worldengine/` | legacy | `AGENTS.md`, `docs/current-implementation.md`, `docs/backend-implementation.md`, `docs/architecture.md` | pre-v0.1 code，作为 historical implementation material 保留。它没有接入 active FastAPI app，v0.2 不应在此增加新 runtime features。 |
| `docs/contracts/*` | documentation / additive contracts | 0.2.7 和 0.2.8 reviews | EntityRef、WorldCell、WorldSpec、EventRef 和 Event.refs contracts 定义 schema/event foundations。它们在 v0.2 不是 runtime loader 或 bridge behavior。 |
| external fixture 或 validation repositories | future external consumers | `docs/external-fixture-boundary.md` | 未来可以通过 public APIs、schemas、CLI contracts、exported contracts 或 redacted reports 消费 WorldEngine；它们不是 core repository 的一部分。 |

## Active Backend Boundary

Active backend 由 `backend/app/api/app_factory.py` 组装，并通过
`backend/app/main.py` 进入。当前 v0.1 runtime model 在 `app.state` 上使用
in-memory singletons：

- event log。
- runtime state 和 engine。
- world params state。
- default world module tree。
- params validation 和 dry-run validation。
- snapshot 和 summary stores。
- archive service。
- params-agent scaffold。

0.2.10 不增加 loaders、repositories、migrations、persistence behavior 或
runtime bridge wiring。

## Active Dashboard Boundary

Active dashboard 位于 `frontend/`。Current implementation docs 将其描述为
用于 health、runtime state、grouped event steps、world params、params-agent
proposals、placeholder agent state、snapshots 和 summaries 的 Vue dashboard。

0.2.10 不改变 frontend files、UI behavior、API selectors、E2E tests 或
dashboard expectations。

## Legacy Backend Boundary

`backend/worldengine/` 仍是 legacy。它可以作为 historical context 阅读，但
不是 active runtime behavior，也不是 v0.2 新功能来源。

规则：

- 不在 `backend/worldengine/` 下增加新 runtime features。
- v0.2.10 不迁移或删除 legacy files。
- 不从 legacy modules 推断 active API behavior。
- 没有后续 reviewed package 前，不恢复 legacy NPC、environment、scheduler、
  HTTP server 或 world state code。
- 未来 migration work 必须先说明 source behavior、compatibility target 和
  test evidence，再移动任何内容到 active paths。

## Placeholder Infrastructure Boundary

`backend/app/infra/ports` 和 `backend/app/infra/sqlite` 是 placeholders。它们
表达未来 repository boundary，但不是 v0.1 runtime state、event storage、
snapshots 或 summaries 的 active persistence。

未来 persistence work 必须保持 additive 或 compatibility-preserving，除非后续
reviewed contract 明确允许 breaking change。

## v0.2 Foundation Boundary

v0.2 schema 和 event work 是 additive：

- `EntityRef` 描述 neutral references。
- `WorldCell` 描述 recursive world units。
- `WorldSpec` 包装 versioned recursive world specification。
- `EventRef` 和可选 `Event.refs` 描述 event-local references。

这些 contracts 不会加载 WorldSpec data，不会替换 `RuntimeEngine`，不会把 event
references 绑定到 runtime objects，不会解析 causality，也不会创建 agent memory。

## Future Bridge Boundary

v0.3 只有通过独立 reviewed package，才可以设计 WorldSpec loading 或 runtime
bridge behavior。该工作必须保持或明确 review：

- 当前 runtime state 和 step behavior。
- 当前 API response envelopes 和 endpoint shapes。
- 当前 event storage、pagination 和 grouped step behavior。
- world params validation 和 dry-run behavior。
- archive snapshot 和 summary behavior。
- frontend-facing compatibility。
- legacy path handling。

0.2.10 只记录边界，不批准 bridge。
