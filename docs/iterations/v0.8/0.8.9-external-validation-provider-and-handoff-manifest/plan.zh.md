# Plan

英文镜像：`plan.md`。

## Objective

创建 documentation-only package，为外部 Validation-Client 的 Agent 自主验证准备
WorldEngine 侧 provider 边界和 handoff manifest 计划。

## Tasks

### 1. Package Documents

创建：

```text
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/README.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/intent.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/contract.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/technical-design.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/test-plan.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/plan.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/validation-client-contract-handoff.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/implementation-task-plan.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/contract-readiness-checklist.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/external-validation-gate-matrix.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/planning-readiness-checklist.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/implementation-handoff-prompt.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/review.md
```

为每个文件创建中文镜像。

### 2. Provider Boundary Plan

定义：

- WorldEngine 拥有 provider configuration。
- validation clients 不管理 keys。
- Kimi Code subscription 是 coding-agent 候选，不自动成为 runtime provider。
- Kimi Platform / Moonshot API 和 DeepSeek API 是 runtime provider 候选，需要
  budget 与 rate-limit controls。

### 3. Handoff Manifest Plan

定义未来 manifest 字段：

- provider class。
- provider readiness。
- credential source class。
- public surface ids。
- evidence references。
- redaction flags。
- blockers and warnings。

### 3.5 Validation Client Contract Handoff

记录外部 Validation Client 需要的精确 public surfaces：

- `GET /manifest`。
- OpenAPI 可发现的 world creation endpoint，优先 `POST /worlds`。
- public world creation response fields。
- 完整自主验证需要的 public director guidance endpoint。
- 验证命令必须证明 Validation Client `/health/worldengine` 报告 world creation
  available，且 `POST /sessions/worldengine` 成功。

### 3.6 Implementation Handoff Prompt

创建 future-chat prompt，要求：

- 列出 required reading。
- 定义精确的 WorldEngine implementation goal。
- 重复 no-Validation-Client-code boundary。
- 重复 no-secret/no-private-prompt/no-provider-raw-trace boundary。
- 写明 verification commands 和 completion wording。

### 3.7 Detailed Implementation Task Plan

创建 task-by-task 实施计划，要求：

- 明确未来实现前置读取文档。
- 拆分 public schemas、`GET /manifest`、`POST /worlds`、director guidance、
  provider readiness redaction、Validation Client compatibility probe 和 closeout。
- 每个 task 写明候选文件、测试重点、验证命令和 stop rules。
- 明确当前 package 仍不授权 implementation。

### 3.8 Contract Readiness Checklist

创建 future implementation 完成后的检查模板，要求：

- 固定结论枚举为 `WORLDENGINE_CONTRACT_READY`、`PARTIAL`、`BLOCKED` 或
  `FAIL`。
- 检查 `/health`、`/manifest`、`/openapi.json`、`POST /worlds` 和 director
  guidance。
- 检查 provider readiness redaction。
- 检查 Validation Client `/health/worldengine` 和 `POST /sessions/worldengine`
  compatibility probe。
- 明确即使 contract ready，也不得声明 external validation PASS 或 human validation
  PASS。

### 3.9 External Validation Gate Matrix

创建 WorldEngine 视角的外部验证门禁矩阵，要求：

- 说明 WorldEngine 只负责 Gate 1：public contract readiness。
- 说明 Validation Client、Codex、第二 Agent 和人类分别负责后续门禁。
- 明确 `WORLDENGINE_CONTRACT_READY` 只表示可以交给 Validation Client 进入 Codex
  autonomous validation。
- 明确 WorldEngine 不实现 Validation Client operation log、E2E、浏览器自主验证、
  第二 Agent 复核或人工体验判断。
- 明确当前 Gate 1 blocker 是缺少 `/manifest` 和 Validation Client 可发现的 world
  creation endpoint。

### 3.10 Planning Readiness Checklist

创建 planning readiness checklist，要求：

- 结论为 `PLAN_READY_FOR_REVIEW`。
- 明确当前 package 仍不授权 implementation。
- 明确后续唯一允许的下一步是 user review 后进入 Gate 1 implementation。
- 明确当前 blocker 仍是 `/manifest` 和可发现 world creation endpoint 缺失。
- 明确本 checklist 不证明 `WORLDENGINE_CONTRACT_READY`。

### 4. Review

运行：

```bash
git diff --check
```

记录 docs-only scope review，并说明 implementation tests 未运行。

## Out Of Scope

- runtime provider implementation。
- API endpoints。
- schemas。
- checkers。
- validation client code。
- external validation scenarios。
- human validation execution。
