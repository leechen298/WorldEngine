# 计划

状态：review complete

1. 确认 `0.6.8` 已 review complete，且无 unresolved P1/P2 finding。
2. 创建 release-candidate package docs 和中文 mirrors。
3. 更新 parent status surfaces 为 `0.6.9 ready for review`，implementation
   authorization 保持关闭。
4. 运行 documentation、scope、required-term、mirror 和 status checks。
5. 请求 read-only release-candidate evaluator。
6. 如果 evaluator 报告无 P1/P2 finding，则把本 package 标记为 review complete。
7. 交接给 `0.6.10-v0.6-final-closeout`。

## 停止条件

- 如果 `0.6.8` 有 unresolved P1/P2 findings，则停止。
- 如果 status surfaces drift 或暗示 final release，则停止。
- 如果 release-candidate text 声明未运行 validation 或 product readiness，则停止。
- 如果本 package 修改任何 implementation file，则停止。
