# Architecture

Status: current architecture overview and v0.2 direction

英文版本：`architecture.md`。

## Current v0.1 State

WorldEngine v0.1 是 experimental monorepo scaffold：

- `backend/app/` 包含 active FastAPI backend。
- `frontend/` 包含 active Vue dashboard。
- `docs/` 包含 architecture 和 process documents。
- `backend/worldengine/` 包含较早的 pre-v0.1 code，不是 active implementation path。

当前 active backend 已经具备 basic runtime primitives：

- `backend/app/core/` 提供 clock、scheduler、event bus 和 runtime engine。
- `backend/app/world/` 提供 world service boundaries、params、archive、modules、validation 和
  storage placeholders。
- `backend/app/agent/` 提供 agent service boundaries。
- `backend/app/schemas/` 提供 shared Pydantic models。
- `backend/app/api/` 提供 HTTP routes 和 app factory。

## v0.2 Architecture Direction

v0.2 是 Recursive World Foundation。它应该先建立 schema 和 spec language，再迁移 runtime：

- `WorldCell` 作为 minimal recursive world unit。
- `WorldSpec` 作为 generated 或 loadable world 的 structured representation。
- `EntityRef` 作为 entities、agents、resources、rules、locations 和 future memory links 的
  shared reference shape。
- additive `Event` fields，用于 source、target、location、visibility、importance 和 causal
  references。
- 一个可验证为 WorldSpec 的 reference `tiny_village.world.json` fixture。

## Runtime Boundary

v0.2 不能用 WorldCell execution 替换 `RuntimeEngine`。Runtime bridging 属于 WorldSpec 和 Event
contracts 稳定后的后续工作。

## Legacy Boundary

`backend/worldengine/` 应该视为 legacy，除非后续 iteration contract 明确允许 cleanup 或 migration。
新功能应该进入 `backend/app/`。

## Projection Boundary

Game、dashboard 和 API projections 应该 consume engine state 与 events。它们不应该拥有 core
world rules、Agent memory 或 Agent pseudo-self formation。
