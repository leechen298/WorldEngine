# Plan

## 执行步骤

1. 读取 v0.8 parent state 和 `0.8.0` review。
2. 创建本 package 的七个英文文档和七个中文镜像。
3. 定义 required core slices、claim taxonomy、evidence classes、exclusions 和 handoff
   criteria。
4. 更新 parent route/status surfaces，标记 `0.8.1` review complete 并选择 `0.8.2`。
5. 运行 `test-plan.md` 中的 documentation checks。
6. 使用 read-only evaluator review 检查 contract completeness 和 overclaim risk。
7. 在 `review.md` 中记录 evidence 和 final assessment。

## 阶段边界

- Phase 1：只做 contract documentation。
- Phase 2：只做 route/status synchronization。
- Phase 3：只做 documentation checks 和 evaluator review。

本 package 不包含 implementation 或 evidence execution。

## 停止条件

出现以下情况时停止：

- package docs 或 mirrors 缺失。
- taxonomy 允许 blocked、skipped 或 out-of-scope states 计为 pass。
- 文本暗示 external validation PASS 或 product readiness。
- Parent 与 child status surfaces 漂移。
- Evaluator 报告 P1 或 unresolved P2。

## Review 更新步骤

更新 `review.md` 和 `review.zh.md`，记录 changed files、exact commands、test results、
compatibility review、scope review、unresolved findings 和 final assessment。
