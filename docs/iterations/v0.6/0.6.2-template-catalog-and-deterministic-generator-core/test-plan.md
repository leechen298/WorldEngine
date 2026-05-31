# Test Plan

Status: review complete

## Documentation Stage Checks

Run before implementation authorization:

```bash
git status --short --branch
git diff --check
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
python3 -c "import subprocess; allowed_prefixes=('docs/iterations/v0.6/',); lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[]; [bad.append(line) for line in lines if line and not line[3:].startswith(allowed_prefixes)]; print('unexpected_status=' + str(len(bad))); [print(item) for item in bad]; raise SystemExit(1 if bad else 0)"
```

Expected:

- `git diff --check` exits `0`.
- required docs/mirrors check prints `missing=0`.
- documentation-stage scope guard prints `unexpected_status=0`.

## Focused Implementation Tests

Run after implementation:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_generation_schema.py app/tests/test_template_catalog.py app/tests/test_deterministic_world_generation.py
```

Expected: all focused generation tests pass.

Focused tests must cover:

- generation schema defaults and required fields.
- same input produces stable `WorldSpec.model_dump()` output.
- different seed material changes reviewed deterministic ids or metadata while
  preserving `WorldSpec` validity.
- generated output contains only generic ids/labels and no concrete world,
  story, oracle, or application data.
- invalid templates produce deterministic diagnostics for duplicate cell ids,
  duplicate entity refs, invalid bounds, unsupported entity kinds, empty ids,
  and unknown/unsupported template versions.
- diagnostics include stable code, severity, message, optional path, and source
  context.
- generator does not mutate template input objects.

## Compatibility Regression Tests

Run after implementation:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_cell_schema.py app/tests/test_worldspec_schema_smoke.py app/tests/test_worldspec_loader.py app/tests/test_runtime_context_bridge.py
```

Expected: existing schema, loader, and runtime-context bridge tests pass.

Run full backend regression if focused and adjacent tests pass:

```bash
cd backend && .venv/bin/python -m pytest app/tests
```

Expected: full backend regression passes, or failures are recorded exactly and
classified before closeout.

## Scope Guard After Implementation

Run from repo root:

```bash
python3 -c "import subprocess; allowed_prefixes=('docs/iterations/v0.6/','backend/app/schemas/world_generation.py','backend/app/core/world_generation.py','backend/app/tests/test_world_generation_schema.py','backend/app/tests/test_template_catalog.py','backend/app/tests/test_deterministic_world_generation.py'); lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[]; [bad.append(line) for line in lines if line and not any(line[3:].startswith(prefix) for prefix in allowed_prefixes)]; print('unexpected_status=' + str(len(bad))); [print(item) for item in bad]; raise SystemExit(1 if bad else 0)"
```

Expected: `unexpected_status=0`.

## Commands Not Run Before Authorization

No backend implementation tests are run before `implementation_authorized: yes`
because the implementation files do not exist yet and this package is still in
documentation review.

Frontend, API smoke, E2E, Agent smoke, autonomous validation, migration,
external validation, projection, and release commands remain out of scope for
this package unless a later reviewed package authorizes them.

## Blocker Recording Rule

Any failed command must be recorded in `review.md` with exact command, exit
status, and failure summary. P1 blocks implementation or closeout. Unresolved
P2 blocks final package handoff unless explicitly accepted by the contract and
review.
