# Current State

Campaign status：planned / ready for review
Active child package：none
Current route：parent documentation review
Implementation authorization：no
Evidence execution authorization：no

## Planned Package Roadmap Status

```text
0.8.0-v0.8-planning-and-v0.7-handoff-baseline: planned
0.8.1-minimum-working-state-contract: planned
0.8.2-core-observable-surface-boundary: planned
0.8.3-generation-runtime-agent-loop-readiness: planned
0.8.4-external-validation-handoff-contract: planned
0.8.5-core-working-state-smoke-evidence: planned
0.8.6-v0.8-evidence-and-boundary-audit: planned
0.8.7-v0.8-release-candidate-bundle: planned
0.8.8-v0.8-final-closeout: planned
```

当前没有 active v0.8 child package。`v0.8-plan.md` 中的 planned package entries
只是 route-map specifications，不授权 implementation。

## Handoff Risk

v0.7 route 是 historical `final / closeout complete`，但
`docs/testing/results/2026-06-02-v0.7-code-review.md` 记录了 post-closeout
issues。在 current-session evidence 修复这些 findings，或 active v0.8 package 把它们
记录为 blockers 之前，它们会阻断 clean pass、minimum working-state PASS、external
validation readiness PASS、product PASS 和 external consumer PASS。

Historical v0.7 和 v0.6 evidence 只能作为 handoff context。它不是 current v0.8
PASS evidence。

## Current Route

Current route：parent documentation review。

v0.8 parent docs 与 Chinese mirrors 已起草，等待 review。这个 parent state 之后的新工作
需要：

- review parent docs，然后创建或确认
  `0.8.0-v0.8-planning-and-v0.7-handoff-baseline`；或
- 用户明确请求某个 child package，并且仍然遵守 child package documentation gate。

## Current Exclusions

当前 v0.8 documentation 不声明：

- runtime behavior passed。
- API behavior passed。
- frontend behavior passed。
- E2E passed。
- Agent smoke passed。
- autonomous runner 或 autonomous suite passed。
- external validation PASS。
- external consumer PASS。
- minimum working-state readiness passed。
- product readiness passed。
- generation-quality passed。
- v0.7 blockers repaired。

## External Validation Boundary

WorldEngine 可以准备 external validation function 所需的 public core-side surfaces。
External validator、connection workflow、private scenarios、oracle logic、UI、app
repository 和 concrete validation content 都在本仓库之外，当前 parent state 不定义它们。

## Next Action

Review v0.8 parent documentation。Parent review 后，在任何 child implementation 或
evidence execution 前，创建或确认
`0.8.0-v0.8-planning-and-v0.7-handoff-baseline` package。
