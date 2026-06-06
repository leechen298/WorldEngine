# 0.9.11 Validation Client Evidence Handoff Contract

Chinese mirror: `README.zh.md`.

Status: documentation reviewed / no implementation authorized
Type: documentation contract package
implementation_authorized: no
provider_live_call_authorized: no
evidence_execution_authorized: no
external_validation_authorized: no

## Package

Name: `0.9.11-validation-client-evidence-handoff-contract`

## Goal

Define the public evidence bundle and artifact fields that a Validation Client
may display or export for LLM-backed lifecycle evidence without making the
client own provider calls, LLM behavior, evaluation authority, or private
WorldEngine internals.

## Documents

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

## Scope Summary

This package is documentation-only. It defines stable public handoff contracts
for evidence artifacts produced by WorldEngine and checked by the autonomous
result checker. It may update this package and parent v0.9 routing/review
docs only.

It must not modify Validation Client code, frontend code, backend runtime
behavior, provider credential handling, checker implementation, fixtures,
generated results, external repositories, or `backend/worldengine/`.

## Status Checklist

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [x] Documentation review complete

## Current Route

```text
0.9.11-validation-client-evidence-handoff-contract-documentation-reviewed
```

Implementation remains unauthorized. A future package or external repository
milestone may implement client display/export behavior against this contract.
