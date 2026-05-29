# 计划

## 执行步骤

1. 读取父级 campaign 文档和 v0.3 source inputs。
2. 确认本包只做规划。
3. 定义仓库和文档检查。
4. 定义后端确定性检查。
5. 定义聚焦 WorldSpec loader 验证。
6. 定义聚焦 runtime context bridge 验证。
7. 定义 event API 和 Event.refs compatibility 验证。
8. 定义 API smoke 检查。
9. 定义 E2E framework 可用性探测。
10. 只在已配置时定义 browser E2E 执行。
11. 定义 E2E 不可用时的 fallback。
12. 定义 v0.3 release claim 和 compatibility claim review。
13. 定义 concrete demo-world regression 检查。
14. 更新 `review.md`，记录 docs-only 证据。

## 阶段边界

本包只到 review-ready docs 为止。实际执行只在 `02-e2e-validation-execution` 中开始。

## 停止条件

出现下列情况时停止：

- 必需 v0.3 source files 缺失。
- 计划需要实现变更。
- 计划引入 demo-world details 或 private oracle details。
- 计划预填成功验证结果。
- 计划改变 v0.3 发布状态。

## Review 更新步骤

在 `review.md` 中记录 changed files、files read、未运行命令、no-test rationale、
compatibility review、scope review、未解决 P1/P2/P3 和最终评估。
