# Intent

## Objective

Create a review-gated audit package that decides whether reviewed v0.8 evidence
is coherent enough to prepare a release-candidate bundle.

## Why This Exists

v0.8 has documentation contracts, one implementation-bearing readiness slice,
and one core-side smoke evidence package. Before release-candidate packaging,
the campaign needs a separate documentation-only audit that verifies evidence
references, status surfaces, compatibility boundaries, and non-claim language.

## In Scope

- Audit `0.8.0` through `0.8.5` review evidence.
- Confirm required evidence references resolve.
- Classify unresolved P1/P2/P3 findings.
- Confirm skipped, blocked, and out-of-scope checks were not converted to PASS.
- Confirm v0.7 handoff evidence is not promoted to current v0.8 PASS.
- Recommend whether release-candidate packaging may start.

## Out Of Scope

- Runtime, schema, API, frontend, backend test, checker, fixture, migration, or
  generated-result changes.
- New code repairs or implementation work.
- External validator or external app execution.
- Product readiness, external validation PASS, frontend/E2E PASS, Agent smoke
  PASS, autonomous PASS, generation-quality PASS, or final v0.8 readiness.

## Success Criteria

The package may close only when the audit report records no unresolved P1 or
blocking P2 for release-candidate packaging, or explicitly blocks handoff with
evidence.
