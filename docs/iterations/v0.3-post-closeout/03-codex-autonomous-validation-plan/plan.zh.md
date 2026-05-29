# 计划

## 执行步骤

1. 读取父级 campaign 文档。
2. 读取 v0.3 release 和 evidence docs。
3. 读取 loader、bridge、RuntimeEngine、WorldCell、Event 和聚焦测试。
4. 定义 reviewer inputs。
5. 定义 reviewer commands。
6. 定义 unsupported-claim checks。
7. 定义 loader、bridge、RuntimeEngine、Event.refs、API / schema / runtime
   compatibility 检查。
8. 定义 concrete demo-world regression check。
9. 定义 blocker 和 finding 分类。
10. 交接给 `04-codex-autonomous-validation-execution`。

## 阶段边界

本包只规划 autonomous review，不执行。

## 停止条件

出现下列情况时停止：

- 必需 reviewer inputs 缺失。
- 计划依赖实现者总结。
- 计划授权代码变更。
- 计划把 autonomous validation 写成已经成功。
- 计划改变 v0.3 发布状态。

## Review 更新步骤

更新 `review.md`，记录 changed files、未运行命令、no-test rationale、scope review、
compatibility review 和最终评估。
