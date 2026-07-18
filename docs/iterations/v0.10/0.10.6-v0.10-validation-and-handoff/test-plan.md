# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Backend

Run from `backend`:

```bash
python3 -m pytest app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py app/tests/test_llm_worldview_generation_api.py app/tests/test_archive_snapshot_summary.py
```

Expected result: all selected tests pass. Record the exact pass/fail count.
Any failure is `FAIL` unless it is proven to be outside v0.10 reviewed scope.

## Frontend

Run from `frontend`:

```bash
pnpm test
pnpm build
pnpm test:e2e -- dashboard.spec.ts
```

Expected results:

- `pnpm test`: all frontend unit tests pass; record file/test counts.
- `pnpm build`: TypeScript and Vite build pass. Record any warnings.
- `pnpm test:e2e -- dashboard.spec.ts`: targeted dashboard E2E passes. If the
  sandboxed web server cannot bind local ports, record the exact failure and
  rerun only with approved elevated permissions.

If E2E is blocked by sandbox port binding, rerun with approved elevated
permissions and record both attempts.

## Manifest Inspection

Run from `backend`:

```bash
python3 - <<'PY'
from fastapi.testclient import TestClient
from app.api.app_factory import create_app
payload = TestClient(create_app()).get('/manifest').json()
print(payload['worldengine_version'])
print(payload['manifest_status'])
print([(item['method'], item['path'], item['status'], item['validation_status']) for item in payload['public_surfaces'] if item['path'].startswith('/sessions')])
print(payload['checker_handoff']['unsupported_items'])
PY
```

Expected result:

- `worldengine_version` is `v0.10`.
- manifest status remains honest; provider/live evidence may remain blocked.
- session create/from-worldview/run/pause/resume/snapshots surfaces are
  discoverable with implemented/pass status.
- unsupported items do not claim v0.11/v0.12 work as complete.

## Docs / Whitespace

Run from repo root:

```bash
git diff --check
```

Expected result: no whitespace errors.

## Recording Rules

- Do not claim a test, build, E2E, manifest, provider, Validation Client, or
  checker result passed unless the command or flow was run in this package
  closeout session.
- Record exact command, working directory, result, and relevant pass/fail
  counts.
- If a command is skipped, blocked, or rerun with elevated permissions, record
  why.
- Do not convert earlier package evidence into a new PASS unless the current
  closeout command re-ran or directly inspected it.

Do not run live provider tests, external Validation Client suites, or v0.11/v0.12
feature validation for this package.
