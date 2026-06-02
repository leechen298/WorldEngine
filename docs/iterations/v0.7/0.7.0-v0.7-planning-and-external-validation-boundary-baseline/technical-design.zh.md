# Technical Design

## Current State

v0.7 parent package 位于 `docs/iterations/v0.7/`，并已通过 read-only parent review。在本
package 之前，parent state 记录 active child 为 none，且没有 implementation authorization。
`v0.7-plan.md` 中 planned `0.7.x` entries 只是 roadmap-level package specs。

`AGENTS.md` 和 `AGENTS.zh.md` 等 root guidance files 不在本 child package 的 allowed changes 中。
如果它们在未来 run 中处于 dirty 状态，除非用户明确授权该 scope，否则必须视为 separate user work。

## Documentation Structure

本 child 创建具体 package directory：

```text
docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline/
```

该目录包含完整 package set 和中文镜像：

```text
README.md
intent.md
contract.md
technical-design.md
test-plan.md
plan.md
review.md
README.zh.md
intent.zh.md
contract.zh.md
technical-design.zh.md
test-plan.zh.md
plan.zh.md
review.zh.md
```

## Affected Files

Allowed child files:

- `docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline/**`

Allowed parent status surfaces:

- `docs/iterations/v0.7/README.md`
- `docs/iterations/v0.7/README.zh.md`
- `docs/iterations/v0.7/v0.7-plan.md`
- `docs/iterations/v0.7/v0.7-plan.zh.md`
- `docs/iterations/v0.7/GOAL_RUNNER.md`
- `docs/iterations/v0.7/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.7/CURRENT_STATE.md`
- `docs/iterations/v0.7/CURRENT_STATE.zh.md`
- `docs/iterations/v0.7/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.7/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.7/review.md`
- `docs/iterations/v0.7/review.zh.md`

## Control Flow

1. `GOAL_RUNNER.md` 将 `完成 v0.7` route 到 `CURRENT_STATE.md`。
2. `CURRENT_STATE.md` 指向 active `0.7.0` child。
3. Agent 按 required order 读取 child package。
4. 因为本 package 是 documentation-only，agent 只运行 documentation verification 和 read-only
   evaluator review。
5. 如果没有 P1/P2，则 package 可以 hand off 给 `0.7.1`；否则保持 review 状态或记录
   blocker。

## Data Model / Schema Changes

无。本 package 不得改变 runtime data models、API schemas、report schemas、checker schemas、
database schemas、persistence、migrations、frontend models 或 external runner result schemas。

## Runtime / Service Design

无。No runtime service、API route、checker implementation、frontend behavior 或 test implementation
changes are authorized。

## Compatibility Strategy

- 将 v0.6 evidence 仅视为 historical handoff context。
- 保持所有 current implementation behavior 不变。
- 在每个 child package 被创建或确认并通过 review 前，planned child package specs 仍然
  non-authoritative。
- 保持 implementation authorization closed。

## Anti-Drift Rules

- Status surfaces 必须在 active child、route 和 implementation authorization 上一致。
- Review evidence 必须区分 current-session checks 与 historical evidence。
- Chinese mirrors 必须保留 status、type、goal、scope、forbidden changes、compatibility
  constraints、findings 和 final assessment semantics。
- 任何 out-of-scope file change 必须分类为 pre-existing user work，或从 package scope 中移除。

## Risks

- Parent status 可能与 child package status 漂移。
- Documentation 可能暗示 implementation authorization。
- Historical v0.6 evidence 可能被提升为 current v0.7 pass evidence。
- Dirty root guidance files 可能被意外纳入 package。
- Chinese mirrors 可能弱化 blocking restriction 或 final-assessment nuance。

Test plan 通过 status checks、required-file checks、scope guards、mirror checks 和
subagent/evaluator review 检测这些风险。
