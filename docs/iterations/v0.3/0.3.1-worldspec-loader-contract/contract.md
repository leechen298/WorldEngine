# Contract

## Public Concepts

- `WorldSpecLoader`: future component that accepts supported generic
  `WorldSpec` input and returns a structured result.
- `WorldSpecInput`: one candidate `WorldSpec` payload from a supported source.
- `LoadedWorldSpec`: validated `WorldSpec` plus neutral source metadata.
- `WorldSpecLoaderError`: structured error for unsupported, parse, validation,
  or input/output failures.
- `WorldSpecLoaderResult`: success or failure outcome from one loader call.

The normative public contract is
`docs/contracts/worldspec-loader-contract.md`.

## Compatibility Constraints

- Existing runtime behavior must stay compatible.
- Existing API response shapes must stay compatible.
- Existing event, archive, params, frontend-facing, and legacy path behavior
  must stay compatible.
- Existing `WorldSpec`, `WorldCell`, and `EntityRef` schema validation behavior
  must be preserved.
- Schema extensions remain additive unless a later reviewed package explicitly
  allows a breaking change.

## Allowed Changes

- Add `docs/contracts/worldspec-loader-contract.md`.
- Create the 0.3.1 package documentation.
- Update the v0.3 milestone index and mirrors to mark 0.3.1 `ready for
  review`.
- Update the v0.3 package plan and mirrors only for 0.3.1 status consistency.
- Define loader input, output, error, validation, and domain-neutral example
  semantics.
- Record documentation-stage verification evidence in `review.md`.

## Forbidden Changes

- Do not implement loader code.
- Do not connect loader behavior to `RuntimeEngine`.
- Do not modify schemas, runtime, API routes, services, frontend, fixtures,
  migrations, or tests.
- Do not create concrete WorldSpec fixture data.
- Do not create external fixture or validation repositories.
- Do not emit events, write persistence records, create archive snapshots, or
  apply params.
- Do not implement runtime bridge, world generation, Agent-in-World loop,
  memory, self-continuity, projection, story generation, or NPC chat behavior.

## Acceptance Requirements

- The loader contract explicitly states accepted input forms.
- The loader contract explicitly states successful output fields.
- The loader contract explicitly separates unsupported input, parse,
  validation, and file I/O errors.
- The loader contract requires validation through the existing `WorldSpec`
  schema or a reviewed wrapper.
- The loader contract states that loaded data is not runtime context.
- The package documents include assumptions, open risks, verification commands,
  and docs-only no-test rationale.
- English and Chinese milestone mirrors keep the 0.3.1 status synchronized.

## North Star Check

This package keeps WorldEngine generic. It defines an engine-level loader
boundary for structured world specs and explicitly forbids concrete demo-world
fixtures, product-specific backend behavior, and external validation internals.

## Out-of-Scope Follow-ups

- `0.3.2` may implement the minimal loader after review approval.
- `0.3.3` may define the runtime context bridge contract.
- `0.3.4` may implement a minimal optional runtime context bridge after its
  contract is reviewed.
- Later milestones may address Agent loops, memory, self-continuity,
  generation, projection, and external product validation.
