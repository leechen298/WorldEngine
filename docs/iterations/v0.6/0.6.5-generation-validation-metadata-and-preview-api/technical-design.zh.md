# 技术设计

状态：review complete

## 设计边界

`0.6.5` 添加 local API preview boundary。该 route 接受 API-facing preview request，
把 source validation 和 generation 委托给现有 core functions，并返回标准 API envelope。
它不持久化 generated worlds，不把 generated worlds 加载进 runtime，不调用 providers，也不暴露
dashboard workflow。

## 计划新增 Schema

`backend/app/schemas/world_generation.py` 可新增：

- `GenerationPreviewSourceKind`，作为 `template`、`plan` 和 `imported_plan` 的
  literal/discriminator。
- `GenerationPreviewRequest`，包含 `request_id`、`source_kind`，并且只能包含
  `template_request`、`plan_request` 或 `import_request` 之一。
- `GenerationPreviewMetadata`，包含 bounded fields：
  - `generation_id`
  - `request_id`
  - `source_kind`
  - public generation metadata 中已有的 source ids 与 versions
  - `seed_digest`
  - `validation_status`
  - `diagnostics_count`
  - bounded `preview_summary`
  - 可选 redacted import source summary
- `GenerationPreviewResponse`，包含 `request_id`、`source_kind`、
  `validation_status`、`metadata`、`diagnostics` 和可选 `worldspec_preview`。

Preview request 和 response schemas 应在这能阻止 prompts/providers/private data 被静默接受时
拒绝 unexpected fields。

## 计划新增 Core

`backend/app/core/world_generation.py` 可新增：

- `preview_generation(request: GenerationPreviewRequest)`。

该 helper 应：

1. 将 `template` requests 路由到 `generate_worldspec_from_template`。
2. 将 `plan` requests 路由到 `generate_worldspec_from_plan`。
3. 将 `imported_plan` requests 路由到 `import_generation_plan`；只有 passed import
   才可继续调用 `generate_worldspec_from_plan`。
4. 将 generation results 转换为 `GenerationPreviewResponse`。
5. 对 failed preview results 返回 diagnostics，且不返回 `worldspec_preview`。
6. 对 successful preview results 返回 public `WorldSpec` preview 和 bounded metadata。

该 helper 不得重新实现 template、plan 或 import validation。

## 计划 API Route

`backend/app/api/routes/world_generation.py` 可定义：

```text
POST /world/generation/preview
```

该 route 应：

- 接受 `GenerationPreviewRequest`。
- 调用 `preview_generation`。
- 返回 `ApiResponse(data=result)`。
- 依赖现有 application validation exception handler 处理 malformed request payloads。

`backend/app/api/routes/__init__.py` 和 `backend/app/api/app_factory.py` 只能 export 和
include 该 router。除了 route inclusion，不得改变 shared handlers 或 existing routers。

## 预览摘要

Preview summary 应保持 deterministic 和 bounded，例如：

- root world id。
- root label。
- total world-cell count。
- maximum child-cell depth。
- entity reference count。

它不得包含 raw source payload echoes、prompts、provider traces、private oracle data、
external app data 或 concrete fixture content。

## 错误与状态模型

Malformed API request shape：

- HTTP status：422。
- envelope：现有 `ApiErrorResponse`。
- code：现有 validation error code `30`。

Generation/import validation failure：

- HTTP status：200。
- envelope：`ApiResponse`。
- `data.validation_status`：`failed`。
- 不包含 `data.worldspec_preview`。
- deterministic diagnostics。

Unexpected server errors：

- 保持现有 FastAPI behavior 和 app-level handlers 不变。

## 确定性与安全

Preview results 不得依赖 wall-clock time、random identity、external network、
environment secret、provider SDK、prompt execution 或 background job。Generation ids 和
seed digests 必须来自现有 deterministic generation behavior。

## 兼容性

Existing template generation、plan compilation、import behavior、API envelope、
runtime、loader、Agent/memory、params、archive、frontend 和 `backend/worldengine/`
behavior 保持不变。

## 范围外

- Regeneration。
- Runtime-readiness checks。
- Persistence。
- Frontend UI 或 client work。
- Live AI generation。
- Prompt execution 或 storage。
- E2E smoke。
- External validation 或 projection readiness。
