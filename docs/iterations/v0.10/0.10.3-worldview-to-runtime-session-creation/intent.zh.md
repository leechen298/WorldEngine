# Intent

## Problem / Purpose

用户需要把 worldview premise 转成 session unit。现有 worldview generation 已返回 public
generated-world data，`0.10.2` 也已创建 session，但两者尚未连接。

## Why Now

`0.10.2` 已创建 session identity/status。下一步是在 `0.10.4` 接入 bounded runtime 前，
从 worldview input 创建 session。

## Relationship To Roadmap

本包只实现 `0.10.3` planned slice。`0.10.4` 负责 session run/snapshot evidence，
`0.10.5` 负责 dashboard flow。

## Non-Goals

- 不声明 live provider quality。
- 不执行 runtime 或创建 snapshot。
- 不做 dashboard UI。
- 不实现 Validation Client 或 checker。

## Expected Handoff

`0.10.4` 接收携带 public generation metadata 的 sessions，并在后续用 bounded runtime controls
驱动。
