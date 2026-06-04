# External Validation Gate Matrix

Chinese mirror: `external-validation-gate-matrix.zh.md`.

Status: planned / ready for review
Type: documentation-only gate plan
implementation_authorized: no
evidence_execution_authorized: no

Purpose: record, from the WorldEngine point of view, the cross-repository gates
for external Validation Client v0.7 autonomous validation. This document does
not authorize runtime, API, schema, test, provider, or Validation Client
implementation.

## 0. WorldEngine Responsibility

WorldEngine owns only Gate 1:

```text
WorldEngine public contract readiness
```

WorldEngine does not own:

- Validation Client operation logs.
- Validation Client E2E.
- Codex browser autonomous validation.
- second-Agent read-only review.
- human experience judgment.
- external validation app storage, screenshots, reports, or UI.

WorldEngine must ensure external clients can consume world state and evidence
through public APIs only, without reading private paths, provider keys, private
prompts, provider raw traces, or Agent private state.

## 1. Full Gate Sequence

| Gate | Name | Owner | WorldEngine responsibility | Next gate condition |
| --- | --- | --- | --- | --- |
| Gate 0 | Documentation planning gate | Planning chat | Provide the 0.8.9 package | Both repositories have executable docs |
| Gate 1 | WorldEngine public contract readiness | WorldEngine | Implement public manifest, world creation, provider readiness redaction, and contract checklist | `WORLDENGINE_CONTRACT_READY` |
| Gate 2 | Validation Client v0.7 implementation readiness | Validation Client | Provide public APIs only; do not modify the client | Client says `READY_FOR_CODEX_AUTONOMOUS_VALIDATION` |
| Gate 3 | Codex autonomous validation | Codex | Keep APIs available and redacted | Codex says `PASS_READY_FOR_HUMAN_VALIDATION` |
| Gate 4 | Second-Agent read-only review | Another Agent | No role | Agent says `READY_FOR_HUMAN_VALIDATION` |
| Gate 5 | Human validation | Human | No role | Human writes `HUMAN_PASS` |

## 2. Required WorldEngine Public Surfaces

Required:

```text
GET /health
GET /manifest
GET /openapi.json
POST /worlds
```

Recommended for full v0.7 autonomous validation:

```text
POST /worlds/{world_id}/director-guidance
```

If director guidance is unavailable, `/manifest` must record a public
unavailable reason. That can be `PARTIAL`, but it is not enough for full v0.7
`WORLDENGINE_CONTRACT_READY`.

## 3. Minimum `/manifest` Public Fields

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
    "private_agent_state_included": false
  },
  "blockers": [],
  "warnings": []
}
```

## 4. Minimum `POST /worlds` Contract

Request:

```json
{
  "world_prompt": "observable small pixel world"
}
```

Response must include:

```json
{
  "world_id": "public-world-id",
  "status": "created|ready|limited",
  "public_initial_state": {},
  "visualization": {},
  "warnings": []
}
```

Forbidden in public responses:

- API key.
- authorization header.
- private prompt.
- provider raw trace.
- provider raw response.
- Agent private memory.
- Agent private goal.
- self_state.
- relationship private details.
- identity private details.
- hidden_context.
- internal helper path.

## 5. Validation Client Compatibility Probe

After implementation, start the Validation Client API and run:

```bash
curl -i http://127.0.0.1:8765/health/worldengine
curl -i -H 'Content-Type: application/json' \
  -d '{"session_name":"Codex contract check","world_prompt":"observable small pixel world"}' \
  http://127.0.0.1:8765/sessions/worldengine
```

Required proof:

- Validation Client reports `world_creation: available`.
- Validation Client `POST /sessions/worldengine` succeeds.
- Validation Client does not need provider keys.
- Validation Client does not need WorldEngine private paths.

## 6. Contract Readiness Conclusion

`contract-readiness-checklist.zh.md` may conclude only:

```text
WORLDENGINE_CONTRACT_READY
PARTIAL
BLOCKED
FAIL
```

`WORLDENGINE_CONTRACT_READY` means only:

```text
WorldEngine public contract can be handed to Validation Client for Codex autonomous validation.
```

It does not mean:

- external validation PASS.
- Codex autonomous validation PASS.
- second-Agent review PASS.
- human validation PASS.

## 7. Stop Rules

The WorldEngine implementation chat must stop and record a non-ready conclusion
when:

- `/manifest` is missing.
- OpenAPI lacks a client-discoverable world creation endpoint.
- `POST /worlds` cannot return public world id and public state.
- provider readiness exposes secrets or pretends to be ready.
- a public response contains private prompt, provider raw trace, or Agent
  private state.
- Validation Client compatibility probe fails.
- Gate 1 requires changing Validation Client.

If Validation Client changes are needed, the WorldEngine chat records a
downstream task and does not implement across repositories.

## 8. Downstream Documents

Validation Client full matrix:

```text
/Users/leechen/projects/WorldEngine-Validation-Client/docs/milestones/v0.7-agent-autonomous-validation/cross-repo-validation-gate-matrix.zh.md
```

WorldEngine implementation entry:

```text
implementation-task-plan.zh.md
contract-readiness-checklist.zh.md
implementation-handoff-prompt.zh.md
```
