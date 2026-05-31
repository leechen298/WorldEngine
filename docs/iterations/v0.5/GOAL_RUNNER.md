# Goal Runner

Status: planned / ready for review

## Goal Entry

Natural-language goals covered by this campaign include:

```text
完成 v0.5
启动 WorldEngine v0.5：Memory and Self-Continuity Substrate
```

## Route Selection

1. Read `CURRENT_STATE.md`.
2. If `CURRENT_STATE.md` points to a child package, read that child package in
   this order:
   - `README.md`
   - `intent.md`
   - `contract.md`
   - `technical-design.md`
   - `test-plan.md`
   - `plan.md`
   - `review.md`
3. Use `CAMPAIGN_PLAN.md` and `v0.5-plan.md` to confirm package sequence and
   handoff rules.
4. Do not implement until the active child package review records
   `implementation_authorized: yes`.

## Documentation Stage Gate

Documentation-only work may create or update v0.5 iteration documents, package
plans, contracts, review evidence, and Chinese mirrors.

Documentation-only work must not modify runtime, schema, API, frontend,
backend test, fixture, migration, external repository, generated result, or
`backend/worldengine/` implementation files.

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

Because v0.5 is a `/goal` campaign with future implementation-bearing
children, use subagent/evaluator checkpoints:

1. Documentation/contract evaluator before recording
   `implementation_authorized: yes`.
2. Implementation-scope evaluator after files are changed and before broad
   verification.
3. Code-review evaluator after focused tests and before broader regression or
   E2E/smoke claims.
4. Validation-evidence evaluator before recording tests, E2E, API smoke,
   Agent smoke, autonomous validation, build, or release claims as passed.
5. Closeout consistency evaluator before any child or parent final assessment.

Documentation-only children that change process rules, package sequencing,
evidence rules, automation-consumption contracts, release status, validation
templates, or mirror obligations require a read-only documentation evaluator.

## Reporting Rules

- Historical v0.4 and post-closeout evidence may be cited only as handoff
  evidence.
- Do not mark v0.5 implementation, runtime, API, frontend, E2E, build, Agent
  smoke, autonomous validation, or release behavior as passed without
  current-session command evidence.
- Record exact commands, exit status, pass counts, skipped checks, and
  rationale in `review.md`.
- P1 blocks implementation or closeout.
- Unresolved P2 blocks final status unless explicitly accepted by the active
  package contract and review.
- P3 can be carried only with explicit handoff.

## Scope Stop Conditions

Stop and record a blocker if a task would:

- modify runtime/schema/API/frontend/test implementation before an active child
  authorizes it.
- add concrete demo-world data, private external validation oracle details, or
  application-specific backend logic.
- implement world generation, external validation readiness, projection app
  readiness, or durable persistence outside a reviewed v0.5 contract.
- add new runtime features under `backend/worldengine/`.
- treat v0.4 historical evidence as current v0.5 pass evidence.
- bypass required subagent/evaluator gates.

