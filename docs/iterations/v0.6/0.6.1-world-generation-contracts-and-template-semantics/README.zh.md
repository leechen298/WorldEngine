# 0.6.1 世界生成契约与模板语义

Status: review complete
Type: documentation-only
implementation_authorized: no

## 目标

定义 World Generation v1 的公开概念、模板语义、结构化计划语义、生成元数据、
预览与再生成边界、兼容性要求，以及后续 v0.6 package 必须遵守的实现授权条件。

本 package 不实现世界生成行为。它先说明生成数据应当具备的含义，让第一个包含实
现的 package 可以被评审；在评审完成前，不允许修改 schema、service、API、
frontend、fixture、migration 或测试实现。

## 范围

允许：

- 在
  `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/`
  下创建本 package。
- 定义以下公开文档概念：
  - `WorldGenerationRequest`
  - `WorldTemplate`
  - `GenerationPlan`
  - `GeneratedWorldSpec`
  - `GenerationMetadata`
  - `GenerationPreview`
  - `RegenerationRequest`
  - generation diagnostics
- 为未来 additive backend schema 定义字段级语义。
- 定义可以产生合法 generic `WorldSpec` 数据的模板约束。
- 将 AI-assisted generation 定义为 provider-independent 的结构化计划导入，而不是
  隐藏的 live model 行为。
- 定义
  `0.6.2-template-catalog-and-deterministic-generator-core`
  的实现授权条件。

禁止：

- 不实现 schema、store、service、API、frontend、fixture、migration、生成结果文
  件、backend test 或外部仓库变更。
- 不修改 `backend/app/**`、`frontend/**`、`backend/worldengine/**`、migration、
  fixture、generated output 或 external validation artifact。
- 不加入具体世界名称、地图、角色、地点、资源、故事规则、seed data、私有验证
  oracle 细节或 application-specific backend 行为。
- 不要求 live external AI-provider 调用。
- 不声明 generated-world quality、runtime behavior、API behavior、E2E、Agent
  smoke、autonomous validation、projection readiness、external validation
  readiness、release readiness 或 product readiness 已通过。

## 交付物

- 完整 package 文档及中文镜像。
- generation request、template、plan、generated spec、metadata、preview、
  regeneration 和 diagnostics 的契约语义。
- 当前 `WorldSpec`、loader、runtime-context bridge、runtime、loop、memory、
  event、params、archive、API envelope 和 frontend-facing behavior 的兼容性约束。
- `0.6.2` 的明确实现授权条件。
- 文档阶段 review evidence 和 evaluator findings。

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

本 documentation-only package 已 review complete。文档检查已通过，read-only
documentation evaluator 报告 PASS 且无 P1/P2/P3 findings，implementation 仍未授权。本
package 将已评审 contract semantics 交接给
`0.6.2-template-catalog-and-deterministic-generator-core`。
