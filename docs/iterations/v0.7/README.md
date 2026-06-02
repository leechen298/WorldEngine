# v0.7 External Validation Readiness / Projection Consumer Readiness

Status: final / closeout complete
Type: Codex `/goal` development campaign and iteration package root

## Goal

v0.7 prepares WorldEngine for external validation suites and projection
consumers through stable public contracts, redacted validation reports,
consumer-facing projection contracts, and compatibility evidence.

The version starts from the v0.6 final closeout and the 0.6.11 reliability and
scope repair handoff. It must keep external validation worlds and projection
applications as consumers of WorldEngine. It must not move concrete validation
worlds, private oracle behavior, product-specific UI, or application-specific
backend logic into the core repository.

## Goal Entry

Natural-language goals:

```text
完成 v0.7
启动 WorldEngine v0.7：External Validation Readiness / Projection Consumer Readiness
编写 v0.7 文档
```

Interpretation:

- Start from `CURRENT_STATE.md`.
- Follow `GOAL_RUNNER.md` for route selection, documentation gates,
  implementation authorization, evaluator checkpoints, verification, and stop
  conditions.
- Follow `CAMPAIGN_PLAN.md` and `v0.7-plan.md` for child sequence,
  deliverables, compatibility constraints, and handoff rules.
- Treat this parent v0.7 package as the only current authoritative entrypoint.
- Before any future child package starts, create or confirm that child's full
  package document set and complete its review gate. Do not treat the planned
  `0.7.x` roadmap entries as execution-approved child contracts.

This is not an external automation controller, external validation suite, or
projection application implementation. Scheduling, orchestration, retry
infrastructure, private fixtures, and Codex role assignment remain outside
WorldEngine.

## Scope

Allowed v0.7 scope:

- external validation readiness public concepts, report semantics, and
  redacted evidence rules.
- projection consumer public concepts and read-only consumption boundaries.
- contract bundles, readiness manifests, compatibility matrices, and evidence
  retention rules that can be consumed by external suites.
- generic report schemas, redaction checks, saved-result checks, and
  documentation/audit tooling when a reviewed child package authorizes them.
- quality regression evidence for public engine contracts, limited to commands
  and checkers that actually run in the current session.
- focused backend, API, frontend, E2E, Agent smoke, autonomous, and
  compatibility checks only when a reviewed child package explicitly
  authorizes those surfaces.

Forbidden v0.7 scope:

- Do not implement the first external projection application; v0.8 owns that
  scope.
- Do not place external validation repositories, concrete validation worlds,
  seed data, maps, characters, locations, resources, story rules, private
  transcripts, UI selectors, or oracle internals in this repository.
- Do not add application-specific backend logic, hidden reset APIs, or product
  packaging behavior.
- Do not claim external suite PASS, projection application readiness,
  generation-quality PASS, full product readiness, live provider behavior, new
  live Agent smoke, or full autonomous runner/full-suite PASS without
  current-session evidence.
- Do not add durable persistence or migrations unless a reviewed v0.7 child
  explicitly authorizes them.
- Do not add new runtime features under `backend/worldengine/`.

## Deliverables

- Parent goal-campaign documents: `README.md`, `v0.7-plan.md`,
  `GOAL_RUNNER.md`, `CURRENT_STATE.md`, `CAMPAIGN_PLAN.md`, and `review.md`,
  with Chinese mirrors.
- Reviewed `0.7.0` documentation-only child package documents, with Chinese
  mirrors, for the planning and external-validation boundary baseline.
- Reviewed `0.7.1` documentation-only public readiness and projection
  contract package, with Chinese mirrors.
- Reviewed `0.7.2` mixed package documents, with Chinese mirrors, authorizing
  only the report schema/checker/template/test implementation scope.
- Reviewed `0.7.3` mixed contract bundle and readiness manifest package, with
  Chinese mirrors.
- Reviewed `0.7.4` mixed projection read-model contract package, with Chinese
  mirrors.
- Reviewed `0.7.5` quality regression and compatibility evidence package,
  with Chinese mirrors.
- Reviewed `0.7.6` evidence and compatibility audit package, with Chinese
  mirrors.
- Reviewed `0.7.7` release-candidate bundle package, with Chinese mirrors.
- Reviewed `0.7.8` final closeout package, with Chinese mirrors.
- Explicit subagent/evaluator checkpoint rules for `/goal` execution.
- Documentation-stage review evidence proving this drafting pass does not
  modify runtime, schema, API, frontend, test implementation, fixture,
  migration, external repository, generated result, or `backend/worldengine/`
  implementation files.

## Planned Package Roadmap

The `0.7.x` entries below and in `v0.7-plan.md` are roadmap-level planned
package specs. They are not current implementation authorization, not
execution-approved contracts, and not an immutable script. A future agent must
create or confirm the active child package documents at the time that child
starts, then complete review before implementation. If implementation reveals
a design gap, stop implementation, update the active child's
`contract.md`, `technical-design.md`, `test-plan.md`, `plan.md`, and
`review.md`, and resume only after the updated package is reviewed.

### `0.7.0-v0.7-planning-and-external-validation-boundary-baseline`

- Type: documentation-only
- Status: review complete
- Purpose: create the v0.7 documentation root, goal-campaign controls,
  version plan, external-validation/projection boundary, compatibility
  baseline, and v0.6 handoff mapping without changing implementation files.

### `0.7.1-public-validation-and-projection-contracts`

- Type: documentation-only
- Status: review complete
- Purpose: define public external-validation readiness concepts, redacted
  report semantics, projection consumer boundaries, and authorization criteria
  before any code or checker work.

### `0.7.2-validation-report-schema-and-redaction-checker`

- Type: mixed or code
- Status: review complete
- Purpose: implement generic report schema/checker support for redacted
  validation evidence after `0.7.1` contracts are reviewed.

### `0.7.3-contract-bundle-and-readiness-manifest`

- Type: mixed or code
- Status: review complete
- Purpose: expose a generic contract bundle and readiness manifest that
  external suites can consume without private repository knowledge.

### `0.7.4-projection-consumer-read-model-contracts`

- Type: mixed or code
- Status: review complete
- Purpose: define and, if authorized, expose read-only projection consumer
  payloads for runtime, events, Agent loop, memory context summaries, and
  generation readiness without building a product application.

### `0.7.5-quality-regression-and-compatibility-evidence`

- Type: mixed or code
- Status: review complete
- Purpose: run and record generic regression and compatibility evidence for
  public engine contracts touched by v0.7.

### `0.7.6-v0.7-evidence-and-compatibility-audit`

- Type: documentation-only
- Status: review complete
- Purpose: audit v0.7 implementation evidence, compatibility surfaces,
  unresolved findings, and release-candidate readiness.

### `0.7.7-v0.7-release-candidate-bundle`

- Type: documentation-only
- Status: review complete
- Purpose: prepare a release-candidate bundle from reviewed implementation and
  audit evidence without declaring final release.

### `0.7.8-v0.7-final-closeout`

- Type: documentation-only
- Status: review complete / final closeout complete
- Purpose: mark v0.7 final / closeout complete only after release-candidate
  approval, evidence consistency checks, scope review, and unresolved finding
  classification.

## Current State

Active child package: none; `0.7.8-v0.7-final-closeout` completed final
closeout.

Current route: `complete`.

Implementation authorization: no.

Evidence execution authorization: closed after final verification.

## Handoff Baseline

- v0.6 status: `final / closeout complete`, with 0.6.11 post-closeout
  reliability and scope repair complete.
- v0.6 evidence is handoff evidence only, not current v0.7 PASS evidence.
- v0.6 explicitly does not claim external validation readiness, projection
  readiness, product readiness, full autonomous runner/full-suite PASS, live
  provider behavior, generation-quality PASS, or durable generated-world
  persistence.
- v0.7 starts from its own package review gates and does not inherit
  implementation authorization from v0.6.

## Final Assessment State

Current value: `final / closeout complete`.

The parent v0.7 campaign docs passed read-only parent documentation review and
`0.7.0`, `0.7.1`, `0.7.2`, `0.7.3`, `0.7.4`, `0.7.5`, `0.7.6`, `0.7.7`,
and `0.7.8` are review complete. Final verification and evaluator review
passed in `0.7.8`. No runtime, schema, API, frontend, test implementation,
fixture, migration, external repository, generated result, or legacy
implementation work is authorized by this final state.
