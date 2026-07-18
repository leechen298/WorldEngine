# Plan

英文源文件：`plan.md`。

1. 读取 parent v0.12 current state、goal runner、campaign plan、v0.12 plan 和 `0.12.0`
   handoff。
2. 读取现有 Agent loop、perception、action adapter、session store、session routes、manifest
   route 和相关 tests。
3. 完成本 package document set 并运行 documentation checks。
4. 请求 documentation / contract evaluator review。
5. 如果 PASS，只为本 package 记录 `implementation_authorized: yes`。
6. 增加 session Agent list/read/step、client-scripted-action rejection、public evidence、
   redaction boundary 和 manifest discovery 的 focused tests。
7. 实现最小 additive session Agent state 和 runtime loop。
8. 运行 `test-plan.md` 中的 focused backend verification。
9. 请求 implementation-scope evaluator review。
10. 在本 package scope 内修复任何 P1/P2 findings。
11. 如果 verification 和 evaluator review 通过，更新 package 和 parent v0.12 route 到
    `0.12.2-agent-memory-and-rest-consolidation-mvp-documentation-package-needed`。
