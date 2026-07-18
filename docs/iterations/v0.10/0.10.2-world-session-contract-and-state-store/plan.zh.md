# Plan

## Ordered Execution Steps

1. 读取 v0.10 route 和本 package docs。
2. 运行 documentation / contract evaluator。
3. 如果 PASS，记录 `implementation_authorized: yes`。
4. 添加 session schemas。
5. 添加 in-memory session store。
6. 添加 session routes 和 router registration。
7. 更新 manifest surfaces。
8. 添加 focused backend tests。
9. 运行 `test-plan.md` commands。
10. 运行 implementation/evidence evaluator。
11. 更新 package 和 parent review，然后交接到 `0.10.3`。

## Phase Boundaries

review authorization 前不编辑 implementation files。implementation 期间只编辑 allowed files。
closeout 时记录 exact command evidence 和 non-claims。

## Stop Conditions

如果 implementation 需要 worldview generation、runtime run、snapshots、dashboard、persistence、
provider live calls、checker fixture work、Validation Client、generated results、external
validation 或 `backend/worldengine/`，停止。

## Review Update Step

authorization 前和 final closeout 前更新 `review.md`，记录 changed files、commands、test
results、evaluator evidence、compatibility review、scope review、unresolved findings 和 handoff。
