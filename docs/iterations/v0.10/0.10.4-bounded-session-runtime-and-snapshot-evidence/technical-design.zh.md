# Technical Design

英文版本：`technical-design.md`。

## Affected Files

- `backend/app/schemas/session.py`
- `backend/app/core/world_session.py`
- `backend/app/api/routes/session.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_world_session_api.py`
- `backend/app/tests/test_public_handoff_contract_api.py`
- `backend/app/tests/test_runtime_bounded_run.py`
- package 和 parent v0.10 docs/reviews。

## Design

在 `app.schemas.session` 中新增 session-specific response schemas：

- `SessionRunSummary`
- `SessionSnapshotListResponse`
- 如需要，增加小型 evidence/reference models。

扩展 `InMemoryWorldSessionStore`，提供 runtime actions 后刷新 session status 的 helpers。Store
仍是 process-local，不拥有 snapshot storage。

在 `app.api.routes.session` 实现 session runtime routes：

- 读取 session，未知则返回 `404`。
- run 前记录 event 和 snapshot counts。
- 调用现有 runtime engine bounded run/pause/resume methods。
- run 后记录 event 和 snapshot counts。
- 从现有 snapshot store 按 query params bounded list snapshots。
- 返回带 branch-ready timeline labels 的 public evidence summary。

更新 `app.api.routes.world` 的 manifest discovery：

- 测试通过后将 `/sessions/{session_id}/run`、`/pause`、`/resume` 和 `/snapshots`
  标记为 available/pass。
- dashboard 和 external validation surfaces 仍保持 planned/not_run。

## Redaction

run 或 snapshot payloads 不得包含 raw prompts、raw provider responses、provider traces、
secrets、private memory、hidden context 或 private evaluator data。继续复用现有 validation-error
sanitization behavior。

## Non-Goals

不做 durable session runtime partitioning、database migration、external checker fixture、
Validation Client code 或 dashboard UI。
