# v0.6 世界生成 v1

状态：in progress / 0.6.0 review complete
类型：Codex `/goal` development campaign 和 iteration package root

## 目标

v0.6 定义并逐步实现 World Generation v1：从 templates 和 structured
AI-assisted generation plans 生成可运行的 `WorldSpec` 数据，并提供 validation、
metadata、preview 和 regeneration support。

本版本从 v0.5 final closeout handoff 以及 v0.3 `WorldSpec` loader/runtime-context
bridge 出发。生成内容必须保持 generic、inspectable 和 contract-driven。它不得把
concrete demo worlds、external validation worlds、application-specific backend
behavior 或 private validation oracle details 放进 WorldEngine core repository。

## 目标入口

自然语言目标：

```text
完成 v0.6
```

解释：

- 从 `CURRENT_STATE.md` 开始。
- 按 `GOAL_RUNNER.md` 执行 route selection、documentation gates、
  implementation authorization、evaluator checkpoints、verification 和 stop
  conditions。
- 按 `CAMPAIGN_PLAN.md` 与 `v0.6-plan.md` 确认 child sequence、deliverables、
  compatibility constraints 和 handoff rules。
- 在处理 child work 前，先读取 active child package documents。

这不是 automation-controller implementation。Scheduling、orchestration、retry
infrastructure 和 Codex role assignment 都在 WorldEngine 范围之外。

## 范围

v0.6 允许的范围：

- generation request、template、structured generation plan、generation result、
  generation metadata、preview 和 regeneration public concepts。
- 可以产生 valid `WorldSpec` 数据的 generic template semantics，但不得在 core
  repository 中存储 concrete demo-world content。
- 面向已评审 template 和 structured-plan inputs 的 deterministic generator core。
- provider-independent AI-assisted generation boundary，其中 AI output 是待验证的
  structured plan，而不是未评审的 hidden side effect。
- 通过现有 `WorldSpec` 与 loader/runtime-context bridge surfaces 做 validation。
- 在已评审 package 授权后实现 generation preview 和 regeneration support。
- 只有当已评审 child package 明确授权时，才加入 focused backend、API、frontend、
  E2E 和 compatibility tests。

v0.6 禁止的范围：

- 不添加 external validation runner readiness 或 report automation；v0.7 负责该范围。
- 不添加 first external projection application readiness；v0.8 负责该范围。
- 不添加 concrete world names、maps、characters、locations、resources、story rules、
  seed data、UI-specific app behavior 或 private validation oracle details。
- 不添加 durable persistence 或 migrations，除非已评审 v0.6 child 明确授权。
- 不让 generated worlds 依赖 live external LLM calls，除非已评审 child package 明确授权
  provider configuration、failure handling、security boundaries 和 tests。
- 不在 `backend/worldengine/` 下新增 runtime features。
- 不从 v0.6 evidence 声明 full autonomous validation、external validation readiness
  或 projection readiness。

## 交付物

- Parent goal-campaign documents：`README.md`、`v0.6-plan.md`、`GOAL_RUNNER.md`、
  `CURRENT_STATE.md`、`CAMPAIGN_PLAN.md` 和 `review.md`，以及中文镜像。
- First child package：
  `0.6.0-v0.6-planning-and-generation-boundary-baseline`，包含 README、intent、
  contract、technical design、test plan、plan、review 和中文镜像。
- 贯穿 final closeout 的 planned child package sequence。
- `/goal` 执行所需的 explicit evaluator checkpoint rules。
- Documentation-stage review evidence，证明 first package 没有修改 runtime、schema、
  API、frontend、test implementation、fixture、migration、external repository、
  generated result 或 `backend/worldengine/` files。

## 子包索引

### `0.6.0-v0.6-planning-and-generation-boundary-baseline`

- 类型：documentation-only
- 状态：review complete
- 目的：创建 v0.6 documentation root、goal-campaign controls、version plan、
  generation boundary、compatibility baseline 和 v0.5 handoff mapping，且不修改
  implementation files。

### `0.6.1-world-generation-contracts-and-template-semantics`

- 类型：documentation-only
- 状态：planned
- 目的：在写代码前定义 generation public concepts、request/result semantics、
  template semantics、structured-plan semantics、metadata、preview、regeneration、
  compatibility rules 和 authorization criteria。

### `0.6.2-template-catalog-and-deterministic-generator-core`

- 类型：mixed or code
- 状态：planned
- 目的：只实现 generic template contracts、deterministic template-to-`WorldSpec`
  generator core 和 focused backend tests。

### `0.6.3-structured-generation-plan-compiler`

- 类型：mixed or code
- 状态：planned
- 目的：把已验证的 structured generation plans 编译为 valid `WorldSpec` data，同时不引入
  concrete world content 或 hidden AI side effects。

### `0.6.4-ai-assisted-generation-boundary-and-plan-import`

- 类型：mixed or code
- 状态：planned
- 目的：添加 provider-independent AI-assisted plan import boundaries、validation、
  error reporting 和 mock-provider tests，且不要求 live external LLM calls。

### `0.6.5-generation-validation-metadata-and-preview-api`

- 类型：mixed or code
- 状态：planned
- 目的：暴露已评审的 backend schemas/services/API，用于 generation validation、
  metadata 和 preview，同时保持现有 API envelopes。

### `0.6.6-regeneration-and-runtime-readiness-integration`

- 类型：mixed or code
- 状态：planned
- 目的：添加 bounded regeneration support，并证明 generated specs 能通过
  loader/runtime-context readiness，同时不改变无关 runtime tick behavior。

### `0.6.7-dashboard-generation-preview-and-e2e-smoke`

- 类型：mixed or code
- 状态：planned
- 目的：在 backend/API generation contracts 稳定后，加入 dashboard-facing generation
  preview workflow 和 browser E2E smoke。

### `0.6.8-v0.6-evidence-and-compatibility-audit`

- 类型：documentation-only
- 状态：planned
- 目的：审计 v0.6 implementation evidence、compatibility surfaces、unresolved
  findings 和 release-candidate readiness。

### `0.6.9-v0.6-release-candidate-bundle`

- 类型：documentation-only
- 状态：planned
- 目的：基于已评审 implementation 和 audit evidence 准备 release-candidate bundle，
  但不声明 final release。

### `0.6.10-v0.6-final-closeout`

- 类型：documentation-only
- 状态：planned
- 目的：只有在 release-candidate approval、evidence consistency checks 和 unresolved
  finding classification 完成后，才把 v0.6 标记为 final / closeout complete。

## 当前状态

Active child package：
`0.6.1-world-generation-contracts-and-template-semantics`。

Current route：`next-child-documentation-needed`。

Implementation authorization：no。

## 交接基线

- v0.5 状态：`final / closeout complete`。
- v0.5 final backend evidence 只作为 handoff evidence，不是当前 v0.6 pass evidence。
- v0.5 final closeout 不声明 frontend、E2E、Agent smoke、autonomous、external
  validation、projection readiness 或 product readiness checks 已通过。
- v0.6 从自己的 package review gates 开始，不能继承 v0.5 的 implementation
  authorization。

## 最终评估状态

当前值：`in progress / 0.6.0 review complete`。

`0.6.0-v0.6-planning-and-generation-boundary-baseline` 已记录 review complete
documentation evidence。v0.6 implementation 仍未授权，直到某个 implementation-bearing
child package 记录 `implementation_authorized: yes`。
