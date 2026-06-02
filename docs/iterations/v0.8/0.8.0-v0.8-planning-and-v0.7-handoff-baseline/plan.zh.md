# Plan

## 执行步骤

1. 读取 root 和 iteration governance documents。
2. 读取 v0.8 parent `README.md`、`CURRENT_STATE.md`、`GOAL_RUNNER.md`、
   `CAMPAIGN_PLAN.md`、`v0.8-plan.md` 和 `review.md`。
3. 读取当前 v0.7 `CURRENT_STATE.md` 与 v0.7 overall validation result，确认 handoff
   status。
4. 创建 `0.8.0` child package document set 和中文镜像。
5. 更新 parent v0.8 route/status surfaces，记录 `0.8.0` review complete 和 `0.8.1`
   selected / child docs not created。
6. 运行 `test-plan.md` 中的 documentation checks。
7. 使用 read-only subagent/evaluator review 检查 v0.7 handoff drift 和 `0.8.0`
   package completeness。
8. 在 `review.md` 中记录 changed files、commands、test results、compatibility
   review、scope review、unresolved findings 和 final assessment。

## 阶段边界

- Phase 1：只做 documentation review 与 handoff synchronization。
- Phase 2：只做 documentation checks 与 evaluator review。
- Phase 3：只有在无 unresolved P1/P2 后，才 handoff 到 `0.8.1`。

本 package 不包含 implementation、evidence execution、backend test、frontend test、E2E、
Agent smoke、autonomous run、external validation run 或 runtime smoke。

## 停止条件

出现以下情况时停止：

- 无法从当前文件验证 v0.7 handoff evidence。
- 必需的 `0.8.0` package docs 或 mirrors 缺失。
- Parent 与 child status surfaces 不一致。
- Scope guard 报告非 `docs/iterations/v0.8/**` changes。
- Active v0.8 docs 中仍有过时的 v0.7 unresolved-blocker wording。
- Evaluator 报告 P1 或 unresolved P2。
- 任何文本声明本 session 未运行的 v0.8 pass evidence。

## Review 更新步骤

Checks 和 evaluator results 完成后，更新 `review.md` 与 `review.zh.md`，记录 exact
commands、pass/fail outputs、compatibility review、scope review、unresolved findings 和
final assessment。
