# Campaign Plan

英文版本：`CAMPAIGN_PLAN.md`。

状态：`child package documentation review in progress`

## 目标

把 v0.11 作为 review-gated `/goal` campaign 运行，让 MVP 世界通过 rules、directions、
events、diffs 和 fidelity evidence 演化。

本 campaign 的目标是让 WorldEngine 能够：

- 诚实分类 provider/worldview generation mode。
- 把 public structured rules 和 parameters 附着到 session。
- 把 natural-language direction 作为 world-level guidance 入队。
- 在 bounded runtime 中生成或选择 legal events。
- 应用带 replay evidence 的 public diffs。
- 在 bounded runtime 前后检查 worldview fidelity。

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
- `docs/iterations/v0.10/v0.10-plan.md`

## Campaign Rules

- v0.11 必须从 v0.10 session/debug handoff evidence 出发。
- planned `0.11.x` sections 不授权 implementation。
- 用户 direction 必须是 bounded world-level guidance。
- 用户 direction 必须留在世界外：不得投放物品、直接触发细节事件或下达 final-fact commands。
- 每个 applied event/diff 都必须有 public legality evidence。
- Validation Client 保持外部，只消费 evidence。
- MVP claims 需要 current-session command evidence。

## Campaign Exit Criteria

v0.11 只有在以下条件满足时才能 close：

- active child packages review complete 或明确 deferred。
- provider/worldview mode 被诚实分类。
- rules 和 parameters 是 public structured。
- user direction 不能直接施加 final facts。
- direction examples 证明 direct death commands 会被拒绝，而 lightning-risk guidance 仍只是
  external pressure。
- events 和 diffs rule-linked 且可 replay。
- worldview fidelity 可以从 public evidence 评估。
- 没有未接受理由的 P1/P2 finding。

## Handoff

如果 v0.11 以 PASS 或可接受 PARTIAL 收口，v0.12 从 rule-bound running world 出发，
增加 Agent continuity 和完整 Validation Client automation。
