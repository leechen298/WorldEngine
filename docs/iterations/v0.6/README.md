# v0.6 World Generation v1

Status: final / closeout complete
Type: Codex `/goal` development campaign and iteration package root

## Goal

v0.6 defines and then incrementally implements World Generation v1: generating
runnable `WorldSpec` data from templates and structured AI-assisted generation
plans with validation, metadata, preview, and regeneration support.

The version starts from the v0.5 final closeout handoff and the v0.3
`WorldSpec` loader/runtime-context bridge. It keeps generated content generic,
inspectable, and contract-driven. It must not put concrete demo worlds,
external validation worlds, application-specific backend behavior, or private
validation oracle details into the WorldEngine core repository.

## Goal Entry

Natural-language goal:

```text
完成 v0.6
```

Interpretation:

- Start from `CURRENT_STATE.md`.
- Follow `GOAL_RUNNER.md` for route selection, documentation gates,
  implementation authorization, evaluator checkpoints, verification, and stop
  conditions.
- Follow `CAMPAIGN_PLAN.md` and `v0.6-plan.md` for child sequence,
  deliverables, compatibility constraints, and handoff rules.
- Read the active child package documents before doing child work.

This is not an automation-controller implementation. Scheduling,
orchestration, retry infrastructure, and Codex role assignment remain outside
WorldEngine.

## Scope

Allowed v0.6 scope:

- generation request, template, structured generation plan, generation result,
  generation metadata, preview, and regeneration public concepts.
- generic template semantics that can produce valid `WorldSpec` data without
  storing concrete demo-world content in the core repository.
- deterministic generator core for reviewed template and structured-plan
  inputs.
- provider-independent AI-assisted generation boundary where AI output is a
  structured plan to validate, not an unreviewed hidden side effect.
- validation through existing `WorldSpec` and loader/runtime-context bridge
  surfaces.
- generation preview and regeneration support after reviewed packages
  authorize them.
- focused backend, API, frontend, E2E, and compatibility tests only when a
  reviewed child package explicitly authorizes those surfaces.

Forbidden v0.6 scope:

- Do not add external validation runner readiness or report automation; v0.7
  owns that scope.
- Do not add first external projection application readiness; v0.8 owns that
  scope.
- Do not add concrete world names, maps, characters, locations, resources,
  story rules, seed data, UI-specific app behavior, or private validation
  oracle details.
- Do not add durable persistence or migrations unless a reviewed v0.6 child
  explicitly authorizes them.
- Do not make generated worlds depend on live external LLM calls unless a
  reviewed child package explicitly authorizes provider configuration, failure
  handling, security boundaries, and tests.
- Do not add new runtime features under `backend/worldengine/`.
- Do not claim full autonomous validation, external validation readiness, or
  projection readiness from v0.6 evidence.

## Deliverables

- Parent goal-campaign documents: `README.md`, `v0.6-plan.md`,
  `GOAL_RUNNER.md`, `CURRENT_STATE.md`, `CAMPAIGN_PLAN.md`, and `review.md`,
  with Chinese mirrors.
- Reviewed child packages through `0.6.1`, including the first child package:
  `0.6.0-v0.6-planning-and-generation-boundary-baseline`, with README,
  intent, contract, technical design, test plan, plan, review, and Chinese
  mirrors, and
  `0.6.1-world-generation-contracts-and-template-semantics`, with the same
  full document set and Chinese mirrors.
- Planned child package sequence through final closeout.
- Explicit evaluator checkpoint rules for `/goal` execution.
- Documentation-stage review evidence proving the first package does not
  modify runtime, schema, API, frontend, test implementation, fixture,
  migration, external repository, generated result, or `backend/worldengine/`
  files.

## Package Index

### `0.6.0-v0.6-planning-and-generation-boundary-baseline`

- Type: documentation-only
- Status: review complete
- Purpose: create the v0.6 documentation root, goal-campaign controls,
  version plan, generation boundary, compatibility baseline, and v0.5 handoff
  mapping without changing implementation files.

### `0.6.1-world-generation-contracts-and-template-semantics`

- Type: documentation-only
- Status: review complete
- Purpose: define generation public concepts, request/result semantics,
  template semantics, structured-plan semantics, metadata, preview,
  regeneration, compatibility rules, and authorization criteria before code.

### `0.6.2-template-catalog-and-deterministic-generator-core`

- Type: mixed or code
- Status: review complete
- Purpose: implement only generic template contracts, a deterministic
  template-to-`WorldSpec` generator core, and focused backend tests.

### `0.6.3-structured-generation-plan-compiler`

- Type: mixed or code
- Status: review complete
- Purpose: compile validated structured generation plans into valid
  `WorldSpec` data without introducing concrete world content or hidden AI
  side effects.

### `0.6.4-ai-assisted-generation-boundary-and-plan-import`

- Type: mixed or code
- Status: review complete
- Purpose: add provider-independent AI-assisted plan import boundaries,
  validation, error reporting, and mock-provider tests without requiring live
  external LLM calls.

### `0.6.5-generation-validation-metadata-and-preview-api`

- Type: mixed or code
- Status: review complete
- Purpose: expose reviewed backend schemas/services/API for generation
  validation, metadata, and preview while preserving existing API envelopes.

### `0.6.6-regeneration-and-runtime-readiness-integration`

- Type: mixed or code
- Status: review complete
- Purpose: add bounded regeneration support and prove generated specs can pass
  loader/runtime-context readiness without changing unrelated runtime tick
  behavior.

### `0.6.7-dashboard-generation-preview-and-e2e-smoke`

- Type: mixed or code
- Status: review complete
- Purpose: add a dashboard-facing generation preview workflow and browser E2E
  smoke only after backend/API generation contracts are stable.

### `0.6.8-v0.6-evidence-and-compatibility-audit`

- Type: documentation-only
- Status: review complete
- Purpose: audit v0.6 implementation evidence, compatibility surfaces,
  unresolved findings, and release-candidate readiness.

### `0.6.9-v0.6-release-candidate-bundle`

- Type: documentation-only
- Status: review complete
- Purpose: prepare a release-candidate bundle from reviewed implementation and
  audit evidence without declaring final release.

### `0.6.10-v0.6-final-closeout`

- Type: documentation-only
- Status: final / closeout complete
- Purpose: mark v0.6 final / closeout complete only after release-candidate
  approval, evidence consistency checks, and unresolved finding
  classification.

### `0.6.11-post-closeout-reliability-and-scope-repair`

- Type: mixed post-closeout repair
- Status: review complete
- Purpose: authorize and repair the post-closeout reliability/scope findings
  from the 2026-06-01 validation run, including failed-generation fallback seed
  digest reliability, public preview API sensitive provenance coverage, and
  implementation evidence synchronization.

## Current State

Active child package:
none.

Current route: `final-closeout-complete`.

Implementation authorization: no.

## Handoff Baseline

- v0.5 status: `final / closeout complete`.
- v0.5 final backend evidence is handoff evidence only, not current v0.6 pass
  evidence.
- v0.5 final closeout does not claim frontend, E2E, Agent smoke, autonomous,
  external validation, projection readiness, or product readiness checks
  passed.
- v0.6 starts from its own package review gates and does not inherit
  implementation authorization from v0.5.

## Final Assessment State

Current value: `final / closeout complete`.

`0.6.0-v0.6-planning-and-generation-boundary-baseline`,
`0.6.1-world-generation-contracts-and-template-semantics`,
`0.6.2-template-catalog-and-deterministic-generator-core`, and
`0.6.3-structured-generation-plan-compiler` have review complete evidence
recorded. `0.6.4-ai-assisted-generation-boundary-and-plan-import` is review
complete and hands reviewed import/provenance semantics to `0.6.5`.
`0.6.5-generation-validation-metadata-and-preview-api` is review complete and
hands public preview/API metadata semantics to
`0.6.6-regeneration-and-runtime-readiness-integration`. `0.6.6` is review
complete and hands stable regeneration/readiness API semantics to
`0.6.7-dashboard-generation-preview-and-e2e-smoke`. `0.6.7` is review
complete and hands dashboard preview plus E2E smoke evidence to
`0.6.8-v0.6-evidence-and-compatibility-audit`. `0.6.8` is review complete and
hands evidence/compatibility audit results to
`0.6.9-v0.6-release-candidate-bundle`. `0.6.9` is review complete and hands
release-candidate approval to `0.6.10-v0.6-final-closeout`. `0.6.10` is
`final / closeout complete`. `0.6.11` is a post-closeout reliability/scope
repair package with clean pass for its authorized repair scope; no v0.6 child
package remains active.
