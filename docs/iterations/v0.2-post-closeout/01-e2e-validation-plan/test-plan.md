# Test Plan

Status: planned / ready for review

## Future Execution Checks

The later execution package should run or explicitly record blockers for:

```bash
git status --short --branch
git rev-parse HEAD
git diff --check
```

Documentation and release claim checks:

```bash
test -f docs/releases/v0.2.md
test -f docs/iterations/v0.2/evidence-index.md
test -f docs/iterations/v0.2/compatibility-review.md
test -f docs/iterations/v0.2/boundary-audit.md
rg -n "final / closeout complete|0.2.12 verification is documentation-only|does not rerun" docs/releases/v0.2.md
```

Backend deterministic checks to consider:

```bash
cd backend && .venv/bin/python -m pytest app/tests -q
```

Focused checks to consider:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_cell_schema.py app/tests/test_worldspec_schema_smoke.py -q
cd backend && .venv/bin/python -m pytest app/tests/test_event_schema_compat.py app/tests/test_event_api_compat.py -q
cd backend && .venv/bin/python -m pytest app/tests/test_runtime_step.py app/tests/test_world_params.py app/tests/test_archive_snapshot_summary.py -q
```

API smoke may use TestClient or curl. If curl is used, execution must first
start the backend using the repository-supported command and record the server
command, port, environment variables, and shutdown handling.

E2E availability check:

```bash
test -f frontend/playwright.config.ts
test -f frontend/package.json
```

Presence of these files is not enough to prove E2E is runnable. Execution must
discover install, start, and test commands and record blockers for missing
dependencies, browser binaries, ports, services, or environment variables.

## Expected Results

- Commands that run successfully must record exit code and output summary.
- Commands that cannot run must record blocker, reason, and impact.
- Browser E2E may be marked not configured or blocked if unavailable.
- Fallback validation must use API smoke plus backend integration checks.

## Commands Not Run In This Package

All backend, frontend, E2E, API smoke, runtime, schema execution, fixture, and
migration commands are not run here because this package is planning-only.

## Blocker Recording Rule

If any required command cannot run, the execution report must classify the
result as `blocked` unless another completed validation line proves the same
claim and the report explains the substitution.

## No Unverified Claims Rule

Do not claim a check succeeded unless it ran in the same execution session and
its command result is recorded.
