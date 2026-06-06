# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Design Summary

Add a small provider smoke layer in the active backend path, `backend/app/`.
The layer should reuse the current provider readiness environment mapping
where practical, but separate environment readiness from live call evidence.

The smoke path should return public structured evidence even when the provider
is not configured. This makes the package testable without secrets and keeps
live execution optional and bounded.

## Candidate Backend Shape

Expected implementation surfaces:

```text
backend/app/agent/llm_provider.py
backend/app/api/routes/provider.py
backend/app/api/routes/__init__.py
backend/app/api/app_factory.py
backend/app/schemas/provider.py
backend/app/tests/test_provider_live_smoke_api.py
backend/app/tests/test_public_handoff_contract_api.py
```

Alternative file names are allowed if they match local conventions and remain
inside the allowed paths.

## Endpoint Contract

Preferred endpoint:

```text
POST /provider/live-smoke
operation_id: provider_live_smoke
```

Request body should be empty or contain only public control fields such as:

```json
{
  "mode": "safe"
}
```

The request must not accept raw prompt text, API keys, provider headers,
provider account ids, or private evaluator data.

Response shape:

```json
{
  "schema_version": "0.9.1",
  "provider_class": "deepseek_api",
  "model_label": "deepseek-chat",
  "call_attempted": true,
  "call_status": "success",
  "latency_ms": 123,
  "token_usage_bucket": "1-100",
  "public_failure_category": "none",
  "worldengine_owned_call": true,
  "redaction": {
    "api_keys_included": false,
    "authorization_headers_included": false,
    "raw_prompts_included": false,
    "raw_provider_requests_included": false,
    "raw_provider_responses_included": false,
    "provider_traces_included": false,
    "private_agent_memory_included": false,
    "raw_thought_included": false,
    "hidden_context_included": false
  }
}
```

For unconfigured provider state:

```json
{
  "call_attempted": false,
  "call_status": "not_configured",
  "public_failure_category": "not_configured",
  "worldengine_owned_call": true
}
```

## Provider Call Strategy

The implementation should support two testable paths:

- unconfigured path: no key or unsupported provider returns public
  `not_configured` or `blocked` evidence without attempting a live call.
- safe mock path: tests can inject a provider implementation that returns a
  redacted public outcome without network access.

Live DeepSeek execution is optional and must be gated by environment
configuration plus explicit package authorization. A live call should use a
fixed internal smoke intent, not user-supplied prompt content, and must not
include the fixed prompt in public evidence.

## Redaction Strategy

Response serialization tests must scan for secret-like values and forbidden
markers, including:

```text
api_key
apikey
authorization
bearer
credential
provider_secret
raw prompt
raw_prompt
raw request
raw_request
raw response
raw_response
provider_trace
hidden_context
private memory
private goal
self_state
```

Redaction status is not enough by itself; tests must verify serialized public
responses do not contain injected secret-like env values.

## Compatibility Strategy

- Keep `/manifest` response compatible and additive.
- If `/manifest` lists the smoke endpoint, it must still warn that provider
  readiness is not live-call proof until a smoke response is produced.
- Keep existing public handoff tests passing.
- Do not change `POST /worlds`.

## Anti-Drift Rules

- Do not let smoke prompt design expand into world generation.
- Do not make Validation Client part of provider ownership.
- Do not add persistent provider traces.
- Do not record raw provider request/response in operation logs.
- Do not add concrete world content to prove provider behavior.
- Do not mark provider PASS from mock-only evidence.
