# E2E / Integration / API Smoke Validation Report

Status: passed (archived evidence only after campaign reset)

Reopen note: the 2026-05-28 evidence below is preserved as historical evidence.
That run reached `blocked` because the old validation execution context could
not bind the configured localhost backend port. The package was reopened on
2026-05-29 after `agent-iter` validation stages were updated to run with
host-capable localhost binding.

Current campaign note: after the `unverified_restart` reset, this report is
historical evidence. It does not count as current campaign completion unless a
new `/goal` run reruns this package or explicitly re-accepts this evidence with
rationale in `review.md`.

## Metadata

- Reviewed branch: `v0.3-lcoal`
- Reviewed commit: `dbffa069a5e74b6b1e6b60719152922595c60df6`
- Execution date: 2026-05-29
- Executor: Codex F
- Previous final assessment: `blocked`
- Current final assessment: `archived evidence only`

Allowed final assessment values:

- `passed`
- `passed with P3`
- `blocked`
- `failed`
- `not executed`

## Current Execution Summary

The 2026-05-29 host-capable rerun resolved the prior browser E2E localhost bind
blocker. Backend deterministic checks, API smoke, Playwright availability, and
configured browser E2E all passed with current-session command evidence.

## Files Read

- Release docs: `docs/releases/v0.2.md`
- Evidence docs: `docs/iterations/v0.2/evidence-index.md`,
  `docs/iterations/v0.2/compatibility-review.md`,
  `docs/iterations/v0.2/boundary-audit.md`
- Backend route files: `backend/app/api/routes/health.py`,
  `backend/app/api/routes/runtime.py`, `backend/app/api/routes/world.py`,
  `backend/app/api/routes/world_params.py`, `backend/app/api/routes/archive.py`,
  `backend/app/api/routes/world_agent.py`
- Test files: `backend/tests/`, `backend/app/tests/`,
  `frontend/e2e/dashboard.spec.ts`
- E2E config files: `frontend/package.json`,
  `frontend/playwright.config.ts`

## Commands Run

| Command | Purpose | Exit code | Result | Notes |
|---|---|---:|---|---|
| `git status --short --branch && git rev-parse HEAD` | Record reviewed branch and commit for host-capable rerun | 0 | passed | Output: `## v0.3-lcoal`; commit `dbffa069a5e74b6b1e6b60719152922595c60df6`. |
| `git diff --check` | Documentation and whitespace check before validation edits | 0 | passed | No output. |
| `test -f docs/releases/v0.2.md && test -f docs/iterations/v0.2/evidence-index.md && test -f docs/iterations/v0.2/compatibility-review.md && test -f docs/iterations/v0.2/boundary-audit.md` | Required v0.2 evidence-doc presence check | 0 | passed | No output. |
| `find backend/app/api/routes -maxdepth 1 -type f -name '*.py' -print \| sort` | Inspect configured backend API route files | 0 | passed | Route files found: health, runtime, world, world_params, archive, world_agent. |
| `make check-backend` | Backend dependency availability | 0 | passed | No output. |
| `make check-frontend` | Frontend dependency availability | 0 | passed | No output. |
| `cd backend && .venv/bin/python -m pytest tests app/tests -q` | Backend deterministic checks | 0 | passed | `115 passed in 0.86s`. |
| `cd backend && .venv/bin/python - <<'PY' ...` | API smoke, first payload attempt | 1 | failed smoke payload | Read endpoints returned `200 code=0`; `POST /world/params/apply` returned 422 because `validation.smoke` is not a registered writable path. |
| `cd backend && .venv/bin/python - <<'PY' ...` | API smoke with registered safe params payload | 0 | passed | Required endpoints returned `200 code=0`, including `POST /world/params/apply` with `counter.increment`. |
| `cd frontend && pnpm exec playwright --version && pnpm exec playwright install --dry-run chromium` | E2E framework and browser availability check | 0 | passed | Playwright `1.60.0`; Chromium, headless shell, and FFmpeg install targets resolved. |
| `make test-e2e` | Configured browser E2E suite | 0 | passed | Backend bound `127.0.0.1:8000`; `6 passed (7.5s)`. |
| `git diff --name-only` | Confirm no implementation files changed before report updates | 0 | passed | No output before validation doc edits. |
| `rg -n -i 'demo[- ]world\|concrete demo\|application-specific backend\|seed data\|story rules\|characters\|locations\|resources' docs/releases/v0.2.md docs/iterations/v0.2 docs/scope-boundaries.md docs/external-fixture-boundary.md backend/app frontend --glob '!frontend/node_modules/**' --glob '!test-results/**'` | Boundary wording / concrete demo regression sweep | 0 | passed | Matches were boundary, future-scope, and historical references; no implementation change was present. |
| `git status --short --branch` | Record reviewed branch and worktree state | 0 | passed | Output: `## v0.3-lcoal`. |
| `git rev-parse HEAD` | Record reviewed commit | 0 | passed | Output: `47b2dac6a08fdf7c249844b1f5447af17ab37d86`. |
| `git diff --check` | Documentation and whitespace check | 0 | passed | No output. |
| `test -f docs/releases/v0.2.md && test -f docs/iterations/v0.2/evidence-index.md && test -f docs/iterations/v0.2/compatibility-review.md && test -f docs/iterations/v0.2/boundary-audit.md` | Required v0.2 evidence-doc presence check | 0 | passed | No output. |
| `make check-backend` | Backend dependency availability | 0 | passed | No output. |
| `make check-frontend` | Frontend dependency availability | 0 | passed | No output. |
| `backend/.venv/bin/python -m pytest backend/tests backend/app/tests -q` | Backend deterministic check, first invocation from repo root | 2 | failed command invocation | Collection failed with `ModuleNotFoundError: No module named 'app'`; rerun from `backend/` below. |
| `cd backend && .venv/bin/python -m pytest tests app/tests -q` | Backend deterministic checks | 0 | passed | `115 passed in 0.86s`. |
| `cd backend && .venv/bin/python - <<'PY' ...` | API smoke, first payload attempt | 1 | failed smoke payload | Read endpoints returned `200 code=0`; `POST /world/params/apply` returned 422 because the test payload omitted required `op`. |
| `cd backend && .venv/bin/python - <<'PY' ...` | API smoke with safe params payload | 0 | passed | Required endpoints returned `200 code=0`, including `POST /world/params/apply`. |
| `cd frontend && pnpm exec playwright --version && pnpm exec playwright install --dry-run chromium` | E2E framework and browser availability check | 0 | passed | Playwright `1.60.0`; Chromium install target was present in the dry-run output. |
| `make test-e2e` | Configured browser E2E suite | 2 | blocked | Playwright backend web server failed to bind `127.0.0.1:8000`: `operation not permitted`. No browser tests executed. |
| `git diff --name-only` | Confirm no implementation files changed before report updates | 0 | passed | No output before validation doc edits. |
| `git rev-parse HEAD` | Record validation-fix rerun commit | 0 | passed | Output: `f1c99fc94f46b04e9286450bf0af7ebfb17253d3`; changes since the original reviewed commit are validation docs only. |
| `make test-e2e` | Validation-fix rerun of the blocking browser E2E command | 2 | blocked | Same blocker reproduced: backend web server could not bind `127.0.0.1:8000` with `operation not permitted`; no browser tests executed. |
| `git diff --check` | Validation-fix documentation whitespace check | 0 | passed | No output after validation doc edits. |
| `git rev-parse HEAD` | Record second validation-fix rerun commit | 0 | passed | Output: `9be4dc8d2d2696dadf625bd254386b0ad1b292d9`; latest review checkpoint before this validation-fix pass. |
| `make test-e2e` | Second validation-fix rerun of the blocking browser E2E command | 2 | blocked | Same blocker reproduced: Playwright web server started, then failed to bind `127.0.0.1:8000` with `operation not permitted`; no browser tests executed. |
| `git diff --check` | Second validation-fix documentation whitespace check | 0 | passed | No output after validation doc edits. |
| `git rev-parse HEAD` | Record third validation-fix rerun commit | 0 | passed | Output: `5da27c7f051ec21ad01486df78dd35656447cfb6`; only validation findings documentation was modified before this pass. |
| `git status --short --branch` | Record third validation-fix worktree state | 0 | passed | Output: `## v0.3-lcoal` plus modified `docs/iterations/v0.2-post-closeout/findings.md`. |
| `make test-e2e` | Third validation-fix rerun of the blocking browser E2E command | 2 | blocked | Same blocker reproduced: Playwright web server started, then failed to bind `127.0.0.1:8000` with `operation not permitted`; no browser tests executed. |
| `git diff --check` | Third validation-fix documentation whitespace check | 0 | passed | No output after validation doc edits. |
| `git rev-parse HEAD` | Record fourth validation-fix rerun commit | 0 | passed | Output: `6e9c7897e054e898d0854516c754202c9e2f91a8`; latest validation-review checkpoint before this validation-fix pass. |
| `git status --short --branch` | Record fourth validation-fix worktree state | 0 | passed | Output: `## v0.3-lcoal` plus modified `docs/iterations/v0.2-post-closeout/findings.md`. |
| `make test-e2e` | Fourth validation-fix rerun of the blocking browser E2E command | 2 | blocked | Same blocker reproduced: Playwright web server started, then failed to bind `127.0.0.1:8000` with `operation not permitted`; no browser tests executed. |
| `git diff --check` | Fourth validation-fix documentation whitespace check | 0 | passed | No output after validation doc edits. |
| `git rev-parse HEAD` | Record fifth validation-fix rerun commit | 0 | passed | Output: `4a0c82ff74c30e86ef9b41b00f23fd7574b1fcde`; latest validation-review checkpoint before this validation-fix pass. |
| `git status --short --branch` | Record fifth validation-fix worktree state | 0 | passed | Output: `## v0.3-lcoal` plus modified `docs/iterations/v0.2-post-closeout/findings.md`. |
| `make test-e2e` | Fifth validation-fix rerun of the blocking browser E2E command | 2 | blocked | Same blocker reproduced: Playwright web server started, then failed to bind `127.0.0.1:8000` with `operation not permitted`; no browser tests executed. |
| `git diff --check` | Fifth validation-fix documentation whitespace check | 0 | passed | No output after validation doc edits. |
| `git rev-parse HEAD` | Record sixth validation-fix rerun commit | 0 | passed | Output: `36234a82a82eeab196404888c33dc178c38850c8`; latest validation-review checkpoint before this validation-fix pass. |
| `git status --short --branch` | Record sixth validation-fix worktree state | 0 | passed | Output: `## v0.3-lcoal` plus modified `docs/iterations/v0.2-post-closeout/findings.md`. |
| `make test-e2e` | Sixth validation-fix rerun of the blocking browser E2E command | 2 | blocked | Same blocker reproduced: Playwright web server started, then failed to bind `127.0.0.1:8000` with `operation not permitted`; no browser tests executed. |
| `git diff --check` | Sixth validation-fix documentation whitespace check | 0 | passed | No output after validation doc edits. |
| `git rev-parse HEAD` | Record seventh validation-fix rerun commit | 0 | passed | Output: `04ebbe50458e1845dba7104ed983fa89821ea417`; latest validation-review checkpoint before this validation-fix pass. |
| `git status --short --branch` | Record seventh validation-fix worktree state | 0 | passed | Output: `## v0.3-lcoal` plus modified `docs/iterations/v0.2-post-closeout/findings.md`. |
| `make test-e2e` | Seventh validation-fix rerun of the blocking browser E2E command | 2 | blocked | Same blocker reproduced: Playwright web server started, then failed to bind `127.0.0.1:8000` with `operation not permitted`; no browser tests executed. |
| `git diff --check` | Seventh validation-fix documentation whitespace check | 0 | passed | No output after validation doc edits. |

## Checks Not Run

Current 2026-05-29 host-capable rerun: none.

Historical 2026-05-28 blocked run:

| Check | Reason | Blocker |
|---|---|---|
| Browser E2E test cases | Playwright web server failed before test execution. | `make test-e2e` failed to bind backend server on `127.0.0.1:8000` with `operation not permitted`. |

## Release Claim Checks

| Claim | Evidence checked | Result | Finding |
|---|---|---|---|
| v0.2 closeout status remains final / complete | `docs/releases/v0.2.md` says `Status: final / closeout complete`. | passed | none |
| v0.2 does not claim product UI | `docs/releases/v0.2.md` says v0.2 does not provide a product client and lists product UI as future scope. | passed | none |
| v0.2 does not claim WorldSpec runtime loading | `docs/releases/v0.2.md` says v0.2 does not load WorldSpec into runtime and lists loader/runtime bridge as future scope. | passed | none |
| v0.2 preserves existing runtime behavior | Backend tests passed; API smoke passed for runtime state, step, events, event steps, params, snapshots, and summaries; browser E2E passed with 6 tests. | passed | none |

## Compatibility Findings

- API envelope: API smoke returned `code=0` and `data` for required successful
  responses.
- Runtime step: `POST /runtime/step` returned `200 code=0`; backend tests
  passed.
- World events: `GET /world/events` returned `200 code=0`; backend tests
  passed.
- Event steps: `GET /world/event-steps` returned `200 code=0`; backend tests
  passed.
- Params: `GET /world/params` and safe `POST /world/params/apply` returned
  `200 code=0`; the first malformed smoke payload correctly returned 422.
- Archive: `GET /world/snapshots` and `GET /world/summaries` returned
  `200 code=0`; backend tests passed.
- Schema smoke: backend deterministic suite passed, including schema smoke
  tests.
- Event refs: backend deterministic suite passed, including event compatibility
  tests.

## Concrete Demo-World Regression Check

- Files checked: `docs/releases/v0.2.md`, `docs/iterations/v0.2/**`,
  `docs/scope-boundaries.md`, `docs/external-fixture-boundary.md`,
  `backend/app`, `frontend`
- Result: passed; no runtime implementation regression observed.
- Finding: the wording sweep found boundary, future-scope, and historical
  references only. `git diff --name-only` was empty before report edits, so no
  runtime, fixture, frontend, or backend implementation file changed during
  validation.

## Unresolved P1/P2/P3

- P1: none.
- P2: none. The historical browser E2E bind blocker was resolved by the
  2026-05-29 host-capable rerun; `make test-e2e` exited `0` with `6 passed`.
- P3: none.

## Final Assessment

`passed`

Backend deterministic checks, API smoke, Playwright availability, and
configured browser E2E passed with current-session evidence. The historical
browser E2E bind blocker remains visible above as prior evidence, but it is no
longer unresolved for this host-capable validation run.
