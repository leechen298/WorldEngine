# 技术设计

状态：review complete

## 设计边界

`0.6.6` 围绕现有 generation preview service 添加 deterministic regeneration 和 readiness
checks。它不添加 runtime loader，不 activate generated specs，不持久化 regeneration
history，也不改变 `RuntimeEngine.step`。

## 计划新增 Schema

`backend/app/schemas/world_generation.py` 可新增：

- `GenerationLineage`
- `GenerationRegenerationRequest`
- `GenerationRegenerationResult`
- `RuntimeReadinessRequest`
- `RuntimeReadinessResult`

所有 request models 都应拒绝 unexpected fields。Lineage 和 readiness metadata 必须
JSON-compatible 且 bounded。

## 计划新增 Core

`backend/app/core/world_generation.py` 可新增：

- `regenerate_world(request: GenerationRegenerationRequest)`。
- `check_runtime_readiness(request: RuntimeReadinessRequest)`。

Regeneration 应复用 `preview_generation`，并使用明确 override seed 或 constraints，然后附加
deterministic lineage。Runtime readiness 应先调用 `load_worldspec`，再调用
`build_runtime_context`，成功后调用 `summarize_runtime_context`。

## 计划 API Routes

扩展现有 `backend/app/api/routes/world_generation.py` router：

```text
POST /world/generation/regenerate
POST /world/generation/runtime-readiness
```

预计不需要新的 router export 或 app-factory wiring。

## Runtime Readiness 语义

Runtime readiness 表示：

- candidate `WorldSpec` 能通过现有 loader validation。
- loaded spec 能产生 bounded runtime context summary。
- live runtime state 不被改变。
- raw `WorldSpec`、root payload 或 generated content 不会进入 tick events。

它不表示 full runtime migration、product readiness、external validation readiness、
projection readiness 或 quality approval。

## 确定性与安全

Regeneration lineage 必须从 request data deterministic 产生。结果不得依赖 wall-clock time、
random id、network call、provider SDK、prompt execution、persistence 或 background job。

## 兼容性

Existing preview、loader、runtime-context、runtime-step、event、Agent/memory、archive、
params、frontend 和 `backend/worldengine/` behavior 保持不变。
