# Review

Chinese mirror: `review.zh.md`.

Status: final / focused verification passed
implementation_authorized: yes
evidence_execution_authorized: no
provider_live_call_authorized: no
external_validation_authorized: no

## Changed Files

Documentation draft includes this package's README, intent, contract,
technical-design, test-plan, plan, review, and Chinese mirrors.

Planned implementation files are listed in `README.md`.

## Commands Run

```bash
git diff --check
```

Result: passed with no output.

```bash
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.10/0.10.4-bounded-session-runtime-and-snapshot-evidence')
required = {
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
}
missing = sorted(name for name in required if not (pkg / name).exists())
empty = sorted(name for name in required if (pkg / name).exists() and (pkg / name).stat().st_size == 0)
print({'files': len(list(pkg.glob('*.md'))), 'missing': missing, 'empty': empty})
raise SystemExit(1 if missing or empty else 0)
PY
```

Result: `{'files': 14, 'missing': [], 'empty': []}`.

```bash
rg -n "implementation_authorized: yes|evidence_execution_authorized: yes|provider_live_call_authorized: yes|external_validation_authorized: yes" docs/iterations/v0.10/0.10.4-bounded-session-runtime-and-snapshot-evidence
```

Result: only plan instructions mention the future authorization string; no
active authorization field is open.

## Test Results

```bash
python3 -m pytest app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py
```

Initial result before evaluator fix: 29 passed.

Result after repeated-run snapshot evidence fix: 30 passed.

```bash
python3 -m pytest app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py app/tests/test_llm_worldview_generation_api.py app/tests/test_archive_snapshot_summary.py
```

Initial result before evaluator fix: 53 passed.

Result after repeated-run snapshot evidence fix: 54 passed.

## Documentation / Contract Review

Read-only evaluator `019ebd1a-6c2f-7ce1-ae01-6b2ed62722bb`: PASS.

Evidence:

- Required mixed-package docs and mirrors are present: 14 markdown files, no
  missing or empty files.
- Active auth fields remained closed before approval.
- Scope excludes live provider, dashboard, checker fixtures, Validation
  Client, generated results, external validation, durable persistence/migration,
  and `backend/worldengine/`.
- Allowed files are bounded to session schemas/store/routes, manifest route,
  focused backend tests, and package/parent docs.
- Test plan covers focused and expanded focused backend regression and
  explicitly excludes live provider/E2E/Validation Client/external checker
  suites.
- No P1/P2 findings block implementation authorization.

## Compatibility Review

Draft contract is additive. It wraps existing runtime controls and snapshot
stores without breaking existing `/runtime/*` endpoints.

## Scope Review

Draft excludes infinite default runs, live provider calls, provider-cost
execution, dashboard UI, checker fixtures, Validation Client implementation,
generated result files, external validation, durable persistence/migration,
and `backend/worldengine/`.

Implementation closeout evaluator `019ebd1a-6c2f-7ce1-ae01-6b2ed62722bb`
initial result: BLOCKED.

Findings and resolution:

- P1: fixed. The first implementation mixed global `snapshot_count_before`
  with run-window filtered `snapshot_count_after`, so repeated bounded runs
  could report new snapshot ids while returning `snapshot_delta_count: 0`.
  The route now records global snapshot counts before and after the run while
  keeping run-window snapshot ids for evidence. Added
  `test_repeated_session_run_reports_new_snapshot_delta`.
- P2: accepted as broader dirty-worktree scope note, not 0.10.4
  implementation drift. The evaluator saw existing dirty files from earlier
  completed v0.10 packages (`backend/app/api/app_factory.py`,
  `backend/app/api/routes/__init__.py`, and `backend/app/schemas/world.py`).
  0.10.4 implementation remains scoped to the allowed session schema/store,
  session route, manifest route, focused tests, and package/parent docs.

## Unresolved Findings

Implementation closeout evaluator re-review
`019ebd1a-6c2f-7ce1-ae01-6b2ed62722bb`: PASS.

Evidence:

- P1 repeated-run snapshot evidence bug is fixed. Read-only evaluator
  reproduced two consecutive bounded session runs with
  `WORLD_SNAPSHOT_INTERVAL_TICKS=1`; the second run reported
  `snapshot_count_before: 2`, `snapshot_count_after: 4`,
  `snapshot_delta_count: 2`, and two run-window `snapshot_ids`.
- The route now uses global snapshot counts before and after the run for delta
  accounting while preserving run-window snapshot ids.
- P2 broader dirty-worktree scope note is accepted and does not block 0.10.4
  closeout. `backend/app/api/app_factory.py`,
  `backend/app/api/routes/__init__.py`, and `backend/app/schemas/world.py`
  are recorded as broader dirty-worktree files from earlier v0.10 packages,
  not new 0.10.4 implementation drift.
- 0.10.4 remains scoped to session schema/store, session route, manifest
  route, focused tests, and package/parent docs.
- Evaluator reran `git diff --check`: passed with no output.

- P1: none.
- P2: none.
- P3: none.

## Final Assessment

PASS. 0.10.4 implementation is complete within package scope and focused
verification passed.
