# Technical Design

## Implementation Structure

- 在 `backend/app/schemas/session.py` 添加 request/summary models。
- 添加 store method，基于 supplied world id 和 public generation metadata 创建 session。
- 在 `backend/app/api/routes/session.py` 添加 `POST /sessions/from-worldview`。
- 复用 `generate_worldview_response()` 和 `provider_readiness_from_env()`，不改变 generation route。
- 更新 `/manifest` session-from-worldview discovery metadata。

## Affected Files

Implementation files：

- `backend/app/schemas/session.py`：添加 worldview-session request 和 public generation
  summary fields。
- `backend/app/core/world_session.py`：添加 creation helper，把 generation summary metadata
  存到 session。
- `backend/app/api/routes/session.py`：添加复用现有 generation helpers 的
  `POST /sessions/from-worldview` route。
- `backend/app/api/routes/world.py`：更新 session-from-worldview availability 的 manifest
  discovery、blockers 和 unsupported-item metadata。

Focused test files：

- `backend/app/tests/test_world_session_api.py`：添加 worldview-to-session creation、
  redaction、blocked-provider 和 no-runtime-run assertions。
- `backend/app/tests/test_public_handoff_contract_api.py`：更新新 session-from-worldview
  surface 的 manifest discovery expectations。

Package / route documentation：

- `docs/iterations/v0.10/0.10.3-worldview-to-runtime-session-creation/*`
- closeout handoff 需要的 v0.10 parent route/review files。

## API Shape

```text
POST /sessions/from-worldview
```

Request 包含 `worldview_premise`、optional public constraints 和
`allow_deterministic_fallback`。不得接受 raw provider payloads。

## Data / Control Flow

```text
request
-> provider_readiness_from_env()
-> generate_worldview_response()
-> create in-memory session using generated world_id
-> return session with redacted generation summary
```

不执行 runtime tick、snapshot、provider live call、checker result 或 external client action。

## Compatibility Strategy

保持现有 session creation 和 generation APIs 不变。新行为是 additive。

## Anti-Drift Rules

如果 implementation 需要 runtime run、dashboard、provider live calls、checker fixtures、
persistence 或 external repositories，停止。
