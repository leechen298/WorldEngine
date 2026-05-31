# Test Plan

Status: review complete

## Documentation-Stage Checks

```bash
git diff --check
```

```bash
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.3-structured-generation-plan-compiler'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

```bash
rg -n "GenerationPlan|PlanCell|PlanGenerationRequest|generate_worldspec_from_plan|validate_generation_plan|implementation_authorized: yes" docs/iterations/v0.6/0.6.3-structured-generation-plan-compiler
```

```bash
python3 -c "import subprocess, re, sys; allowed=[re.compile(r'^ M docs/iterations/v0\\.6/'), re.compile(r'^\\?\\? docs/iterations/v0\\.6/0\\.6\\.3-structured-generation-plan-compiler/')]; lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); unexpected=[line for line in lines if not any(p.search(line) for p in allowed)]; print('unexpected_status=' + str(len(unexpected))); [print(line) for line in unexpected]; sys.exit(1 if unexpected else 0)"
```

No backend implementation tests are run before `implementation_authorized:
yes` because this package is still at documentation review.

## Focused Implementation Tests

After authorization, add or update tests to cover:

- schema construction for `PlanCell`, `GenerationPlan`, and
  `PlanGenerationRequest`.
- valid plan compilation into deterministic `WorldSpec`.
- deterministic output for identical input and changed digest for changed seed
  material.
- invalid plan diagnostics with stable codes and paths.
- duplicate cell ids and duplicate entity refs.
- min/max child-cell constraints and entity-kind allowlist violations.
- unsupported plan versions.
- strict JSON seed/material failures, including set, tuple, `NaN`,
  `Infinity`, and non-string dict keys.
- no input mutation.
- generated content remains generic and contains no concrete world/story or
  application terms.

Expected focused commands after implementation:

```bash
PYTHONPATH=. .venv/bin/pytest app/tests/test_generation_plan_schema.py app/tests/test_structured_generation_plan_compiler.py app/tests/test_world_generation_schema.py app/tests/test_deterministic_world_generation.py -q
```

## Adjacent Compatibility Tests

After implementation, run:

```bash
PYTHONPATH=. .venv/bin/pytest app/tests/test_generation_plan_schema.py app/tests/test_structured_generation_plan_compiler.py app/tests/test_world_generation_schema.py app/tests/test_deterministic_world_generation.py app/tests/test_worldspec_loader.py app/tests/test_runtime_context_bridge.py app/tests/test_world_cell_schema.py -q
```

## Broader Regression

Run full backend app tests before closeout:

```bash
PYTHONPATH=. .venv/bin/pytest app/tests -q
```

## Evidence Rules

Record each command, exit status, pass/fail count, and failure summary in
`review.md`. P1 blocks implementation or closeout. Unresolved P2 blocks
closeout unless explicitly accepted by this package contract.
