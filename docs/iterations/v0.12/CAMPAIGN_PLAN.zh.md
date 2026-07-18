# Campaign Plan

英文版本：`CAMPAIGN_PLAN.md`。

状态：`closeout complete / PARTIAL`

## 目标

把 v0.12 作为 review-gated `/goal` campaign 运行，通过 visible Agent continuity 和
checker-backed Validation Client automation 完成 MVP。

本 campaign 的目标是让 WorldEngine 能够：

- 在 runtime 中产生 public Agent state 和 actions。
- 保留 public memory summaries 和 consolidation evidence。
- 暴露 read-only 小说式 narrative 和 diagnostic inspection surfaces。
- 保持 narrative 和 diagnostic conversation 在 canonical world timeline 与 Agent memory 之外。
- 为 external client 定义稳定 MVP evidence artifacts。
- 运行或分类 full lifecycle autonomous validation result。
- 用 evidence 把 MVP 关闭为 PASS、PARTIAL、BLOCKED 或 FAIL。

## Parent Drafting 已读取的权威输入

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/project-plan.md`
- `docs/project-plan.zh.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.9/README.md`
- `docs/iterations/v0.10/README.md`
- `docs/iterations/v0.11/README.md`
- `docs/iterations/v0.11/v0.11-plan.md`
- `docs/iterations/v0.11/v0.11-plan.zh.md`

## Campaign Rules

- v0.12 必须从 v0.11 rule-bound world evidence 出发。
- planned `0.12.x` sections 不授权 implementation。
- Agent autonomy 必须来自 WorldEngine public runtime state，而不是 client scripting。
- 文档和证据必须区分世界内 Agent 与 Codex、OpenClaw 等外部验证 Agent。
- Memory/consolidation evidence 只能是 public summaries。
- Narrative 和 diagnostic surfaces 默认 read-only，并且不得绕过 direction queue 引导后续世界演化。
- Complete MVP PASS 需要 checker、scorecard 和 read-only review evidence。

## Campaign Exit Criteria

v0.12 只有在以下条件满足时才能关闭 MVP：

- active child packages review complete 或明确 deferred。
- 存在 Agent observe/intent/action-or-rest/memory evidence。
- public/private redaction boundaries 通过。
- 没有 external validation agent 被记录成世界内 Agent 或玩家。
- Validation Client evidence handoff 已实现或诚实 blocked。
- full lifecycle checker/scorecard/review 对 result 完成分类。
- 没有未接受理由的 P1/P2 finding。

## Handoff

如果 v0.12 以 PASS 收口，项目拥有完整 MVP baseline。如果以 PARTIAL 或 BLOCKED 收口，
closeout 必须说明下一步属于 WorldEngine、WorldEngine-Validation-Client、provider/environment
setup，还是 testing/checker assets。
