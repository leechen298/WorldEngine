# Plan

英文版本：`plan.md`。

1. 创建完整 package docs 和 mirrors。
2. 运行 documentation completeness 和 whitespace checks。
3. 请求 read-only evaluator review。
4. 如果 PASS，记录 `implementation_authorized: yes`。
5. 增加 focused frontend API/client/dashboard tests。
6. 实现最小 scoped dashboard/API-client changes。
7. 运行 frontend unit tests、frontend build、backend compatibility tests，并在环境允许时运行
   targeted E2E。
8. 请求 implementation closeout evaluator review。
9. 更新 package 和 parent v0.10 review/current-state handoff。

如果 docs gate 有 unresolved P1/P2 findings，或 implementation 需要 provider key UI、backend
feature expansion、Validation Client code、concrete demo assets 或 `backend/worldengine/`，
则在 implementation 前停止。
