# Test Plan

## Documentation Gate Checks

Run before implementation authorization:

```bash
git status --short --branch
git diff --check
python3 -c 'from pathlib import Path
pkg=Path("docs/iterations/v0.7/0.7.3-contract-bundle-and-readiness-manifest")
names=["README","intent","contract","technical-design","test-plan","plan","review"]
missing=[str(pkg/(name+suffix)) for name in names for suffix in (".md",".zh.md") if not (pkg/(name+suffix)).exists()]
print("missing_0_7_3_docs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
python3 -c 'import subprocess
allowed_prefixes=(
    "docs/iterations/v0.7/",
    "docs/contracts/external-validation-readiness-contract.md",
    "docs/contracts/projection-consumer-contract.md",
    "docs/testing/external-validation-report-schema.json",
    "docs/validation-report-template.md",
    "tools/testing/validate_external_validation_report.py",
    "tools/testing/test_validate_external_validation_report.py",
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

Expected results:

- Required `0.7.3` package docs and Chinese mirrors exist.
- Changed/untracked files stay inside cumulative v0.7 scope inherited from
  completed child packages and the current `0.7.3` docs.
- Implementation authorization remains closed until evaluator approval.

## Focused Implementation Tests

Run after implementation:

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_readiness_manifest.py
backend/.venv/bin/python tools/testing/validate_readiness_manifest.py docs/contracts/v0.7-readiness-manifest.json
```

Expected results:

- Valid manifest passes.
- Missing required fields fail.
- Required public contract/schema/template references are enforced.
- Unsupported claim values fail.
- Absolute paths and parent traversal fail.
- Forbidden synthetic private-detail markers fail.
- V07-CR-03 regression cases fail: `evidence_references[*].command` containing
  `python /Users/alice/private-suite/run.py` is rejected.
- Every manifest text surface rejects private/local path text, `data-testid`
  selectors, hidden reset/oracle/transcript/event payload references, and
  private runner details.
- Schema-valid but checker-invalid manifest examples are included. JSON Schema
  shape validation is not the semantic authority unless the schema is tightened
  to reject the same cases; otherwise the manifest checker is authoritative.
- CLI exits `0` for valid manifests and `1` for invalid manifests.

## Regression / Scope Checks

Run after implementation:

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_external_validation_report.py
git diff --check
python3 -c 'import subprocess
allowed_prefixes=(
    "docs/iterations/v0.7/",
    "docs/contracts/external-validation-readiness-contract.md",
    "docs/contracts/projection-consumer-contract.md",
    "docs/contracts/v0.7-readiness-manifest-schema.json",
    "docs/contracts/v0.7-readiness-manifest.json",
    "docs/testing/external-validation-report-schema.json",
    "docs/validation-report-template.md",
    "tools/testing/validate_external_validation_report.py",
    "tools/testing/test_validate_external_validation_report.py",
    "tools/testing/validate_readiness_manifest.py",
    "tools/testing/test_validate_readiness_manifest.py",
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

Expected results:

- Focused manifest tests pass.
- Existing external validation report checker tests pass.
- Changed/untracked files stay inside approved cumulative scope.
- `git diff --check` passes.

## Commands Not Run

Backend runtime tests, frontend tests, API smoke, E2E, Agent smoke live run,
full autonomous runner, external validation suite, projection application
validation, and release checks are not required unless implementation touches
those surfaces.

## Blocker Recording Rule

If any documentation gate, focused manifest test, adjacent report-checker
regression, scope guard, evaluator checkpoint, or compatibility check fails,
record the blocker in `review.md` before closeout.

## No Unverified Claims Rule

Do not infer external suite PASS, projection readiness, product readiness,
runtime/API/frontend PASS, or release readiness from manifest checker tests.
