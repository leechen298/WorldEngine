# 计划

状态：final / closeout complete

## 步骤

1. 创建 final closeout package docs 和 mirrors。
2. 运行 final docs/mirror/scope checks。
3. 运行 final focused backend compatibility。
4. 运行 final full backend regression。
5. 记录 final evidence、skipped checks、compatibility review、scope review 和 unresolved findings。
6. 运行 closeout consistency evaluator。
7. 如果 evaluator 通过，同步 final status surfaces 和 roadmap。
8. Status synchronization 后重跑 final lightweight consistency checks。

## 停止条件

- 缺少 docs 或 mirrors 时停止。
- 出现 out-of-scope file changes 时停止。
- Backend verification 失败时停止。
- 存在 unresolved P1/P2 时停止。
- 在 evaluator approval 前应用 final status 时停止。
- Final wording 声称未运行的 frontend、E2E、Agent smoke、autonomous 或 external validation readiness 时停止。

## 交接条件

- Final verification 通过。
- Closeout consistency evaluator 通过。
- v0.5 parent status surfaces 已同步。
- roadmap v0.5 status 已同步。
- final review 记录无 unresolved P1/P2。
- Final verification 后创建 commit。
