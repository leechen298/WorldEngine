# v0.8 Minimum Proved Working WorldEngine / External Validation Readiness

Status: final / closeout complete
Type: Codex `/goal` development campaign and iteration package root

## Goal

v0.8 prepares WorldEngine to reach a minimum normally working state that an
external validation function can inspect from outside the core repository.

The version goal is not to build the external validation function or the first
external product application in this repository. The goal is to make the core
engine's generation, runtime, Agent loop, memory-context, event, and projection
surfaces coherent enough that a separate external validator or projection
application can judge whether WorldEngine works.

v0.8 starts from historical v0.7 closeout evidence plus the current `0.7.9`
checker/docs repair evidence. `0.7.9-v07-cr-checker-schema-repair` clears the
V07-CR checker/docs blocker gate for the current v0.7 checker/docs validation
scope, but it is handoff evidence only. It does not prove v0.8 clean pass,
minimum working-state PASS, external validation readiness PASS, product
readiness, external consumer PASS, runtime/API/frontend/E2E PASS, live Agent
smoke PASS, full autonomous PASS, or generation-quality PASS.

## Goal Entry

Natural-language goals:

```text
完成 v0.8
启动 WorldEngine v0.8：Minimum Proved Working WorldEngine / External Validation Readiness
编写 v0.8 文档
生成 v0.8 文档
```

Interpretation:

- Start from `CURRENT_STATE.md`.
- Follow `GOAL_RUNNER.md` for route selection, documentation gates,
  implementation authorization, evaluator checkpoints, verification, and stop
  conditions.
- Follow `CAMPAIGN_PLAN.md` and `v0.8-plan.md` for child sequence,
  deliverables, compatibility constraints, and handoff rules.
- Treat this parent v0.8 package as the only current authoritative entrypoint.
- Before any future child package starts, create or confirm that child's full
  package document set and complete its review gate. Do not treat planned
  `0.8.x` roadmap entries as execution-approved child contracts.

This is not an external validation application, external projection
application, external repository, product packaging workflow, deployment
process, concrete validation scenario, or application-specific backend.

## External Validation Boundary

WorldEngine may know that an external validation function will exist and will
verify whether the engine works. WorldEngine must not own the external
validator's implementation, private scenarios, product UI, application state,
runner internals, oracle logic, private repository paths, or concrete world
content.

Inside this repository, v0.8 may define only core-side public surfaces and
evidence expectations that make external validation possible:

- stable public API and read-model expectations.
- minimum working-state claim taxonomy.
- observable event, runtime, generation, Agent loop, and memory-context
  evidence boundaries.
- redaction and no-private-detail rules for any future external evidence.
- stop rules that prevent internal tests from being overclaimed as external
  validation PASS.

## Handoff Baseline From v0.7

The v0.7 parent route is historical `final / closeout complete`, and
`docs/testing/results/2026-06-02-v0.7-code-review.md` recorded post-closeout
issues across checker, schema, manifest, and projection read-model semantics.

The current v0.7 state records `0.7.9-v07-cr-checker-schema-repair` as review
complete. `docs/testing/results/2026-06-02-v0.7-overall-validation.md` records
clean pass for the current v0.7 checker/docs validation scope and clears the
V07-CR checker/docs blocker gate.

That repair evidence remains a bounded handoff baseline. It does not claim
external suite PASS, projection readiness PASS, product readiness PASS,
runtime/API/frontend/E2E PASS, live Agent smoke PASS, full autonomous
runner/full-suite PASS, or v0.8 readiness.

## Scope

Allowed v0.8 scope:

- minimum normally working WorldEngine readiness concepts.
- engine-side public surface requirements for external validation.
- core-side generation/runtime/Agent-loop/memory-context readiness boundaries.
- generic read-only projection or read-model payload hardening when a reviewed
  child package explicitly authorizes implementation.
- provider-boundary, credential, mock fallback, or live-smoke semantics only
  when a reviewed child package explicitly owns that scope.
- core-side smoke and compatibility evidence for public engine surfaces.
- release-candidate, final closeout, and post-closeout evidence documents.

Forbidden v0.8 scope:

- Do not implement the external validation function or external projection
  application inside this repository.
- Do not add concrete app worlds, names, maps, locations, characters,
  resources, story rules, seed data, UI selectors, private transcripts,
  product routes, product packaging, deployment scripts, or app-specific
  backend logic.
- Do not add private external repository paths, private runner state, hidden
  reset APIs, validation oracle internals, prompt/provider traces, secrets, or
  non-redacted external event payloads.
- Do not claim external validation PASS, external consumer PASS, product
  readiness, runtime/API/frontend/E2E PASS, Agent smoke PASS, autonomous PASS,
  or generation-quality PASS without current-session evidence.
- Do not add durable persistence, migrations, live provider behavior, or
  generated-world active runtime execution unless a reviewed child package
  explicitly authorizes that scope.
- Do not add new runtime features under `backend/worldengine/`.

## Deliverables

- Parent goal-campaign documents: `README.md`, `v0.8-plan.md`,
  `GOAL_RUNNER.md`, `CURRENT_STATE.md`, `CAMPAIGN_PLAN.md`, and `review.md`,
  with Chinese mirrors.
- Planned `0.8.x` child-package specifications inside `v0.8-plan.md`.
- Explicit v0.7 handoff-risk handling and stop rules.
- Explicit boundary rules stating that external validation is outside this
  repository while core-side readiness for that validation is in scope.
- Documentation-stage review evidence proving this drafting pass does not
  modify runtime, schema, API, frontend, test implementation, fixture,
  migration, external repository, generated result, or `backend/worldengine/`
  implementation files.

## Planned Package Roadmap

The `0.8.x` entries below and in `v0.8-plan.md` are roadmap-level planned
package specs. They are not current implementation authorization, not
execution-approved contracts, and not an immutable script. A future agent must
create or confirm the active child package documents at the time that child
starts, then complete review before implementation.

### `0.8.0-v0.8-planning-and-v0.7-handoff-baseline`

- Type: documentation-only
- Status: review complete
- Purpose: create the v0.8 documentation root, goal-campaign controls, v0.7
  handoff-risk baseline, minimum working-state boundary, external-validation
  boundary, and package sequence.

### `0.8.1-minimum-working-state-contract`

- Type: documentation-only
- Status: review complete
- Purpose: define what v0.8 may call a minimum normally working WorldEngine
  state without claiming product readiness or external validation PASS.

### `0.8.2-core-observable-surface-boundary`

- Type: documentation-only
- Status: review complete
- Purpose: define the public runtime, event, generation, Agent loop,
  memory-context, and read-model surfaces an external validator may observe.

### `0.8.3-generation-runtime-agent-loop-readiness`

- Type: mixed or code
- Status: review complete
- Purpose: harden the core-side minimum generation -> runtime -> Agent loop
  readiness slices if a reviewed child package authorizes implementation.

### `0.8.4-external-validation-handoff-contract`

- Type: documentation-only
- Status: review complete
- Purpose: define what WorldEngine exposes or records for an external
  validation function, without defining how the external validator connects or
  operates.

### `0.8.5-core-working-state-smoke-evidence`

- Type: mixed validation package
- Status: review complete
- Purpose: run core-side smoke and compatibility evidence for in-scope public
  engine surfaces without running or implementing the external validator.

### `0.8.6-v0.8-evidence-and-boundary-audit`

- Type: documentation-only
- Status: review complete
- Purpose: audit evidence, compatibility surfaces, unresolved findings, and
  external-validation leakage risks before release-candidate packaging.

### `0.8.7-v0.8-release-candidate-bundle`

- Type: documentation-only
- Status: review complete
- Purpose: prepare a release-candidate bundle from reviewed evidence without
  declaring final readiness beyond current-session evidence.

### `0.8.8-v0.8-final-closeout`

- Type: documentation-only
- Status: final / closeout complete
- Purpose: mark v0.8 final only after reviewed package completion, evidence
  consistency checks, scope review, blocker classification, and evaluator
  approval.

### Post-closeout addendum: `0.8.9-external-validation-provider-and-handoff-manifest`

- Type: documentation-only planning package
- Status: implemented / `WORLDENGINE_CONTRACT_READY`
- Purpose: capture the WorldEngine-side public manifest, provider-readiness,
  and Validation Client world-creation contract prerequisites discovered while
  preparing Codex autonomous validation.
- Boundary: this addendum does not reopen `0.8.8` final closeout and does not
  claim external validation PASS, Codex autonomous validation PASS, or human
  validation PASS.

### Implementation child package: `0.8.9.1-public-handoff-manifest-and-world-creation-contract`

- Type: mixed implementation package
- Status: implementation complete / `WORLDENGINE_CONTRACT_READY`
- Purpose: provide the concrete reviewed gate for implementing `GET
  /manifest`, OpenAPI-discoverable `POST /worlds`, public world creation
  response, provider-readiness redaction, and optional public director guidance
  status.
- Boundary: this child package implemented only WorldEngine Gate 1. It did not
  modify Validation Client code, add concrete demo-world content, expose
  secrets or private Agent state, or claim external validation PASS.

## Current State

Active child package: `0.8.8-v0.8-final-closeout`.

Current route: `final / closeout complete`.

Implementation authorization: no.

Evidence execution authorization: no.

Audit execution authorization: no.

Final verification commands listed in
`0.8.8-v0.8-final-closeout/test-plan.md` ran and evidence is recorded.
Closeout evaluator review passed for the reviewed v0.8 package scope. No
runtime, schema, API, frontend, test implementation, fixture, migration,
external repository, generated result, external validation implementation, or
`backend/worldengine/` implementation work is authorized by this parent state.

## Handoff Baseline

- v0.7 status: historical `final / closeout complete`, with `0.7.9`
  checker/docs repair complete for the current v0.7 checker/docs validation
  scope.
- v0.7 `0.7.9` repair evidence is handoff evidence only, not current v0.8 PASS
  evidence.
- v0.7 does not prove v0.8 minimum working-state readiness, external
  validation readiness, product readiness, or external consumer PASS.
- v0.8 starts from its own package review gates and does not inherit
  implementation authorization from v0.7.

## Final Assessment State

Current value: `final / closeout complete`.

The parent v0.8 campaign docs are reviewed through
`0.8.8-v0.8-final-closeout` documentation/contract review. Planned `0.8.x`
entries remain route-map specifications only. `0.8.4` is review complete and
hands the external-validation handoff contract to `0.8.5`. The
`0.8.5-core-working-state-smoke-evidence` is review complete and hands
core-side smoke evidence to the audit package. The
`0.8.6-v0.8-evidence-and-boundary-audit` is review complete and recommends
release-candidate packaging. The
`0.8.7-v0.8-release-candidate-bundle` is review complete and authorizes only
bounded release-candidate bundle handoff to final-closeout review. The
`0.8.8-v0.8-final-closeout` documentation/contract review passed, final
verification commands ran, and results are recorded. Final closeout remains
authorized for the reviewed v0.8 package scope after closeout evaluator PASS.
External validation execution,
projection app build, product readiness, and v0.8 readiness PASS claims remain
unauthorized.
