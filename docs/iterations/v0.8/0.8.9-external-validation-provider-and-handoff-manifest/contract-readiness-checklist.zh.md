# Contract Readiness Checklist

英文镜像：`contract-readiness-checklist.md`。

本文记录 external Validation Client v0.7 campaign 所需的 WorldEngine Gate 1
public contract readiness。本文不证明 Codex autonomous validation passed，也不证明
human validation passed。

## 0. 结论

```text
WORLDENGINE_CONTRACT_READY
```

一句话原因：

```text
WorldEngine 已暴露 /manifest、OpenAPI 可发现 POST /worlds、public world creation response、public director guidance status、脱敏 provider readiness，且 Validation Client compatibility probes 已通过。
```

## 1. Implementation Metadata

```text
package: 0.8.9.1-public-handoff-manifest-and-world-creation-contract
branch: v0.8
commit: pending commit at checklist write time
working_tree_status: implementation diff present before commit
implementation_chat: campaign-authorized by user request on 2026-06-04
review file: docs/iterations/v0.8/0.8.9.1-public-handoff-manifest-and-world-creation-contract/review.zh.md
WorldEngine API base: http://127.0.0.1:8000
Validation Client API base: http://127.0.0.1:8765
```

## 2. Required Reading Confirmed

- [x] `AGENTS.md`
- [x] `docs/project-north-star.md`
- [x] `docs/product-model.md`
- [x] `docs/scope-boundaries.md`
- [x] `docs/roadmap.md`
- [x] `docs/iterations/README.md`
- [x] `docs/iterations/AGENTS.md`
- [x] package `README.zh.md`
- [x] package `contract.zh.md`
- [x] package `technical-design.zh.md`
- [x] package `test-plan.zh.md`
- [x] package `validation-client-contract-handoff.zh.md`
- [x] package `implementation-task-plan.zh.md`

## 3. Public Surface Checklist

### `GET /health`

```text
curl result: 200
public response summary: {"code":0,"data":{"status":"ok","service":"worldengine-backend"},"msg":"ok"}
```

- [x] returns 200。
- [x] does not expose secrets or private paths。

### `GET /manifest`

```text
curl result: 200
schema_version: 0.8.9.1
worldengine_version: v0.8
provider.provider_class: unconfigured
provider.provider_readiness: not_configured
provider.credential_source_class: none
provider.model_label: unconfigured
public_surfaces: /health, /openapi.json, /manifest, /worlds, /worlds/{world_id}/director-guidance
redaction flags: all false
blockers: []
warnings: live provider calls outside 0.8.9.1; provider credentials not configured
```

- [x] returns 200。
- [x] includes `/health`。
- [x] includes `/openapi.json`。
- [x] includes world creation surface。
- [x] includes redaction flags。
- [x] does not expose API key。
- [x] does not expose private prompt。
- [x] does not expose provider raw trace。
- [x] does not expose private Agent state。

### `GET /openapi.json`

```text
curl result: 200
world creation path: /worlds
world creation operation id: create_world
world creation tags: worlds
director guidance path: /worlds/{world_id}/director-guidance
director guidance operation id: submit_director_guidance
```

- [x] OpenAPI includes a Validation Client-discoverable world creation endpoint。
- [x] `POST /worlds` is present。
- [x] operation id is `create_world`。

### `POST /worlds`

```text
request body: {"world_prompt":"一个可观察的小型像素世界"}
status code: 200
world_id: world-fde588b26c4d
status: created
public_initial_state: present
visualization: present
warnings: none in response
```

- [x] returns public `world_id`。
- [x] returns `status`。
- [x] returns public state。
- [x] returns visualization payload。
- [x] does not include private generation prompt。
- [x] does not include provider raw response。
- [x] does not include internal helper path。

### `POST /worlds/{world_id}/director-guidance`

```text
request body: {"instruction_text":"让天气逐渐转冷","public_context":{"surface":"validation"}}
status code: 200
status: accepted
public_explanation: public explanation states private Agent state was not mutated
applied_event_id: present
error_message: null
```

- [x] endpoint exists and returns public status。
- [x] request does not allow Agent private memory mutation。
- [x] request does not allow private goal、identity、relationship、self_state 或
      hidden_context mutation。

## 4. Provider Readiness Redaction

- [x] provider readiness is public summary only。
- [x] credential source class is public category only。
- [x] missing provider is not reported as fake ready。
- [x] no API key、authorization header、account id、raw request 或 raw response
      appears in public output。

## 5. Validation Client Compatibility Probe

Commands：

```bash
curl -s -o /tmp/vc-health-worldengine.json -w '%{http_code}' http://127.0.0.1:8765/health/worldengine
curl -s -o /tmp/vc-session-worldengine.json -w '%{http_code}' -H 'Content-Type: application/json' -d '{"session_name":"Codex contract check","world_prompt":"一个可观察的小型像素世界"}' http://127.0.0.1:8765/sessions/worldengine
```

Results：

```text
health/worldengine status: 200
reachable: true
openapi_available: true
world_creation: available
session creation status: 201
session_id: 904c889a-8622-44e8-b8a9-354c7c2ae6c7
worldengine_world_id: world-fde588b26c4d
```

- [x] `world_creation: available`。
- [x] `POST /sessions/worldengine` succeeded。
- [x] Validation Client did not need to read WorldEngine private paths。
- [x] Validation Client did not need provider key。

## 6. Commands Run

```text
focused backend tests:
20 passed, 1 warning in 0.38s

full backend tests:
248 passed, 1 warning in 1.21s

git diff --check:
passed with no output

curl /health:
200

curl /manifest:
200

curl /openapi.json:
200

curl POST /worlds:
200

curl director guidance:
200

Validation Client /health/worldengine:
200

Validation Client POST /sessions/worldengine:
201

redaction scan:
allowed hits only in documentation requirements, redaction helpers, tests, and review text;
saved public response files contained no test secret-like strings
```

## 7. Boundary Findings

```text
Finding ID: WE-0.8.9.1-P3-001
Severity: P3
Evidence: /manifest reports provider_readiness=not_configured.
Impact: Real provider heartbeat/live calls remain future work.
Required follow-up: plan provider heartbeat/probe in a later package.
Blocks WORLDENGINE_CONTRACT_READY: no
```

```text
Finding ID: WE-0.8.9.1-P3-002
Severity: P3
Evidence: Validation Client manifest summary shows version=null because it reads legacy version while WorldEngine returns schema_version.
Impact: Does not block world creation, session creation, or Gate 1.
Required follow-up: adjust Validation Client manifest summary during v0.7 if useful.
Blocks WORLDENGINE_CONTRACT_READY: no
```

## 8. Final Decision Rules

- [x] `/manifest` ready。
- [x] OpenAPI-discoverable world creation ready。
- [x] `POST /worlds` returns public world creation response。
- [x] provider readiness is redacted。
- [x] Validation Client reports `world_creation: available`。
- [x] Validation Client can create a WorldEngine-backed session。
- [x] no public leak of secrets、private prompts、provider raw traces 或 private
      Agent state。
- [x] review.md and review.zh.md record commands and evidence。

该 `WORLDENGINE_CONTRACT_READY` 结论只表示 contract 可以交给 Validation Client 进入
v0.7 readiness implementation 和后续 Codex autonomous validation。不得声明 external
validation PASS、Codex autonomous validation PASS、second-Agent review PASS、human
validation PASS 或 product readiness。
