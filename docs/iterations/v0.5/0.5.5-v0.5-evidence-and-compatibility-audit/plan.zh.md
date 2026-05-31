# 计划

状态：review complete

## 步骤

1. 读取已完成的 v0.5 child package reviews。
2. 创建 evidence index 和 compatibility audit。
3. 运行 documentation checks、scope guard、forbidden-surface sentinel、focused backend
   compatibility 和 full backend regression。
4. 记录 unresolved finding classification。
5. 运行只读 evidence/compatibility evaluator。
6. 如果 evaluator 通过，将 `0.5.5` 标记为 review complete 并交接给 `0.5.6`。

## 停止条件

- 缺少 docs 或 mirrors 时停止。
- Parent/child status stale 时停止。
- Implemented surfaces 缺少 current-session evidence 时停止。
- 存在 unresolved P1/P2 时停止。
- Audit 试图扩展为 implementation、RC declaration 或 final release 时停止。

## 交接条件

- Evidence index 完整。
- Compatibility audit 完整。
- Current verification commands 已记录。
- 无 unresolved P1/P2。
- Evaluator PASS 已记录。
- Parent status surfaces 指向 `0.5.6`。
