# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Documentation Gate

Run before implementation authorization:

```bash
git diff --check
python3 -c "from pathlib import Path; p=Path('docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor'); required=['README.md','README.zh.md','intent.md','intent.zh.md','contract.md','contract.zh.md','technical-design.md','technical-design.zh.md','test-plan.md','test-plan.zh.md','plan.md','plan.zh.md','review.md','review.zh.md']; print({'missing':[n for n in required if not (p/n).exists()],'empty':[n for n in required if (p/n).exists() and not (p/n).read_text().strip()]})"
rg -n "implementation_authorized: yes|external_repository_changes_authorized: yes|evidence_execution_authorized: yes" docs/iterations/v0.13
rg -n "Godot.*(node|scene tree|collision|frame)|concrete.*world|raw thought|private memory" docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor
```

Expected result: no whitespace errors; no missing/empty package files; no
active authorization set to `yes`; no contract wording that moves concrete
external content or engine-specific runtime semantics into WorldEngine.

## Planned Focused Backend Tests

After implementation authorization, add and run focused tests covering:

```bash
cd backend
.venv/bin/python -m pytest \
  app/tests/test_engine_v1_generation.py \
  app/tests/test_engine_v1_session.py \
  app/tests/test_engine_v1_agent.py \
  app/tests/test_engine_v1_interventions.py \
  app/tests/test_engine_v1_protocol.py -q
```

Required assertions:

- `AC-01`: same normalized brief and seed produce the same ready package hash;
  an allowed input change changes the hash and relevant public field.
- `AC-02`: session source hash equals the generated package hash; initial
  snapshot, canonical state, and projection revision/state hash agree.
- `AC-03`: `step N` advances exactly N ticks and monotonic time, sequence, and
  revision.
- `AC-04`: one Agent produces perception -> decision -> action request -> rule
  judgment -> result -> event -> diff -> experience evidence.
- `AC-05`: a later Agent decision cites prior public experience and produces a
  machine-observable changed decision/evidence result.
- `AC-06`: one bounded direction is accepted in an explicit window and applied
  only through a later rule-linked event and non-empty diff.
- `AC-07`: one direct-final-fact direction submitted in the same window is
  rejected with stable reason, rejected event, no diff, and no target change.
- `AC-08`: duplicate request IDs are idempotent; stale revisions conflict
  without mutation.
- `AC-09`: every current state hash can be reproduced from the recorded
  snapshot/diff chain owned by this minimum run.
- `AC-10`: a black-box test client using only base URL and capability manifest
  completes generation, boot, step, Agent inspection, both directions, event
  polling, and evidence export.

## Planned Frontend Verification

```bash
cd frontend
pnpm test
pnpm build
pnpm test:e2e --grep "minimum runnable anchor"
```

Required coverage:

- administration console generates a package and displays readiness/hash.
- it boots and steps the same session through APIs.
- it displays session ID, tick, revision, and state hash from public projection.
- it displays the Agent causal chain and prior-experience reference.
- it submits accepted and rejected directions through the explicit window.
- it displays events/diffs/snapshots and can request evidence export.
- it does not import backend code or write storage directly.

## Planned Regression Verification

After focused verification and implementation-scope review:

```bash
cd backend
.venv/bin/python -m pytest -q
cd ../frontend
pnpm test
pnpm build
```

Run broader E2E only after focused backend/frontend tests pass and the
code-review evaluator reports no P1/P2.

## Black-box API Smoke

The implementation plan must add a command or test that starts WorldEngine in
a clean process and drives the flow using only HTTP and manifest discovery. It
must print correlation IDs and the final WorldEngine-side classification but
must not claim complete v0.13 PASS.

## Blocker And Result Rules

- `PASS`: assertion executed and current evidence proves expected behavior.
- `FAIL`: assertion executed but behavior or evidence differs.
- `BLOCKED`: a required command cannot execute because a required dependency or
  environment is unavailable.
- `NOT_RUN`: intentionally not executed in the current stage.
- Missing evidence is never PASS and should be FAIL when the path executed.
- Record exact commands, exit codes, counts, and artifact paths in `review.md`.

## Not Run During Documentation Stage

- Backend/frontend/runtime tests: no implementation is authorized yet.
- Provider live calls: forbidden for the required path.
- Godot and external checker: owned by `0.13.1` and `0.13.2`.
- Complete MVP validation: requires external current-run evidence.
