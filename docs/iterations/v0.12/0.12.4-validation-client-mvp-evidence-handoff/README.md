# 0.12.4 Validation Client MVP Evidence Handoff

Chinese mirror: `README.zh.md`.

Status: review complete
Type: mixed documentation/contract package
implementation_authorized: no
provider_live_call_authorized: no
external_validation_authorized: no

## Goal

Define the public evidence artifacts, result directory shape, operation/API log
requirements, redaction checks, terminology, and handoff prompt that a separate
WorldEngine-Validation-Client iteration can use for MVP validation.

This package is a WorldEngine-side handoff contract. It does not implement the
external client, run provider live calls, operate an external validation agent,
or claim MVP PASS.

## Scope

Allowed after review approval:

- Define MVP evidence artifact names and required/optional fields.
- Define result directory shape for public exported evidence.
- Define operation-log and API-log requirements.
- Define scorecard inputs and status taxonomy.
- Define redaction scan requirements.
- Define in-world Agent versus external validation agent terminology.
- Add a Codex/OpenClaw-style handoff prompt for a future Validation Client
  iteration.
- Add focused schema/checker documentation or tests only if this package later
  records implementation authorization for them.

Forbidden:

- No Validation Client implementation in this repository.
- No client-owned provider calls, evaluator logic, world mutation, Agent
  autonomy, or PASS decision authority.
- No raw/private evidence, raw thought, private memory, private goals, hidden
  context, provider traces, raw prompts, raw provider responses, secrets, or
  private evaluator data.
- No provider live calls, external validation execution, frontend, autonomous
  validation, complete MVP closeout, or `backend/worldengine/` changes.

## Deliverables

- `mvp-evidence-artifact-contract.md`
- `validation-client-handoff-prompt.md`
- package docs, review evidence, and parent route update after closeout.

## Documents

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`
- [x] `mvp-evidence-artifact-contract.md`
- [x] `validation-client-handoff-prompt.md`

## Status Checklist

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [ ] Implementation authorized
- [ ] Implementation complete
- [ ] Tests complete
- [x] Review complete

## Current Assessment

Documentation evaluator review passed. This package is complete for the
WorldEngine-side MVP evidence handoff contract. No implementation, provider
live-call, or external validation execution was authorized.
