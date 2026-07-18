# Contract

## Public Concepts

- `world_session`：public MVP runtime unit，包含稳定 `session_id`、关联 `world_id`、
  public lifecycle status、runtime reference、event count、snapshot count 和 timestamps。
- `session_status`：`created`、`ready`、`blocked` 或 `closed`。
- `session_runtime_ref`：当前 runtime tick/time 的 public reference，不是 private runtime object。
- `session_evidence_refs`：与 session 关联的 events 和 snapshots 的 public counts 或 ids。

## Compatibility Requirements

- 现有 `/worlds`、`/runtime/*`、`/world/events`、`/manifest` 和 provider surfaces 保持
  additive-compatible。
- Session payloads 不得暴露 raw prompts、provider traces、secrets、private Agent memory、
  hidden context 或 private evaluator data。
- Session store 仅为 process-local in-memory，不承诺 persistence。
- Manifest updates 必须诚实描述仍属于 future scope 的 session runtime/run/snapshot capabilities。

## Allowed Changes

- 在 allowed file list 中添加 session schema/store/router 和 focused tests。
- 在 app factory 注册 session router。
- 更新 manifest surfaces for session create/list/read/status。
- 更新 package 和 parent v0.10 docs/reviews。

## Forbidden Changes

- 不实现 session run controls、bounded runtime wrappers、snapshot generation、worldview
  generation、dashboard UI、durable storage、migrations、checker fixtures、provider live
  calls、Validation Client code、generated results、external validation 或
  `backend/worldengine/`。
- 不声明 create/list/read/status 之外的 runnable session flow PASS。

## North Star Check

本包定义 reusable public session unit，而不是 application-specific state 或 external-client-owned
behavior，保持 WorldEngine generic。

## Out-of-Scope Follow-ups

- `0.10.3`：create sessions from worldview input。
- `0.10.4`：run sessions and collect snapshot evidence。
- `0.10.5`：dashboard session flow。
