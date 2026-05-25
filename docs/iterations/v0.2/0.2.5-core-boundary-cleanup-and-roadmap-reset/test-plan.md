# Test Plan

## Documentation-Planning Pass

This pass creates only the 0.2.5 iteration package documents. Do not run
backend tests, frontend tests, E2E tests, runtime smoke tests, schema tests, or
fixture tests during this pass.

Allowed documentation checks:

```bash
git status --short --branch
find docs/iterations/v0.2/0.2.5-core-boundary-cleanup-and-roadmap-reset -maxdepth 1 -type f | sort
git diff --check
```

## Implementation-Stage Commands

After the contract, technical design, test plan, and plan are reviewed and
approved, the implementation stage should run:

```bash
rg -n "tiny|village|Village|Tiny|workshop|square|notice-board|reference village|village-like" .
make check-backend
cd backend && .venv/bin/python -m pytest app/tests/test_worldspec_schema_smoke.py -q
cd backend && .venv/bin/python -m pytest app/tests -q
git diff --check
```

If the implementation keeps the old test file name instead of creating
`test_worldspec_schema_smoke.py`, replace the focused pytest command with the
actual focused test path used by the implementation.

## Search Acceptance

The `rg` search is expected to find historical references before cleanup. After
implementation:

- active docs must not retain concrete Demo world anchors.
- active tests must not retain concrete Demo world anchors.
- active fixtures must not retain concrete Demo world anchors.
- historical iteration documents may retain old wording only when marked as
  historical context by the 0.2.5 cleanup.
- this 0.2.5 package may mention old terms to define the cleanup scope.

## Backend Checks

`make check-backend` verifies that the backend virtual environment exists. It
does not prove backend tests pass.

The focused backend pytest command must prove the generic WorldSpec schema
smoke test passes. The broader backend pytest command should run because the
implementation changes backend test and fixture files.

## Frontend Checks

Do not run frontend tests unless implementation changes frontend files or a
repository-level check command is introduced that intentionally covers frontend
verification. This package forbids frontend dashboard changes, so frontend test
execution should normally be out of scope.

## No Unverified Claims

Do not claim tests, runtime behavior, frontend behavior, E2E behavior, or smoke
flows passed unless the exact command or flow was run in the current
implementation session and recorded in `review.md`.
