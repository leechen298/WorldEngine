# Technical Design

英文版本：`technical-design.md`。

## Affected Files

评审后允许修改的 implementation files：

- `backend/app/schemas/provider_preflight.py`
- `backend/app/api/routes/provider.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_provider_worldview_preflight_api.py`

允许修改的文档：

- 本 package directory。
- parent v0.11 route/review docs。

## API Shape

新增：

```text
POST /provider/worldview-preflight
```

Request：

- optional `worldview_premise`
- optional `allow_deterministic_fallback`，默认 `true`

Response 应包含：

- provider readiness summary。
- `live_call_authorized: false`。
- 如果提供 premise，则包含 worldview generation mode/status。
- blockers/warnings/diagnostics。
- 证明 private content 未输出的 redaction summary。

## Implementation Notes

- 复用 `provider_readiness_from_env()`。
- 仅为 non-live classification 复用 `generate_worldview_response()`。
- 不调用 `ProviderClient` 或 external HTTP APIs。
- 使用现有 provider readiness rules 保持 model labels redacted。
- 只返回 public summaries；不得 echo raw private 或 rejected input。
