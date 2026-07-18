# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Affected Files

Allowed implementation files after review:

- `backend/app/schemas/provider_preflight.py`
- `backend/app/api/routes/provider.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_provider_worldview_preflight_api.py`

Allowed documentation files:

- this package directory.
- parent v0.11 route/review docs.

## API Shape

Add:

```text
POST /provider/worldview-preflight
```

Request:

- optional `worldview_premise`
- optional `allow_deterministic_fallback`, default `true`

Response should include:

- provider readiness summary.
- `live_call_authorized: false`.
- worldview generation mode/status when a premise is supplied.
- blockers/warnings/diagnostics.
- redaction summary proving private content is excluded.

## Implementation Notes

- Reuse `provider_readiness_from_env()`.
- Reuse `generate_worldview_response()` only for non-live classification.
- Do not call `ProviderClient` or external HTTP APIs.
- Keep model labels redacted by existing provider readiness rules.
- Return public summaries only; do not echo raw private or rejected input.
