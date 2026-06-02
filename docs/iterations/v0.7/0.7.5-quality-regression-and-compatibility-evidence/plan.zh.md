# Plan

## Phase 1: Documentation Gate

1. 读取 `0.7.2`、`0.7.3` 和 `0.7.4` review evidence。
2. Draft package docs and Chinese mirrors。
3. Run documentation-gate checks。
4. Use documentation/contract and mirror/scope evaluators。
5. 修复 P0/P1/P2 findings 或停止。
6. 只有 evaluator approval 后，才记录 `evidence_execution_authorized: yes`。

## Phase 2: Evidence Execution

1. 运行 `tools/testing` 下的 existing checker tests。
2. 运行 readiness manifest 与 projection read-model CLI validators。
3. Parse v0.7 JSON schema/manifest files。
4. Run formatting and changed-file scope checks。
5. 将未运行 surfaces 标记为 skipped 或 out of scope。

## Phase 3: Evidence Matrix

1. 创建 `evidence-matrix.md` 和中文镜像。
2. 记录 exact commands、results、supported claims 和 exclusions。
3. 记录 compatibility 与 residual-risk notes。

## Phase 4: Review And Handoff

1. 更新 `review.md` 和中文镜像。
2. Use validation-evidence and closeout consistency evaluators。
3. 更新 parent v0.7 route/status surfaces，handoff 到 `0.7.6`。

## Stop Conditions

- 任一 in-scope command 失败。
- Evidence 需要 product-code repair。
- Skipped 或 out-of-scope check 被写成 PASS。
- Broad readiness claim 缺少 current-session evidence。
- Scope guard 报告 out-of-scope files。
