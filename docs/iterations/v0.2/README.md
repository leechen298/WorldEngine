# v0.2 Recursive World Foundation

Status: planned

## Goal

v0.2 establishes the recursive world foundation for WorldEngine without
turning the project into a village game backend.

## Version Boundary

v0.2 may define documentation governance, WorldCell/WorldSpec schema language,
additive event structure, a reference WorldSpec fixture, and legacy directory
boundaries.

v0.2 must not implement full world generation, village runtime, agent
pseudo-self continuity, game UI, or a separate game repository.

## Package Index

| Package | Type | Status | Purpose |
|---|---|---|---|
| `0.2.1-project-north-star` | documentation-only | review complete | Establish north star, product model, scope, roadmap, iteration templates, and docs governance. |
| `0.2.2-recursive-world-contract` | code | review complete | Add EntityRef, WorldCell, WorldSpec schemas, and schema tests. |
| `0.2.3-event-contract-extension` | code | ready for review | Extend Event with optional structured references while preserving compatibility. |
| `0.2.4-worldspec-reference-fixture` | code | planned | Add and validate the first reference WorldSpec fixture. |
| `0.2.5-legacy-boundary-cleanup` | documentation-only | planned | Mark legacy backend path and update architecture boundary. |
| `0.2.6-release-closeout` | documentation-only | planned | Record v0.2 capability boundary, evidence, limitations, and next work. |

## Required Reading

- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/iterations/README.md`
- `docs/iterations/v0.2/v0.2-plan.md`
