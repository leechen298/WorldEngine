# Contract Readiness Checklist

英文镜像：`contract-readiness-checklist.md`。

用途：未来实现 0.8.9 后，用本文检查 WorldEngine public contract 是否已经可以
交给 Validation Client 进入 Codex 自主验证。

本文不证明 Codex 自主验证通过，也不证明人工验证通过。它只证明 WorldEngine 侧
public contract ready 或不 ready。

## 0. 结论

结论只能选择一个：

```text
WORLDENGINE_CONTRACT_READY
PARTIAL
BLOCKED
FAIL
```

当前结论：

```text
<one allowed conclusion>
```

一句话原因：

```text
<short public reason>
```

## 1. Implementation Metadata

```text
package:
branch:
commit:
working_tree_status:
implementation_chat:
review file:
WorldEngine API base:
Validation Client API base:
```

## 2. Required Reading Confirmed

- [ ] `AGENTS.md`
- [ ] `docs/project-north-star.md`
- [ ] `docs/product-model.md`
- [ ] `docs/scope-boundaries.md`
- [ ] `docs/roadmap.md`
- [ ] `docs/iterations/README.md`
- [ ] `docs/iterations/AGENTS.md`
- [ ] package `README.zh.md`
- [ ] package `contract.zh.md`
- [ ] package `technical-design.zh.md`
- [ ] package `test-plan.zh.md`
- [ ] package `validation-client-contract-handoff.zh.md`
- [ ] package `implementation-task-plan.zh.md`

## 3. Public Surface Checklist

### `GET /health`

```text
curl result:
status code:
public response summary:
```

- [ ] returns 200.
- [ ] does not expose secrets or private paths.

### `GET /manifest`

```text
curl result:
status code:
schema_version:
worldengine_version:
provider.provider_class:
provider.provider_readiness:
provider.credential_source_class:
provider.model_label:
public_surfaces:
redaction flags:
blockers:
warnings:
```

- [ ] returns 200.
- [ ] includes `/health`.
- [ ] includes `/openapi.json`.
- [ ] includes world creation surface.
- [ ] includes redaction flags.
- [ ] does not expose API key.
- [ ] does not expose private prompt.
- [ ] does not expose provider raw trace.
- [ ] does not expose private Agent state.

### `GET /openapi.json`

```text
curl result:
status code:
world creation path:
world creation operation id:
world creation tags:
director guidance path:
director guidance operation id:
```

- [ ] OpenAPI includes a Validation Client-discoverable world creation endpoint.
- [ ] Prefer `POST /worlds`.
- [ ] operation id is `create_world` or `createWorld`, or tags/path satisfy
      Validation Client discovery.

### `POST /worlds`

```text
request body:
status code:
world_id:
status:
public_initial_state or initial_state:
visualization or visualization_payload:
warnings:
```

- [ ] returns public `world_id`.
- [ ] returns `status`.
- [ ] returns public state.
- [ ] returns visualization payload.
- [ ] does not include private generation prompt.
- [ ] does not include provider raw response.
- [ ] does not include internal helper path.

### `POST /worlds/{world_id}/director-guidance`

```text
request body:
status code:
status:
public_explanation:
applied_event_id:
error_message:
```

- [ ] endpoint exists and returns public status, or the manifest records a clear
      public unavailable reason.
- [ ] request does not allow Agent private memory mutation.
- [ ] request does not allow private goal, identity, relationship, self_state or
      hidden_context mutation.

If director guidance is unavailable, conclusion may be `PARTIAL` but not
`WORLDENGINE_CONTRACT_READY` for full v0.7 autonomous validation.

## 4. Provider Readiness Redaction

检查：

- [ ] provider readiness is public summary only.
- [ ] credential source class is public category only.
- [ ] missing provider is not reported as fake ready.
- [ ] no API key, authorization header, account id, raw request, or raw response
      appears in public output.

## 5. Validation Client Compatibility Probe

Commands:

```bash
curl -i http://127.0.0.1:8765/health/worldengine
curl -i -H 'Content-Type: application/json' \
  -d '{"session_name":"Codex contract check","world_prompt":"一个可观察的小型像素世界"}' \
  http://127.0.0.1:8765/sessions/worldengine
```

Results:

```text
health/worldengine status:
reachable:
openapi_available:
world_creation:
session creation status:
session_id:
worldengine_world_id:
```

必须满足：

- [ ] `world_creation: available`。
- [ ] `POST /sessions/worldengine` 成功。
- [ ] Validation Client 不需要读取 WorldEngine private paths。
- [ ] Validation Client 不需要 provider key。

## 6. Commands Run

只记录当前会话实际运行过的命令：

```text
cd backend && .venv/bin/python -m pytest app/tests -q:
git diff --check:
curl /health:
curl /manifest:
curl /openapi.json:
curl POST /worlds:
curl director guidance:
Validation Client /health/worldengine:
Validation Client POST /sessions/worldengine:
redaction scan:
```

## 7. Boundary Findings

```text
Finding ID:
Severity:
Evidence:
Impact:
Required follow-up:
Blocks WORLDENGINE_CONTRACT_READY: yes/no
```

## 8. Final Decision Rules

`WORLDENGINE_CONTRACT_READY` 要求：

- [ ] `/manifest` ready。
- [ ] OpenAPI-discoverable world creation ready。
- [ ] `POST /worlds` returns public world creation response。
- [ ] provider readiness is redacted。
- [ ] Validation Client reports `world_creation: available`。
- [ ] Validation Client can create a WorldEngine-backed session。
- [ ] no public leak of secrets, private prompts, provider raw traces, or private
      Agent state。
- [ ] review.md and review.zh.md record commands and evidence。

缺任一项时不能写 `WORLDENGINE_CONTRACT_READY`。

即使结论是 `WORLDENGINE_CONTRACT_READY`，也只能说明可以交给 Validation Client
进入 Codex 自主验证；不得声明 external validation PASS 或 human validation PASS。
