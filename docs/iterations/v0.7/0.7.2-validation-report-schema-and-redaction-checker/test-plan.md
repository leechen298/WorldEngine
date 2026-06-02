# Test Plan

## Documentation Gate Checks

Run before implementation authorization:

```bash
git status --short --branch
git diff --check
python3 -c 'from pathlib import Path
pkg=Path("docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker")
names=["README","intent","contract","technical-design","test-plan","plan","review"]
missing=[str(pkg/(name+suffix)) for name in names for suffix in (".md",".zh.md") if not (pkg/(name+suffix)).exists()]
print("missing_0_7_2_docs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
python3 -c 'import subprocess
allowed_prefixes=("docs/iterations/v0.7/","docs/contracts/external-validation-readiness-contract.md","docs/contracts/projection-consumer-contract.md")
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

- Required `0.7.2` package docs and Chinese mirrors exist.
- Changed/untracked files stay inside the cumulative documentation-gate
  scope. The two `docs/contracts/` files are inherited `0.7.1` artifacts in
  the same campaign worktree; `0.7.2` must not edit them.
- Implementation authorization remains closed until evaluator approval.

## Focused Implementation Tests

Run after implementation:

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_external_validation_report.py
python3 tools/testing/validate_external_validation_report.py <valid-report-json>
python3 tools/testing/validate_external_validation_report.py <invalid-report-json>
```

Expected results:

- Valid redacted `pass` report returns no validation errors.
- Missing required fields fail.
- Unsupported status fails.
- `pass` requires `redaction_confirmed: true`.
- `pass` rejects unresolved P1/P2 findings.
- `blocked`, `skipped`, and `out_of_scope` require explicit reasons and are
  not treated as pass.
- Forbidden detail review flags set to true fail.
- Generic leaked-detail markers fail.
- CLI exits `0` for valid reports and `1` for invalid reports.

## Regression / Scope Checks

Run after implementation:

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_smoke_result.py tools/testing/test_validate_agent_autonomous_result.py
git diff --check
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

- Focused checker tests pass.
- Existing Agent smoke/autonomous checker tests pass if shared testing
  expectations could be affected.
- Changed/untracked files stay inside the approved cumulative scope. The two
  `docs/contracts/` files remain inherited `0.7.1` artifacts and are not
  active `0.7.2` write targets.
- `git diff --check` passes.

## Commands Not Run

Backend runtime tests, frontend tests, API smoke, E2E, Agent smoke live run,
full autonomous runner, external validation suite, projection application
validation, and release checks are not required for this package unless a
later review finds the implementation touched those surfaces.

## Blocker Recording Rule

If any required focused test, scope guard, evaluator checkpoint, or
compatibility check fails, record the blocker in `review.md` before closeout.

## No Unverified Claims Rule

Only commands run in the current session may be recorded as passed. Do not
infer external validation readiness, projection readiness, product readiness,
or runtime/API/frontend PASS from schema/checker tests.
