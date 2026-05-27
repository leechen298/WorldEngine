# Intent

## Problem

`0.3.1` defines the WorldSpec loader contract, but WorldEngine still has no
implementation that can accept generic `WorldSpec` input and return either a
validated loaded result or structured loader errors. Without a scoped
implementation package, loader code could accidentally gain runtime authority,
invent fixture policy, or blur into the future runtime bridge.

## Goal

Add the minimal loader implementation and focused tests needed to satisfy
`docs/contracts/worldspec-loader-contract.md`.

Successful completion means the loader can:

- accept supported domain-neutral input forms.
- validate data through the existing `WorldSpec` schema.
- return neutral source metadata on success.
- return stable structured errors on unsupported input, parse failure, schema
  validation failure, and file I/O failure if file input is implemented.
- prove through tests that it has no runtime, API, event, persistence, archive,
  params, or frontend side effects.

## Non-goals

- Do not connect loaded data to `RuntimeEngine`.
- Do not define or implement runtime context bridge semantics.
- Do not add API routes, service endpoints, persistence models, archive writes,
  params application, event emission, frontend behavior, fixtures, or
  migrations.
- Do not create concrete demo-world or external validation-world input data.
- Do not implement world generation, Agent-in-World loop, memory,
  self-continuity, projection, story generation, or NPC chat behavior.

## Why Now

v0.3 bridges the v0.2 `WorldSpec` schema foundation toward runtime context in
small reviewable steps. The loader must exist and be tested before `0.3.3`
defines how loaded data may become runtime context.

## North Star Alignment

This package supports WorldEngine as a generic recursive world engine by
creating a domain-neutral data entry point for structured world specifications.
It preserves the boundary between specification loading and runtime execution,
keeping application-specific worlds and external validation internals outside
the core repository.

## Assumptions

- `0.3.1-worldspec-loader-contract` has been reviewed and remains the
  normative loader contract.
- `WorldSpec` in `backend/app/schemas/world_cell.py` remains the validation
  source for this package.
- A minimal loader is useful before runtime bridge work because it establishes
  validated data and error semantics independently.
- File-backed JSON input is optional; if omitted, `io_error` behavior is not
  required beyond documenting that file input is unsupported.

## Open Risks

- Pydantic error structures may expose more detail than the public loader
  contract needs; implementation must normalize errors without relying on
  private formatting.
- File-backed input could expand scope into fixture directories if not limited
  to one caller-supplied JSON document.
- Source labels could accidentally carry domain meaning; tests and docs must
  keep labels neutral.
- Future bridge work may need additional metadata, but this package must not
  predesign runtime context fields.
