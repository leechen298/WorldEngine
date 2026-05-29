# Test Plan

Status: planned / ready for review

## Autonomous Reviewer Checks

The later Codex reviewer must run or record blockers for:

```bash
git status --short --branch
git rev-parse HEAD
git diff --check
```

The reviewer should inspect required docs and code:

```bash
test -f README.md
test -f docs/releases/v0.2.md
test -f docs/iterations/v0.2/evidence-index.md
test -f docs/iterations/v0.2/compatibility-review.md
test -f docs/iterations/v0.2/boundary-audit.md
test -f docs/scope-boundaries.md
test -f backend/app/schemas/world_cell.py
test -f backend/app/schemas/event.py
test -d backend/app/tests
```

The reviewer should run focused validation commands when the environment is
ready, or record blockers when it is not:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_cell_schema.py app/tests/test_worldspec_schema_smoke.py -q
cd backend && .venv/bin/python -m pytest app/tests/test_event_schema_compat.py app/tests/test_event_api_compat.py -q
```

The reviewer may run broader checks if the environment is ready:

```bash
cd backend && .venv/bin/python -m pytest app/tests -q
```

## Expected Results

- Every file read must be listed in the independent review.
- Every command run must include exit code and result summary.
- Every skipped command must include reason and blocker impact.
- Unsupported claims must be listed.

## Commands Not Run In This Package

No autonomous validation commands are run during this planning package.

## Blocker Recording Rule

If the reviewer cannot run a required command, the review must record the
blocker and explain whether it prevents final recommendation.

## No Unverified Claims Rule

The reviewer must not state that tests, runtime behavior, API behavior, or E2E
behavior succeeded unless the reviewer ran the relevant command in the same
session.
