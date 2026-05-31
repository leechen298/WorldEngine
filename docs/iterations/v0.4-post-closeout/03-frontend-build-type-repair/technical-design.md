# Technical Design

## Current State

`cd frontend && pnpm build` fails in TypeScript checking:

- Vue Test Utils `get()` returns a wrapper type that intentionally omits
  `exists()`, because `get()` throws when the selector is missing.
- `TimelinePanel.vue` passes a zero-argument object-literal function to
  Ant Design Vue `customRow`; the inferred return object has no typed overlap
  with `GetComponentProps<any>`.

## Contract Alignment And Invariants

The implementation must keep the same selectors and test intent:

- presence assertions remain presence assertions.
- text assertions continue to use required selectors.
- `TimelinePanel` still attaches `data-test="timeline-row"` to table rows.

No backend, API, schema, migration, or autonomous-runner behavior may change.

## Proposed Implementation

1. Replace `.get(selector).exists()` presence checks with
   `.find(selector).exists()` at the reported test lines. This preserves the
   assertion while using the Vue Test Utils API whose type exposes `exists()`.
2. Give `TimelinePanel` `customRow` an Ant Design Vue-compatible function type
   and return the row `data-test` attribute through a typed helper object.

## Affected Surfaces

- Frontend component tests:
  - `MemoryPanel.test.ts`
  - `TimelinePanel.test.ts`
  - `WorldPanel.test.ts`
- Frontend component typing:
  - `TimelinePanel.vue`
- Iteration/evidence docs named by the contract.

## Data Model / Schema Changes

None.

## Runtime / Service Design

No backend service or runtime flow changes. The only product-file change is a
typed row-prop helper for an existing dashboard table selector.

## Compatibility

Dashboard markup keeps the same `data-test` selectors. Existing tests and E2E
selectors should keep working.

## Risks

- A type assertion around `customRow` could hide an incompatible return shape.
  The build and Vitest rerun detect compile-time and test-level regressions.
- The build fix could reveal later TypeScript failures. The package records
  any new failure as the actual blocker.
