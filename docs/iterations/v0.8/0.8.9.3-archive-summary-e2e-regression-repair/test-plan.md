# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Verification Order

Run commands in this order during implementation closeout. Record exact
commands, results, and important output in `review.md`.

## 1. Baseline Reproduction

Goal: prove the current failure or prove it is intermittent before changing
implementation files.

```bash
cd frontend
pnpm exec playwright test e2e/dashboard.spec.ts -g "dashboard-archive-summary creates and renders a newer archive summary"
```

If the focused test unexpectedly passes, rerun once and inspect API/UI state
before deciding the package is unnecessary. Do not close the package only
because one retry passes.

## 2. Diagnostic Probe

Goal: classify the root cause bucket.

Required evidence:

- summary before stepping.
- summary list after stepping.
- runtime state after stepping.
- MemoryPanel rendered summary stats/text if UI is involved.
- Playwright artifact path if the focused test fails.

The exact command or script may be chosen during implementation, but it must
not write product code and must not rewrite saved validation results.

## 3. Focused Repair Verification

Run the focused scenario after the repair:

```bash
cd frontend
pnpm exec playwright test e2e/dashboard.spec.ts -g "dashboard-archive-summary creates and renders a newer archive summary"
```

PASS requires the focused scenario to pass without skipping or weakening the
newer-summary assertions.

## 4. Broad E2E Verification

Run the full E2E suite:

```bash
make test-e2e
```

PASS requires the full suite to pass in the current session.

## 5. Adjacent Regression Commands

Run only the commands required by touched files:

- If backend archive/API code changes:

```bash
uv run pytest backend/app/tests
```

- If frontend source code changes:

```bash
cd frontend
pnpm test
pnpm build
```

- If only Playwright test harness changes:

```bash
cd frontend
pnpm exec playwright test e2e/dashboard.spec.ts
```

The implementation agent may add narrower focused backend tests first, but
must still run the appropriate broader adjacent command before closeout.

## 6. Basic Full Lifecycle Saved-Result Checker

Confirm the latest basic autonomous lifecycle result still validates:

```bash
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle
```

This is not a new live autonomous run. It only verifies the latest saved result
against the checker.

## 7. Documentation and Diff Checks

```bash
git diff --check
```

Also inspect `git status --short --branch` before staging or closeout.

## PASS Source

This package may report PASS only if:

- focused E2E repair verification passes.
- `make test-e2e` passes.
- required adjacent regressions pass or are explicitly not applicable.
- saved-result checker passes or is recorded as blocked by unavailable local
  artifacts with exact reason.
- review records no unresolved P1 or blocking P2.

## FAIL or BLOCKED Source

Report FAIL or BLOCKED if:

- focused E2E still fails after attempted repair.
- `make test-e2e` still fails.
- the root cause requires broader archive redesign.
- the repair requires Validation Client changes.
- verification would require rewriting saved results.
- a redaction or private-evidence leak is discovered.
