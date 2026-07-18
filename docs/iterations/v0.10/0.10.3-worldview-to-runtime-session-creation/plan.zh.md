# Plan

## Ordered Execution Steps

1. 读取 package docs 和现有 generation/session code。
2. 运行 documentation / contract evaluator。
3. 如果 PASS，记录 `implementation_authorized: yes`。
4. 添加 session request/summary schema。
5. 扩展 session store 和 route。
6. 更新 manifest discovery。
7. 添加 focused tests。
8. 运行 `test-plan.md` commands。
9. 运行 implementation/evidence evaluator。
10. 更新 package 和 parent review，然后交接到 `0.10.4`。

## Phase Boundaries

authorization 前不做 implementation edits。Implementation 限于 allowed files。Closeout 必须记录
non-claims。

## Stop Conditions

如果需要 live provider calls、runtime execution、snapshots、dashboard、checker、Validation
Client、persistence、generated results、external validation 或 `backend/worldengine/`，停止。

## Review Update Step

authorization 和 closeout 前更新 review，记录 changed files、commands、test results、
evaluator evidence、compatibility、scope、findings 和 handoff。
