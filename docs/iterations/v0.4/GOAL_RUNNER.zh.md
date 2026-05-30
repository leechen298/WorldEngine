# GOAL_RUNNER.md

用途：定义 v0.4 的 Codex App `/goal` prompt 和 campaign 指引。

本文件不是 WorldEngine runtime behavior，也不是 automation-controller 实现。它只定义 v0.4 开发 campaign 的可读入口、状态机、实现授权规则、subagent/evaluator checkpoints、stop conditions、evidence rules 和 review update rules。

## Campaign 入口

当用户说：

```text
完成 v0.4
```

Codex 应按本文件、`CURRENT_STATE.md`、`CAMPAIGN_PLAN.md` 和 active child package 文档运行 campaign。

默认行为：

- 从 `CURRENT_STATE.md` 中的 active child package 开始。
- 先读父级文档，再读 active child package docs。
- 只有 active child 达到必需 exit state 后才推进。
- 遇到 blocker、failed evidence、缺失必需文件、source conflict、越界变更或缺失必需 evaluator checkpoint 时停止。

## 首读文件

- `README.md`
- `CURRENT_STATE.md`
- `CAMPAIGN_PLAN.md`
- `v0.4-plan.md`
- `review.md`
- `docs/iterations/AGENTS.md`
- 根目录 `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/v0.3-post-closeout/05-final-validation-bundle/final-validation-bundle.md`

然后读 active child package：`README.md`、`intent.md`、`contract.md`、`technical-design.md`、`test-plan.md`、`plan.md` 和 `review.md`。

## Child Package 顺序

1. `0.4.0-v0.4-planning-and-compatibility-baseline`
2. `0.4.1-agent-in-world-loop-contract`
3. `0.4.2-agent-perception-and-schemas`
4. `0.4.3-action-intent-validation-and-result-adapter`
5. `0.4.4-minimal-agent-loop-orchestration-and-api`
6. `0.4.5-agent-loop-evidence-and-compatibility-audit`
7. `0.4.6-v0.4-release-candidate-bundle`
8. `0.4.7-v0.4-final-closeout`

## 允许 Route Types

- `goal-entry`
- `documentation-planning`
- `contract-review`
- `human-review`
- `implementation-authorization-review`
- `schema-implementation`
- `action-validation-implementation`
- `loop-orchestration-implementation`
- `evidence-audit`
- `release-candidate-review`
- `final-closeout`
- `repair-loop`
- `blocker-recording`
- `needs-user-input`

## 实现授权规则

只有 child package 包含完整七件套、contract/design/test-plan/plan 已评审、documentation / contract evaluator 报告无 P1 或未解决 P2 finding、active package contract 明确允许相关文件类别，并且 `review.md` 记录授权和 findings 后，child package 才能记录 `implementation_authorized: yes`。

docs-only child 不授权 runtime implementation，除非后续带实现 child 重新执行本规则。

## 强制 Subagent / Evaluator Checkpoints

带实现 child package 必须包含：

1. 在 `implementation_authorized: yes` 前完成 documentation / contract evaluator。
2. 文件变更后、宽验证前完成 implementation-scope evaluator。
3. 聚焦测试后、最终状态前完成 code-review subagent 或 evaluator。
4. 在标记 tests、API smoke、E2E、backend checks 或 runtime behavior passed 前完成 validation-evidence evaluator。
5. 在 `review.md` 记录 final route status 前完成 closeout consistency review。

当 docs-only child 改动 goal routing、process rules、evidence rules、package sequencing、validation templates、release status、automation-consumption contracts 或英文/中文镜像义务时，需要 read-only documentation evaluator。

subagents 默认只读。只有 active child contract 明确允许 worker implementation，且主 agent 记录 delegated write scope 时，subagent 才能编辑文件。

## 停止条件

出现以下情况时，停止并记录 `blocked`、`failed` 或 `needs-user-input`：

- 缺失必需父级或 child 文档。
- 必需 evaluator checkpoint 不可用。
- 必需 evaluator 报告 P1 或未解决 P2。
- 实现会触碰 active child contract 未允许的文件。
- docs-only package 需要 runtime、schema、API、frontend、fixture、migration 或 backend test 变更。
- 测试失败且 active package 未授权 repair。
- 缺少命令证据，但报告试图声称 pass。
- 实现试图加入范围外后续版本工作或具体世界/应用行为。
- git state 显示越界修改。

## 证据要求

任何未来 execution claim 必须记录 branch、commit、active child package、executor、changed files、必要时的 files read、exact commands run、summarized command results、checks not run and why、subagent/evaluator checkpoints、P1/P2/P3 findings、compatibility review、scope review 和 final assessment。

v0.3 历史证据只是 handoff context。除非 child contract 带理由明确接受，否则它不算 v0.4 新鲜实现或验证证据。

## Review 更新规则

每个 child closeout 必须更新自己的 `review.md`，记录 changed files、commands run、commands not run、test results、compatibility review、scope review、subagent/evaluator findings、unresolved P1/P2/P3 和 final assessment。

父级 `CURRENT_STATE.md` 只能在 child 达到 reviewed route status 后更新。

## 禁止范围扩张规则

本 campaign 不得绕过 iteration package review gates，不得实现 v0.5 memory/self-continuity，不得实现 v0.6 world generation，不得实现 v0.7 external validation readiness，不得实现 v0.8 projection readiness，不得添加具体世界内容，不得添加应用特定后端逻辑，也不得在 `backend/worldengine/` 下新增 runtime feature。
