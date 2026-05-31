# v0.5 记忆与自连续性基底

状态：final / closeout complete
类型：Codex `/goal` development campaign 与 iteration package root

## 目标

v0.5 定义并逐步实现 Agent 在 WorldEngine world 中生活时需要的第一层通用
memory 与 self-continuity substrate。

本版本从已经评审通过的 v0.4 request-driven Agent-in-World loop 出发，保持
memory/self-continuity 边界通用、可检查、以证据为准。它不得把 WorldEngine
收窄成 demo-specific backend 或 application surface。

## 目标入口

自然语言目标：

```text
完成 v0.5
```

解释：

- 从 `CURRENT_STATE.md` 开始。
- 按 `GOAL_RUNNER.md` 进行 route selection、subagent/evaluator checkpoints、
  implementation authorization、verification 与 stop conditions。
- 按 `CAMPAIGN_PLAN.md` 和 `v0.5-plan.md` 确认 child sequence、
  deliverables、compatibility constraints 与 handoff rules。
- 做任何 child work 前，必须先读取 active child package docs。

这不是 automation-controller 实现。Scheduling、orchestration、retry
infrastructure 和 Codex role assignment 仍在 WorldEngine 范围外。

## 范围

v0.5 允许：

- 定义 working memory 概念、provenance、bounded read/write semantics，并在后续
  package 中做 additive generic implementation。
- 定义 episodic memory 概念、event-linked semantics，并在后续 package 中做
  additive generic implementation。
- 先定义 relationship state schema semantics，再实现行为。
- 先定义 self-summary schema semantics，再实现 summarization behavior。
- 先定义 reflection record schema semantics，再实现 automatic reflection behavior。
- 先定义 personality drift signal schema semantics，再实现 action modification
  behavior。
- 只有在已评审 child package 明确授权时，才允许 additive backend schemas、
  in-memory substrate services 和 focused backend tests。

v0.5 禁止：

- 不实现 world generation；该范围属于 v0.6。
- 不实现 external validation runner readiness 或 report automation；该范围属于 v0.7。
- 不实现 projection application readiness；该范围属于 v0.8。
- 不添加具体 world names、maps、characters、locations、resources、story rules、
  seed data、UI-specific app behavior 或 private validation oracle details。
- 除非后续已评审 v0.5 child 明确授权，不添加 frontend product behavior。
- 除非后续已评审 v0.5 child 明确授权，不添加 migrations 或 durable persistence。
- 不在 `backend/worldengine/` 下新增 runtime feature。

## 交付物

- Parent goal-campaign documents：`README.md`、`v0.5-plan.md`、
  `GOAL_RUNNER.md`、`CURRENT_STATE.md`、`CAMPAIGN_PLAN.md`、`review.md`，
  以及中文镜像。
- 第一个 child package：
  `0.5.0-v0.5-planning-and-continuity-boundary-baseline`，包含 README、
  intent、contract、technical design、test plan、plan、review 和中文镜像。
- 直到 final closeout 的 planned child package sequence。
- `/goal` 执行所需的 subagent/evaluator checkpoint rules。
- Documentation-stage review evidence，证明 `0.5.0` 没有修改 runtime、schema、
  API、frontend、test implementation、fixture、migration、external repository 或
  `backend/worldengine/` 文件。

## 包索引

### `0.5.0-v0.5-planning-and-continuity-boundary-baseline`

- 类型：documentation-only
- 状态：review complete
- 目的：创建 v0.5 documentation root、goal-campaign controls、version plan、
  memory/self-continuity boundary、compatibility baseline 和 v0.4 handoff mapping，
  且不修改实现文件。

### `0.5.1-memory-self-continuity-contracts`

- 类型：documentation-only
- 状态：review complete
- 目的：在实现前定义 public memory/self-continuity concepts 与 schema semantics。

### `0.5.2-working-and-episodic-memory-substrate`

- 类型：mixed or code
- 状态：review complete
- 目的：只实现 additive generic working-memory 与 episodic-memory schemas、
  in-memory substrate 和 focused backend tests。

### `0.5.3-memory-context-loop-integration`

- 类型：mixed or code
- 状态：review complete
- 目的：把 bounded read-only memory context 接入 Agent Loop perception path，
  不改变 action semantics。

### `0.5.4-reflection-relationship-and-drift-contract-followup`

- 类型：documentation-only or mixed
- 状态：review complete
- 目的：在任何行为影响 action 前，细化 relationship state、self-summary、
  reflection record 和 personality drift signal contracts。

### `0.5.5-v0.5-evidence-and-compatibility-audit`

- 类型：documentation-only
- 状态：review complete
- 目的：审计 v0.5 implementation evidence、compatibility surfaces、unresolved
  findings 和 release-candidate review handoff readiness。

### `0.5.6-v0.5-release-candidate-bundle`

- 类型：documentation-only
- 状态：review complete
- 目的：基于已评审 implementation 和 audit evidence 准备 v0.5 release-candidate
  bundle，但不声明 final release。

### `0.5.7-v0.5-final-closeout`

- 类型：documentation-only
- 状态：final / closeout complete
- 目的：只有在 release-candidate review approval、evidence consistency checks 和
  unresolved finding classification 完成后，才标记 v0.5 final / closeout complete。

## 当前状态

Active child package：
none。

Current route：`final-closeout-complete`。

Implementation authorization：no。

## 交接基线

- v0.4 状态：`final / closeout complete`。
- v0.4 post-closeout 状态：validation clean pass after frontend build repair。
- v0.4 与 post-closeout command evidence 只作为 baseline 和 handoff evidence。
  它们不是当前 v0.5 implementation pass claims。
- v0.5 final current-session evidence：`git diff --check` 通过；required
  docs/mirrors `missing=0`；changed-file scope guard `out_of_scope=0`；
  focused backend memory/loop/action compatibility `33 passed`；full backend
  regression `145 passed`；closeout consistency evaluator PASS。
- 不声明 frontend、E2E、Agent smoke、autonomous、external validation、projection
  readiness 或 product readiness 已通过。

## 最终评估状态

当前值：`final / closeout complete`。
