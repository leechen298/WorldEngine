# 0.8.9 Detailed Implementation Plan

Chinese mirror: `implementation-task-plan.zh.md`.

Status: planned / pending implementation

This document decomposes 0.8.9 future implementation into tasks that a future
chat can execute, verify, and record one by one. The current package remains a
documentation-only planning package. Implementation must start only after user
review and explicit authorization.

## 0. Preconditions

The future implementation chat must read:

```text
AGENTS.md
docs/project-north-star.md
docs/product-model.md
docs/scope-boundaries.md
docs/roadmap.md
docs/iterations/README.md
docs/iterations/AGENTS.md
docs/iterations/v0.8/README.zh.md
docs/iterations/v0.8/CURRENT_STATE.zh.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/README.zh.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/contract.zh.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/technical-design.zh.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/test-plan.zh.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/validation-client-contract-handoff.zh.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/implementation-task-plan.zh.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/contract-readiness-checklist.zh.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/implementation-handoff-prompt.zh.md
```

Before implementation, confirm:

- this package passed user review.
- the current chat explicitly authorizes implementation.
- the target is limited to WorldEngine public contract.
- the Validation Client repository will not be modified.
- no concrete demo world, character, map, or application-specific logic will be
  added.

## 1. Candidate File Responsibilities

Future implementation should inspect and may modify:

```text
backend/app/main.py
backend/app/api/app_factory.py
backend/app/api/routes/__init__.py
backend/app/api/routes/health.py
backend/app/api/routes/world_generation.py
backend/app/api/routes/world.py
backend/app/schemas/api.py
backend/app/schemas/world_generation.py
backend/app/schemas/world.py
backend/app/core/world_generation.py
backend/app/tests/test_generation_core_readiness_api.py
backend/app/tests/test_world_generation_schema.py
```

If standalone contract documentation is needed, create:

```text
docs/contracts/validation-client-handoff-manifest.md
docs/contracts/validation-client-handoff-manifest.zh.md
```

Do not modify:

```text
backend/worldengine/
Validation Client repository
demo-specific world fixtures
private prompt files
provider credential storage
external validator implementation
```

## 2. Task Sequence

Each task should be committed separately. If a task exposes a design gap, stop,
update this package's contract, technical design, or test plan, and then
continue.

### Task 1: Public handoff schemas

Goal: define public response shapes for `/manifest`, `POST /worlds`, and
director guidance.

Implement schemas for:

- manifest schema version.
- WorldEngine public version label.
- provider public readiness.
- public surface ids.
- redaction flags.
- blockers and warnings.
- public world creation request / response.
- public director guidance request / response.

The fields must be public summaries only. Do not include provider raw traces,
private prompts, or private Agent state.

Test:

- schemas serialize.
- redaction flags default to no secrets.
- forbidden private fields are not present in response models.

Run:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests/test_world_generation_schema.py app/tests/test_generation_core_readiness_api.py -q
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
git diff --check
```

### Task 2: `GET /manifest`

Goal: provide a public readiness document for Validation Client.

Implement:

- public route `GET /manifest`.
- public provider readiness, public surfaces, redaction flags, blockers, and
  warnings.
- provider fields limited to provider class, readiness, credential source class,
  and public model label.
- missing provider returns `blocked` or `unknown`; do not fake ready.

Test:

- `GET /manifest` returns 200.
- response contains `/health`, `/openapi.json`, and `/worlds`.
- secrets, private prompts, and provider raw traces are absent.
- missing provider yields a public blocker or warning.

Run:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests/test_generation_core_readiness_api.py -q
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
git diff --check
```

### Task 3: OpenAPI-discoverable `POST /worlds`

Goal: let Validation Client discover and call world creation.

Implement:

- public `POST /worlds`, or make an existing public endpoint satisfy Validation
  Client discovery.
- operation id `create_world` or `createWorld` is preferred.
- response includes public `world_id`, `status`, `public_initial_state` or
  `initial_state`, and `visualization` or `visualization_payload`.
- existing world generation core may be reused, but concrete demo-world
  fixtures must not be introduced.

Test:

- OpenAPI includes `POST /worlds`.
- `POST /worlds` accepts a base `world_prompt` and returns public world data.
- response contains no private generation prompt, provider raw response, or
  internal helper path.

Run:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests/test_generation_core_readiness_api.py app/tests/test_deterministic_world_generation.py -q
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
git diff --check
```

### Task 4: Public director guidance endpoint

Goal: support high-level evolution guidance without mutating Agent private
state.

Implement:

- `POST /worlds/{world_id}/director-guidance`, or a clear public unavailable
  response if unsupported.
- request accepts `instruction_text`, optional `branch_id`, optional `tick`, and
  optional public context.
- response returns `accepted`, `applied`, `blocked`, or `unavailable`, plus
  public explanation and optional public event id.
- no direct writes to Agent memory, private goal, identity, relationship, or
  self_state.

Test:

- endpoint appears in OpenAPI.
- normal request returns public status.
- forbidden fields are not accepted as Agent private mutations.

Run:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests/test_agent_loop_api.py app/tests/test_generation_core_readiness_api.py -q
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
git diff --check
```

### Task 5: Provider readiness redaction

Goal: expose provider status while never exposing credentials or raw traces.

Implement:

- public readiness label from environment configuration or provider abstraction.
- credential source class such as `environment`, `not_configured`, or `unknown`.
- public model label.
- no API key, authorization header, account id, raw request, or raw response.

Test:

- missing configuration is not reported as fake ready.
- public response contains no real forbidden sensitive value.
- redaction flags match response contents.

Run:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests/test_generation_core_readiness_api.py -q
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
git diff --check
```

### Task 6: Validation Client compatibility probe

Goal: prove the external client can consume the contract.

1. Start WorldEngine:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

2. In another shell, verify WorldEngine:

```bash
curl -i http://127.0.0.1:8000/health
curl -i http://127.0.0.1:8000/manifest
curl -i http://127.0.0.1:8000/openapi.json
curl -i -H 'Content-Type: application/json' \
  -d '{"world_prompt":"a small observable pixel world"}' \
  http://127.0.0.1:8000/worlds
```

3. Start Validation Client API:

```bash
cd /Users/leechen/projects/WorldEngine-Validation-Client
uv run --project apps/api uvicorn app.main:app --host 127.0.0.1 --port 8765 --app-dir apps/api
```

4. Verify client discovery:

```bash
curl -i http://127.0.0.1:8765/health/worldengine
curl -i -H 'Content-Type: application/json' \
  -d '{"session_name":"Codex contract check","world_prompt":"a small observable pixel world"}' \
  http://127.0.0.1:8765/sessions/worldengine
```

Done when `/health/worldengine` reports `world_creation: available` and
`POST /sessions/worldengine` succeeds. Do not claim Codex autonomous validation
PASS or human validation PASS.

### Task 7: Full regression and review closeout

Goal: record reliable implementation evidence.

Run:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests -q
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
git diff --check
rg -n "api_key|apikey|secret|token|password|credential|authorization|private_prompt|provider raw|raw_response|private memory|private goal|self_state|hidden_context" backend/app docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest
```

Update:

```text
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/review.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/review.zh.md
```

Done when review records changed files, commands, test results, compatibility
review, scope review, and unresolved findings. The
`contract-readiness-checklist.zh.md` can be filled as this run's contract
readiness evidence. The conclusion may only say WorldEngine public contract is
ready for Validation Client autonomous validation. Do not claim external
validation PASS or human validation PASS.

## 3. Stop Rules

- Stop if implementation needs concrete demo-world content.
- Stop and FAIL if a public response would expose secrets, private prompts,
  provider raw traces, or private Agent state.
- Stop if Validation Client code needs to be changed; record it as a downstream
  task.
- Stop if the implementation changes the meaning of v0.8 final closeout.
- Stop if director guidance would directly mutate Agent private state.
- Do not claim contract ready if tests do not prove OpenAPI discoverability.
