# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Scope

Tests must prove only WorldEngine public contract readiness for Validation
Client handoff. They must not claim external Validation Client autonomous PASS
or human validation PASS.

## Pre-Implementation Documentation Checks

Run before any code changes:

```bash
git status --short --branch
git diff --check
```

Confirm this package has been approved for implementation.

## Focused Backend Tests

Run during implementation:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests/test_world_generation_schema.py app/tests/test_generation_core_readiness_api.py -q
```

Expected coverage:

- schema serialization for manifest, world creation, and director guidance.
- `GET /manifest` returns 200.
- manifest includes `/health`, `/openapi.json`, and `/worlds`.
- manifest redaction flags are false for private content.
- provider readiness does not fake ready when provider is missing.
- OpenAPI exposes `POST /worlds`.
- `POST /worlds` accepts `world_prompt`.
- `POST /worlds` returns top-level `world_id`, `status`,
  `public_initial_state`, and `visualization`.
- public responses do not include forbidden private fields.

## Regression Tests

Run before closeout:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests -q
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
git diff --check
```

## Runtime Probe

Start WorldEngine:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Probe:

```bash
curl -i http://127.0.0.1:8000/health
curl -i http://127.0.0.1:8000/manifest
curl -i http://127.0.0.1:8000/openapi.json
curl -i -H 'Content-Type: application/json' \
  -d '{"world_prompt":"a small observable generic world"}' \
  http://127.0.0.1:8000/worlds
```

## Optional Validation Client Compatibility Probe

If the Validation Client repository and dependencies are available, run:

```bash
cd /Users/leechen/projects/WorldEngine-Validation-Client
uv run --project apps/api uvicorn app.main:app --host 127.0.0.1 --port 8765 --app-dir apps/api
curl -i http://127.0.0.1:8765/health/worldengine
curl -i -H 'Content-Type: application/json' \
  -d '{"session_name":"Codex contract check","world_prompt":"a small observable generic world"}' \
  http://127.0.0.1:8765/sessions/worldengine
```

This probe may support `WORLDENGINE_CONTRACT_READY` only. It is not external
validation PASS or human validation PASS.

## Redaction Scan

Run:

```bash
rg -n "api_key|apikey|secret|token|password|credential|authorization|private_prompt|raw_response|raw_request|private memory|private goal|self_state|hidden_context" backend/app docs/iterations/v0.8/0.8.9.1-public-handoff-manifest-and-world-creation-contract
```

Review matches manually because docs may mention forbidden terms as negative
requirements.

## Pass Criteria

This package may conclude `WORLDENGINE_CONTRACT_READY` only when:

- backend tests pass.
- runtime probes pass.
- OpenAPI proves `POST /worlds` discoverability.
- public responses prove required fields.
- redaction checks find no secret or private data leak in public outputs.
- review evidence records changed files, commands, test results,
  compatibility review, scope review, and unresolved findings.
