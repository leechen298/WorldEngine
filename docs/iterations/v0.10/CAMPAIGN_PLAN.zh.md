# Campaign Plan

英文版本：`CAMPAIGN_PLAN.md`。

状态：`closeout PASS / handed off to v0.11`

## 目标

把 v0.10 作为 review-gated `/goal` campaign 运行，用来创建 MVP debug contract 和第一条
runnable world session。

本 campaign 的目标是让 WorldEngine 能够：

- 从 worldview input 创建 session。
- 暴露正确的 MVP manifest 和 checker handoff skeleton。
- 把 initial public world state 加载到 runtime。
- 用 bounded controls 运行 session。
- 记录 events、diffs 和 snapshots。
- 保持 replay/worldline branch terminology 为类似代码分支的时间线分支，而不是
  parent/source-world relationships。
- 在 dashboard 中展示该流程。
- 暴露足够 public discovery/evidence 给 external client 调试。

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
- `docs/iterations/v0.9/CURRENT_STATE.md`
- `docs/iterations/v0.9/v0.9-plan.md`

## Campaign Rules

- Parent `v0.10` docs 是 campaign entrypoint。
- `v0.10-plan.md` 中的 planned `0.10.x` sections 不授权 implementation。
- code/mixed children 必须先有完整 package docs 并通过 review。
- Validation Client 保持外部仓库身份。
- 用户/玩家保持为外部操作者；v0.10 不得实现 player-as-world-entity gameplay、投放物品或直接触发细节事件。
- MVP claims 必须有 current-session command evidence。
- 中文镜像必须保留 status、scope、forbidden changes、compatibility constraints、
  findings 和 final assessment 语义。

## Campaign Exit Criteria

v0.10 只有在以下条件满足时才能 close：

- active child packages review complete 或明确 deferred。
- worldview 可以创建 runnable session。
- bounded run controls 和 snapshots 有证据。
- dashboard create/run/inspect flow 有证据。
- manifest 或 public discovery 标识 session surfaces，并诚实保留 blocked/not_run/pass/fail
  status。
- 没有未接受理由的 P1/P2 finding。

## Handoff

如果 v0.10 以 PASS 或可接受 PARTIAL 收口，v0.11 从 runnable session 出发，继续增加
rule-bound world evolution。Living Agent continuity 仍属于 v0.12。
