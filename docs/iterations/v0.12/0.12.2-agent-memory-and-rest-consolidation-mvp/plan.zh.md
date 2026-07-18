# Plan

英文源文件：`plan.md`。

1. 读取 parent v0.12 current state、goal runner、campaign plan、v0.12 plan、`0.12.0`
   handoff 和 `0.12.1` closeout。
2. 读取现有 Agent memory schemas/store、session Agent runtime loop、session routes、manifest
   route 和相关 tests。
3. 完成本 package document set 并运行 documentation checks。
4. 请求 documentation / contract evaluator review。
5. 如果 PASS，只为本 package 记录 `implementation_authorized: yes`。
6. 新增 public memory read、working summary creation、rest consolidation、redaction、no
   personality/skill mutation、evidence refs 和 manifest discovery 的 focused tests。
7. 实现最小 additive public memory/consolidation path。
8. 运行 `test-plan.md` 中的 focused backend verification。
9. 请求 implementation-scope evaluator review。
10. 在本 package scope 内修复 P1/P2 findings。
11. 如果 verification 和 evaluator review 通过，更新 package 和 parent v0.12 route 到 parent
    `CURRENT_STATE.md` 记录的 active `0.12.3-narrative-and-diagnostic-inspection-surfaces`
    route。
