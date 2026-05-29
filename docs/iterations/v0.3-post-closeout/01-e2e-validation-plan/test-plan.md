# Test Plan

Status: planned / not executed

This is a plan for future validation. Do not run these commands in this
package.

## Future Exact Commands

Repository and documentation checks:

```bash
git status --short --branch
git diff --check
```

Branch and commit recording:

```bash
git rev-parse HEAD
```

Backend deterministic checks:

```bash
cd backend
../.venv/bin/python -m pytest app/tests
```

If the repository's active backend venv path differs, record the actual command
and why it changed.

Focused WorldSpec loader tests:

```bash
cd backend
../.venv/bin/python -m pytest app/tests/test_worldspec_loader.py
```

Focused runtime context bridge tests:

```bash
cd backend
../.venv/bin/python -m pytest app/tests/test_runtime_context_bridge.py
```

Event API compatibility tests:

```bash
cd backend
../.venv/bin/python -m pytest app/tests/test_event_api_compat.py app/tests/test_event_schema_compat.py
```

API smoke checks:

- Inspect route files and app factory.
- Use FastAPI `TestClient` or `curl` against a running local backend.
- Cover health, runtime step, `/world/events`, and `/world/event-steps`.

E2E framework availability:

- Check for package scripts, Playwright config, dependencies, and browser
  availability.
- Record `not configured` or `blocked` when no runnable setup exists.

Browser E2E execution:

- Run the configured E2E command only when dependencies, services, ports, and
  browsers are available.

## Expected Results

- Documentation checks report no whitespace or required-file issues.
- Backend deterministic checks complete or record a blocker.
- Loader tests validate valid mapping/JSON input, malformed JSON,
  unsupported input, schema errors, and pointer paths.
- Runtime context bridge tests validate context derivation, invalid inputs,
  inert runtime storage, and absence of raw WorldSpec/root payloads in events.
- Event compatibility tests validate empty refs omission and non-empty refs
  presence.
- API smoke validates current response shapes without changing routes.
- E2E either runs with evidence or is recorded as not configured / blocked.
- Release claim validation distinguishes historical evidence from current
  campaign evidence.
- Concrete demo-world regression check confirms no new concrete demo-world
  details appear in core docs or code changed by the validation campaign.

## Commands Not Run And Why

No commands in this test plan are run by `01-e2e-validation-plan` because this
package is planning-only.

## Blocker Recording Rule

If any future command cannot run, record:

- exact command.
- working directory.
- exit code, if available.
- stderr or summarized failure.
- whether the result is `blocked` or `failed`.
- follow-up owner or package.

## No Unverified Claims Rule

Do not mark any check as successful unless the future execution package records
current-session evidence or an explicit accepted historical-evidence rationale.
