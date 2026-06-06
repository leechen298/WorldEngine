# 计划

英文原文：`plan.md`。

Status：reviewed / ready for implementation

## 目标

在任何 runtime、schema、API 或 test implementation 开始前，创建并 review concrete `0.9.7` mixed implementation package。

## 已读取的权威输入

- `AGENTS.md`
- `docs/iterations/AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/iterations/README.md`
- `docs/iterations/v0.9/CURRENT_STATE.md`
- `docs/iterations/v0.9/GOAL_RUNNER.md`
- `docs/iterations/v0.9/v0.9-plan.md`
- `docs/iterations/v0.9/0.9.3-world-model-rule-parameter-schema/contract.md`
- `docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/contract.md`
- `docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/contract.md`
- 当前 active-backend 的 event、runtime、rule-parameter 和 direction code surfaces。

## 文档类型

Mixed implementation package documentation。Required files：

```text
README.md
README.zh.md
intent.md
intent.zh.md
contract.md
contract.zh.md
technical-design.md
technical-design.zh.md
test-plan.md
test-plan.zh.md
plan.md
plan.zh.md
review.md
review.zh.md
```

## 要创建或更新的文件

Create：

```text
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/*
```

Documentation review 后，只有 review gate 通过时才更新 parent route/status docs。

## Documentation Stage 明确不在范围内的文件

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- package documentation 外的 `tests/**`。
- checker fixtures 和 generated results。
- external repositories 和 Validation Client。

## Required Package Status Values

Drafting 阶段：

```text
Status: ready for documentation review
implementation_authorized: no
provider_live_call_authorized: no
generated_result_creation_authorized: no
checker_execution_authorized: no
external_validation_authorized: no
```

Documentation evaluator PASS 后，status 可推进到 `reviewed / ready for implementation`，并且只对本 package 记录 implementation approval。

## Review Gates

1. Documentation checks pass。
2. Read-only subagent/evaluator review package docs，并报告无 P0/P1 且无 blocking P2。
3. `review.md` 记录 findings 和 authorization state。
4. 只有 review evidence 记录后，parent v0.9 route 才推进。

## Approval 后的 Implementation Plan

如果后续授权 implementation，应按 TDD 执行：

1. 添加 focused tests，覆盖 extra fields、legal acceptance、illegal rejection、redaction、direction-biased acceptance 和 diff consistency。
2. 添加 candidate、patch、legality result、diagnostics、state diff 和 evidence schemas。
3. 添加 deterministic legality helper。
4. 只有 approved contract 需要时，才添加 additive route 或 event integration。
5. 运行 focused、related、backend 和 diff checks。
6. closeout 前请求 implementation-scope subagent review。

## 停止条件

如果出现以下情况，停止且不得 implementation：

- evaluator 报告 P0/P1 或 blocking P2。
- implementation 需要 provider-backed interpretation。
- implementation 需要 checker fixtures 或 external validation。
- implementation 需要 durable scheduling、generated-result creation 或 persistent rule installation。
- implementation 需要 Agent continuity、private state mutation、narrative projection、diagnostic dialogue、frontend、Validation Client 或 `backend/worldengine/` changes。
