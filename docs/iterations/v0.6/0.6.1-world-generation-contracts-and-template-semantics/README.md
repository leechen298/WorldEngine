# 0.6.1 World Generation Contracts And Template Semantics

Status: review complete
Type: documentation-only
implementation_authorized: no

## Goal

Define the public World Generation v1 concepts, template semantics,
structured-plan semantics, generation metadata, preview and regeneration
boundaries, compatibility requirements, and implementation authorization
criteria that later v0.6 packages must follow.

This package does not implement generation behavior. It makes the first
implementation-bearing package reviewable by stating what generated data must
mean before any schema, service, API, frontend, fixture, migration, or test
implementation changes are allowed.

## Scope

Allowed:

- create this package under
  `docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/`.
- define public documentation concepts for:
  - `WorldGenerationRequest`
  - `WorldTemplate`
  - `GenerationPlan`
  - `GeneratedWorldSpec`
  - `GenerationMetadata`
  - `GenerationPreview`
  - `RegenerationRequest`
  - generation diagnostics
- define field-level semantics for future additive backend schemas.
- define template constraints that can produce valid generic `WorldSpec` data.
- define provider-independent AI-assisted generation as structured plan import,
  not hidden live model behavior.
- define authorization criteria for
  `0.6.2-template-catalog-and-deterministic-generator-core`.

Forbidden:

- do not implement schemas, stores, services, APIs, frontend, fixtures,
  migrations, generated result files, backend tests, or external repository
  changes.
- do not change `backend/app/**`, `frontend/**`, `backend/worldengine/**`,
  migrations, fixtures, generated outputs, or external validation artifacts.
- do not add concrete world names, maps, characters, locations, resources,
  story rules, seed data, private validation oracle details, or
  application-specific backend behavior.
- do not require live external AI-provider calls.
- do not claim generated-world quality, runtime behavior, API behavior, E2E,
  Agent smoke, autonomous validation, projection readiness, external
  validation readiness, release readiness, or product readiness.

## Deliverables

- Complete package documentation and Chinese mirrors.
- Contract semantics for generation requests, templates, plans, generated
  specs, metadata, previews, regeneration, and diagnostics.
- Compatibility constraints for current `WorldSpec`, loader,
  runtime-context bridge, runtime, loop, memory, event, params, archive, API
  envelope, and frontend-facing behavior.
- Explicit implementation authorization criteria for `0.6.2`.
- Documentation-stage review evidence and evaluator findings.

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

This documentation-only package is review complete. Documentation checks
passed, the read-only documentation evaluator reported PASS with no P1/P2/P3
findings, and implementation remains unauthorized. The package hands reviewed
contract semantics to
`0.6.2-template-catalog-and-deterministic-generator-core`.
