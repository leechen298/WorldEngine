# Validation Client Contract Handoff

Chinese mirror: `validation-client-contract-handoff.zh.md`.

## Purpose

This document defines the minimum WorldEngine public contract needed before an
external Validation Client can run Codex autonomous validation and then hand off
to human validation.

It is a planning document only. It does not authorize runtime, API, schema,
frontend, test, fixture, migration, or provider implementation.

## Current Observed Gap

As of 2026-06-04, local checks showed:

- WorldEngine can start locally.
- `GET /health` returns 200.
- `GET /openapi.json` returns 200.
- `GET /world/params` returns 200.
- `GET /manifest` returns 404.
- `GET /world/generation/readiness` returns 404.
- Validation Client can call `GET /health/worldengine`.
- Validation Client reports `reachable: true` and `openapi_available: true`.
- Validation Client reports `world_creation: unknown`.
- Validation Client `POST /sessions/worldengine` returns 502 with
  `WorldEngine public world creation endpoint not found`.

This means the Validation Client can detect WorldEngine, but cannot create a
WorldEngine-backed session. Codex autonomous browser validation must stop until
this contract gap is closed.

## Required Public Surfaces

### `GET /manifest`

Required purpose:

- expose public validation-readiness information.
- expose provider readiness without secrets.
- expose public surface ids for external consumers.
- expose redaction flags, blockers, and warnings.

Minimum response shape:

```json
{
  "schema_version": "0.8.x",
  "worldengine_version": "v0.8",
  "provider": {
    "provider_class": "mock|kimi_platform_api|deepseek_api|unknown",
    "provider_readiness": "ready|limited|blocked|unknown",
    "credential_source_class": "environment|not_configured|unknown",
    "model_label": "public-or-redacted-label"
  },
  "public_surfaces": [
    "/health",
    "/openapi.json",
    "/worlds",
    "/worlds/{world_id}/director-guidance"
  ],
  "redaction": {
    "secrets_included": false,
    "private_prompts_included": false,
    "provider_raw_traces_included": false,
    "private_validator_details_included": false
  },
  "blockers": [],
  "warnings": []
}
```

### Public world creation endpoint

The current Validation Client auto-discovers a public creation endpoint from
OpenAPI. It recognizes:

- a POST path ending in `/worlds`.
- or a POST operation id equal to `createWorld` / `create_world`.
- or a POST operation tagged `worlds` with `create` in the operation id.

Recommended endpoint:

```text
POST /worlds
```

Minimum request:

```json
{
  "world_prompt": "A small observable pixel world"
}
```

Minimum response:

```json
{
  "world_id": "world-001",
  "status": "created",
  "public_initial_state": {
    "summary": "public summary",
    "public_agents": [
      {
        "agent_id": "agent-1",
        "display_name": "Ada",
        "location": "market",
        "public_status": "observing",
        "visible_action": "opens a stall"
      }
    ]
  },
  "visualization": {
    "tiles": [],
    "entities": []
  }
}
```

### Public director guidance endpoint

Required for full v0.7 Validation Client autonomous validation.

Recommended endpoint:

```text
POST /worlds/{world_id}/director-guidance
```

Minimum request:

```json
{
  "instruction_text": "Make the next events trend toward peaceful interaction",
  "branch_id": "branch-public-id",
  "tick": 0,
  "public_context": {}
}
```

Minimum response:

```json
{
  "status": "accepted|applied|blocked",
  "public_explanation": "public summary only",
  "applied_event_id": "event-public-id",
  "error_message": null
}
```

## Forbidden Data

These values must never appear in public responses, manifest, evidence,
OpenAPI examples, or Validation Client logs:

```text
api_key
authorization
credential
password
provider secret
private prompt
provider raw trace
private validator oracle
Agent private memory
Agent private goal
Agent self_state
hidden_context
private filesystem path
```

## Verification Commands

After a future implementation package adds the contract, run:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests -q
.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

In another shell:

```bash
curl -i http://127.0.0.1:8000/health
curl -i http://127.0.0.1:8000/manifest
curl -i http://127.0.0.1:8000/openapi.json
curl -i -H 'Content-Type: application/json' \
  -d '{"world_prompt":"A small observable pixel world"}' \
  http://127.0.0.1:8000/worlds
```

Then verify the Validation Client:

```bash
cd /Users/leechen/projects/WorldEngine-Validation-Client
uv run --project apps/api uvicorn app.main:app --host 127.0.0.1 --port 8765 --app-dir apps/api
curl -i http://127.0.0.1:8765/health/worldengine
curl -i -H 'Content-Type: application/json' \
  -d '{"session_name":"Codex contract check","world_prompt":"A small observable pixel world"}' \
  http://127.0.0.1:8765/sessions/worldengine
```

## Acceptance Criteria

WorldEngine contract is ready for Validation Client autonomous validation only
when:

- `/manifest` returns a redacted public readiness document.
- OpenAPI exposes a Validation Client-discoverable world creation endpoint.
- world creation returns public `world_id`, `status`, state, and visualization.
- provider readiness is public but secrets remain hidden.
- Validation Client `/health/worldengine` reports `world_creation: available`.
- Validation Client `POST /sessions/worldengine` succeeds.

## Stop Rules

- If `/manifest` is missing, Codex autonomous validation may not claim provider
  readiness.
- If world creation is not discoverable by the Validation Client, browser
  autonomous validation must stop before UI flow.
- If public responses leak secrets or private prompts, the result is FAIL.
- If director guidance is missing, the result may be PARTIAL but not full
  ready-for-human-validation PASS.
