# Plan

Chinese mirror: `plan.zh.md`.

## Objective

Create and review the concrete `0.9.6` package, then implement only the
reviewed active-backend natural-language world direction boundary after
authorization.

## Authoritative Inputs Read

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.9/README.md`
- `docs/iterations/v0.9/CURRENT_STATE.md`
- `docs/iterations/v0.9/GOAL_RUNNER.md`
- `docs/iterations/v0.9/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.9/v0.9-plan.md`
- `backend/app/api/routes/world.py`
- `backend/app/schemas/world.py`
- `backend/app/tests/test_public_handoff_contract_api.py`
- `docs/testing/llm-backed-lifecycle-validation-plan.md`
- `docs/testing/agent-autonomous/llm-backed-artifact-contract.md`
- `docs/testing/agent-autonomous/scenarios/rule-compliant-event-generation.md`

## Documentation Stage

1. Create the required package docs and Chinese mirrors.
2. Verify package file count and required terms.
3. Request read-only documentation/contract evaluator review.
4. Fix P0/P1/blocking P2 findings before implementation authorization.
5. If clean, update `review.md` to record implementation authorization for
   this package only.

## Implementation Stage

Implementation may start only after the documentation gate passes.

1. Add focused tests for direction schema and API behavior.
2. Run the focused tests and confirm the expected RED failure.
3. Add additive public direction schemas and deterministic classifier.
4. Add in-memory queued guidance behavior and public summaries.
5. Preserve existing director-guidance compatibility.
6. Run focused and related tests.
7. Request implementation-scope subagent review.
8. Fix findings with tests first.
9. Run backend regression.
10. Update `review.md` with changed files, commands, compatibility, scope,
    subagent findings, unresolved findings, and final route.

## Files To Create Or Update

Documentation stage:

```text
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/README.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/README.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/intent.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/intent.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/contract.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/contract.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/technical-design.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/technical-design.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/test-plan.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/test-plan.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/plan.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/plan.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/review.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/review.zh.md
```

Implementation stage candidate files:

```text
backend/app/schemas/world_direction.py
backend/app/schemas/world.py
backend/app/api/routes/world.py
backend/app/tests/test_world_direction_boundary.py
backend/app/tests/test_public_handoff_contract_api.py
```

## Files Explicitly Out Of Scope

- `backend/worldengine/`
- frontend files
- checker implementation and fixtures
- generated result directories
- Validation Client repository
- provider configuration or live provider call paths
- durable scheduler or deployment infrastructure

## Review Gates

- Documentation/contract evaluator before implementation authorization.
- Implementation-scope evaluator after code changes and before broad
  verification.
- Closeout consistency review before parent route advances to `0.9.7`.

## Verification Commands

Use the commands in `test-plan.md`. Do not claim package pass from narrower
checks.

## Stop Conditions

Stop if:

- direction handling starts mutating final facts.
- direct Agent private state, goals, memory, relationship, inventory, or life
  state can be changed by user text.
- implementation requires live provider interpretation.
- event legality or rule adjudication is needed to finish this package.
- frontend, Validation Client, checker, generated-result, durable scheduler,
  or `backend/worldengine/` changes become necessary.
- a required subagent checkpoint reports unresolved P0/P1 or blocking P2.

## Handoff After Closeout

If implementation closes cleanly, update the parent v0.9 route to
`0.9.7-rule-linked-evolution-and-event-legality-documentation-package-needed`.
