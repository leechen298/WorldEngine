# Technical Design

## Documentation Structure

This documentation-only package defines a contract and taxonomy. It includes
`technical-design.md` and `test-plan.md` because it changes version semantics,
evidence rules, package sequencing, and automation-consumption vocabulary.

## Affected Files

Allowed files:

- this package's seven English documents and seven Chinese mirrors.
- parent v0.8 route/status files.

No runtime, schema, API, frontend, backend test, checker implementation,
fixture, migration, generated result, external repository, or legacy
implementation file is affected.

## Data / Control Flow

1. `CURRENT_STATE.md` routes to `0.8.1-documentation-package-needed`.
2. This package defines required core slices and claim taxonomy.
3. Parent state moves to `0.8.2-documentation-package-needed`.
4. `0.8.2` uses the taxonomy to define observable public surfaces.

## Compatibility Strategy

- Keep all current behavior unchanged.
- Treat this package as contract vocabulary only.
- Record all runtime/API/frontend/E2E/Agent/autonomous/external validation
  checks as not run.
- Prevent v0.7 handoff evidence from becoming v0.8 pass evidence.

## Anti-Drift Rules

- `core contract ready` must not be written as runtime pass.
- `external validation handoff ready` must not be written as external
  validation PASS.
- `blocked`, `skipped`, and `out of scope` must not count as pass.
- Any future implementation package must identify the exact claim taxonomy
  values it is allowed to change.
