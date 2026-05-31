# 0.6.4 AI 辅助生成边界与计划导入

Status: review complete
Type: mixed
implementation_authorized: yes

## 目标

定义并且仅在 review authorization 之后实现 provider-independent AI-assisted plan import
boundary。本 package 导入可能由 AI system 产生的 structured plans，记录 redacted
provenance，通过 `0.6.3` compiler contract 验证 imported plan，并且永不调用 live providers。

## 范围

文档阶段：

- 创建本 package 和中文镜像。
- 定义 import envelope、provenance、diagnostics、tests 和 forbidden provider behavior。
- 定义 authorization 后可以触碰的准确 backend files。

实现阶段，仅在授权后：

- 扩展 `backend/app/schemas/world_generation.py`，添加 additive import 和 provenance
  schemas。
- 扩展 `backend/app/core/world_generation.py`，添加 import validation 和 conversion
  helpers。
- 添加 focused backend tests，覆盖 plan import schema 和 boundary behavior。
- 只在 compatibility 需要时更新 existing generation-plan tests。

禁止：

- 不添加 live provider credentials、network calls、model orchestration、background
  jobs、hidden retry loops、prompt libraries 或 prompt execution。
- 不添加 public API routes、frontend、persistence、migrations、fixtures、external
  repositories、`backend/worldengine/`、runtime tick/event、Agent/memory 或
  projection/external-validation readiness。
- 不添加 concrete world/story/application content、private validation oracle details、
  secrets、prompts 或 external application data。

## 交付物

- 完整 package docs 和中文镜像。
- Provider-independent import/provenance contract。
- 授权后的 focused import tests 和 structured compiler compatibility evidence。
- 区分 structured plan import 与 live AI generation 的 review evidence。

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

Review complete。Implementation 和 validation evidence 已记录在 `review.md`，
本 package 将 import/provenance semantics 交接给 `0.6.5`。
