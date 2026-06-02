# Test Plan

## Documentation Gate Checks

Run before implementation authorization:

```bash
git status --short --branch --untracked-files=all
git diff --check
python3 -c 'from pathlib import Path
pkg=Path("docs/iterations/v0.7/0.7.9-v07-cr-checker-schema-repair")
names=["README","intent","contract","technical-design","test-plan","plan","review"]
missing=[str(pkg/(name+suffix)) for name in names for suffix in (".md",".zh.md") if not (pkg/(name+suffix)).exists()]
print("missing_0_7_9_docs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
python3 -c 'import subprocess
allowed_prefixes=("docs/iterations/v0.7/0.7.9-v07-cr-checker-schema-repair/",)
untracked=subprocess.check_output(["git","ls-files","--others","--exclude-standard"], text=True).splitlines()
bad=[p for p in untracked if p.startswith("docs/iterations/v0.7/") and not p.startswith(allowed_prefixes)]
print("unexpected_untracked_v0_7_docs=" + str(len(bad)))
print("\n".join(bad))
raise SystemExit(1 if bad else 0)'
```

Expected results:

- Required `0.7.9` package docs and Chinese mirrors exist.
- Existing untracked `docs/iterations/v0.8/**` is excluded from this package
  and not treated as a v0.7 repair artifact.
- Implementation authorization remains closed until evaluator approval.

## Red Tests Before Repair

Add focused regression tests, then run the relevant tests before changing
checker implementation:

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_external_validation_report.py -q
backend/.venv/bin/python -m pytest tools/testing/test_validate_readiness_manifest.py -q
backend/.venv/bin/python -m pytest tools/testing/test_validate_projection_read_model_contract.py -q
```

Expected red failures before repair:

- accepted P1/P2 pass reports are incorrectly accepted.
- `data-testid` and local `/Users/...` report text is incorrectly accepted.
- private manifest command/text is incorrectly accepted.
- `private_application_state_summary` is incorrectly accepted.
- schema-valid/checker-invalid authority cases are missing or fail.

## Focused Repair Tests

After repair, run:

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_external_validation_report.py -q
backend/.venv/bin/python -m pytest tools/testing/test_validate_readiness_manifest.py -q
backend/.venv/bin/python -m pytest tools/testing/test_validate_projection_read_model_contract.py -q
backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_smoke_result.py tools/testing/test_validate_agent_autonomous_result.py -q
backend/.venv/bin/python -m pytest tools/testing -q
backend/.venv/bin/python tools/testing/validate_readiness_manifest.py docs/contracts/v0.7-readiness-manifest.json
backend/.venv/bin/python tools/testing/validate_projection_read_model_contract.py docs/contracts/projection-read-model-schema.json
backend/.venv/bin/python -m json.tool docs/testing/external-validation-report-schema.json
backend/.venv/bin/python -m json.tool docs/contracts/v0.7-readiness-manifest-schema.json
backend/.venv/bin/python -m json.tool docs/contracts/v0.7-readiness-manifest.json
backend/.venv/bin/python -m json.tool docs/contracts/projection-read-model-schema.json
make validate-agent-autonomous-fixtures
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/20260531T122230+0800
```

Expected results:

- All focused checker tests pass.
- `tools/testing` passes.
- Valid readiness manifest and projection read model still pass.
- JSON files parse.
- Agent autonomous saved-result checker fixtures and existing saved result
  still pass.

## Final Validation Checks

Run after implementation and result update:

```bash
git diff --check
python3 -c 'from pathlib import Path
paths=[
"docs/testing/results/2026-06-02-v0.7-overall-validation.md",
"docs/testing/results/2026-06-02-v0.7-overall-validation.zh.md",
"docs/testing/results/2026-06-02-v0.7-agent-autonomous-saved-result-validation.md",
"docs/testing/results/2026-06-02-v0.7-agent-autonomous-saved-result-validation.zh.md",
]
missing=[p for p in paths if not Path(p).exists()]
print("checked_validation_refs=" + str(len(paths)))
print("missing_validation_refs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
python3 -c 'import subprocess
out=subprocess.check_output(["git","status","--porcelain","--untracked-files=all"], text=True)
files=[line[3:] for line in out.splitlines() if line]
scoped_prefixes=("docs/iterations/v0.7/0.7.9-v07-cr-checker-schema-repair/",)
scoped_exact={
    "docs/contracts/projection-read-model-contract.md",
    "docs/contracts/v0.7-readiness-manifest-schema.json",
    "docs/iterations/v0.7/CAMPAIGN_PLAN.md",
    "docs/iterations/v0.7/CAMPAIGN_PLAN.zh.md",
    "docs/iterations/v0.7/CURRENT_STATE.md",
    "docs/iterations/v0.7/CURRENT_STATE.zh.md",
    "docs/iterations/v0.7/GOAL_RUNNER.md",
    "docs/iterations/v0.7/GOAL_RUNNER.zh.md",
    "docs/iterations/v0.7/README.md",
    "docs/iterations/v0.7/README.zh.md",
    "docs/iterations/v0.7/review.md",
    "docs/iterations/v0.7/review.zh.md",
    "docs/iterations/v0.7/v0.7-plan.md",
    "docs/iterations/v0.7/v0.7-plan.zh.md",
    "docs/testing/external-validation-report-schema.json",
    "docs/testing/results/2026-06-02-v0.7-overall-validation.md",
    "docs/testing/results/2026-06-02-v0.7-overall-validation.zh.md",
    "docs/validation-report-template.md",
    "tools/testing/test_validate_external_validation_report.py",
    "tools/testing/test_validate_projection_read_model_contract.py",
    "tools/testing/test_validate_readiness_manifest.py",
    "tools/testing/validate_external_validation_report.py",
    "tools/testing/validate_projection_read_model_contract.py",
    "tools/testing/validate_readiness_manifest.py",
}
known_unrelated_prefixes=("docs/iterations/v0.8/",)
known_unrelated_exact={"docs/roadmap.md","docs/scope-boundaries.md"}
known_unrelated_license_metadata={
    "LICENSE",
    "NOTICE",
    "README.md",
    "README.zh.md",
    "backend/pyproject.toml",
    "frontend/package.json",
}
scoped=[p for p in files if p in scoped_exact or any(p.startswith(prefix) for prefix in scoped_prefixes)]
known_unrelated_v0_8=[p for p in files if any(p.startswith(prefix) for prefix in known_unrelated_prefixes)]
known_unrelated_boundary_docs=[p for p in files if p in known_unrelated_exact]
known_unrelated_license=[p for p in files if p in known_unrelated_license_metadata]
known_reported=set(scoped + known_unrelated_v0_8 + known_unrelated_boundary_docs + known_unrelated_license)
bad=[p for p in files if p not in known_reported]
print("changed_or_untracked_files=" + str(len(files)))
print("scoped_repair=" + str(len(scoped)))
print("known_unrelated_untracked_v0_8=" + str(len(known_unrelated_v0_8)))
print("known_unrelated_tracked_boundary_docs=" + str(len(known_unrelated_boundary_docs)))
print("known_unrelated_license_metadata=" + str(len(known_unrelated_license)))
print("out_of_scope_changed_or_untracked=" + str(len(bad)))
print("\n".join(bad))
raise SystemExit(1 if bad else 0)'
```

Expected results:

- No whitespace errors.
- Result docs and autonomous detail records exist.
- Scope guard shows no out-of-scope v0.7 repair changes. Current scoped repair
  files, including parent status surfaces and Campaign Plan sync, are reported
  as `scoped_repair`; any unrelated v0.8 or roadmap/scope-boundary files are
  reported separately when present. Unrelated license metadata files are also
  reported separately when present and must not be included in a v0.7 repair
  commit.

## Commands Not Run

Backend runtime tests, API smoke, frontend tests/build, E2E, live Agent smoke,
full autonomous runner/full suite, external validation suite, projection
application validation, and v0.8 checks are not required unless implementation
touches those surfaces.

## Blocker Recording Rule

Any failed command, evaluator P1/P2, or remaining V07-CR issue must be recorded
in `review.md` and the overall validation result before closeout.

## No Unverified Claims Rule

Do not claim clean pass until current-session evidence proves all in-scope
commands pass, V07-CR P1/P2 blockers are repaired, and result docs preserve
explicit non-claims for external suite, projection readiness, product
readiness, live Agent smoke, full autonomous runner, runtime/API/frontend/E2E,
and v0.8 readiness.
