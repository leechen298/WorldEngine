# Technical Design

## Implementation Structure

新增：

- `backend/app/schemas/session.py`：pydantic session request/response models。
- `backend/app/core/world_session.py`：in-memory store 和 session construction helpers。
- `backend/app/api/routes/session.py`：public session endpoints。
- 在 `backend/app/api/routes/__init__.py` 和 `backend/app/api/app_factory.py` 注册 router。

更新：

- `backend/app/api/routes/world.py` manifest surfaces。
- `backend/app/tests/` 下的 focused tests。

## API Shape

```text
POST /sessions
GET /sessions
GET /sessions/{session_id}
GET /sessions/{session_id}/status
```

`POST /sessions` 接收 optional `world_id` 和 optional public label。不接收 worldview prompts
或 provider data。

## Data / Control Flow

```text
POST /sessions
-> read current runtime state, event count, snapshot count
-> create in-memory WorldSessionRecord
-> return redacted public session payload
```

不运行 tick，不创建 snapshot，不发起 provider call。

## Compatibility Strategy

- Session APIs 是 additive new routes。
- Existing runtime/world APIs 保持不变。
- Manifest 对 future run/snapshot surfaces 继续标记为 planned/not_run，直到后续 package 实现。

## Anti-Drift Rules

- 如果 implementation 需要 runtime execution，停止并交接 `0.10.4`。
- 如果 implementation 需要 worldview input，停止并交接 `0.10.3`。
- 如果 implementation 需要 frontend/dashboard，停止并交接 `0.10.5`。
- 如果 implementation 需要 persistence/migrations，停止并标为 out of scope。
