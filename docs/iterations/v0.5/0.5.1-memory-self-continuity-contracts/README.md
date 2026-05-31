# 0.5.1 Memory Self-Continuity Contracts

Status: review complete
Type: documentation-only
implementation_authorized: no

## Goal

Define the public memory and self-continuity concepts that v0.5 may later
implement: working memory, episodic memory, relationship state, self-summary,
reflection record, and personality drift signal.

This package establishes schema semantics, provenance expectations,
authorization criteria, compatibility requirements, and explicit non-goals
before any runtime, schema, API, service, frontend, fixture, migration, or
test implementation changes occur.

## Scope

Allowed:

- create and update this package's documentation and Chinese mirrors.
- define public concept contracts for the six v0.5 memory/self-continuity
  surfaces.
- define planned additive schema semantics for later implementation packages.
- define the authorization criteria that `0.5.2` must satisfy before adding
  working-memory and episodic-memory code.

Forbidden:

- do not implement schemas, stores, services, APIs, frontend behavior,
  fixtures, migrations, or tests.
- do not connect memory to the Agent Loop perception or action path.
- do not make memory, relationship state, self-summary, reflection, or
  personality drift alter action selection or action results.
- do not add concrete world names, maps, characters, locations, resources,
  story rules, seed data, private validation oracle details, or
  application-specific backend logic.
- do not modify `backend/worldengine/`.

## Deliverables

- Full package document set and Chinese mirrors.
- Contract semantics for all six v0.5 concepts.
- Implementation authorization criteria for `0.5.2`.
- Documentation-stage review evidence, evaluator evidence, and scope guard
  evidence.

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

This package is documentation-only and review complete. Implementation
authorization remains closed for this package; `0.5.2` must pass its own
documentation/contract evaluator before any code changes.
