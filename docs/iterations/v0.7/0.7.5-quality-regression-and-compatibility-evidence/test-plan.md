# Test Plan

## Documentation Gate Checks

Run before evidence execution authorization:

```bash
git status --short --branch
git diff --check
python3 -c 'from pathlib import Path
pkg=Path("docs/iterations/v0.7/0.7.5-quality-regression-and-compatibility-evidence")
names=["README","intent","contract","technical-design","test-plan","plan","review"]
missing=[str(pkg/(name+suffix)) for name in names for suffix in (".md",".zh.md") if not (pkg/(name+suffix)).exists()]
print("missing_0_7_5_docs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
```

Expected results:

- Required `0.7.5` package docs and Chinese mirrors exist.
- Changed/untracked files stay inside cumulative v0.7 scope inherited from
  completed child packages and current `0.7.5` docs.
- Evidence execution remains closed until evaluator approval.

## In-Scope Evidence Commands

Run after evidence execution authorization:

```bash
backend/.venv/bin/python -m pytest tools/testing
backend/.venv/bin/python tools/testing/validate_readiness_manifest.py docs/contracts/v0.7-readiness-manifest.json
backend/.venv/bin/python tools/testing/validate_projection_read_model_contract.py docs/contracts/projection-read-model-schema.json
backend/.venv/bin/python -m json.tool docs/testing/external-validation-report-schema.json
backend/.venv/bin/python -m json.tool docs/contracts/v0.7-readiness-manifest-schema.json
backend/.venv/bin/python -m json.tool docs/contracts/v0.7-readiness-manifest.json
backend/.venv/bin/python -m json.tool docs/contracts/projection-read-model-schema.json
git diff --check
```

Run the changed-file scope guard from the regression section below.

## Regression / Scope Checks

```bash
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

## Commands Not Run Unless Scope Expands

Backend runtime tests, API smoke, frontend tests, frontend build, browser E2E,
live Agent smoke, full autonomous runner/full suite, external validation suite,
projection application validation, product-readiness checks, generation-quality
checks, and release checks are not required unless the reviewed package scope
is explicitly widened.

## Blocker Recording Rule

If any in-scope command fails, record the blocker in `review.md` and
`evidence-matrix.md` before closeout. Do not repair implementation code inside
this package.
