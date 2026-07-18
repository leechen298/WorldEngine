# Technical Design

## Documentation Structure

本 documentation-only package 在以下目录创建标准 package file set：

```text
docs/iterations/v0.10/0.10.0-mvp-debug-session-planning-and-v0.9-handoff/
```

因为本包改变 routing、evidence 和 process semantics，所以包含 `README`、`intent`、
`contract`、`technical-design`、`test-plan`、`plan`、`review` 的中英文镜像。

## Affected Files

允许的 package-local files：

- `README.md`
- `README.zh.md`
- `intent.md`
- `intent.zh.md`
- `contract.md`
- `contract.zh.md`
- `technical-design.md`
- `technical-design.zh.md`
- `test-plan.md`
- `test-plan.zh.md`
- `plan.md`
- `plan.zh.md`
- `review.md`
- `review.zh.md`

允许的 parent status files：

- `docs/iterations/v0.10/README.md`
- `docs/iterations/v0.10/README.zh.md`
- `docs/iterations/v0.10/v0.10-plan.md`
- `docs/iterations/v0.10/v0.10-plan.zh.md`
- `docs/iterations/v0.10/GOAL_RUNNER.md`
- `docs/iterations/v0.10/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.10/CURRENT_STATE.md`
- `docs/iterations/v0.10/CURRENT_STATE.zh.md`
- `docs/iterations/v0.10/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.10/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.10/review.md`
- `docs/iterations/v0.10/review.zh.md`

## Data / Control Flow

本包只改变 documented goal route：

```text
v0.10-parent-documentation-ready-for-review
-> 0.10.0 review complete
-> 0.10.1-mvp-public-manifest-and-debug-handoff-documentation-package-needed
```

不改变 runtime data flow、API control flow、frontend state flow、checker flow 或 external
Validation Client flow。

## Compatibility Strategy

- 保持 parent planned-package specs 作为 future route-map inputs。
- 只将 `0.10.0` 标为 review complete。
- 将 `0.10.1` 标为 documentation-package-needed，而不是 implementation-ready。
- 保持所有 authorization fields 关闭。
- 保留 v0.9 BLOCKED 状态，不改写 earlier evidence。

## Anti-Drift Rules

- 不用本包夹带 code、tests、fixtures、checker assets、generated results、provider
  configuration 或 Validation Client behavior。
- 不把后续 `0.10.1` implementation 描述为已 review。
- 不让 external client 成为 provider calls、world generation、runtime mutation 或
  evaluator authority 的 owner。
- replay 或 worldline branches 不使用 parent/source-world wording。
- 不声明本包实际运行过的 documentation checks 之外的任何 current-session runtime behavior。
