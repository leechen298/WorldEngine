# Natural-Language Code Review Triggers

Status: reusable agent routing guide

英文版本：`natural-language-code-review-triggers.md`。

当用户说出这类短 code-review request 时使用本指南：

```text
审核 <version> 代码
review <version> code
审核 <iteration-package> 代码
代码审核 <feature-or-package>
```

## Primary Workflow

执行 `docs/testing/code-review-playbook.zh.md`。

这个 trigger 与 final closeout、validation 和 test-documentation trigger 分开。它审查
implementation 是否可靠、是否符合 active contracts；它本身不声明 product validation 已通过，
也不声明 tests 已运行。

## Required Reading

报告结果前必须：

- 读取 active version 或 package state。
- 读取 `CURRENT_STATE.md`、`GOAL_RUNNER.md`、`CAMPAIGN_PLAN.md`、version plan，
  以及存在的 code-bearing child package docs。
- 从 package `review.md`、contracts、test plans 和当前 git state 映射 implementation
  files。
- 不要把 final-closeout status 当成 code review 的替代品。

## Review Scope

审查被 review 的 version、package、feature 或 current implementation surface 范围内的：

- runtime code。
- schemas。
- API routes。
- frontend surfaces。
- tests。
- checkers。
- fixtures。
- compatibility boundaries。
- implementation 影响 evidence rules 时，也审查 evidence 和 artifact rules。

## Subagents And Verification

在工具可用且授权时使用 code-review subagent/evaluator，包括适用的 Superpowers
code-review workflows。

只有在需要验证某个 finding 或 claim 时运行 focused commands；否则明确说明哪些 tests 没有运行
以及原因。

## Findings-First Output

先报告 findings，按严重级别排序：

- P0。
- P1。
- P2。
- P3。

每个 finding 应包含：

- file 和 line reference。
- scope assessment。
- evidence gap 或 behavioral risk。
- 为什么重要。
- 是否运行 tests 来验证。

summary 只作为次要信息。如果没有发现问题，明确说明，并列出剩余 test gaps 或 residual risks。

## Repair Boundary

如果 code review 发现需要 implementation changes 的问题，不要在 review-only request 中静默修复。

修改 runtime、schema、API、frontend、test、fixture、migration 或 durable evidence behavior
前，必须创建或使用所需 iteration package，并获得适当 implementation authorization。
