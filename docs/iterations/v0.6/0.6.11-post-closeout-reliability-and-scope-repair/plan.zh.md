# 计划

状态：review complete

## 步骤

1. 创建本 post-closeout repair package，并在 review 前保持 implementation authorization closed。
2. 运行或记录 documentation/contract evaluator checkpoint。
3. 如果没有 P0/P1/blocking P2，则更新 review evidence 为
   `implementation_authorized: yes`。
4. 为 fallback digest seed preservation 添加失败回归测试。
5. 为 sensitive imported-plan provenance failure 添加 public preview API 覆盖。
6. 修改 fallback digest payload，保留可 canonical 的 seed material。
7. 运行 `test-plan.md` 中的 focused backend tests，以及更广的
   backend/frontend/E2E/checker verification。
8. 用准确证据更新 reliability result、parent review、implementation summaries 和 package
   review。
9. 只有当 scope guard 为零且所有 P1/P2 blockers 已解决或被 review 明确接受时，才能把最终
   verdict 从 partial pass 改为 clean pass。

## 停止条件

- documentation/contract evaluator 报告 P0/P1 或 blocking P2。
- scope guard 无法在不扩大 package contract 的情况下达到 `out_of_scope=0`。
- backend/API P2 无法在 allowed file set 内修复。
- verification 失败且无法在本 package 内做 root-cause repair。
