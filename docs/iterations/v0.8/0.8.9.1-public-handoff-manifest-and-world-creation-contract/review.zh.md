# Review

英文源文件：`review.md`。

状态：implementation complete
implementation_authorized: campaign-authorized by user request on 2026-06-04
evidence_execution_authorized: yes，仅限 WorldEngine Gate 1 和 Validation Client compatibility probes

## Changed Files

Implementation files：

- `backend/app/api/app_factory.py`
- `backend/app/api/routes/__init__.py`
- `backend/app/api/routes/world.py`
- `backend/app/schemas/world.py`

Tests：

- `backend/app/tests/test_public_handoff_contract_api.py`
- `backend/app/tests/test_world_generation_schema.py`

Review evidence：

- `docs/iterations/v0.8/0.8.9.1-public-handoff-manifest-and-world-creation-contract/review.md`
- `docs/iterations/v0.8/0.8.9.1-public-handoff-manifest-and-world-creation-contract/review.zh.md`
- `docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/contract-readiness-checklist.md`
- `docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/contract-readiness-checklist.zh.md`

## Implementation Summary

- 新增 top-level `GET /manifest`。
- 新增 top-level OpenAPI 可发现 `POST /worlds`，operation id 为 `create_world`。
- 新增 public world creation request / response schemas。
- 新增 provider readiness summary，不执行 live provider calls，不暴露 credential。
- 新增 redaction flags 和 secret-like public label redaction。
- 新增 `POST /worlds/{world_id}/director-guidance`，返回 public `accepted`
  status 和 public event id，不修改 Agent private state。
- 保持既有 `/world/*` 和 `/world/generation/*` API envelope 兼容。
- 未修改 `backend/worldengine/`、Validation Client code、frontend、provider calls、
  provider credential storage、migrations 或 concrete demo world content。

## Commands Run

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_world_generation_schema.py backend/app/tests/test_public_handoff_contract_api.py backend/app/tests/test_generation_core_readiness_api.py -q
```

Result: `20 passed, 1 warning in 0.38s`。

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests -q
```

Result: `248 passed, 1 warning in 1.21s`。

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project uvicorn app.main:app --host 127.0.0.1 --port 8000
curl -s -o /tmp/we-health.json -w '%{http_code}' http://127.0.0.1:8000/health
curl -s -o /tmp/we-manifest.json -w '%{http_code}' http://127.0.0.1:8000/manifest
curl -s -o /tmp/we-openapi.json -w '%{http_code}' http://127.0.0.1:8000/openapi.json
curl -s -o /tmp/we-worlds.json -w '%{http_code}' -H 'Content-Type: application/json' -d '{"world_prompt":"一个可观察的小型像素世界"}' http://127.0.0.1:8000/worlds
curl -s -o /tmp/we-director.json -w '%{http_code}' -H 'Content-Type: application/json' -d '{"instruction_text":"让天气逐渐转冷","public_context":{"surface":"validation"}}' http://127.0.0.1:8000/worlds/world-fde588b26c4d/director-guidance
```

Results：

- `/health`: `200`。
- `/manifest`: `200`。
- `/openapi.json`: `200`。
- `POST /worlds`: `200`。
- `POST /worlds/{world_id}/director-guidance`: `200`。

```bash
WORLDENGINE_API_BASE=http://127.0.0.1:8000 uv run --project apps/api uvicorn app.main:app --host 127.0.0.1 --port 8765 --app-dir apps/api
curl -s -o /tmp/vc-health-worldengine.json -w '%{http_code}' http://127.0.0.1:8765/health/worldengine
curl -s -o /tmp/vc-session-worldengine.json -w '%{http_code}' -H 'Content-Type: application/json' -d '{"session_name":"Codex contract check","world_prompt":"一个可观察的小型像素世界"}' http://127.0.0.1:8765/sessions/worldengine
```

Results：

- Validation Client `/health/worldengine`: `200`。
- Validation Client `POST /sessions/worldengine`: `201`。
- Validation Client reported `world_creation: available`。
- Validation Client session response included
  `worldengine_world_id=world-fde588b26c4d`。

```bash
git diff --check
```

Result: passed with no output。

```bash
rg -n "api_key|apikey|secret|token|password|credential|authorization|private_prompt|provider raw|raw_response|private memory|private goal|self_state|hidden_context" backend/app docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest docs/iterations/v0.8/0.8.9.1-public-handoff-manifest-and-world-creation-contract
```

Result: allowed hits only in documentation requirements, redaction helpers, tests, and review text. No public response leak was identified。

```bash
rg -n "sk-live-secret-key|sk-live-secret-model|must-not-be-accepted|private trace" /tmp/we-health.json /tmp/we-manifest.json /tmp/we-worlds.json /tmp/we-director.json /tmp/vc-health-worldengine.json /tmp/vc-session-worldengine.json
```

Result: no matches。

## Test Results

- Focused API/schema regression: passed。
- Full backend regression: passed。
- Runtime WorldEngine public contract probe: passed。
- Validation Client compatibility probe: passed。
- Diff whitespace check: passed。
- Secret-like response scan: passed。

## Compatibility Review

- 既有 `/world/events`、`/world/event-steps`、`/world/generation/*`、`/runtime/*`、
  `/archive/*` 和 Agent-loop endpoints 仍使用既有 API envelopes。
- `POST /worlds` 按 Validation Client contract 要求，故意返回 top-level public
  fields。
- Schema changes 是 additive。
- Provider readiness 不执行 live provider calls，也不要求 key。
- Provider credentials 缺失时返回 `not_configured`，不伪装 ready。

## Scope Review

In scope：

- public manifest。
- OpenAPI-discoverable world creation。
- public world creation response。
- provider readiness redaction。
- public director guidance status。
- focused backend tests。
- contract readiness evidence。

Out of scope and not done：

- provider runtime calls。
- provider heartbeat/probe。
- provider credential storage。
- Validation Client implementation changes。
- frontend changes。
- concrete demo-world names、maps、characters、resources、story rules 或 seed data。
- Codex autonomous validation。
- second-Agent review。
- human validation。

## Unresolved Findings

- P3：runtime probe 中 `GET /manifest` 报告 provider credentials 为
  `not_configured`，因为 provider heartbeat 和真实 provider configuration 不属于
  0.8.9.1。
- P3：Validation Client manifest summary 当前读到 `version: null`，因为客户端摘要
  仍读取旧 `version` 字段，而 WorldEngine 返回 `schema_version`。这不阻塞 world
  creation 或 Gate 1 readiness。

## Final Assessment

`WORLDENGINE_CONTRACT_READY`。

该结论只表示 WorldEngine Gate 1 public contract 可以交给 Validation Client 继续
v0.7 readiness implementation 和 Codex autonomous validation preparation。它不声
明 external validation PASS、Codex autonomous validation PASS、second-Agent review
PASS、human validation PASS、live provider PASS 或 product readiness。
