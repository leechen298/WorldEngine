# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Scope

This package is documentation-only. No runtime, API, schema, frontend, test,
fixture, migration, or external repository implementation is authorized.

## Documentation Checks

Run:

```bash
git status --short --branch
git diff --check
```

Check:

- required package files exist.
- Chinese mirrors exist.
- package status does not claim implementation complete.
- no runtime, API, schema, frontend, backend test, fixture, migration, or
  external repository files are touched by this package.

## Implementation Checks

Do not run implementation tests as pass evidence for this package. Backend,
frontend, E2E, Agent smoke, autonomous, live provider, and external validation
checks are out of scope until a future implementation package is reviewed.

## Provider Information Check

Provider claims must be treated as planning notes and must cite public
documentation in `technical-design.md` or final reports. Current provider
prices, quotas, and terms may change and must be rechecked during
implementation.

## Pass Criteria

This package can be ready for user review when:

- docs are present.
- mirrors are present.
- formatting check passes.
- scope review confirms docs-only changes.
- review records that runtime tests were not run and why.
