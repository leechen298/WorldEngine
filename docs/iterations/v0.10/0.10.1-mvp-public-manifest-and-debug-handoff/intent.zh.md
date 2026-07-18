# Intent

## Problem / Purpose

WorldEngine 已经暴露 public `/manifest`，但它仍带有旧版本语义，还没有清楚描述 v0.10
MVP debug handoff。后续 session、runtime、dashboard 和 validation work 不应依赖模糊的
discovery 或 status vocabulary。

本包让 public manifest 对外部客户端调试变得诚实且有用，同时不把 client implementation
或 evaluator authority 移入 WorldEngine。

## Why Now

v0.10 从 public discovery 和 debug handoff 开始，然后才进入更深的 session features。
`0.10.0` 已关闭 planning/handoff baseline，并选择本包作为下一个 documentation gate。

## Relationship To Roadmap

roadmap 要求 v0.10 先对齐 public manifest/debug handoff contract，再创建第一条 runnable
session slice。本包只负责该对齐。World session storage 属于 `0.10.2`；worldview session
creation 属于 `0.10.3`；bounded session runtime 属于 `0.10.4`。

## Non-Goals

- 不实现 Validation Client behavior。
- 不实现 v0.10 sessions、runtime controls、dashboard flow 或 validation closeout。
- 不运行 provider live calls，也不声明 provider readiness PASS。
- 不修改 checker code 或 fixtures。
- 不暴露 raw prompts、raw provider payloads、secrets、private Agent state、hidden context
  或 private evaluator data。
- 不把 replay/worldline branches 描述成 parent/child worlds 或 source worlds。

## Expected Handoff

本包关闭后，`/manifest` 应足够稳定，使
`0.10.2-world-session-contract-and-state-store` 能添加真实 session surfaces，而无需重新定义
status taxonomy、provider ownership、redaction posture 或 external client role。
