# Review

Chinese mirror: `review.zh.md`.

Status: implementation complete / focused verification passed

implementation_authorized: yes
provider_live_call_authorized: no
generated_result_creation_authorized: no
external_validation_authorized: no

## Changed Files

Documentation draft:

```text
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/README.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/README.zh.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/intent.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/intent.zh.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/contract.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/contract.zh.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/technical-design.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/technical-design.zh.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/test-plan.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/test-plan.zh.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/plan.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/plan.zh.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/review.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/review.zh.md
```

Implementation files:

```text
backend/app/schemas/runtime.py
backend/app/core/runtime_engine.py
backend/app/api/routes/runtime.py
backend/app/tests/test_runtime_bounded_run.py
```

## Commands Run

Documentation checks:

```text
git diff --check
```

Result: exit 0, no output.

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget"); expected={"README","intent","contract","technical-design","test-plan","plan","review"}; names={p.name for p in root.glob("*.md")}; missing=[]; [missing.append(f"{base}.md") for base in sorted(expected) if f"{base}.md" not in names]; [missing.append(f"{base}.zh.md") for base in sorted(expected) if f"{base}.zh.md" not in names]; print("files", len(names)); print("missing", missing); raise SystemExit(1 if missing else 0)'
```

Result: exit 0; `files 14`; `missing []`.

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget"); combined="\n".join(p.read_text() for p in root.glob("*.md")); required=["implementation_authorized: n[o]","provider_live_call_authorized: no","generated_result_creation_authorized: no","external_validation_authorized: no","RuntimeRunRequest","RuntimeRunSummary","pause","resume","bounded runtime"]; missing=[term for term in required if term not in combined]; print("missing", missing); raise SystemExit(1 if missing else 0)'
```

Result before documentation review authorization: exit 0; `missing []`.

```text
rg -n 'implementation_authorized: y[e]s|provider_live_call_authorized: y[e]s|generated_result_creation_authorized: y[e]s|external_validation_authorized: y[e]s|Status: read[y] for implementation|Status：read[y] for implementation' docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget
```

Result before documentation review authorization: exit 1, no output; no
implementation authorization or live execution authorization text found at that
time.

Focused implementation test:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_runtime_bounded_run.py -q
```

Initial RED result: exit 2, expected import failure for missing
`app.schemas.runtime`.

GREEN result after implementation: exit 0; `7 passed in 0.28s`.

Post-review P1/P2 regression result after adding max-duration guard and
extra-field coverage: exit 0; `8 passed in 0.31s`.

Related runtime regression:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_runtime_bounded_run.py app/tests/test_runtime_step.py app/tests/test_archive_snapshot_summary.py app/tests/test_dry_run_validation.py app/tests/test_agent_loop_api.py -q
```

Initial result: exit 0; `53 passed in 0.91s`.

Post-review P1/P2 regression result: exit 0; `54 passed in 0.94s`.

Backend regression:

```text
cd backend && .venv/bin/python -m pytest app/tests -q
```

Initial result: exit 0; `296 passed in 2.84s`.

Post-review P1/P2 regression result: exit 0; `297 passed in 2.87s`.

Final closeout verification after review and parent route documentation
updates:

- `git diff --check`: exit 0, no output.
- `cd backend && .venv/bin/python -m pytest app/tests/test_runtime_bounded_run.py -q`:
  exit 0; `8 passed in 0.31s`.
- `cd backend && .venv/bin/python -m pytest app/tests/test_runtime_bounded_run.py app/tests/test_runtime_step.py app/tests/test_archive_snapshot_summary.py app/tests/test_dry_run_validation.py app/tests/test_agent_loop_api.py -q`:
  exit 0; `54 passed in 0.88s`.
- `cd backend && .venv/bin/python -m pytest app/tests -q`: exit 0;
  `297 passed in 2.72s`.

## Test Results

Focused, related runtime, and backend regression tests passed as recorded
above, including final closeout verification after documentation route
updates. Provider, checker, external validation, generated-result, E2E,
autonomous, and Validation Client tests were not run because this package does
not authorize them.

## Compatibility Review

Implementation added additive runtime-control schemas, synchronous in-memory
bounded run behavior, and runtime API endpoints while preserving existing
`/runtime/step`, `/runtime/state`, event, snapshot, archive, world params,
Agent loop, and world generation behavior under regression tests.

## Scope Review

Implementation stayed scoped to active-backend in-memory bounded runtime
controls. It did not add live provider calls, generated-result creation,
checker execution, external validation, Validation Client code, frontend UI,
durable scheduling, event legality, Agent continuity, or `backend/worldengine/`
changes.

## Subagent Findings

Read-only documentation/contract evaluator:

```text
agent: 019e98bb-e5c2-7b61-a6fc-afd598a87fd4
scope: docs/contract/test-plan/mirror review only
status: initial review complete
```

Initial verdict: FAIL due to one blocking P2 and no P0/P1.

- P2: `test-plan.md` and `test-plan.zh.md` did not explicitly require focused
  tests for public run summary fields, even though the contract exit criteria
  required public run summary coverage.

Fix applied:

- `test-plan.md` and `test-plan.zh.md` now explicitly require focused tests for
  public run summary fields.

Final documentation gate assessment:

- P0: none.
- P1: none.
- P2: none after the local fix above.
- Implementation is authorized only for the reviewed active-backend in-memory
  `0.9.5` bounded runtime control scope.
- Provider live calls, generated-result creation, checker execution, external
  validation, Validation Client changes, frontend UI, durable scheduling,
  event legality, Agent continuity, and `backend/worldengine/` remain
  unauthorized.

Implementation-scope review verdict: initial FAIL due to one P1 and one P2.

- P1: tick-targeted bounded runs did not enforce `max_duration_seconds`.
- P2: extra-field rejection existed through `extra="forbid"` but was not
  covered by focused tests.

Fix applied:

- Added focused tests for extra-field rejection in `RuntimeRunRequest` and
  `/runtime/run`.
- Added focused test for tick-targeted runs stopping before the next step would
  exceed `max_duration_seconds`.
- Added `max_duration_reached` stop reason.
- Updated `RuntimeEngine.run_bounded()` to stop before the next step would
  exceed `max_duration_seconds`.

Implementation re-review verdict: PASS.

- Agent: `019e98bb-e5c2-7b61-a6fc-afd598a87fd4`.
- Result: no new P0/P1/P2/P3 findings.
- P1 closed: tick-targeted runs now stop before the next `step()` would exceed
  `max_duration_seconds`, and `max_duration_reached` is a public stop reason.
- P2 closed: extra-field rejection remains enforced by `extra="forbid"` and is
  now covered by focused schema and API tests.
- Scope remains clean: no live provider calls, generated-result creation,
  checker execution, external validation, Validation Client work, frontend UI
  work, durable scheduling/background worker behavior, event legality, Agent
  continuity, or `backend/worldengine/` changes were found in the reviewed
  `0.9.5` path.

## Unresolved P1/P2/P3

- None.

## Final Assessment

Implementation complete for the reviewed active-backend in-memory bounded
runtime-control scope. Focused, related runtime, and backend regression
verification passed as recorded above, and read-only implementation re-review
reported PASS with no unresolved P1/P2/P3 findings.

Provider live calls, generated-result creation, checker execution, external
validation, Validation Client changes, frontend UI, durable scheduling,
event legality, Agent continuity, and `backend/worldengine/` changes remain
unauthorized and unclaimed.
