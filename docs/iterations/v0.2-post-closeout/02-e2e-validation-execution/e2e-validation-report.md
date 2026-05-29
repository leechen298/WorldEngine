# E2E / Integration / API Smoke Validation Report

Status: blocked

## Metadata

- Reviewed branch: `v0.3-lcoal`
- Reviewed commit: `47b2dac6a08fdf7c249844b1f5447af17ab37d86`
- Execution date: 2026-05-28
- Executor: Codex F
- Final assessment: `blocked`

Allowed final assessment values:

- `passed`
- `passed with P3`
- `blocked`
- `failed`
- `not executed`

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

## Checks Not Run

| Check | Reason | Blocker |
|---|---|---|
| Browser E2E test cases | Playwright web server failed before test execution. | `make test-e2e` failed to bind backend server on `127.0.0.1:8000` with `operation not permitted`. |

## Release Claim Checks

| Claim | Evidence checked | Result | Finding |
|---|---|---|---|
| v0.2 closeout status remains final / complete | `docs/releases/v0.2.md` says `Status: final / closeout complete`. | passed | none |
| v0.2 does not claim product UI | `docs/releases/v0.2.md` says v0.2 does not provide a product client and lists product UI as future scope. | passed | none |
| v0.2 does not claim WorldSpec runtime loading | `docs/releases/v0.2.md` says v0.2 does not load WorldSpec into runtime and lists loader/runtime bridge as future scope. | passed | none |
| v0.2 preserves existing runtime behavior | Backend tests passed; API smoke passed for runtime state, step, events, event steps, params, snapshots, and summaries. | passed with E2E blocker | Browser E2E remains blocked. |

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
- Result: blocked overall, no runtime implementation regression observed.
- Finding: the wording sweep found boundary, future-scope, and historical
  references only. `git diff --name-only` was empty before report edits, so no
  runtime, fixture, frontend, or backend implementation file changed during
  validation.

## Unresolved P1/P2/P3

- P1: none.
- P2: Browser E2E is blocked because `make test-e2e` cannot bind the backend
  web server to `127.0.0.1:8000` in this execution context.
- P3: none.

## Final Assessment

`blocked`

Backend deterministic checks and API smoke passed with current-session
evidence. Configured browser E2E did not run because server startup was
blocked before Playwright executed any tests. This package cannot record a
clean validation pass until browser E2E is rerun in an environment that can
bind the configured backend port, or the blocker is explicitly accepted by a
later validation bundle.
