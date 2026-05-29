# Intent

状态：package complete / plan accepted current campaign

## 问题 / 目的

Post-closeout validation 需要一条独立的 Codex review 线。只复述 implementer summaries
的 reviewer 不能提供足够 evidence。

## 为什么现在做

当前 campaign 已通过 `02-e2e-validation-execution`。在 `04` 执行独立 review 前，需要先
接受 autonomous validation plan，让 reviewer 明确要读什么、运行什么、禁止修改什么，以及
如何报告 unsupported claims。

## 与 Roadmap 的关系

本 validation 用于增强后续 roadmap 的可信度，但不实现 WorldEngine Agent-in-World
behavior。

## 非目标

- 本 package 不运行 autonomous validation。
- 不修改 code。
- 不接受 unverified claims。
- 不使用 private external validation details。

## 预期交接

`04-codex-autonomous-validation-execution/` 使用本 plan 来运行并验证 independent Codex
review。
