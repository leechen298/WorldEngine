# 0.8.9 Planning Readiness Checklist

Chinese mirror: `planning-readiness-checklist.zh.md`.

Status: PLAN_READY_FOR_REVIEW
Type: documentation-only planning evidence
implementation_authorized: no
evidence_execution_authorized: no

Purpose: prove that the 0.8.9 WorldEngine public contract package has the
planning documents needed for a future implementation chat. This document does
not prove the WorldEngine public contract has been implemented.

## 0. Conclusion

```text
PLAN_READY_FOR_REVIEW
```

Reason:

```text
The 0.8.9 package defines intent, contract, technical design, test plan,
implementation task plan, external validation gate matrix, contract readiness
checklist, and future-chat prompt.
```

## 1. Allowed Next Step

Only allowed next step:

```text
User review of this package, then Gate 1 public contract implementation in a future implementation chat.
```

Not allowed:

- Modify runtime, API, schema, test, or provider code in this planning package.
- Claim `WORLDENGINE_CONTRACT_READY`.
- Claim Validation Client autonomous validation PASS.
- Claim human validation PASS.

## 2. Required Documents

Required:

```text
README.zh.md
intent.zh.md
contract.zh.md
technical-design.zh.md
test-plan.zh.md
plan.zh.md
validation-client-contract-handoff.zh.md
implementation-task-plan.zh.md
external-validation-gate-matrix.zh.md
contract-readiness-checklist.zh.md
implementation-handoff-prompt.zh.md
review.zh.md
planning-readiness-checklist.zh.md
```

## 3. Coverage

This package covers:

- `GET /manifest` public handoff manifest.
- OpenAPI-discoverable world creation endpoint, preferably `POST /worlds`.
- public world creation response.
- optional director guidance public endpoint.
- provider readiness redaction.
- Validation Client compatibility probe.
- `WORLDENGINE_CONTRACT_READY` conclusion boundary.
- WorldEngine does not implement Validation Client operation logs, E2E, Codex
  browser run, second-Agent review, or human validation.

## 4. Current Blockers

External validation remains blocked:

- current WorldEngine public API lacks `/manifest`.
- current WorldEngine OpenAPI lacks a Validation Client-discoverable world
  creation endpoint.
- Validation Client still cannot create a WorldEngine-backed session.

These blockers can be closed only by a future implementation package or
implementation chat.

## 5. Future Implementation Done Criteria

The future implementation chat may write `WORLDENGINE_CONTRACT_READY` only when:

- `/health` returns 200.
- `/manifest` returns 200 with public redacted fields only.
- `/openapi.json` exposes a discoverable world creation endpoint.
- `POST /worlds` succeeds and returns public world id, status, public state,
  and visualization.
- director guidance endpoint is available, or manifest records a public
  unavailable reason.
- provider readiness leaks no secret, private prompt, or provider raw trace.
- Validation Client `/health/worldengine` reports `world_creation: available`.
- Validation Client `POST /sessions/worldengine` succeeds.
- `contract-readiness-checklist.zh.md` records the evidence.

## 6. Stop Rules

The future implementation chat must stop and record a non-ready conclusion if:

- public responses include keys, authorization headers, private prompts,
  provider raw traces, or Agent private state.
- world creation requires Validation Client to read private paths.
- Gate 1 requires changing Validation Client.
- provider readiness pretends to be ready.
- implementation introduces demo-world content or external validator behavior.

## 7. Handoff Prompt

Current handoff status:

```text
handoff-status.zh.md
```

Future implementation uses:

```text
implementation-handoff-prompt.zh.md
```
