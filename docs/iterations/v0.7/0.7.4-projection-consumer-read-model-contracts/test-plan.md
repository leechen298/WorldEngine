# Test Plan

## Documentation Gate Checks

Run before implementation authorization:

```bash
git status --short --branch
git diff --check
python3 -c 'from pathlib import Path
pkg=Path("docs/iterations/v0.7/0.7.4-projection-consumer-read-model-contracts")
names=["README","intent","contract","technical-design","test-plan","plan","review"]
missing=[str(pkg/(name+suffix)) for name in names for suffix in (".md",".zh.md") if not (pkg/(name+suffix)).exists()]
print("missing_0_7_4_docs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
```

Expected results:

- Required `0.7.4` package docs and Chinese mirrors exist.
- Changed/untracked files stay inside cumulative v0.7 scope inherited from
  completed child packages and the current `0.7.4` docs.
- Implementation authorization remains closed until evaluator approval.

## Focused Implementation Tests

Run after implementation:

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_projection_read_model_contract.py
backend/.venv/bin/python tools/testing/validate_projection_read_model_contract.py docs/contracts/projection-read-model-schema.json
```

Expected results:

- Valid projection read-model contract passes.
- Missing required families fail for `runtime_summary`,
  `event_timeline_summary`, `agent_loop_summary`, `memory_context_summary`,
  `generation_readiness_summary`, `readiness_manifest_summary`, and
  `redacted_report_summary`.
- Non-read-only families fail.
- Write capability markers fail.
- Forbidden private-detail markers fail.
- CLI exits `0` for valid contract and `1` for invalid contract.

## Regression / Scope Checks

Run after implementation:

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_readiness_manifest.py
git diff --check
python3 -c 'import subprocess
allowed_prefixes=(
    "docs/iterations/v0.7/",
    "docs/contracts/external-validation-readiness-contract.md",
    "docs/contracts/projection-consumer-contract.md",
    "docs/contracts/v0.7-readiness-manifest-schema.json",
    "docs/contracts/v0.7-readiness-manifest.json",
    "docs/contracts/projection-read-model-contract.md",
    "docs/contracts/projection-read-model-schema.json",
    "docs/testing/external-validation-report-schema.json",
    "docs/validation-report-template.md",
    "tools/testing/validate_external_validation_report.py",
    "tools/testing/test_validate_external_validation_report.py",
    "tools/testing/validate_readiness_manifest.py",
    "tools/testing/test_validate_readiness_manifest.py",
    "tools/testing/validate_projection_read_model_contract.py",
    "tools/testing/test_validate_projection_read_model_contract.py",
)
tracked=subprocess.check_output(["git","diff","--name-only"], text=True).splitlines()
untracked=subprocess.check_output(["git","ls-files","--others","--exclude-standard"], text=True).splitlines()
files=tracked+untracked
bad=[p for p in files if not any(p.startswith(prefix) if prefix.endswith("/") else p == prefix for prefix in allowed_prefixes)]
print("changed_or_untracked=" + str(len(files)))
print("out_of_scope_changed_or_untracked=" + str(len(bad)))
print("\n".join(bad))
raise SystemExit(1 if bad else 0)'
```

## Commands Not Run

Backend runtime tests, frontend tests, API smoke, E2E, Agent smoke live run,
full autonomous runner, external validation suite, projection application
validation, and release checks are not required unless implementation touches
those surfaces.

## Blocker Recording Rule

If any documentation gate, focused test, scope guard, evaluator checkpoint, or
compatibility check fails, record the blocker in `review.md` before closeout.

## No Unverified Claims Rule

Do not infer projection app readiness, product readiness, external consumer
PASS, runtime/API/frontend PASS, or v0.8 readiness from schema/checker tests.
