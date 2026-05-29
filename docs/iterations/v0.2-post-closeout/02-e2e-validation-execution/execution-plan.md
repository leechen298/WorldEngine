# Execution Plan

Status: package complete / passed current campaign

## Steps

1. Confirm branch and commit:

   ```bash
   git status --short --branch
   git rev-parse HEAD
   ```

2. Run documentation checks:

   ```bash
   git diff --check
   test -f docs/releases/v0.2.md
   test -f docs/iterations/v0.2/evidence-index.md
   test -f docs/iterations/v0.2/compatibility-review.md
   test -f docs/iterations/v0.2/boundary-audit.md
   ```

3. Run backend deterministic checks if dependencies are available.

4. Inspect API route files under `backend/app/api/routes/`.

5. Run API smoke using TestClient or curl.

6. Check E2E framework availability by inspecting `frontend/package.json`,
   `frontend/playwright.config.ts`, installed dependencies, browser binaries,
   service start commands, ports, and required environment variables.

7. Run browser E2E if configured and runnable.

8. Record E2E as not configured or blocked if unavailable. Do not treat config
   files alone as a successful run.

9. Fill `e2e-validation-report.md`.

10. Classify unresolved issues as P1/P2/P3.

## Required API Smoke Areas

- `GET /health`
- `GET /runtime/state`
- `POST /runtime/step`
- `GET /world/events`
- `GET /world/event-steps`
- `GET /world/params`, if available
- `POST /world/params/apply`, if available and safe test payload exists
- `GET /world/snapshots`, if available
- `GET /world/summaries`, if available

## Stop Conditions

Stop and record a blocker if:

- dependencies are missing and cannot be installed in the execution context.
- required services cannot start.
- ports are unavailable and no alternate port is configured.
- browser dependencies are missing.
- a command fails before producing meaningful validation evidence.
- a release claim conflicts with observed behavior.

## Output

The execution output is `e2e-validation-report.md` plus an updated
`review.md`.

The current campaign reran this output state on 2026-05-29. The rerun kept
prior evidence visible, recorded the sandbox localhost bind blocker, and then
used a host-capable `make test-e2e` rerun. Backend deterministic checks, API
smoke, Playwright availability, and configured browser E2E all passed.
