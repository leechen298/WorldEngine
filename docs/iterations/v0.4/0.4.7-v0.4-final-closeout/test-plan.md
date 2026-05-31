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
- Record backend/frontend/API/E2E/runtime tests as not required by this documentation-only package; if the final evaluator reruns backend/API commands, record the commands and results in `review.md` and `final-closeout.md`.

If this package changes backend implementation files in a future execution pass, run focused backend tests from `backend/` with `.venv/bin/python -m pytest ...` and then run adjacent compatibility tests named in the active implementation review.

## Expected Results

- Documentation checks exit `0`.
- Required files and mirrors exist.
- No changed files appear outside the active package contract.
- Any backend/API/E2E/runtime pass claim is backed by a command from the current session or is recorded as not run.

## Commands Not Run And Why

Backend, frontend, API smoke, E2E, Agent smoke, runtime behavior, build, schema execution, fixture, migration, and test implementation commands are not required during documentation drafting. If final closeout repair or evaluator review reruns backend/API checks, those current-session results must be recorded in `review.md` and `final-closeout.md`.

## Blocker Recording Rule

If a command cannot run, if an evaluator checkpoint is unavailable, or if a required file is missing, record `blocked` or `needs-user-input` in `review.md` with the exact command, missing file, or unavailable checkpoint.

## No Unverified Claims Rule

Do not mark tests, API smoke, E2E, backend checks, frontend checks, runtime behavior, migration, fixture behavior, release status, or closeout status as passed unless the command or review was run in the current session or explicitly accepted by the active contract with rationale.
