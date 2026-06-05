# Review

Chinese mirror: `review.zh.md`.

Status: implementation complete / PASS

## Documentation Stage Review

Date: 2026-06-05

This review records the documentation-stage state for
`0.8.9.3-archive-summary-e2e-regression-repair`.

## Changed Files

Created:

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

Updated parent status/index documents:

```text
docs/iterations/v0.8/README.md
docs/iterations/v0.8/README.zh.md
docs/iterations/v0.8/CURRENT_STATE.md
docs/iterations/v0.8/CURRENT_STATE.zh.md
```

## Commands Run

```bash
find docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair -maxdepth 1 -type f -print | sort
```

Result: passed. The package contains the required English files and Chinese
mirrors:

```text
README.md
README.zh.md
contract.md
contract.zh.md
intent.md
intent.zh.md
plan.md
plan.zh.md
review.md
review.zh.md
technical-design.md
technical-design.zh.md
test-plan.md
test-plan.zh.md
```

```bash
rg -n "implementation_authorized: yes|evidence_execution_authorized: yes|Status: implementation complete|PASS" docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair docs/iterations/v0.8/CURRENT_STATE.md docs/iterations/v0.8/CURRENT_STATE.zh.md
```

Result: passed for documentation-stage consistency. `implementation_authorized:
yes` appears only as the future approval state, exit criterion, or recommended
approval target. No current `evidence_execution_authorized: yes` or
implementation-complete package status was introduced for `0.8.9.3`.

```bash
git status --short --branch
```

Result: inspected. Existing unrelated testing-documentation changes were
already present in the working tree. This package added only the `0.8.9.3`
iteration directory and updated v0.8 parent status/index docs.

```bash
git diff --check
```

Result: passed with no output.

## Product Tests

Not run in this documentation stage. This package has not started
implementation and does not claim E2E, backend, frontend, runtime, API,
autonomous validation, or LLM-backed lifecycle PASS.

## Scope Review

Documentation scope only:

- no runtime implementation files changed.
- no schema/API implementation files changed.
- no frontend implementation files changed.
- no E2E implementation files changed.
- no fixtures, migrations, generated results, external repositories, or
  `backend/worldengine/` files changed.

## Compatibility Review

No compatibility-affecting code or schema changes were made during the
documentation stage.

The implementation contract requires additive compatibility for archive
summary response shape, stable MemoryPanel selectors, existing runtime/API
surfaces, and E2E-only environment configuration.

## Findings

Current documentation-stage findings:

- P0: none recorded.
- P1: none recorded.
- P2: none blocking.

Documentation/contract evaluator checkpoint:

- Date: 2026-06-05.
- Reviewer: read-only subagent/evaluator.
- Result: no P0, no P1, no blocking P2 in contract, technical design, or
  test plan.
- Required closeout checkpoints confirmed: implementation-scope evaluator,
  code-review evaluator, validation-evidence evaluator, and closeout
  consistency evaluator.

## Authorization State

```text
implementation_authorized: yes
evidence_execution_authorized: yes, limited to test-plan.md commands
```

User approval recorded on 2026-06-05:

```text
批准 0.8.9.3-archive-summary-e2e-regression-repair 进入实现
```

Implementation may start inside this package contract only.

## Implementation Review Template

## Implementation Review

Date: 2026-06-05

### Root Cause Bucket

```text
e2e_environment_gap
```

Focused evidence:

- With no existing backend on port `8000`, the focused scenario passed twice
  using Playwright-managed servers.
- `make test-e2e` also passed once in that clean-server state.
- A diagnostic ordinary backend was then started manually on `127.0.0.1:8000`
  without E2E archive interval environment variables:

```bash
cd backend
.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

- Running the focused scenario while that ordinary backend was active failed
  with the historical symptom: timeout waiting for a newer summary.
- Playwright reused the existing backend after `/health` probes instead of
  launching the configured E2E backend command with
  `WORLD_SUMMARY_INTERVAL_TICKS=2`.
- Error context showed runtime `tick_id 4`, event rows for ticks 1-4, and
  MemoryPanel still rendering `No summaries yet`.
- API probes against the reused ordinary backend showed:

```text
/runtime/state -> tick_id: 4
/world/summaries?limit=5&order=desc -> items: [], total: 0
```

The failure was therefore not archive generation, summary API ordering, or
MemoryPanel refresh. The test environment could silently reuse a non-E2E
backend where the default summary interval does not create a summary within
four runtime steps.

### Repair

Final repair:

- `frontend/playwright.config.ts` now uses E2E-specific default ports
  `18000` for backend and `15173` for frontend.
- Playwright web servers now set `reuseExistingServer: false`, so local E2E
  does not silently reuse a stale or ordinary dev server.
- The backend web server command now sets `CORS_ORIGINS` to the configured
  E2E frontend origin.
- The final config uses `appUrl.origin` for `CORS_ORIGINS`, so custom
  `E2E_APP_BASE_URL` values with a path or trailing slash do not produce a
  browser-origin mismatch.
- `frontend/e2e/agent-loop.spec.ts` and `frontend/e2e/dashboard.spec.ts` now
  use the same E2E backend default URL.
- The `dashboard-archive-summary` scenario still steps exactly four times and
  still asserts that a newer summary is created through API evidence and
  rendered in MemoryPanel.

Rejected intermediate change:

- A temporary helper that stepped up to 24 times was removed after code-review
  evaluator feedback. It could have hidden the environment gap by making a
  normal backend pass, so it is not part of the final repair.

### Files Changed For This Package

```text
frontend/playwright.config.ts
frontend/e2e/agent-loop.spec.ts
frontend/e2e/dashboard.spec.ts
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/README.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/README.zh.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/review.md
docs/iterations/v0.8/0.8.9.3-archive-summary-e2e-regression-repair/review.zh.md
docs/iterations/v0.8/README.md
docs/iterations/v0.8/README.zh.md
docs/iterations/v0.8/CURRENT_STATE.md
docs/iterations/v0.8/CURRENT_STATE.zh.md
```

Unrelated pre-existing dirty files under `docs/testing/**` remain out of this
package scope and must not be staged as part of this package.

### Commands Run

Baseline and diagnosis:

```bash
cd frontend
pnpm exec playwright test e2e/dashboard.spec.ts -g "dashboard-archive-summary creates and renders a newer archive summary"
```

Result: initial sandbox run failed before test execution because the sandbox
blocked binding `127.0.0.1:8000`. Elevated rerun passed: `1 passed`.

```bash
cd frontend
pnpm exec playwright test e2e/dashboard.spec.ts -g "dashboard-archive-summary creates and renders a newer archive summary"
```

Result: second elevated focused rerun passed: `1 passed`.

```bash
make test-e2e
```

Result before repair in clean-server state: `17 passed`.

```bash
git diff --check
```

Result after final CORS origin hardening: passed with no output.

```bash
make test-e2e
```

Result after final CORS origin hardening: `17 passed`.

```bash
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle
```

Result after final CORS origin hardening: `PASS`.

```bash
cd backend
.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Result: started ordinary backend without E2E summary interval environment.

```bash
cd frontend
pnpm exec playwright test e2e/dashboard.spec.ts -g "dashboard-archive-summary creates and renders a newer archive summary"
```

Result against reused ordinary backend: failed with timeout waiting for newer
summary. Artifact path:

```text
test-results/e2e/artifacts/dashboard-dashboard-archiv-20000-ers-a-newer-archive-summary/trace.zip
```

```bash
curl -s http://127.0.0.1:8000/runtime/state
curl -s 'http://127.0.0.1:8000/world/summaries?limit=5&order=desc'
```

Result: runtime reached `tick_id: 4`; summary list was empty.

Final verification:

```bash
cd frontend
pnpm exec playwright test e2e/dashboard.spec.ts -g "dashboard-archive-summary creates and renders a newer archive summary"
```

Result: passed, `1 passed`.

```bash
cd frontend
pnpm exec playwright test e2e/dashboard.spec.ts
```

Result: passed, `6 passed`.

```bash
make test-e2e
```

Result: passed, `17 passed`.

```bash
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle
```

Result: passed.

```bash
git diff --check
```

Result: passed with no output.

```bash
git status --short --branch
```

Result: inspected. Branch is `v0.8...origin/v0.8`. Unrelated dirty
`docs/testing/**` files remain in the working tree and are excluded from this
package.

### Adjacent Regression Decision

No backend archive/API code changed, so `uv run pytest backend/app/tests` was
not required by `test-plan.md`.

No frontend source code under `frontend/src/**` changed, so `pnpm test` and
`pnpm build` were not required by `test-plan.md`.

Only Playwright config/spec files changed, so the required adjacent command was
`cd frontend && pnpm exec playwright test e2e/dashboard.spec.ts`, which passed
with `6 passed`.

### Subagent / Evaluator Findings

Documentation/contract evaluator:

- P0: none.
- P1: none.
- Blocking P2: none.
- Verdict: implementation may proceed after recording authorization.

Implementation-scope evaluator:

- P0: none.
- P1: none.
- P2: unrelated `docs/testing/**` dirty files are out of package scope and
  must remain excluded.
- P2: `review.md` needed root-cause evidence before closeout. Addressed in
  this implementation review.

Code-review evaluator:

- Initial P1: temporary 24-step helper could mask an E2E environment gap.
- Resolution: removed the helper and repaired the E2E environment configuration
  instead.
- Final rerun: no P0/P1. P2 stale final assessment was resolved by this
  closeout update.

Validation-evidence evaluator:

- P0: none.
- P1: none.
- P2: `frontend/e2e/agent-loop.spec.ts` needed to be added to the allowed
  contract scope because all E2E specs must share the same E2E backend default.
  Addressed by updating `contract.md` and `contract.zh.md`.
- P2: stale closeout/status text needed update. Addressed by this final
  review and parent/package status updates.
- Verdict: scoped functional PASS evidence is supported by the current-session
  commands.

Closeout consistency:

- Final status text and parent route were updated after validation-evidence
  review.
- `docs/testing/**` dirty files remain explicitly outside this package scope.

### Compatibility Review

- Archive summary API response shape was not changed.
- Backend archive generation behavior was not changed.
- MemoryPanel selectors and rendering behavior were not changed.
- Runtime step, event, snapshot, params, generation, and Agent loop behavior
  were not changed.
- E2E environment defaults changed only for the Playwright test environment.

### Scope Review

- No `backend/worldengine/` files changed.
- No Validation Client repository changes were made.
- No generated validation result directories were rewritten.
- No live provider, DeepSeek, LLM-backed world generation, concrete validation
  world content, or app-specific backend logic was added.
- No product-readiness, external validation PASS, or LLM-backed lifecycle PASS
  is claimed.

### Unresolved Findings

- P0: none.
- P1: none after the temporary helper was removed.
- P2: unrelated dirty `docs/testing/**` files remain in the working tree and
  are excluded from this package.
- P3: none.

## Implementation Review Template

Historical template kept for reference:

```text
Root cause bucket:
Focused diagnosis evidence:
Files changed:
Commands run:
Focused E2E result:
make test-e2e result:
Adjacent regression result:
Saved-result checker result:
Subagent/evaluator findings:
Compatibility review:
Scope review:
Unresolved findings:
Final assessment:
```

## Final Assessment

PASS.

`0.8.9.3-archive-summary-e2e-regression-repair` repaired the
`dashboard-archive-summary` regression as an `e2e_environment_gap`. The final
implementation keeps the four-step newer-summary assertion intact and makes
the Playwright environment deterministic by using E2E-specific default ports,
disabling silent existing-server reuse, and aligning E2E CORS/API defaults.

Current-session verification passed:

- focused archive-summary E2E: `1 passed`.
- dashboard E2E adjacent regression: `6 passed`.
- full E2E suite: `17 passed`.
- saved-result checker:
  `PASS: validated agent autonomous result at test-results/agent-autonomous/20260604T193039+0800-worldengine-full-lifecycle`.
- `git diff --check`: passed.

No external validation PASS, product-readiness PASS, or LLM-backed lifecycle
PASS is claimed.
