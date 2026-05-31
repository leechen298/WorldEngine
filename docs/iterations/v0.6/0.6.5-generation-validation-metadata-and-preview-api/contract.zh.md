# 合同

状态：review complete

implementation_authorized: yes

## 公共概念

- `GenerationPreviewSourceKind`：用于 preview `template`、`plan` 或
  `imported_plan` source 的 public discriminator。
- `GenerationPreviewRequest`：API-facing request，携带一个 source payload、request
  id、可选 seed material 和 request constraints。
- `GenerationPreviewMetadata`：bounded response metadata，来源于现有
  `GenerationMetadata`，并附加 public preview counters 和可选 redacted import
  provenance。
- `GenerationPreviewResponse`：deterministic response，包含 source kind、
  validation status、diagnostics、bounded metadata，以及仅在 generation validation
  passed 时包含 public `WorldSpec` preview。
- Preview diagnostics：复用 template validation、plan validation 和 import validation
  的现有 `GenerationDiagnostic` records。

## API 合同

Implementation 可新增：

```text
POST /world/generation/preview
```

该 route 必须返回：

- success envelope：`ApiResponse[GenerationPreviewResponse]`。
- request validation errors：使用 application validation handler 的现有
  `ApiErrorResponse`，包括 code `30`。
- generation validation failures：HTTP 200 success envelope，且
  `data.validation_status == "failed"`、包含 diagnostics、不包含
  `worldspec_preview`，并提供 bounded metadata。

该 route 不得改变任何 existing path、router、handler、response model 或 envelope。

## 请求语义

`GenerationPreviewRequest` 必须：

- 要求 `request_id` 和 `source_kind`。
- 只允许一个匹配的 source payload：
  - `source_kind: "template"` 时使用 `template_request: TemplateGenerationRequest`。
  - `source_kind: "plan"` 时使用 `plan_request: PlanGenerationRequest`。
  - `source_kind: "imported_plan"` 时使用 `import_request: PlanImportRequest`。
- 将 missing、mismatched 或 multiple source payloads 作为 request-shape validation
  errors 拒绝。
- 拒绝 unexpected fields，而不是忽略它们。

## 响应语义

`GenerationPreviewResponse` 必须：

- 包含 `request_id`、`source_kind`、`validation_status`、`metadata`、`diagnostics`
  和可选 `worldspec_preview`。
- 仅在 validation passes 时包含 `worldspec_preview`。
- 只使用 public `WorldSpec` schema 作为 generated-world preview payload。
- 仅在 successful imported-plan preview 时包含 redacted import provenance。
- 不包含 raw prompts、provider traces、hidden retry state、credentials、private
  oracle details 或 source payload echoes。

## 允许变更

Documentation stage：

- 创建并更新 `docs/iterations/v0.6/` 下的本 package。
- 只为 current child state 和 evidence 更新 parent v0.6 status surfaces。
- 记录 subagent/evaluator evidence。

Implementation stage，仅在 `implementation_authorized: yes` 后：

- 更新 `backend/app/schemas/world_generation.py`。
- 更新 `backend/app/core/world_generation.py`。
- 新增 `backend/app/api/routes/world_generation.py`。
- 更新 `backend/app/api/routes/__init__.py`。
- 更新 `backend/app/api/app_factory.py`。
- 添加 focused tests：
  - `backend/app/tests/test_generation_preview_api.py`
- 只在 compatibility 需要时更新现有 focused generation/API tests：
  - `backend/app/tests/test_world_generation_schema.py`
  - `backend/app/tests/test_deterministic_world_generation.py`
  - `backend/app/tests/test_generation_plan_schema.py`
  - `backend/app/tests/test_structured_generation_plan_compiler.py`
  - `backend/app/tests/test_plan_import_schema.py`
  - `backend/app/tests/test_plan_import_boundary.py`
  - `backend/app/tests/test_agent_loop_api.py`
  - `backend/app/tests/test_event_api_compat.py`
- 更新本 package `review.md` / `review.zh.md`。
- 只为 current child state 和 evidence 更新 parent v0.6 status surfaces。

如果 implementation 需要 frontend files、persistence files、migrations、fixtures、
generated result artifacts、new provider modules 或不同 API route shape，必须停止并先回到
documentation review。

## 禁止变更

- 不修改 `frontend/**`、persistence/repository modules、migrations、fixtures、
  generated output files、external repositories 或 `backend/worldengine/**`。
- 不修改 runtime tick/event semantics、Agent/memory semantics、archive/params
  behavior、loader/runtime-context behavior 或 existing route response envelopes。
- 不添加 live AI provider credentials、network calls、SDKs、prompt execution、prompt
  storage、hidden retries、background jobs 或 model orchestration。
- 不暴露 raw private prompts、unredacted provider traces、secrets、external
  application data、private validation oracle details、generated seed data、concrete
  maps、characters、locations、resources、story rules 或 application-specific backend
  logic。
- 不声明 runtime readiness、regeneration readiness、dashboard behavior、E2E behavior、
  autonomous validation、external validation readiness、projection readiness、product
  readiness、release readiness 或 generation quality。

## 兼容要求

- Existing API success 和 error envelope behavior 保持兼容。
- Existing routes 保持兼容，并保持其 response shapes。
- Existing template generation、structured-plan compiler 和 import boundary behavior
  保持兼容。
- Existing `WorldSpec`、loader、runtime-context、runtime、Agent/memory、archive、
  params 和 frontend behavior 保持不变。
- Schema additions 是 additive，且 request models 在 API safety 需要时拒绝
  unexpected fields。

## 授权标准

本 package 只有在满足以下条件后才可记录 `implementation_authorized: yes`：

- 所有 package docs 和中文镜像存在。
- Documentation/contract evaluator 报告 PASS，且无 P0/P1、无 blocking unresolved P2。
- contract/design/test-plan/plan 明确保留 API envelopes，并禁止 frontend UI、
  persistence、migrations、live AI、raw prompts、provider traces、concrete content 和
  `backend/worldengine/**`。
- planned tests 覆盖 successful template preview、successful plan preview、
  imported-plan preview、generation validation failure、import validation failure、
  request shape validation、preview payload shape、existing envelope compatibility、
  route wiring、full backend regression 和 scope guard。

## 北极星检查

本 package 暴露 generic world generation preview，同时不让 WorldEngine 变成
provider-specific 或 application-specific。它为后续 runtime-readiness work 提供可检查的
generated worlds。

## 范围外后续

- `0.6.6`：regeneration and runtime-readiness integration。
- `0.6.7`：dashboard preview and E2E smoke。
- v0.7 external validation readiness。
- v0.8 projection application readiness。
