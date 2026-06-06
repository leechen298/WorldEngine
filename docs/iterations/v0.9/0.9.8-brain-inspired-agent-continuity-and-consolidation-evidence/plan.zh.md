# Plan

英文原文：`plan.md`。

Status：reviewed / ready for implementation

## Objective

在任何 runtime、schema、API、test、checker、fixture、provider、frontend 或 Validation Client implementation 开始前，创建并 review 具体 `0.9.8` mixed implementation package。

## Authoritative Inputs Read

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/iterations/AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/v0.9/CURRENT_STATE.md`
- `docs/iterations/v0.9/GOAL_RUNNER.md`
- `docs/iterations/v0.9/v0.9-plan.md`
- `docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/contract.md`
- current active-backend Agent loop、memory、runtime、event 和 public handoff surfaces，作为 future implementation inputs。

## Documentation Type

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

## Files To Create Or Update

Create：

```text
docs/iterations/v0.9/0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence/*
```

Documentation review 后，只有 review gate 通过时才更新 parent route/status docs。

## Files Explicitly Out Of Scope During Documentation Stage

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- package documentation 之外的 backend tests。
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

Documentation evaluator PASS 后，status 可以推进到 `reviewed / ready for implementation`，并只为本包记录 implementation approval。

## Review Gates

1. Documentation checks pass。
2. Read-only subagent/evaluator reviews package docs，并报告 no P0/P1 且 no blocking P2。
3. `review.md` 记录 findings 和 authorization state。
4. 只有 review evidence 记录后，parent v0.9 route 才能推进。

## Implementation Plan After Approval

如果 later authorized，implementation 应按 TDD 进行：

1. 为 continuity artifacts、consolidation artifacts、accepted autonomous action evidence、no-intent/rest states、event reactions、scripted-autonomy rejection、redaction 和 compatibility 添加 focused tests。
2. 添加 continuity、consolidation、autonomous action、event reaction、diagnostics 和 scripted-autonomy rejection evidence schemas。
3. 添加 deterministic continuity/consolidation helper。
4. 仅在 approved contract 要求时添加 additive route 或 event integration。
5. 运行 focused、related、backend 和 diff checks。
6. closeout 前请求 implementation-scope subagent review。

## Stop Conditions

如果出现以下情况，停止且不实现：

- evaluator 报告 P0/P1 或 blocking P2。
- implementation 需要 raw thought、chain-of-thought、private memory payloads、private goals 或 hidden context。
- implementation 需要 provider-backed interpretation。
- implementation 需要 checker fixtures 或 external validation。
- implementation 需要 durable scheduling、generated-result creation 或 persistent background processes。
- implementation 需要 narrative projection、diagnostic dialogue、frontend、Validation Client 或 `backend/worldengine/` changes。
