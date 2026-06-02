# Goal Runner

Status: planned / ready for review

## Goal Entry

Natural-language goals covered by this campaign include:

```text
完成 v0.8
启动 WorldEngine v0.8：Minimum Proved Working WorldEngine / External Validation Readiness
编写 v0.8 文档
生成 v0.8 文档
```

Current v0.8 route is parent documentation review. No child package is active.
Implementation authorization is closed.

v0.7 post-closeout code review recorded blocking findings in
`docs/testing/results/2026-06-02-v0.7-code-review.md`. v0.8 must not be
reported as clean pass, minimum working-state PASS, external validation
readiness PASS, product PASS, or external consumer PASS until affected blockers
are repaired with current-session evidence or explicitly recorded as blockers
in the active v0.8 package.

## Route Selection

1. Read `CURRENT_STATE.md`.
2. If `CURRENT_STATE.md` does not point to a child package, remain in parent
   documentation review. Use `v0.8-plan.md` only as a roadmap of planned
   package specs.
3. If `CURRENT_STATE.md` points to a child package, first create or confirm
   that child's complete package document set, then read it in this order:
   - `README.md`
   - `intent.md`
   - `contract.md`
   - `technical-design.md`
   - `test-plan.md`
   - `plan.md`
   - `review.md`
4. Use `CAMPAIGN_PLAN.md` and `v0.8-plan.md` to confirm package sequence and
   handoff rules.
5. Do not implement until the active child package review records
   `implementation_authorized: yes`.

`v0.8-plan.md` is not itself an execution-approved child contract. Its `0.8.x`
sections are planned package specs that must be re-confirmed or rewritten in
real child package docs before implementation.

## Documentation Stage Gate

Documentation-only work may create or update v0.8 iteration documents, parent
package plans, roadmap specs, review evidence, minimum working-state contract
documentation, external-validation boundary documentation, readiness taxonomy,
and Chinese mirrors.

Documentation-only work must not modify runtime, schema, API, frontend,
backend test, checker implementation, fixture, migration, external repository,
generated result, external validation implementation, or `backend/worldengine/`
implementation files unless a reviewed active child package explicitly
authorizes that file class.

## Implementation Authorization Rule

Implementation authorization is closed by default.

For mixed or code children:

1. `contract.md`, `technical-design.md`, `test-plan.md`, and `plan.md` must be
   reviewed.
2. A documentation/contract evaluator must report no P0/P1 and no blocking
   P2.
3. `review.md` must record `implementation_authorized: yes`.
4. The implementation must stay inside the active child package contract.

If implementation reveals a design gap, stop implementation, update the
relevant documents, and resume only after the updated contract/design/test
plan/execution plan is reviewed.

## Subagent / Evaluator Requirements

Because v0.8 is a `/goal` campaign with future implementation-bearing
children, use subagent/evaluator checkpoints when available and authorized:

1. Documentation/contract evaluator before recording
   `implementation_authorized: yes`.
2. Implementation-scope evaluator after files are changed and before broad
   verification.
3. Code-review evaluator after focused tests and before broader regression,
   E2E, API smoke, Agent smoke, autonomous checks, core-side readiness
   evidence, or readiness claims.
4. Validation-evidence evaluator before recording tests, E2E, API smoke,
   Agent smoke, autonomous validation, core-side readiness checks, build, or
   release claims as passed.
5. Closeout consistency evaluator before any child or parent final assessment.

Documentation-only children that change process rules, package sequencing,
evidence rules, automation-consumption contracts, release status, validation
templates, report schemas, projection contracts, readiness taxonomy, or mirror
obligations require a read-only documentation evaluator. If subagent/evaluator
tooling is unavailable or not authorized, record the missing checkpoint and
keep status at `planned / ready for review` rather than claiming review
complete.

## Reporting Rules

- Historical v0.7 and v0.6 evidence may be cited only as handoff evidence.
- Do not mark v0.8 runtime, API, frontend, E2E, build, Agent smoke,
  autonomous validation, minimum working-state readiness, external validation
  readiness, external consumer validation, product readiness,
  generation-quality, or release behavior as passed without current-session
  command evidence.
- Do not record external validation PASS unless a later package and external
  workflow explicitly provide redacted public evidence; the current parent
  docs do not define that workflow.
- Record exact commands, exit status, pass counts, skipped checks, blockers,
  artifact paths, and rationale in `review.md`.
- Distinguish `core contract ready`, `core observable surface ready`,
  `minimum working-state evidence ready`, `external validation handoff ready`,
  `external validation pass`, `skipped`, `blocked`, and `out of scope`.
- P1 blocks implementation or closeout.
- Unresolved P2 blocks final status unless explicitly accepted by the active
  package contract and review.
- P3 can be carried only with explicit handoff.

## Scope Stop Conditions

Stop and record a blocker if a task would:

- modify runtime/schema/API/frontend/test/checker implementation before an
  active child authorizes it.
- implement the external validation function, external projection application,
  product UI, application state, application routing, product packaging,
  deployment, or application-specific backend logic in the core repository.
- define how the external validator connects, authenticates, runs private
  scenarios, evaluates oracle outcomes, or stores external application state.
- add concrete app worlds, external validation worlds, seed data, characters,
  locations, resources, story rules, private transcripts, UI selectors, hidden
  reset APIs, private oracle details, private runner state, private external
  repository paths, or non-redacted external event payloads.
- add durable persistence, migrations, live provider behavior, generated-world
  active runtime execution, or new runtime features under `backend/worldengine/`
  without active child authorization.
- treat historical v0.7/v0.6 evidence as current v0.8 PASS evidence.
- ignore v0.7 post-closeout P1/P2 blockers while making an affected readiness
  claim.
- bypass required documentation, implementation authorization, evaluator, or
  evidence gates.
- continue a problematic child plan without updating and reviewing that active
  child package.
