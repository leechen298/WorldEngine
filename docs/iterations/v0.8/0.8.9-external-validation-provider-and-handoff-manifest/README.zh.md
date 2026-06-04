# 0.8.9 外部验证 Provider 与 Handoff Manifest

状态：planned / ready for review
类型：documentation-only planning package
implementation_authorized: no
evidence_execution_authorized: no

英文镜像：`README.md`。

## Package

名称：`0.8.9-external-validation-provider-and-handoff-manifest`

这是 v0.8 closeout 之后的补充规划包，用来定义 WorldEngine 侧支持外部验证客
户端进行 Agent 自主验证和人工验证交接所需的前置条件。

它不重新打开 v0.8 final closeout，只记录一个后续实现聊天可审查使用的新计划
包。

## 目标

定义 WorldEngine 如何公开、脱敏、可被验证客户端消费的 provider readiness 和
handoff manifest 信息，同时不把外部 validator 逻辑、私有场景、产品 UI、具体世
界内容、LLM secret 或应用特定行为放进核心仓库。

## 文档

- [x] `README.md`
- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `validation-client-contract-handoff.md`
- [x] `implementation-task-plan.md`
- [x] `contract-readiness-checklist.md`
- [x] `external-validation-gate-matrix.md`
- [x] `planning-readiness-checklist.md`
- [x] `handoff-status.md`
- [x] `implementation-handoff-prompt.md`
- [x] `review.md`
- [x] 中文镜像

## 范围摘要

本包可以定义：

- LLM provider 验证边界。
- provider class label 和脱敏 provider readiness status。
- 外部验证客户端可消费的 public handoff manifest 字段。
- Validation Client 创建世界和导演引导所需的 contract handoff 要求。
- blocked、skipped、unavailable、partial、ready 等证据分类。
- provider 缺失、public manifest 缺失或 public surface 不足时的 stop rules。

本包不得实现：

- provider runtime code。
- API routes。
- schema files。
- checker code。
- tests。
- migrations。
- 外部验证应用行为。

## Provider 边界

WorldEngine 拥有 provider 配置和凭据处理。外部验证客户端可以观察 public
provider readiness label 和 public failure summary，但不得管理 provider API key
或直接调用 provider API。

后续实现可评估的 provider 选项：

- Kimi Code subscription / `kimi-for-coding`：适合 coding-agent 或开发工具场景，
  具有 OpenAI-compatible 和 Anthropic-compatible endpoint、会员 quota 和
  `kimi-for-coding` model id。
- Kimi Platform / Moonshot API：更适合产品式程序化 runtime 集成和按量 API 评估。
- DeepSeek API：按量付费备选项，必须通过 max tokens、rate limits 和 budget
  controls 控制使用。

后续实现必须通过 WorldEngine contract 决定 provider 用法，而不是让验证客户端
决定。

## Validation Client Contract Handoff

详细 contract handoff 计划：

```text
validation-client-contract-handoff.md
validation-client-contract-handoff.zh.md
implementation-task-plan.md
implementation-task-plan.zh.md
contract-readiness-checklist.md
contract-readiness-checklist.zh.md
external-validation-gate-matrix.md
external-validation-gate-matrix.zh.md
planning-readiness-checklist.md
planning-readiness-checklist.zh.md
handoff-status.md
handoff-status.zh.md
implementation-handoff-prompt.md
implementation-handoff-prompt.zh.md
```

外部验证门禁矩阵：

```text
external-validation-gate-matrix.md
external-validation-gate-matrix.zh.md
```

该矩阵说明 WorldEngine 只负责 `WORLDENGINE_CONTRACT_READY` 门禁，不负责
Validation Client operation log、Codex browser autonomous validation、第二 Agent
复核或人工体验判断。

Planning readiness checklist：

```text
planning-readiness-checklist.md
planning-readiness-checklist.zh.md
```

该 checklist 只证明 0.8.9 planning package 可进入 user review 和后续 implementation
chat，不证明 `WORLDENGINE_CONTRACT_READY`。

Handoff status：

```text
handoff-status.md
handoff-status.zh.md
```

该 status 用单页记录当前等待 implementation、当前 blocker 和
`WORLDENGINE_CONTRACT_READY` 完成条件。

当前实测 blocker：

- Validation Client 能访问 WorldEngine `/health` 和 `/openapi.json`。
- Validation Client 不能创建 WorldEngine-backed session，因为 OpenAPI 没有暴露
  Validation Client 可发现的 world creation endpoint。
- `/manifest` 也缺失。

未来实现必须先修复这些缺口，外部浏览器自主验证才能声明可以进入人工验证。

## Handoff

本包 review 后，后续实现可以再创建具体 child package 去新增 contract files、
schemas、checkers、API docs 或 public endpoint changes。在该 package review 前，
本包仅是文档计划，不授权 runtime changes。
