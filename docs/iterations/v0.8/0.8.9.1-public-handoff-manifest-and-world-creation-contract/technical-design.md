# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Design Summary

Expose a small public contract layer in the active backend path
`backend/app/`. The layer adapts existing generation/readiness capabilities
into Validation Client-discoverable public surfaces while keeping provider,
prompt, evaluator, and Agent-private data out of public responses.

Do not add application-specific worlds or move external validation logic into
WorldEngine.

## Candidate Files

Expected implementation files:

```text
backend/app/schemas/world.py
backend/app/api/routes/world.py
backend/app/api/routes/__init__.py
backend/app/api/app_factory.py
backend/app/core/world_generation.py
backend/app/tests/test_world_generation_schema.py
backend/app/tests/test_generation_core_readiness_api.py
```

The final implementation may choose a separate schema or route file if it
matches existing backend conventions.

## Public Manifest

`GET /manifest` should return a top-level JSON object, not private evidence.
Expected shape:

```json
{
  "schema_version": "0.8.9.1",
  "worldengine_version": "v0.8",
  "provider": {
    "provider_class": "mock|unconfigured|unknown",
    "provider_readiness": "ready|degraded|unavailable|blocked|not_configured",
    "credential_source_class": "environment|secret_manager|developer_local|none|unknown",
    "model_label": "public-or-redacted"
  },
  "public_surfaces": [],
  "redaction": {
    "secrets_included": false,
    "private_prompts_included": false,
    "provider_raw_traces_included": false,
    "private_validator_details_included": false,
    "agent_private_state_included": false
  },
  "blockers": [],
  "warnings": []
}
```

Provider readiness may initially report `not_configured` or `unknown` rather
than fake readiness. This package does not require live provider calls.

## World Creation

`POST /worlds` must be discoverable from OpenAPI by Validation Client:

- path ends in `/worlds`.
- method is `POST`.
- operation id is `create_world`.
- tag may include `worlds`.

Request:

```json
{
  "world_prompt": "a concise generic world request"
}
```

Response should be top-level JSON with:

```json
{
  "world_id": "public stable id",
  "status": "created",
  "public_initial_state": {},
  "visualization": {}
}
```

The route may adapt `world_prompt` into existing preview or deterministic
generation helpers, but it must not introduce concrete demo-world fixtures or
return private generation prompts.

## Director Guidance

If implemented, `POST /worlds/{world_id}/director-guidance` accepts public
guidance only:

```json
{
  "instruction_text": "public high-level guidance",
  "branch_id": "optional-public-branch",
  "tick": 1,
  "public_context": {}
}
```

Response status may be `accepted`, `applied`, `blocked`, or `unavailable`.
Direct mutation of private Agent memory, private goals, identity,
relationships, or `self_state` is forbidden.

If not implemented in code, `/manifest` must record a public unavailable
reason and closeout must not claim full ready-for-human-validation.

## Redaction

Public responses must not contain:

```text
api_key
apikey
secret
token
password
authorization
bearer
private_prompt
raw_response
raw_request
private memory
private goal
self_state
hidden_context
```

Tests should serialize public responses and assert forbidden private terms and
known secret-like inputs are absent.
