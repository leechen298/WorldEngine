# 计划

状态：review complete

## 步骤

1. 读取 `0.5.5` audit 和 child package reviews。
2. 创建 release-candidate bundle documents 和 mirrors。
3. 运行 docs/mirror/scope/status-boundary checks。
4. 记录 implementation tests 继承自 fresh `0.5.5` audit evidence；除非 evaluator 要求，
   本 package 不重跑。
5. 运行只读 release-candidate bundle evaluator。
6. 如果 evaluator 通过，将 package 标记为 review complete 并交接给 `0.5.7`。

## 停止条件

- 缺少 bundle docs 或 mirrors 时停止。
- 出现 out-of-scope implementation changes 时停止。
- 文案声明 final release 时停止。
- Evidence stale 或 missing 时停止。
- 存在 unresolved P1/P2 时停止。

## 交接条件

- Bundle docs 和 mirrors 存在。
- Bundle status 是 prepared for review，不是 final。
- Evidence 和 compatibility references 与 `0.5.5` 一致。
- Evaluator PASS 已记录。
- Parent status surfaces 指向 `0.5.7`。
