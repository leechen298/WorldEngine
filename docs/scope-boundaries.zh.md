# Scope Boundaries

Status: authoritative boundary guide

英文版本：`scope-boundaries.md`。

## Global Rules

- WorldEngine 必须与 `docs/project-north-star.md` 保持一致。
- 第一款 game surface 不能把 engine 重新定义成 village-game backend。
- Tiny Village 可以提前作为 reference fixture 或 acceptance target 使用，但在 iteration
  contract 明确允许之前，不能变成 game-specific runtime logic。
- Code work 必须限定在一个 iteration package 内。
- Schema changes 必须 additive，除非当前 contract 允许 breaking changes。
- Runtime behavior 必须保留，除非当前 contract 明确改变它。

## v0.2 Does

v0.2 Recursive World Foundation 可以：

- 增加 north star 和 documentation governance。
- 在 schema/spec layer 定义 WorldCell 和 WorldSpec。
- 定义 EntityRef 等 shared references。
- 增加 optional event structure fields。
- 增加 reference WorldSpec fixture。
- 标记 `backend/worldengine/` 为 legacy。
- 保留现有 runtime behavior。

## v0.2 Does Not

v0.2 不能：

- 完整迁移 RuntimeEngine 到 WorldCell。
- 把 Agent inner-world 实现为 WorldCell。
- 实现完整 world generation。
- 实现 village game runtime。
- 创建单独的 game repository。
- 增加 vector memory。
- 增加 multi-agent society simulation。
- 实现 Agent pseudo-self continuity。
- 修改 frontend dashboard，除非 iteration contract 明确要求。

## Future Boundaries

- v0.3 可以把 WorldSpec 桥接进 runtime loading。
- v0.4 可以加入 minimal agent-in-world loop。
- v0.5 可以加入 memory 和 self-continuity。
- v0.6 可以加入 world generation v1。
- v0.7 可以构建 reference village world。
- v0.8 可以开始 first game surface。
