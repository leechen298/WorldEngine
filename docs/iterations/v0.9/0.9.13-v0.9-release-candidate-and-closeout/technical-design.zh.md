# Technical Design

英文镜像：`technical-design.md`。

## Closeout Model

Closeout 是 documentation-only。最终状态从已记录 evidence 推导，不执行新的 runtime behavior。

```text
0.9.1-0.9.10 implementation reviews
        +
0.9.11 handoff contract review
        +
0.9.12 checker-valid BLOCKED result
        ->
v0.9 closeout status: blocked
```

## Status Rules

- Parent `CURRENT_STATE.md` 指向 completed 0.9.13 closeout state。
- Parent `README.md`、`GOAL_RUNNER.md`、`CAMPAIGN_PLAN.md`、`v0.9-plan.md` 和
  `review.md` 使用相同 closeout wording。
- `provider_live_call_authorized`、`evidence_execution_authorized` 和
  `implementation_authorized` 保持 `no`。

## Compatibility Review Shape

本 package 不修改影响 compatibility 的代码。它引用 implementation-bearing child reviews 已记录的
compatibility evidence，并保持 provider/runner gaps classified。
