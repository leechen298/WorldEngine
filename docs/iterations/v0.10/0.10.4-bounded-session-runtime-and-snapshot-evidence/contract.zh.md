# Contract

英文版本：`contract.md`。

## Public API Contract

新增 additive endpoints：

- `POST /sessions/{session_id}/run`
- `POST /sessions/{session_id}/pause`
- `POST /sessions/{session_id}/resume`
- `GET /sessions/{session_id}/snapshots`

`POST /sessions/{session_id}/run` 接收现有 bounded `RuntimeRunRequest` shape。如果 request
同时缺少 `ticks` 和 `duration_seconds`、两者都提供，或超过 guard fields，仍应 invalid。

未知 session id 返回现有 public 404 envelope。

## Session Evidence Contract

Run responses 只包含 public evidence：

- session id。
- run status 和 stop reason。
- runtime start/end tick 和 world time。
- ticks executed。
- event count before/after 和 event delta count。
- snapshot count before/after 和 snapshot delta count。
- run window 内创建或可见的 snapshot ids。
- timeline label 使用 branch-ready wording，不含 parent/source hierarchy。
- runtime summary 继承的 guard summary 和 cost counters。

Snapshot list responses 必须 public、bounded、redacted。可以暴露 snapshot ids、tick ids、
world time、created_at、runtime state 和 public params。

## Compatibility Contract

现有 `/runtime/state`、`/runtime/step`、`/runtime/run`、`/runtime/pause` 和 `/runtime/resume`
endpoints 必须保持兼容。Session-scoped routes 包装同一个 in-memory runtime engine；本包不创建
durable 或 multi-runtime architecture。

## Forbidden Claims

本包不得声明：

- live provider pass。
- external checker pass。
- dashboard pass。
- durable persistence。
- Agent autonomous behavior。
- 带 parent/source worlds 的 replay hierarchy。
