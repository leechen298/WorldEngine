# Test Plan

## Exact Commands To Run

Required documentation commands for this package:

```bash
git status --short --branch
git diff --check
```

Package-specific verification expectations:

- `git status --short --branch`
- `git diff --check`
- file existence checks for required docs and mirrors
- changed-file scope guard against the active package contract
- Run focused backend/API tests from `backend/`:

```bash
.venv/bin/python -m pytest app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py app/tests/test_params_agent.py app/tests/test_event_api_compat.py app/tests/test_runtime_step.py -q
```

- Run the broad backend regression from `backend/` after implementation changes:

```bash
.venv/bin/python -m pytest app/tests tests -q
```

- Treat `app/tests/test_agent_loop_api.py` as the FastAPI TestClient API smoke for the new route and the compatibility check for the existing `/world/agent/params/propose-and-apply` route.

If this package changes backend implementation files in a future execution pass, run the focused backend/API command above and then the broad backend regression command above.

## Expected Results

- Documentation checks exit `0`.
- Required files and mirrors exist.
- No changed files appear outside the active package contract.
- Any backend/API/E2E/runtime pass claim is backed by a command from the current session or is recorded as not run.

## Commands Not Run And Why

Backend, API smoke, runtime behavior, and test implementation commands are not run during documentation drafting unless implementation files are changed in a later authorized pass. Frontend, E2E, Agent smoke, build, fixture, and migration commands are not expected unless this package unexpectedly touches those surfaces; such scope expansion would require review before execution.

## Blocker Recording Rule

If a command cannot run, if an evaluator checkpoint is unavailable, or if a required file is missing, record `blocked` or `needs-user-input` in `review.md` with the exact command, missing file, or unavailable checkpoint.

## No Unverified Claims Rule

Do not mark tests, API smoke, E2E, backend checks, frontend checks, runtime behavior, migration, fixture behavior, release status, or closeout status as passed unless the command or review was run in the current session or explicitly accepted by the active contract with rationale.
