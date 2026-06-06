# Plan

英文原文：`plan.md`。

## 有序执行步骤

1. 读取 parent v0.9 state、v0.9 plan、0.9.2 output contract、0.9.3
   rule/parameter contract、LLM-backed lifecycle validation plan、scorecard、
   artifact contract 和 iteration rules。
2. 起草具体 `0.9.4` package documents 和 Chinese mirrors。
3. 运行 documentation checks 和 required-term checks。
4. 请求 read-only subagent documentation/contract evaluator。
5. 修复或记录 evaluator findings。存在任何 P0/P1 或 blocking P2 时，不得授权 implementation。
6. 如果 review 通过，更新 `review.md`，把 `implementation_authorized` 从 `no` 改为
   `yes`，同时保持：

```text
provider_live_call_authorized: no
generated_result_creation_authorized: no
external_validation_authorized: no
```

7. 只实现 reviewed `0.9.4` helper/schema/test scope。
8. 运行 `test-plan.md` 中的 focused tests、related regressions、backend regression 和 documentation checks。
9. 请求 implementation-scope/code-review subagent evaluation。
10. 修复 blocking findings，或停止。
11. 仅在 implementation evidence current 且一致后，更新 package `review.md`、package README status
    和 parent v0.9 state。

## 阶段边界

Documentation phase 只有在 subagent review 记录无 P0/P1 且无 blocking P2 后结束。

Implementation phase 只有在 `review.md` 记录 implementation authorization enabled 后开始。

Closeout phase 只有在 focused 和 regression verification commands 有当前会话证据后开始。

## 停止条件

如遇以下情况，停止：

- review authorization 之前需要开始 implementation。
- immediate evaluator 的实现需要 bounded runtime controls。
- fidelity PASS 需要 subjective judgement 而不是 deterministic public evidence。
- 需要 live provider calls 或 generated result creation。
- 必须修改 contract 范围外的 implementation file。
- subagent 报告 unresolved P0/P1 或 blocking P2。
- tests 失败且无法在 `0.9.4` 范围内修复。

## Review 更新步骤

`review.md` 必须记录 changed files、exact commands、command results、
compatibility review、scope review、subagent findings、unresolved findings，以及
handoff to `0.9.5`。
