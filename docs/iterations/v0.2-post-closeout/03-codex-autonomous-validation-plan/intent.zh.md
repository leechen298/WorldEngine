# Intent

状态：`planned / ready for review`

## 问题 / 目的

Post-closeout validation 需要独立 Codex review line。只复述 implementation summaries
的 reviewer 不能提供足够 evidence。

## 为什么现在做

autonomous validation instructions 必须先于 separate Codex run 存在，这样 reviewer 才知道
要读什么、运行什么、禁止修改什么，以及如何报告 unsupported claims。

## 与 Roadmap 的关系

本 validation 支撑后续 roadmap confidence，但不实现 WorldEngine Agent-in-World behavior。

## 非目标

- 本 package 不运行 autonomous validation。
- 不修改 code。
- 不接受 unverified claims。
- 不使用 private external validation details。

## 预期交接

`04-codex-autonomous-validation-execution/` 使用本 plan 来运行并验证 independent Codex
review。
