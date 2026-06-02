# 0.7.4 Projection Consumer Read Model Contracts

Status: review complete
Type: mixed
implementation_authorized: yes

## Goal

Define generic, read-only projection consumer read-model contracts for public
runtime, event, Agent loop, bounded memory context, generation-readiness, and
readiness-manifest summaries without building a product application.

## Scope

Allowed scope:

- Create this child package document set and Chinese mirrors.
- Add `docs/contracts/projection-read-model-contract.md`.
- Add `docs/contracts/projection-read-model-schema.json`.
- Add `tools/testing/validate_projection_read_model_contract.py`.
- Add `tools/testing/test_validate_projection_read_model_contract.py`.
- Update package review evidence and parent v0.7 route/status surfaces after
  review and closeout.

Forbidden scope:

- Do not add projection product UI, game UI, concrete world viewer, product
  dashboard, packaging flow, external app repository, write API, hidden reset
  API, private runner hook, persistence, migration, or consumer-specific
  backend behavior.
- Do not expose private application state, concrete worlds, character names,
  location names, maps, story rules, seed data, UI selectors, raw memory
  records, provider secrets, prompts, traces, transcripts, or event payloads.
- Do not claim projection application readiness, product readiness, external
  consumer PASS, runtime/API/frontend PASS, or v0.8 readiness.

## Deliverables

- Complete package docs and Chinese mirrors.
- Reviewed implementation authorization before code changes.
- Public projection read-model contract.
- Projection read-model schema with bounded, read-only payload families.
- Generic checker and focused tests for required model families, read-only
  fields, redaction rules, no write capability, and forbidden markers.
- Review evidence and handoff to `0.7.5`.

## Status Checklist

- [x] Package documents drafted.
- [x] Chinese mirrors drafted.
- [x] Documentation/contract evaluator complete.
- [x] Implementation authorization recorded.
- [x] Contract/schema/checker/tests complete.
- [x] Focused tests complete.
- [x] Implementation-scope evaluator complete.
- [x] Code-review evaluator complete.
- [x] Validation-evidence evaluator complete.
- [x] Closeout consistency review complete.
- [x] Parent v0.7 route updated.

## Final Assessment State

Current value: `review complete`.

Implementation and validation evidence are recorded. Parent v0.7 route is
handed off to `0.7.5-quality-regression-and-compatibility-evidence`.
