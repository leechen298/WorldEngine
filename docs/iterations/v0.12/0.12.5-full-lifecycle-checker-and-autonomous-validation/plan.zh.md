# Plan

英文原文：`plan.md`。

1. 读取 v0.12 parent state、`0.12.4` handoff contract、existing autonomous checker、fixtures 和 result docs。
2. 起草 package docs，明确 validation/classification boundaries。
3. 运行 documentation gate checks。
4. 请求 documentation evaluator review。
5. 在 package scope 内修复 P1/P2 findings。
6. 如果 review 通过，只为 checker commands 记录 `evidence_execution_authorized: yes`。
7. 运行 `test-plan.md` 中的 deterministic autonomous fixture checker commands。
8. 检查当前 v0.12 external Validation Client result directory 是否存在。如果不存在，记录 fresh external validation 为 BLOCKED。
9. 创建 result docs：validation result、scorecard summary 和 read-only evaluator review。
10. 请求 result/classification 的 read-only evaluator review。
11. 修复 scope 内 P1/P2 findings，或记录 PARTIAL/BLOCKED/FAIL。
12. 更新 parent route 到 `0.12.6-mvp-release-candidate-and-closeout`。
