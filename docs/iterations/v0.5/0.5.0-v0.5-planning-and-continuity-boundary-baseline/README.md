# 0.5.0 v0.5 Planning And Continuity Boundary Baseline

Status: planned / ready for review
Type: documentation-only
implementation_authorized: no

## Goal

Create the v0.5 documentation root, `/goal` campaign controls, version plan,
memory/self-continuity boundary, compatibility baseline, and v0.4 handoff
mapping without changing implementation files.

## Scope

Allowed:

- create parent v0.5 campaign docs under `docs/iterations/v0.5/`.
- create this child package under
  `docs/iterations/v0.5/0.5.0-v0.5-planning-and-continuity-boundary-baseline/`.
- define the v0.5 capability split across working memory, episodic memory,
  relationship state, self-summary, reflection records, and personality drift
  signals.
- define planned child sequence and review gates.
- record v0.4 final closeout and v0.4 post-closeout clean pass as handoff
  evidence only.

Forbidden:

- do not modify runtime, schema, API, frontend, backend test, fixture,
  migration, generated result, external repository, or `backend/worldengine/`
  implementation files.
- do not implement memory, self-continuity, loop integration, public APIs,
  frontend behavior, durable persistence, migrations, or tests.
- do not add concrete world data, application-specific backend logic, private
  validation oracle details, world generation, external validation readiness,
  or projection app readiness.

## Deliverables

- v0.5 parent campaign docs and Chinese mirrors.
- `0.5.0` child package docs and Chinese mirrors.
- Documentation-stage verification plan and review evidence.
- Explicit handoff to `0.5.1-memory-self-continuity-contracts`.

## Documents

- [x] `README.md`
- [x] `README.zh.md`
- [x] `intent.md`
- [x] `intent.zh.md`
- [x] `contract.md`
- [x] `contract.zh.md`
- [x] `technical-design.md`
- [x] `technical-design.zh.md`
- [x] `test-plan.md`
- [x] `test-plan.zh.md`
- [x] `plan.md`
- [x] `plan.zh.md`
- [x] `review.md`
- [x] `review.zh.md`

## Current Assessment

This package is documentation-stage only and ready for review after
documentation verification is recorded in `review.md`.

