# 0.8.9.1 Public Handoff Manifest And World Creation Contract

Status: drafted / ready for user review
Type: mixed implementation package
implementation_authorized: no
evidence_execution_authorized: no

Chinese mirror: `README.zh.md`.

## Package

Name: `0.8.9.1-public-handoff-manifest-and-world-creation-contract`

This package is the concrete implementation child package for
`0.8.9-external-validation-provider-and-handoff-manifest`.

It exists because the 0.8.9 parent addendum is documentation-only and does not
authorize runtime, API, schema, test, or evidence changes. This package defines
the reviewed implementation gate required before adding WorldEngine public
contract surfaces for external Validation Client consumption.

## Goal

Implement the WorldEngine-side public contract required for external
Validation Client handoff:

- `GET /manifest` returns a redacted public handoff manifest.
- `POST /worlds` is OpenAPI-discoverable by Validation Client world creation
  probes.
- world creation returns public world id, status, initial state, and
  visualization payload.
- provider readiness is exposed only through redacted public labels.
- director guidance is either exposed as a public endpoint or recorded as
  unavailable in the manifest.

## Required Documents

- [x] `README.md`
- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`
- [x] Chinese mirrors

## Scope Summary

Allowed once this package is reviewed and implementation is explicitly
authorized:

- add public schema models under `backend/app/schemas/`.
- add public routes under `backend/app/api/routes/`.
- register routes in the active FastAPI app factory.
- reuse existing generation/readiness helpers to create a generic public world
  summary.
- add focused backend tests proving OpenAPI discoverability, response shape,
  and redaction.
- update this package's `review.md` and `review.zh.md` with implementation
  evidence.

Forbidden:

- Validation Client repository changes.
- concrete demo-world content.
- provider API calls or credential storage.
- raw provider traces, private prompts, raw responses, private evaluator data,
  product UI selectors, private Agent memory, private goals, `self_state`, or
  hidden context in public output.
- changes under `backend/worldengine/`.
- claims of external validation PASS, Codex autonomous PASS, or human
  validation PASS.

## Handoff

This package is ready for user review only. Implementation may start only after
the user approves this implementation package or otherwise explicitly records
that this package's contract, technical design, test plan, and plan are
approved for implementation.
