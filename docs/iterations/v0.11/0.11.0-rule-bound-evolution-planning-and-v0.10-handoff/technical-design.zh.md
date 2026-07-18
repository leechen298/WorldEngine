# Technical Design

英文版本：`technical-design.md`。

这是 documentation-only package，没有 runtime technical design。

## Affected Files

允许影响的文件：

- `docs/iterations/v0.11/0.11.0-rule-bound-evolution-planning-and-v0.10-handoff/*`
- `docs/iterations/v0.11/README.md`
- `docs/iterations/v0.11/README.zh.md`
- `docs/iterations/v0.11/CURRENT_STATE.md`
- `docs/iterations/v0.11/CURRENT_STATE.zh.md`
- `docs/iterations/v0.11/GOAL_RUNNER.md`
- `docs/iterations/v0.11/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.11/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.11/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.11/v0.11-plan.md`
- `docs/iterations/v0.11/v0.11-plan.zh.md`
- `docs/iterations/v0.11/review.md`
- `docs/iterations/v0.11/review.zh.md`

Backend、frontend、schema、provider、checker、fixture、migration 或 Validation Client
文件不在范围内。

## Route Update Design

评审前，parent v0.11 可以保持 `v0.11-parent-documentation-ready-for-review`，也可以指向本包。
评审通过后，parent v0.11 应选择：

```text
0.11.1-provider-and-worldview-generation-preflight-documentation-package-needed
```

Implementation authorization 保持关闭。
