# v0.8 Minimum Proved Working WorldEngine / External Validation Readiness

状态：planned / ready for review
类型：Codex `/goal` development campaign and iteration package root

## 目标

v0.8 准备 WorldEngine 达到一个最小“正常工作”状态，并让仓库外部的 validation
function 可以从外部观察和判断这个状态。

本版本不在本仓库内实现 external validation function，也不实现第一个 external
product application。目标是让 core engine 的 generation、runtime、Agent loop、
memory-context、event 和 projection surfaces 足够一致、可观察，让独立的外部
validator 或 projection application 能判断 WorldEngine 是否正常工作。

v0.8 从 v0.7 历史 closeout evidence 之后开始，但 v0.7 已记录 post-closeout
code-review blockers。这些 blockers 是 handoff 风险，不是已解决证据。除非当前
session 证据证明受影响 blockers 已修复，或 active v0.8 package 明确把它们记录为
blockers，否则 v0.8 不得声明 clean pass、minimum working-state PASS、external
validation readiness PASS、product readiness 或 external consumer PASS。

## Goal Entry

自然语言目标：

```text
完成 v0.8
启动 WorldEngine v0.8：Minimum Proved Working WorldEngine / External Validation Readiness
编写 v0.8 文档
生成 v0.8 文档
```

解释：

- 从 `CURRENT_STATE.md` 开始。
- 按 `GOAL_RUNNER.md` 选择 route、执行 documentation gates、
  implementation authorization、evaluator checkpoints、verification 和 stop
  conditions。
- 按 `CAMPAIGN_PLAN.md` 与 `v0.8-plan.md` 确认 child sequence、
  deliverables、compatibility constraints 和 handoff rules。
- 把 parent v0.8 package 作为当前唯一 authoritative entrypoint。
- 任何未来 child package 开始前，都必须在当时创建或确认完整 package document
  set 并完成 review gate。不得把 planned `0.8.x` roadmap entries 当成
  execution-approved child contracts。

这不是 external validation application、external projection application、
external repository、product packaging workflow、deployment process、concrete
validation scenario 或 application-specific backend。

## External Validation Boundary

WorldEngine 可以知道外部会存在一个 validation function，并由它验证 engine 是否正常
工作。WorldEngine 不拥有该外部 validator 的实现、private scenarios、product UI、
application state、runner internals、oracle logic、private repository paths 或
concrete world content。

本仓库内，v0.8 只可以定义让外部验证成为可能的 core-side public surfaces 和 evidence
expectations：

- stable public API 与 read-model expectations。
- minimum working-state claim taxonomy。
- observable event、runtime、generation、Agent loop 和 memory-context evidence
  boundaries。
- 未来 external evidence 的 redaction 与 no-private-detail rules。
- 防止 internal tests 被过度声明为 external validation PASS 的 stop rules。

## v0.7 交接风险

v0.7 parent route 历史状态是 `final / closeout complete`，但
`docs/testing/results/2026-06-02-v0.7-code-review.md` 记录了 post-closeout
issues，涉及 checker、schema、manifest 和 projection read-model semantics。

这些 findings 会阻断 clean pass、minimum working-state PASS、external validation
readiness PASS、product PASS，以及任何依赖受影响 v0.7 contracts 的 v0.8 readiness
claim；直到当前 session 证据证明它们已修复，或 active v0.8 package 明确把它们记录为
blockers。

## 范围

v0.8 允许范围：

- minimum normally working WorldEngine readiness concepts。
- external validation 所需的 engine-side public surface requirements。
- core-side generation/runtime/Agent-loop/memory-context readiness boundaries。
- 只有在 reviewed child package 明确授权实现时，才可 harden generic read-only
  projection 或 read-model payload。
- provider-boundary、credential、mock fallback 或 live-smoke semantics 只有在
  reviewed child package 明确拥有该范围时才可处理。
- public engine surfaces 的 core-side smoke 与 compatibility evidence。
- release-candidate、final closeout 和 post-closeout evidence documents。

v0.8 禁止范围：

- 不在本仓库内实现 external validation function 或 external projection application。
- 不添加 concrete app worlds、names、maps、locations、characters、resources、
  story rules、seed data、UI selectors、private transcripts、product routes、
  product packaging、deployment scripts 或 app-specific backend logic。
- 不添加 private external repository paths、private runner state、hidden reset
  APIs、validation oracle internals、prompt/provider traces、secrets 或
  non-redacted external event payloads。
- 没有当前 session 证据时，不声明 external validation PASS、external consumer
  PASS、product readiness、runtime/API/frontend/E2E PASS、Agent smoke PASS、
  autonomous PASS 或 generation-quality PASS。
- 除非 reviewed child package 明确授权该范围，不添加 durable persistence、
  migrations、live provider behavior 或 generated-world active runtime execution。
- 不在 `backend/worldengine/` 下添加新 runtime features。

## 交付物

- Parent goal-campaign documents：`README.md`、`v0.8-plan.md`、
  `GOAL_RUNNER.md`、`CURRENT_STATE.md`、`CAMPAIGN_PLAN.md`、`review.md`，以及
  Chinese mirrors。
- `v0.8-plan.md` 内的 planned `0.8.x` child-package specifications。
- 明确的 v0.7 handoff-risk handling 与 stop rules。
- 明确的 boundary rules：external validation 在本仓库外，core-side readiness
  for that validation 在本仓库范围内。
- Documentation-stage review evidence，证明本次 drafting pass 不修改 runtime、
  schema、API、frontend、test implementation、fixture、migration、external
  repository、generated result 或 `backend/worldengine/` implementation files。

## Planned Package Roadmap

下列 `0.8.x` entries 以及 `v0.8-plan.md` 中的条目是 roadmap-level planned
package specs。它们不是当前 implementation authorization，不是 execution-approved
contracts，也不是不可变脚本。未来 agent 必须在 child 启动时创建或确认 active child
package documents，然后完成 review 才能 implementation。

### `0.8.0-v0.8-planning-and-v0.7-handoff-baseline`

- 类型：documentation-only
- 状态：planned
- 目的：创建 v0.8 documentation root、goal-campaign controls、v0.7
  handoff-risk baseline、minimum working-state boundary、external-validation
  boundary 和 package sequence。

### `0.8.1-minimum-working-state-contract`

- 类型：documentation-only
- 状态：planned
- 目的：定义 v0.8 何时可以称为 minimum normally working WorldEngine state，同时不声明
  product readiness 或 external validation PASS。

### `0.8.2-core-observable-surface-boundary`

- 类型：documentation-only or mixed
- 状态：planned
- 目的：定义 external validator 可观察的 public runtime、event、generation、
  Agent loop、memory-context 和 read-model surfaces。

### `0.8.3-generation-runtime-agent-loop-readiness`

- 类型：mixed or code
- 状态：planned
- 目的：如果 reviewed child package 授权实现，则 harden core-side minimum
  generation -> runtime -> Agent loop readiness slices。

### `0.8.4-external-validation-handoff-contract`

- 类型：documentation-only or mixed
- 状态：planned
- 目的：定义 WorldEngine 为 external validation function 暴露或记录什么，但不定义外部
  validator 如何连接或运行。

### `0.8.5-core-working-state-smoke-evidence`

- 类型：mixed validation package
- 状态：planned
- 目的：对 in-scope public engine surfaces 运行 core-side smoke 与 compatibility
  evidence，不运行也不实现 external validator。

### `0.8.6-v0.8-evidence-and-boundary-audit`

- 类型：documentation-only
- 状态：planned
- 目的：在 release-candidate packaging 前 audit evidence、compatibility surfaces、
  unresolved findings 和 external-validation leakage risks。

### `0.8.7-v0.8-release-candidate-bundle`

- 类型：documentation-only
- 状态：planned
- 目的：基于 reviewed evidence 准备 release-candidate bundle，不超出当前 session
  evidence 声明 final readiness。

### `0.8.8-v0.8-final-closeout`

- 类型：documentation-only
- 状态：planned
- 目的：只有在 reviewed package completion、evidence consistency checks、scope
  review、blocker classification 和 evaluator approval 后，才标记 v0.8 final。

## 当前状态

Active child package：none。

Current route：parent documentation drafted / ready for review。

Implementation authorization：no。

Evidence execution authorization：no。

这个 parent state 不授权任何 runtime、schema、API、frontend、test implementation、
fixture、migration、external repository、generated result、external validation
implementation 或 `backend/worldengine/` implementation work。

## 交接基线

- v0.7 状态：historical `final / closeout complete`，但记录了 post-closeout
  code-review blockers。
- v0.7 evidence 只能作为 handoff evidence，不能作为 current v0.8 PASS evidence。
- v0.7 不证明 v0.8 minimum working-state readiness、external validation readiness、
  product readiness 或 external consumer PASS。
- v0.8 从自己的 package review gates 开始，不继承 v0.7 implementation
  authorization。

## Final Assessment State

当前值：`planned / ready for review`。

Parent v0.8 campaign docs 已起草，等待 review。Planned `0.8.x` entries 仍只是
route-map specifications。当前状态不授权 implementation、external validation
execution、projection app build 或 readiness PASS claim。
