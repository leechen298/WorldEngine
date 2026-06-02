# Plan

## Stage 1: Documentation Gate

1. 创建完整 0.8.3 package document set 和 Chinese mirrors。
2. 保持 `implementation_authorized: no` 和 `evidence_execution_authorized: no`。
3. 运行 documentation shape、status、scope 和 claim guards。
4. 派出 read-only documentation/contract evaluator。
5. 如果 evaluator 报告无 P0/P1 且无 blocking P2，则更新 `review.md`，记录 evaluator
   evidence，并决定是否可授权 implementation。

## Stage 2: Implementation If Authorized

1. 按 required order 读取 package docs。
2. 为 core-readiness probe 添加 red tests。
3. 在 `backend/app/schemas/world_generation.py` 添加 additive schemas。
4. 在 `backend/app/core/world_generation.py` 添加 isolated probe helper。
5. 在 `backend/app/api/routes/world_generation.py` 添加 read-only route。
6. 运行 focused tests，直到 red tests 通过。
7. 运行 adjacent generation/runtime/Agent-loop compatibility tests。
8. 运行 scope、redaction 和 claim guards。
9. 在任何 broader readiness claim 前，派 implementation-scope 或 code-review evaluator。

## Stop Conditions

- `review.md` 未明确记录 `implementation_authorized: yes` 前停止 implementation。
- 如果 probe 需要 contract 外文件，停止。
- 如果 app runtime、app event log、params、memory store、archive store 或 external state 被
  mutate，停止。
- 如果 evidence 会暴露 raw memory、prompt/provider traces、secrets、private transcript
  data、UI selectors、oracle internals 或 external app data，停止。
- 如果 implementation 开始定义 external validator connection、external app behavior、product
  UI、persistence、migrations 或 live provider calls，停止。

## Handoff

如果 implementation clean closeout，则 hand off bounded core-readiness evidence 给
`0.8.4-external-validation-handoff-contract`。如果未实现，则 hand off reviewed design 和 exact
missing authorization/evidence。
