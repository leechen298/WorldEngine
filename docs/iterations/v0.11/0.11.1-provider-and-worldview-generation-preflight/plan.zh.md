# Plan

英文版本：`plan.md`。

1. 创建并评审 package docs。
2. 只有 evaluator PASS 后，才设置 `implementation_authorized: yes`。
3. 新增 provider/worldview preflight schema。
4. 新增 `POST /provider/worldview-preflight`。
5. 新增 manifest discovery entry。
6. 增加 focused backend tests。
7. 运行 focused backend tests 和 `git diff --check`。
8. 记录 review evidence，并请求 implementation closeout evaluator。
9. 如果 PASS，将 v0.11 route 推进到 `0.11.2-structured-world-rules-and-parameters`。
