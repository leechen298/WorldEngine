# v0.7 External Validation Readiness / Projection Consumer Readiness 文档

状态：final / closeout complete；已记录 post-closeout code-review blockers
类型：Codex `/goal` development campaign 与迭代包根目录

## 目标

v0.7 通过稳定的 public contracts、redacted validation reports、面向
projection consumer 的契约，以及 compatibility evidence，让 WorldEngine 准备好被
external validation suites 和 projection consumers 消费。

本版本从 v0.6 final closeout 与 0.6.11 reliability/scope repair 的交接开始。外部验证世界和
projection application 必须继续作为 WorldEngine 的 consumers；本仓库不能接收具体 external
validation world、private oracle behavior、product-specific UI 或 application-specific
backend logic。

## Goal 入口

自然语言 goal：

```text
完成 v0.7
启动 WorldEngine v0.7：External Validation Readiness / Projection Consumer Readiness
编写 v0.7 文档
```

执行解释：

- 先读 `CURRENT_STATE.md`。
- 按 `GOAL_RUNNER.md` 执行 route selection、documentation gate、implementation
  authorization、evaluator checkpoints、verification 和 stop conditions。
- 按 `CAMPAIGN_PLAN.md` 与 `v0.7-plan.md` 确认 child sequence、deliverables、
  compatibility constraints 和 handoff rules。
- 将 v0.7 parent package 作为当前唯一权威入口。
- 任何 future child package 开始前，都必须在当时创建或确认该 child 的完整 package document set，
  并完成 review gate。不得把 planned `0.7.x` roadmap entries 当作 execution-approved child contracts。

这不是 external automation controller、external validation suite 或 projection
application 的实现。Scheduling、orchestration、retry infrastructure、private fixtures 和
Codex role assignment 都不属于 WorldEngine。

## Post-Closeout Code Review Boundary

`0.7.8` final closeout 仍是 v0.7 的历史 package closeout 记录，但它不是 v0.7 clean pass、
product PASS、external suite PASS 或 projection readiness PASS。

`docs/testing/results/2026-06-02-v0.7-code-review.md` 在 final closeout 之后记录了
blocking findings：3 个 P1、2 个 P2、1 个 P3。后续若要声明 v0.7 clean pass、
external suite PASS、projection readiness PASS 或 product readiness PASS，必须先通过新的
reviewed package 修复这些 findings，或在 validation report 中把它们明确记录为 blockers。

## 范围

v0.7 允许：

- 定义 external validation readiness 的 public concepts、report semantics 和 redacted
  evidence rules。
- 定义 projection consumer 的 public concepts 与 read-only consumption boundaries。
- 定义可被 external suites 消费的 contract bundles、readiness manifests、
  compatibility matrices 和 evidence retention rules。
- 在 reviewed child package 授权后，加入通用 report schema、redaction check、saved-result
  check 和文档 / audit tooling。
- 只针对当前 session 实际运行的命令和 checker 记录 public engine contracts 的 quality
  regression evidence。
- 只有在 reviewed child package 明确授权时，才运行或修改 focused backend、API、frontend、
  E2E、Agent smoke、autonomous 和 compatibility checks。

v0.7 禁止：

- 不实现第一个 external projection application；v0.8 负责该范围。
- 不把 external validation repositories、concrete validation worlds、seed data、maps、
  characters、locations、resources、story rules、private transcripts、UI selectors 或 oracle
  internals 放入本仓库。
- 不添加 application-specific backend logic、hidden reset APIs 或 product packaging
  behavior。
- 没有当前 session 证据时，不声明 external suite PASS、projection application readiness、
  generation-quality PASS、full product readiness、live provider behavior、新 live Agent smoke
  或 full autonomous runner/full-suite PASS。
- 除非 reviewed v0.7 child 明确授权，不添加 durable persistence 或 migrations。
- 不在 `backend/worldengine/` 下新增 runtime features。

## 交付物

- Parent goal-campaign documents：`README.md`、`v0.7-plan.md`、`GOAL_RUNNER.md`、
  `CURRENT_STATE.md`、`CAMPAIGN_PLAN.md`、`review.md`，以及中文镜像。
- Reviewed `0.7.0` documentation-only child package documents，以及中文镜像，用于 planning and
  external-validation boundary baseline。
- Reviewed `0.7.5` quality regression and compatibility evidence package，以及中文镜像。
- Reviewed `0.7.6` evidence and compatibility audit package，以及中文镜像。
- Reviewed `0.7.7` release-candidate bundle package，以及中文镜像。
- Reviewed `0.7.8` final closeout package，以及中文镜像。
- `/goal` 执行所需的 subagent/evaluator checkpoint rules。
- documentation-stage review evidence，证明本次 drafting 没有修改 runtime、schema、API、
  frontend、test implementation、fixture、migration、external repository、generated result 或
  `backend/worldengine/` implementation files。

## Planned Package Roadmap 计划路线图

下面的 `0.7.x` entries 以及 `v0.7-plan.md` 中的对应 sections 都只是 roadmap-level planned
package specs。它们不是当前 implementation authorization，不是 execution-approved contracts，也不是不可变
execution script。未来 agent 必须在 child 启动时创建或确认 active child package documents，然后完成
review 后才可 implementation。如果 implementation 发现 design gap，必须停止 implementation，更新 active
child 的 `contract.md`、`technical-design.md`、`test-plan.md`、`plan.md` 和 `review.md`，并且只有 updated
package reviewed 后才能继续。

### `0.7.0-v0.7-planning-and-external-validation-boundary-baseline`

- 类型：documentation-only
- 状态：review complete
- 目的：创建 v0.7 documentation root、goal-campaign controls、version plan、
  external-validation/projection boundary、compatibility baseline 和 v0.6 handoff mapping，不修改
  implementation files。

### `0.7.1-public-validation-and-projection-contracts`

- 类型：documentation-only
- 状态：review complete
- 目的：在任何 code 或 checker work 前，定义 public external-validation readiness concepts、
  redacted report semantics、projection consumer boundaries 与 authorization criteria。

### `0.7.2-validation-report-schema-and-redaction-checker`

- 类型：mixed or code
- 状态：review complete
- 目的：在 `0.7.1` contracts reviewed 后，为 redacted validation evidence 实现通用 report
  schema/checker support。

### `0.7.3-contract-bundle-and-readiness-manifest`

- 类型：mixed or code
- 状态：review complete
- 目的：暴露 external suites 可消费的 generic contract bundle 和 readiness manifest，不依赖
  private repository knowledge。

### `0.7.4-projection-consumer-read-model-contracts`

- 类型：mixed or code
- 状态：review complete
- 目的：定义并在授权后暴露 runtime、events、Agent loop、memory context summaries 和 generation
  readiness 的 read-only projection consumer payload，不构建 product application。

### `0.7.5-quality-regression-and-compatibility-evidence`

- 类型：mixed or code
- 状态：review complete
- 目的：为 v0.7 public engine contracts 运行并记录 generic regression 与 compatibility evidence。

### `0.7.6-v0.7-evidence-and-compatibility-audit`

- 类型：documentation-only
- 状态：review complete
- 目的：审计 v0.7 implementation evidence、compatibility surfaces、unresolved findings 和
  release-candidate readiness。

### `0.7.7-v0.7-release-candidate-bundle`

- 类型：documentation-only
- 状态：review complete
- 目的：从 reviewed implementation 和 audit evidence 准备 release-candidate bundle，但不声明
  final release。

### `0.7.8-v0.7-final-closeout`

- 类型：documentation-only
- 状态：review complete / final closeout complete
- 目的：只有在 release-candidate approval、evidence consistency checks、scope review 和 unresolved
  finding classification 完成后，才标记 v0.7 final / closeout complete。

## 当前状态

Active child package：无；`0.7.8-v0.7-final-closeout` 已完成 final closeout。

Current route：`complete`。

Implementation authorization：no。

Evidence execution authorization：final verification 后已关闭。

## Handoff 基线

- v0.6 状态：`final / closeout complete`，且 0.6.11 post-closeout reliability/scope
  repair 已完成。
- v0.6 evidence 只能作为 handoff evidence，不能作为当前 v0.7 PASS evidence。
- v0.6 明确不声明 external validation readiness、projection readiness、product readiness、
  full autonomous runner/full-suite PASS、live provider behavior、generation-quality PASS 或
  durable generated-world persistence。
- v0.7 从自己的 package review gates 开始，不继承 v0.6 的 implementation authorization。

## 最终评估状态

Current value：`final / closeout complete`。

v0.7 parent campaign docs 已通过 read-only parent documentation review，且 `0.7.0`、`0.7.1`
、`0.7.2`、`0.7.3`、`0.7.4`、`0.7.5`、`0.7.6`、`0.7.7` 与 `0.7.8`
已 review complete。`0.7.8` final verification 和 evaluator review 已通过。该 final state 不授权
runtime、schema、API、frontend、test implementation、fixture、migration、external repository、
generated result 或 legacy implementation work。
