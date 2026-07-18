# Plan

英文版本：`plan.md`。

1. 创建并评审 package docs。
2. 只有 evaluator PASS 后，才设置 `implementation_authorized: yes`。
3. 扩展 session schema/store，加入 rule summary 和 validation result。
4. 新增 session rule attach/read endpoints。
5. 更新 manifest discovery。
6. 增加 focused backend tests。
7. 运行 focused backend tests 和 `git diff --check`。
8. 记录 evidence，并请求 closeout evaluator review。
9. 如果 PASS，路由到 `0.11.3-natural-language-direction-queue-and-boundary`。
