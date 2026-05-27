# Technical Design

## Current State

`WorldSpec` is defined by `backend/app/schemas/world_cell.py` and documented in
`docs/contracts/worldspec-contract.md`. v0.2 explicitly left loader behavior
unimplemented. v0.3 plans a loader package before any runtime bridge package.

## Contract Alignment and Invariants

The loader contract must preserve these invariants:

- schema validation remains delegated to `WorldSpec` or a reviewed wrapper.
- loaded data remains specification data.
- runtime, API, event, archive, params, frontend, fixture, migration, test, and
  legacy implementation files remain untouched in this package.
- examples remain domain-neutral.

## Proposed Future Implementation Shape

The later implementation package should add a small data-boundary module, most
likely under `backend/app/core/`, that:

1. accepts one supported input source.
2. parses only when needed.
3. validates the resulting mapping through `WorldSpec`.
4. returns a structured success or failure result.
5. performs no runtime side effects.

This package does not create that module.

## Affected Surfaces

Documentation surfaces affected by this package:

- `docs/contracts/worldspec-loader-contract.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/**`
- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`

Implementation surfaces intentionally unaffected:

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- tests, fixtures, migrations, API routes, schemas, runtime services.

## Data Model / Schema Changes

No schema changes are made. The future loader result names in the contract are
conceptual until `0.3.2` implements them.

## Runtime / Service Design

No runtime or service behavior changes in this package. The contract forbids
runtime authority for loaded data and reserves runtime context semantics for a
later bridge contract.

## Verification Design

Documentation verification should prove:

- package files exist.
- required headings and error categories exist in the loader contract.
- status is synchronized in English and Chinese milestone indexes.
- touched docs do not introduce concrete demo-world anchors.
- no implementation files were modified.
- `git diff --check` passes.

## Risks

- The future implementation could overfit to validation-library error text.
  The contract mitigates this by requiring stable error codes and testable
  paths without relying on private exception formatting.
- File-backed input could be mistaken for fixture directories. The contract
  limits file-backed input to one JSON document and forbids external
  repositories or fixture bundles.
- Bridge requirements could leak into loader scope. The contract states that
  loaded data is not runtime context.
