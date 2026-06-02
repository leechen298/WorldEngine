# Technical Design

## Documentation Structure

This package is documentation-only but includes `technical-design.md` and
`test-plan.md` because it defines observable surface semantics, evidence
rules, compatibility rules, and later implementation authorization criteria.

## Affected Files

Allowed files:

- this package's seven English documents and seven Chinese mirrors.
- parent v0.8 route/status files.

No runtime, schema, API, frontend, backend test, checker implementation,
fixture, migration, generated result, external repository, or legacy
implementation file is affected.

## Surface Design

The package organizes observable surfaces by family instead of endpoint
implementation. A later package may map a family to one or more API routes,
schemas, reports, manifests, or evidence bundles, but this package does not
create those artifacts.

Surface families must preserve these design rules:

- read-only by default.
- no hidden reset or private runner hooks.
- no concrete external validation content.
- bounded memory summaries only.
- status taxonomy from `0.8.1`.
- compatibility with v0.7 redaction and read-model rules.

## Compatibility Strategy

- Reuse v0.7 projection and external-validation contracts as the redaction
  baseline.
- Reuse `docs/current-implementation.md` and existing API references as source
  maps, not as new pass evidence.
- Preserve all current backend/frontend behavior.
- Defer implementation and focused tests to later reviewed packages.

## Anti-Drift Rules

- A surface family is not an implemented API.
- A read-model contract is not projection application readiness.
- An observable boundary is not minimum working-state evidence.
- External validation handoff is not external validation PASS.
- Bounded memory context is not raw memory export.
