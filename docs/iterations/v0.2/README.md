# v0.2 Recursive World Foundation

Status: planned / in progress

## Goal

v0.2 establishes the recursive world foundation for WorldEngine without
turning the project into a demo-specific backend.

## Version Boundary

v0.2 may define documentation governance, WorldCell/WorldSpec schema language,
additive event structure, generic schema smoke validation, external fixture
boundaries, legacy directory boundaries, iterative automation workflow, and
release-candidate evidence.

v0.2 must not implement a WorldSpec loader, RuntimeEngine migration, runtime
bridge, Agent-in-World loop, memory/self-continuity substrate, world
generation, projection API, product UI, external fixture repository, external
validation repository, or concrete demo world fixture.

## Detailed Plan Source

This file is the summary index. The execution-grade remaining-package plan is
`docs/iterations/v0.2/v0.2-plan.md`.

## Package Index

### `0.2.1-project-north-star`

Type: documentation-only
Status: review complete
Purpose: Establish north star, product model, scope, roadmap, iteration
templates, and docs governance.

### `0.2.2-recursive-world-contract`

Type: code
Status: review complete
Purpose: Add EntityRef, WorldCell, WorldSpec schemas, and schema tests.

### `0.2.3-event-contract-extension`

Type: code
Status: review complete
Purpose: Extend Event with optional structured references while preserving
compatibility.

### `0.2.4-worldspec-reference-fixture`

Type: code
Status: historical artifact
Purpose: Historical concrete fixture package superseded by 0.2.5 for future
direction.

### `0.2.5-core-boundary-cleanup-and-roadmap-reset`

Type: mixed
Status: review complete
Purpose: Remove concrete external-world anchors, reset roadmap, and replace
fixture tests with generic schema smoke coverage.

### `0.2.6-iteration-workflow-and-plan-reset`

Type: documentation-only
Status: review complete
Purpose: Reset the remaining v0.2 plan, add iterative automation workflow
docs, and abstract residual concrete demo anchors in v0.2 iteration docs.

### `0.2.7-recursive-schema-contract-hardening`

Type: mixed
Status: review complete
Purpose: Harden EntityRef, WorldCell, and WorldSpec contracts and generic
schema tests without runtime loading.

### `0.2.8-event-reference-contract-hardening`

Type: mixed
Status: ready for review
Purpose: Harden EventRef and Event.refs as additive event reference contracts
without resolver or causality runtime.

### `0.2.9-generic-schema-evidence-and-boundary-audit`

Type: documentation-only or mixed
Status: planned
Purpose: Audit schema, event, external boundary, and legacy boundary evidence.

### `0.2.10-legacy-boundary-and-compatibility-review`

Type: documentation-only or mixed
Status: planned
Purpose: Clarify v0.1 runtime scaffold compatibility and legacy boundary
before v0.3 bridge work.

### `0.2.11-v0.2-release-candidate-bundle`

Type: documentation-only
Status: planned
Purpose: Prepare release-candidate evidence for human / ChatGPT review
without declaring final release.

### `0.2.12-v0.2-final-closeout`

Type: documentation-only
Status: planned
Purpose: Perform final closeout only after 0.2.11 review approval.

## Required Reading

- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/iterations/README.md`
- `docs/iterations/v0.2/v0.2-plan.md`
