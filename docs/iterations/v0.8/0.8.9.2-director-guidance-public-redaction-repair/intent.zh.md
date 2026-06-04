# Intent

英文版本：`intent.md`。

## Problem

第一次正式 `worldengine-full-lifecycle-autonomous` run 已覆盖 world creation、
runtime progression、Agent action evidence 和 director guidance，但在 evidence
integrity 失败。saved-result checker 拒绝结果，因为
`world-lifecycle-summary.json` 记录：

```text
evidence_integrity.redaction_scan_passed: false
```

failure analysis 指向 public director guidance output：它通过命名 private Agent
memory、goals、relationship internals、`self_state`、hidden context 等
private/internal markers 来说明没有 mutation，导致 public evidence 被保守 redaction。

## Why Now

`0.8.9.1` 已经让 WorldEngine public handoff contract 可用。下一次 full
lifecycle validation 已经能跑到 director guidance surface，并且只在 public
evidence redaction 上失败。这个 public wording 问题是下一步必须修复的
WorldEngine-side blocker。

## Relationship To Roadmap

本 package 支持 v0.8 目标：为 external validation 准备 public core-side surfaces，
但不把 external validation logic、external app code 或 concrete validation content
移入本仓库。

## Non-Goals

- 不实现 Validation Client behavior。
- 不放松 autonomous checker 来掩盖真实 public-evidence leak。
- 不移除 director guidance surface。
- 不 mutate Agent private memory、goals、identity、relationships、self-state 或
  private validation internals。
- 不添加 concrete demo-world fixtures、seed data、characters、maps、locations、
  resources 或 story rules。
- 没有当前 checker PASS 时，不声明 full lifecycle autonomous validation PASS。

## Expected Handoff

review approval 后，implementation 应更新 public response 和 focused tests，然后重跑
documented verification。如果当前环境不能重跑 full lifecycle run，review 必须记录
blocker，且只能声明更窄的 focused repair evidence。
