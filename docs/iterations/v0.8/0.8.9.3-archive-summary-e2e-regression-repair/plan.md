# Plan

Chinese mirror: `plan.zh.md`.

## Objective

Prepare and, after review approval, execute a narrow repair for the
`dashboard-archive-summary` E2E regression discovered during current-product
validation.

## Authoritative Inputs Read

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/README.md`
- `docs/iterations/v0.8/CURRENT_STATE.md`
- `docs/iterations/v0.8/README.md`
- `docs/testing/e2e-scenarios/dashboard-archive-summary.md`
- `frontend/e2e/dashboard.spec.ts`

## Files To Create Or Update

Create:

```text
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/README.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/README.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/intent.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/intent.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/contract.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/contract.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/technical-design.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/technical-design.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/test-plan.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/test-plan.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/plan.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/plan.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/review.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/review.zh.md
```

Update:

```text
docs/iterations/v0.8/README.md
docs/iterations/v0.8/README.zh.md
docs/iterations/v0.8/CURRENT_STATE.md
docs/iterations/v0.8/CURRENT_STATE.zh.md
```

## Explicitly Out Of Scope

- Runtime, schema, API, frontend, E2E, fixture, migration, and checker
  implementation changes during the documentation stage.
- Validation Client repository changes.
- LLM-backed lifecycle validation execution.
- DeepSeek/provider implementation or smoke testing.
- Generated validation result rewrites.

## Required Status Values

During documentation drafting:

```text
Status: drafted / ready for user review
implementation_authorized: no
evidence_execution_authorized: no
```

After review approval, implementation may update the package to:

```text
implementation_authorized: yes
```

## Phase 1: Documentation Gate

1. Read required governance and package context.
2. Draft full package docs and Chinese mirrors.
3. Add parent v0.8 route/status references.
4. Run documentation-stage checks.
5. Stop before implementation.

## Phase 2: Review And Authorization

Implementation may start only after:

1. documentation/contract evaluator or reviewer records no P0/P1 and no
   blocking P2.
2. `review.md` records approval.
3. `implementation_authorized: yes` is visible in package and parent status.

## Phase 3: Reproduce And Diagnose

1. Run the focused E2E scenario.
2. If it fails, collect API/UI/artifact evidence.
3. If it passes once, rerun once and collect state to classify intermittency.
4. Record one root-cause bucket.

## Phase 4: Minimal Repair

1. Choose backend, frontend, or E2E harness repair based on evidence.
2. Keep changes inside allowed files.
3. Preserve the newer-summary creation and render assertions.
4. Add focused regression coverage only if touched path requires it.

## Phase 5: Verification

Run commands in `test-plan.md`:

1. focused E2E.
2. broad E2E.
3. adjacent backend/frontend regressions based on touched files.
4. latest basic full lifecycle saved-result checker.
5. `git diff --check`.

## Phase 6: Required Evaluators

For implementation-bearing closeout, use the repository's evaluator/subagent
model when available:

1. documentation/contract evaluator before implementation authorization.
2. implementation-scope evaluator after files are changed.
3. code-review evaluator after focused verification.
4. validation-evidence evaluator before PASS claims.
5. closeout consistency evaluator before final assessment.

## Stop Conditions

- Stop if the root cause requires Validation Client changes.
- Stop if the fix requires LLM-backed/provider work.
- Stop if the repair requires broad archive redesign.
- Stop if any P1 remains.
- Stop if any blocking P2 remains without accepted rationale.
- Stop if the only way to pass is to skip/weaken the failing test.
- Stop if evidence would require rewriting generated result directories.

## Handoff After Approval

Use this package with `worldengine-iteration-dev` for implementation. A later
agent may execute the full repair without asking the user to dispatch each
sub-step, as long as it stays inside this contract and records evidence.
