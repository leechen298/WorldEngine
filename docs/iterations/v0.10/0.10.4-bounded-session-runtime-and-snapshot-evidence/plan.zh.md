# Plan

英文版本：`plan.md`。

1. 创建完整 package docs 和 mirrors。
2. 运行 documentation completeness 和 whitespace checks。
3. 请求 read-only evaluator review。
4. 如果 PASS，记录 `implementation_authorized: yes`。
5. 为 session run/pause/resume/snapshot behavior 添加 focused failing tests。
6. 实现最小 scoped backend changes。
7. 运行 focused 和 expanded focused backend tests。
8. 请求 implementation closeout evaluator review。
9. 更新 package 和 parent v0.10 review/current-state handoff。

如果 documentation gate 有 unresolved P1/P2 findings，或 implementation 需要超范围 runtime
architecture、persistence、external validation、provider calls、dashboard work 或
`backend/worldengine/` changes，则在 implementation 前停止。
