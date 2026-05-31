# 合同

状态：review complete

implementation_authorized: yes

## 公共概念

- `GenerationLineage`：bounded metadata，用于连接 parent generation request 或
  generation id 与 regenerated output。
- `GenerationRegenerationRequest`：API-facing request，复用已评审的
  `GenerationPreviewRequest`，应用 bounded override seed/constraints，并记录为什么请求
  regeneration。
- `GenerationRegenerationResult`：response，包含 lineage、regenerated preview、
  runtime-readiness result 和 deterministic diagnostics。
- `RuntimeReadinessRequest`：API-facing request，携带 candidate `WorldSpec` 和 source
  label，用于 loader/context checks。
- `RuntimeReadinessResult`：bounded result，显示 loader success、runtime context bridge
  success、可选 bounded runtime context summary、diagnostics，以及
  `does_not_mutate_runtime: true`。

## API 合同

Implementation 可扩展现有 generation router：

```text
POST /world/generation/regenerate
POST /world/generation/runtime-readiness
```

两个 route 对 accepted request shapes 必须返回 `ApiResponse[...]`，对 malformed request
payloads 必须使用现有 `ApiErrorResponse` validation handler。Generation、regeneration、
loader 或 runtime-context validation failures 应返回 HTTP 200、failed status 和 diagnostics。

## 允许变更

Documentation stage：

- 创建并更新 `docs/iterations/v0.6/` 下的本 package。
- 只为 current child state 和 evidence 更新 parent v0.6 status surfaces。
- 记录 subagent/evaluator evidence。

Implementation stage，仅在 `implementation_authorized: yes` 后：

- 更新 `backend/app/schemas/world_generation.py`。
- 更新 `backend/app/core/world_generation.py`。
- 更新 `backend/app/api/routes/world_generation.py`。
- 添加 focused tests：
  - `backend/app/tests/test_generation_regeneration_api.py`
- 只在需要时更新现有 focused compatibility tests：
  - `backend/app/tests/test_generation_preview_api.py`
  - `backend/app/tests/test_worldspec_loader.py`
  - `backend/app/tests/test_runtime_context_bridge.py`
  - `backend/app/tests/test_runtime_step.py`
  - 直接受影响的 existing generation schema/compiler/import tests。
- 更新本 package `review.md` / `review.zh.md`。
- 只为 current child state 和 evidence 更新 parent v0.6 status surfaces。

由于 `0.6.5` 已 include generation router，预计不需要修改
`backend/app/api/routes/__init__.py` 和 `backend/app/api/app_factory.py`。如果
implementation 需要触碰它们，必须停止并回到 documentation review。

## 禁止变更

- 不改变 `RuntimeEngine.step`、tick/time semantics、event emission semantics 或 existing
  runtime route response shapes。
- 不自动 install、persist 或 activate generated specs 到 live runtime。
- 不添加 persistence/repository modules、migrations、fixtures、generated output files、
  external repositories 或 `backend/worldengine/**`。
- 不添加 frontend UI、dashboard workflow、E2E、external validation runner、projection
  app behavior、live provider calls、network calls、prompt execution、provider traces、
  private oracle details 或 concrete world content。
- 不在 runtime events 或 readiness summaries 中暴露 raw `WorldSpec` payloads 或 root
  payloads。
- 不声明超出 loader/context bridge readiness 的 runtime readiness。

## 兼容要求

- Existing generation preview API 保持兼容。
- Existing API envelopes 保持兼容。
- Existing `worldspec_loader`、`runtime_context` 和 `RuntimeEngine` behavior 保持兼容。
- Runtime-context summaries 保持 bounded。
- Readiness checks inert，且不 mutate runtime state。

## 授权标准

本 package 只有在满足以下条件后才可记录 `implementation_authorized: yes`：

- 所有 package docs 和中文镜像存在。
- Documentation/contract evaluator 报告 PASS，且无 P0/P1、无 blocking unresolved P2。
- contract/design/test-plan/plan 明确禁止 runtime mutation、tick/event semantic changes、
  persistence/migrations、frontend UI、external validation/projection behavior、live
  AI/provider behavior、concrete content 和 `backend/worldengine/**`。
- planned tests 覆盖 regeneration success/failure、deterministic lineage、readiness
  success/failure、bounded context summary、runtime events 中不出现 raw `WorldSpec`、
  existing preview compatibility、runtime bridge compatibility、full backend regression
  和 scope guard。

## 范围外后续

- `0.6.7`：dashboard preview and E2E smoke。
- v0.7 external validation readiness。
- v0.8 projection application readiness。
