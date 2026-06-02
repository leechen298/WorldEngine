# Intent

## Problem

v0.7 parent docs 已定义完整 `/goal` campaign，但 parent roadmap 故意只把 `0.7.x` 条目作为
planned package specs。为了在不绕过 iteration gates 的情况下继续推进 goal，第一个 planned child
必须先成为具体、可 review 的 package，然后才能启动后续 public contract 或 implementation work。

## Goal

创建并 review `0.7.0` documentation-only baseline package。成功状态是一个已 review 的 child
package，确认 v0.7 campaign controls、v0.6 handoff boundaries、external-validation boundaries、
projection consumer boundaries、verification expectations，以及向 `0.7.1` 的 handoff。

## Why Now

`完成 v0.7` 必须先具备确定性 route selection。Parent review 已确认 v0.7 campaign docs 内部一致，
但 campaign 不能进入后续 children，直到第一个 child package 存在并通过自己的 review gate。

## Relationship To Roadmap

v0.7 通过 public contracts、redacted reports、readiness manifests 和 compatibility evidence 准备
WorldEngine 的 external validation readiness 和 projection consumer readiness。本 child 为该序列提供
documentation baseline，不实现后续 contract、checker、manifest、projection 或 regression work。

## Non-goals

- 不实现 `0.7.1` public readiness contracts。
- 不实现 `0.7.2` report schema 或 redaction checker support。
- 不实现 `0.7.3` readiness manifest 或 contract bundle support。
- 不实现 `0.7.4` projection consumer read models。
- 不运行或声明 v0.7 product validation、external suite pass、Agent smoke、autonomous、E2E、
  frontend、API、runtime 或 release readiness。
- 不修改 runtime、schema、API、frontend、tests、checkers、fixtures、migrations、external
  repositories、generated results 或 legacy `backend/worldengine/` code。

## Expected Handoff

Review 通过后，`0.7.0` 交接给 `0.7.1-public-validation-and-projection-contracts`。该 handoff
仍是 documentation-only，表示 `0.7.1` 可以定义 public validation 和 projection contract semantics，
但仍必须创建或确认自己的完整 package docs，并先通过 review，后续 implementation 才可能被授权。

## North Star Alignment

本 package 保持 WorldEngine 作为通用 recursive world generation and runtime engine。它准备 public
readiness boundaries，但不把 core repository 变成 product-specific validation app 或 projection
application。
