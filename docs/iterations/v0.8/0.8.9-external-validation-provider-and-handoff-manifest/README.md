# 0.8.9 External Validation Provider And Handoff Manifest

Status: planned / ready for review
Type: documentation-only planning package
implementation_authorized: no
evidence_execution_authorized: no

Chinese mirror: `README.zh.md`.

## Package

Name: `0.8.9-external-validation-provider-and-handoff-manifest`

This post-closeout planning package defines the WorldEngine-side prerequisites
for an external validation client to run Agent autonomous validation and hand
off evidence to human validation.

It does not reopen the v0.8 final closeout. It records a new, reviewable
planning package for future implementation chats.

## Goal

Define how WorldEngine should expose public, redacted, validation-consumable
provider readiness and handoff manifest information without moving external
validator logic, private scenarios, product UI, concrete world content, LLM
secrets, or application-specific behavior into the core repository.

## Documents

- [x] `README.md`
- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `validation-client-contract-handoff.md`
- [x] `implementation-task-plan.md`
- [x] `contract-readiness-checklist.md`
- [x] `external-validation-gate-matrix.md`
- [x] `planning-readiness-checklist.md`
- [x] `handoff-status.md`
- [x] `implementation-handoff-prompt.md`
- [x] `review.md`
- [x] Chinese mirrors

## Scope Summary

This package may define documentation for:

- LLM provider validation boundary.
- Provider class labels and redacted provider readiness status.
- Public handoff manifest fields that an external validation client may
  consume.
- Validation Client contract handoff requirements for world creation and
  director guidance.
- Evidence classification for blocked, skipped, unavailable, partial, and
  ready states.
- Stop rules for missing provider, missing public manifest, or insufficient
  public surfaces.

This package must not implement:

- provider runtime code.
- API routes.
- schema files.
- checker code.
- tests.
- migrations.
- external validation application behavior.

## Provider Boundary

WorldEngine owns provider configuration and credential handling. External
validation clients may observe public provider readiness labels and public
failure summaries, but must not manage provider API keys or call provider APIs
directly.

Provider options discussed for future implementation:

- Kimi Code subscription / `kimi-for-coding`: useful for coding-agent or
  developer-tool scenarios, with OpenAI-compatible and Anthropic-compatible
  endpoints, membership quota, and `kimi-for-coding` model id.
- Kimi Platform / Moonshot API: more appropriate for product-style
  programmatic runtime integration and pay-as-you-go API evaluation.
- DeepSeek API: pay-as-you-go fallback option whose usage must be bounded with
  max tokens, rate limits, and budget controls.

The future implementation must decide provider usage through WorldEngine
contracts, not through the validation client.

## Validation Client Contract Handoff

Detailed contract handoff plan:

```text
validation-client-contract-handoff.md
validation-client-contract-handoff.zh.md
implementation-task-plan.md
implementation-task-plan.zh.md
contract-readiness-checklist.md
contract-readiness-checklist.zh.md
external-validation-gate-matrix.md
external-validation-gate-matrix.zh.md
planning-readiness-checklist.md
planning-readiness-checklist.zh.md
handoff-status.md
handoff-status.zh.md
implementation-handoff-prompt.md
implementation-handoff-prompt.zh.md
```

External validation gate matrix:

```text
external-validation-gate-matrix.md
external-validation-gate-matrix.zh.md
```

The matrix states that WorldEngine owns only the
`WORLDENGINE_CONTRACT_READY` gate. It does not own Validation Client operation
logs, Codex browser autonomous validation, second-Agent review, or human
experience judgment.

Planning readiness checklist:

```text
planning-readiness-checklist.md
planning-readiness-checklist.zh.md
```

This checklist only proves the 0.8.9 planning package is ready for user review
and future implementation chat. It does not prove `WORLDENGINE_CONTRACT_READY`.

Handoff status:

```text
handoff-status.md
handoff-status.zh.md
```

This status records the current implementation wait state, current blockers,
and `WORLDENGINE_CONTRACT_READY` completion criteria in one page.

Current observed blocker:

- Validation Client can reach WorldEngine `/health` and `/openapi.json`.
- Validation Client cannot create a WorldEngine-backed session because OpenAPI
  does not expose a Validation Client-discoverable world creation endpoint.
- `/manifest` is also missing.

Future implementation must close those gaps before external browser
autonomous validation can claim ready-for-human-validation.

## Handoff

After review, future implementation may create a concrete child package to add
contract files, schemas, checkers, API docs, or public endpoint changes. Until
that package is reviewed, this package is documentation-only and does not
authorize runtime changes.
