# Execution Plan

Status: blocked

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

The 2026-05-28 execution reached this output state, but browser E2E remains
blocked because the configured backend web server cannot bind
`127.0.0.1:8000` in the execution context.
