# 0.6.6 再生成与运行就绪集成

状态：review complete
类型：mixed
implementation_authorized: yes

## 目标

定义并仅在评审授权后实现 generated `WorldSpec` data 的 bounded regeneration support 和
runtime-readiness checks。本 package 必须证明 generated specs 可通过现有 loader 和
runtime-context bridge，同时不改变 runtime tick/time behavior、不默认 mutate live runtime、
不添加 persistence，也不把该边界夸大为 product/runtime readiness。

## 范围

Documentation stage：

- 创建本 package 及中文镜像。
- 定义 regeneration、lineage 和 runtime-readiness public concepts。
- 定义评审授权后可触碰的精确 backend files。
- 为 active child state 更新 parent v0.6 status surfaces。

Implementation stage，仅在授权后：

- 在 `backend/app/schemas/world_generation.py` 中以 additive 方式扩展 regeneration、
  lineage 和 runtime-readiness schemas。
- 在 `backend/app/core/world_generation.py` 中加入 deterministic regeneration 和
  runtime-readiness helpers，并复用现有 preview、loader 和 runtime-context bridge。
- 扩展 `backend/app/api/routes/world_generation.py` 中已批准的 generation routes，且不改变
  existing route envelopes。
- 添加 focused backend tests，覆盖 regeneration、lineage、runtime-readiness
  success/failure、request validation 和 runtime event non-leakage。
- 更新本 package review evidence 和 parent status surfaces。

禁止：

- 不改变 runtime tick/time/event semantics。
- 不让 generated specs 自动 mutate live runtime。
- 不添加 persistence、repositories、migrations、fixtures、generated output files、
  external repositories 或 `backend/worldengine/**`。
- 不添加 frontend UI、dashboard workflow、E2E、external validation runner 或 projection
  app behavior。
- 不添加 live AI calls、provider SDKs、network calls、credentials、prompt execution、raw
  prompts、provider traces、private validation oracle details、secrets、external
  application data 或 concrete world/story content。

## 交付物

- 完整 package docs 和中文镜像。
- 已评审的 regeneration 和 runtime-readiness contract。
- 授权后提供 focused backend API/service tests，以及 adjacent loader、runtime-context、
  runtime-step 和 full backend regression evidence。
- Review evidence 必须区分 loader/context readiness 与 runtime mutation、regeneration
  quality、external validation readiness、projection readiness、product readiness 和
  release readiness。

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

Approved 0.6.6 backend schema/core/existing-route/test scope 内的 implementation
和 validation 已完成。Focused 与 full backend regression evidence 通过，evaluator
checkpoints 均报告无 P1/P2/P3 findings。
