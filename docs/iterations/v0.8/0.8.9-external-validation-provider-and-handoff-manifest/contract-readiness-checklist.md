# Contract Readiness Checklist

Chinese mirror: `contract-readiness-checklist.zh.md`.

Use this checklist after 0.8.9 implementation to decide whether WorldEngine
public contract is ready for Validation Client Codex autonomous validation.

This checklist does not prove Codex autonomous validation passed and does not
prove human validation passed. It only proves whether WorldEngine-side public
contract is ready.

## 0. Conclusion

Choose exactly one:

```text
WORLDENGINE_CONTRACT_READY
PARTIAL
BLOCKED
FAIL
```

Current conclusion:

```text
<one allowed conclusion>
```

Short reason:

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
- [ ] request does not allow private goal, identity, relationship, self_state, or
      hidden_context mutation.

If director guidance is unavailable, conclusion may be `PARTIAL` but not
`WORLDENGINE_CONTRACT_READY` for full v0.7 autonomous validation.

## 4. Provider Readiness Redaction

Check:

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
  -d '{"session_name":"Codex contract check","world_prompt":"a small observable pixel world"}' \
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

Required:

- [ ] `world_creation: available`.
- [ ] `POST /sessions/worldengine` succeeds.
- [ ] Validation Client does not need WorldEngine private paths.
- [ ] Validation Client does not need provider keys.

## 6. Commands Run

Record only commands run in the current session:

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

`WORLDENGINE_CONTRACT_READY` requires:

- [ ] `/manifest` ready.
- [ ] OpenAPI-discoverable world creation ready.
- [ ] `POST /worlds` returns public world creation response.
- [ ] provider readiness is redacted.
- [ ] Validation Client reports `world_creation: available`.
- [ ] Validation Client can create a WorldEngine-backed session.
- [ ] no public leak of secrets, private prompts, provider raw traces, or private
      Agent state.
- [ ] review.md and review.zh.md record commands and evidence.

If any item is missing, do not write `WORLDENGINE_CONTRACT_READY`.

Even when the conclusion is `WORLDENGINE_CONTRACT_READY`, it only means the
contract can be handed to Validation Client for Codex autonomous validation. Do
not claim external validation PASS or human validation PASS.
