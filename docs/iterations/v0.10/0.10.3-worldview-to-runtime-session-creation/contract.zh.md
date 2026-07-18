# Contract

## Public Concepts

- `worldview_session_creation`：从 public worldview input 和 redacted generation output
  创建 session。
- `session_generation_summary`：public generation status、mode、provider class、fallback
  labels、generation id 和 premise digest。
- `runtime_ready_session`：public generated model 已附着到 session，足以后续 runtime package
  检查；不是已经运行过的 session。

## Compatibility Requirements

- 现有 `/sessions` create/list/read/status behavior 保持兼容。
- 现有 `/world/generation/worldview` behavior 保持兼容。
- 需要 live call 的 provider configured states 必须保持 `blocked`，不得静默执行。
- fallback 必须标记 deterministic 或 safe mock，并标明 non-live。

## Allowed Changes

- 扩展 session schemas/store/routes，支持 worldview session creation。
- 复用现有 worldview generation helper。
- 更新 manifest 和 focused tests。
- 更新 package 和 parent v0.10 docs/reviews。

## Forbidden Changes

- 不执行 live provider calls。
- 不运行 runtime ticks、创建 snapshots、写 generated results、添加 dashboard UI、修改 checker
  fixtures、实现 Validation Client behavior、添加 persistence/migrations 或修改
  `backend/worldengine/`。

## North Star Check

本包保持 WorldEngine 拥有 provider/generation，同时只向 client 暴露 redacted public session
evidence。

## Out-of-Scope Follow-ups

- `0.10.4`：bounded runtime and snapshot evidence。
- `0.10.5`：dashboard MVP session flow。
