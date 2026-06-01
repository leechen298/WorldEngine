# Goal Runner

Status: planned / ready for review

## Goal Entry

Natural-language goals covered by this campaign include:

```text
完成 v0.7
启动 WorldEngine v0.7：External Validation Readiness / Projection Consumer Readiness
编写 v0.7 文档
```

## Route Selection

1. Read `CURRENT_STATE.md`.
2. If `CURRENT_STATE.md` does not point to a child package, remain in parent
   documentation review. Use `v0.7-plan.md` only as a roadmap of planned
   package specs.
3. If future work selects a planned child package, first create or confirm that
   child's complete package document set, then read it in this order:
   - `README.md`
   - `intent.md`
   - `contract.md`
   - `technical-design.md`
   - `test-plan.md`
   - `plan.md`
   - `review.md`
4. Use `CAMPAIGN_PLAN.md` and `v0.7-plan.md` to confirm package sequence and
   handoff rules.
5. Do not implement until the active child package review records
   `implementation_authorized: yes`.

`v0.7-plan.md` is not itself an execution-approved child contract. Its
`0.7.x` sections are planned package specs that must be re-confirmed or
rewritten in real child package docs before implementation.

## Documentation Stage Gate

Documentation-only work may create or update v0.7 iteration documents,
parent package plans, roadmap specs, review evidence, validation
documentation, report templates, projection contract documentation, and
Chinese mirrors.

Documentation-only work must not modify runtime, schema, API, frontend,
backend test, checker implementation, fixture, migration, external repository,
generated result, or `backend/worldengine/` implementation files unless a
reviewed active child package explicitly authorizes that file class.

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

Because v0.7 is a `/goal` campaign with future implementation-bearing
children, use subagent/evaluator checkpoints when available and authorized:

1. Documentation/contract evaluator before recording
   `implementation_authorized: yes`.
2. Implementation-scope evaluator after files are changed and before broad
   verification.
3. Code-review evaluator after focused tests and before broader regression,
   E2E, API smoke, Agent smoke, autonomous checks, external validation, or
   readiness claims.
4. Validation-evidence evaluator before recording tests, E2E, API smoke,
   Agent smoke, autonomous validation, external suite checks, build, or release
   claims as passed.
5. Closeout consistency evaluator before any child or parent final assessment.

Documentation-only children that change process rules, package sequencing,
evidence rules, automation-consumption contracts, release status, validation
templates, report schemas, projection contracts, readiness taxonomy, or mirror
obligations require a read-only documentation evaluator. If subagent/evaluator
tooling is unavailable or not authorized, record the missing checkpoint and
keep status at `planned / ready for review` rather than claiming review
complete.

If implementation discovers that the active child's approved plan is wrong,
incomplete, or unsafe, stop implementation. Update the active child's
`contract.md`, `technical-design.md`, `test-plan.md`, `plan.md`, and
`review.md` as needed, then continue only after the updated package is
reviewed. Do not keep executing an outdated plan because the parent roadmap
listed an order.

## Reporting Rules

- Historical v0.6 evidence may be cited only as handoff evidence.
- Do not mark v0.7 runtime, API, frontend, E2E, build, Agent smoke,
  autonomous validation, external validation, projection readiness, product
  readiness, generation quality, or release behavior as passed without
  current-session command evidence.
- Record exact commands, exit status, pass counts, skipped checks, blockers,
  artifact paths, and rationale in `review.md`.
- Distinguish `contract ready`, `report format ready`, `core-side
  compatibility ready`, `external suite pass`, `projection consumer contract
  ready`, `skipped`, `blocked`, and `out of scope`.
- P1 blocks implementation or closeout.
- Unresolved P2 blocks final status unless explicitly accepted by the active
  package contract and review.
- P3 can be carried only with explicit handoff.

## Scope Stop Conditions

Stop and record a blocker if a task would:

- modify runtime/schema/API/frontend/test/checker implementation before an
  active child authorizes it.
- add concrete external validation world data, seed data, characters,
  locations, resources, story rules, private transcripts, UI selectors, hidden
  reset APIs, private oracle details, or application-specific backend logic.
- implement the first external projection application or product packaging
  behavior; v0.8 owns that scope.
- add durable persistence, migrations, live provider behavior, or generated
  world execution outside a reviewed v0.7 contract.
- add new runtime features under `backend/worldengine/`.
- treat v0.6 historical evidence as current v0.7 PASS evidence.
- bypass required documentation, implementation authorization, evaluator, or
  evidence gates.
- continue a problematic child plan without updating and reviewing that
  active child package.
