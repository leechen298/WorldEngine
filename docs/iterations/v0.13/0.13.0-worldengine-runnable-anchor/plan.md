# Plan

Chinese mirror: `plan.zh.md`.

Status: closed / execution complete

## Objective

Prepare and, after explicit authorization, implement the WorldEngine-side
minimum runnable anchor without depending on current implementation design,
live providers, Godot, or external infrastructure.

## Authoritative Inputs Read

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/project-plan.md`
- `docs/roadmap.md`
- `docs/living-world-development-flow.zh.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- v0.13 parent documents

## Documentation Type

Full mixed implementation package prepared in documentation stage.

## Files To Create Or Update During Documentation Stage

- v0.13 parent index, campaign state/runner/plan, and version plan with Chinese
  mirrors.
- complete `0.13.0-worldengine-runnable-anchor` package with Chinese mirrors.
- `docs/project-plan(.zh).md` and `docs/roadmap(.zh).md` routing updates.

## Files Explicitly Out Of Scope During Documentation Stage

- `backend/`
- `frontend/`
- tests, fixtures, migrations, generated evidence, and runtime data.
- `/Users/leechen/projects/WorldEngine-Validation-Client`.

## Ordered Execution Steps

### Phase A: Documentation Gate

1. Draft the parent v0.13 campaign and detailed package sequence.
2. Draft this package's intent, contract, technical design, test plan, plan,
   and documentation-stage review in English and Chinese.
3. Integrate read-only subagent findings on vertical-slice completeness and
   anti-false-pass boundaries.
4. Run package completeness, mirror, authorization, terminology, and
   `git diff --check` checks.
5. Request an independent read-only documentation/contract evaluator.
6. Repair all P1/P2 findings.
7. Present the package for user review. Stop before implementation.

### Phase B: Authorization

8. After user approval and evaluator PASS, change authorization to `yes` for
   `0.13.0` only and record the approval in parent/current-state/review mirrors.
9. Read the active code and tests as implementation inventory.
10. If the audit reveals a contract gap, stop and update/review the documents.

### Phase C: Test-first Implementation

11. Add failing focused tests for AC-01 through AC-10.
12. Implement generic manifest and schemas.
13. Implement deterministic package generation/readiness/hash.
14. Implement session boot, atomic lockstep step, event/diff/snapshot/state
    hash, projection, and evidence export.
15. Implement deterministic Agent causal loop and experience-linked later
    decision.
16. Implement explicit intervention windows and accepted/rejected direction
    paths.
17. Implement generic action/feedback and idempotency/revision boundaries.
18. Implement the administration console over the same APIs.

### Phase D: Verification And Review

19. Run focused backend tests.
20. Request implementation-scope evaluator and repair P1/P2.
21. Run frontend unit/build and focused E2E.
22. Request code-review evaluator and repair P1/P2.
23. Run regression and black-box API smoke.
24. Request validation-evidence evaluator.
25. Update `review.md`/`review.zh.md` with exact current evidence.
26. Request closeout-consistency evaluator.
27. If all gates pass, close `0.13.0` without claiming complete MVP PASS and
    route to the external `0.13.1` documentation package.

## Allowed Changes After Authorization

Only the backend/frontend/test/doc surfaces listed in `contract.md` and
`technical-design.md`.

## Forbidden Changes

- External repository, Godot, provider live, concrete fixture world,
  production persistence/deployment, or legacy `backend/worldengine/` work.
- Unreviewed contract changes.
- Reverting unrelated dirty files.

## Review Gates

- Documentation/contract evaluator before authorization.
- Implementation-scope evaluator after implementation changes.
- Code-review evaluator after focused tests.
- Validation-evidence evaluator before runtime/E2E claims.
- Closeout-consistency evaluator before package PASS.

## Verification Commands

Exact commands are defined in `test-plan.md`. No command may be marked passed
unless run in the current package session.

## Assumptions

- Process-local persistence is sufficient for the first anchor.
- Deterministic generation and Agent policy are valid MVP execution paths.
- HTTP polling with event cursor is sufficient for the first generic client.
- Existing Web administration technology can remain, but validation-client Web
  code does not constrain this package.

## Stop Conditions

- User or evaluator rejects the contract.
- Required behavior can only be implemented through live provider, concrete
  core fixture, private state, or client-owned canonical mutation.
- Existing dirty work makes scoped implementation impossible without
  destructive overwrite.
- Any unresolved P1/P2 remains.

## Handoff After Approval

Use `worldengine-iteration-dev` for the approved `0.13.0` scope. Do not start
`0.13.1` until this package publishes a verified contract bundle.
