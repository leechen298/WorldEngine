# Plan

## 执行步骤

1. 读取 v0.8 parent state、`0.8.0` review 和 `0.8.1` review。
2. 读取 v0.7 projection/read-model、external-validation readiness contracts，以及当前
   implementation/API maps。
3. 创建本 package 的七个英文文档和七个中文镜像。
4. 定义 observable surface families、public source boundaries、allowed summary classes、
   forbidden exposure 和 implementation authorization criteria。
5. 更新 parent route/status surfaces，标记 `0.8.2` review complete 并选择 `0.8.3`。
6. 运行 `test-plan.md` 中的 documentation checks。
7. 使用 read-only evaluator review 检查 boundary completeness 和 leakage risk。
8. 在 `review.md` 中记录 evidence 和 final assessment。

## 阶段边界

- Phase 1：只做 observable boundary documentation。
- Phase 2：只做 parent route/status synchronization。
- Phase 3：只做 documentation checks 和 evaluator review。

本 package 不包含 implementation、checker、schema、API、frontend 或 evidence execution。

## 停止条件

出现以下情况时停止：

- package docs 或 mirrors 缺失。
- boundary 需要 concrete validator identity、private paths、UI selectors、app data 或
  consumer-specific backend behavior。
- 文本暗示已实现 API 或 readiness PASS。
- Parent 与 child status surfaces 漂移。
- Evaluator 报告 P1 或 unresolved P2。

## Review 更新步骤

更新 `review.md` 和 `review.zh.md`，记录 changed files、exact commands、test results、
compatibility review、scope review、unresolved findings 和 final assessment。
