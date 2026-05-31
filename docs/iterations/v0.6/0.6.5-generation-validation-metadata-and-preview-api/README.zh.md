# 0.6.5 生成校验元数据与预览 API

状态：review complete
类型：mixed
implementation_authorized: yes

## 目标

定义并仅在评审授权后实现 generation validation、bounded metadata 和 preview 的
backend API surface。该 API 必须通过现有 `ApiResponse` / `ApiErrorResponse`
envelope 暴露已评审的 `0.6.2`、`0.6.3` 和 `0.6.4` generation behavior，且不改变
runtime、persistence、frontend UI 或 live AI-provider behavior。

## 范围

Documentation stage：

- 创建本 package 及中文镜像。
- 定义 preview API contract、metadata boundary、route wiring、tests 和 forbidden
  leak surfaces。
- 定义评审授权后可触碰的精确 backend files。
- 为 active child state 更新 parent v0.6 status surfaces。

Implementation stage，仅在授权后：

- 在 `backend/app/schemas/world_generation.py` 中以 additive 方式扩展 preview API
  request/response schemas。
- 在 `backend/app/core/world_generation.py` 中加入 preview helper，并复用现有
  template、plan 和 import validation/generation functions。
- 新增 `backend/app/api/routes/world_generation.py`。
- 仅为 export/include route 更新 `backend/app/api/routes/__init__.py` 和
  `backend/app/api/app_factory.py`。
- 添加 focused API tests，覆盖 successful preview、generation validation failure、
  import validation failure、request-envelope validation、preview payload shape 和
  existing envelope compatibility。
- 更新本 package review evidence 和 parent status surfaces。

禁止：

- 不添加 frontend UI 或 dashboard workflow。
- 不添加 persistence、repositories、migrations、fixtures、generated output files
  或 external repositories。
- 不添加 live AI calls、provider SDKs、network calls、credentials、prompt execution、
  hidden retries 或 background jobs。
- 不暴露 raw prompts、unredacted provider traces、private validation oracle
  details、secrets、external application data、concrete maps、characters、
  locations、resources、story rules 或 seed content。
- 不改变 existing route response envelopes、existing error handler behavior、
  runtime tick/event behavior、Agent/memory behavior、loader/runtime behavior 或
  `backend/worldengine/**`。

## 交付物

- 完整 package docs 和中文镜像。
- 已评审的 preview API contract 和 bounded metadata semantics。
- 授权后提供 focused backend API/service tests 与 full backend regression evidence。
- Review evidence 必须区分 structural preview validity 与 runtime readiness、
  generation quality、external validation readiness、projection readiness 和 product
  readiness。

## 文档

- [x] `README.md`
- [x] `README.zh.md`
- [x] `intent.md`
- [x] `intent.zh.md`
- [x] `contract.md`
- [x] `contract.zh.md`
- [x] `technical-design.md`
- [x] `technical-design.zh.md`
- [x] `test-plan.md`
- [x] `test-plan.zh.md`
- [x] `plan.md`
- [x] `plan.zh.md`
- [x] `review.md`
- [x] `review.zh.md`

## 当前评估

Documentation/contract evaluator review 已通过，且无 P1/P2/P3 findings。
Implementation 和 validation evidence 已记录在 `review.md`，本 package 将
preview/API metadata semantics 交接给 `0.6.6`。
