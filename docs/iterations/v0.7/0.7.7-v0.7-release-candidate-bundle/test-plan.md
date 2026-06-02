# Test Plan

## Documentation And Evidence Link Checks

```bash
git diff --check
python3 -c 'from pathlib import Path
pkg=Path("docs/iterations/v0.7/0.7.7-v0.7-release-candidate-bundle")
names=["README","intent","contract","technical-design","test-plan","plan","review","release-candidate-summary"]
missing=[str(pkg/(name+suffix)) for name in names for suffix in (".md",".zh.md") if not (pkg/(name+suffix)).exists()]
print("missing_0_7_7_docs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
python3 -c 'from pathlib import Path
paths=[
 "docs/iterations/v0.7/review.md",
 "docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline/review.md",
 "docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/review.md",
 "docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/review.md",
 "docs/iterations/v0.7/0.7.3-contract-bundle-and-readiness-manifest/review.md",
 "docs/iterations/v0.7/0.7.4-projection-consumer-read-model-contracts/review.md",
 "docs/iterations/v0.7/0.7.5-quality-regression-and-compatibility-evidence/review.md",
 "docs/iterations/v0.7/0.7.5-quality-regression-and-compatibility-evidence/evidence-matrix.md",
 "docs/iterations/v0.7/0.7.6-v0.7-evidence-and-compatibility-audit/review.md",
 "docs/iterations/v0.7/0.7.6-v0.7-evidence-and-compatibility-audit/audit-report.md",
]
missing=[p for p in paths if not Path(p).exists()]
print("missing_v0_7_rc_refs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
```

## Changed-File Scope Guard

Run the full cumulative v0.7 changed-file scope guard:

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

Expected results:

- `git diff --check` exits `0`.
- Required `0.7.7` package docs, release-candidate summary, and Chinese mirrors
  exist.
- Release-candidate evidence references back to parent and completed child
  package reviews exist.
- Changed-file scope guard exits `0` with `out_of_scope_changed_or_untracked=0`.
- Status guard matches appear only in forbidden-scope or "not final" contexts.

## Status Guard

Search the release-candidate package for accidental final closeout claims:

```bash
rg -n "final / closeout complete|v0.7 final|final release" docs/iterations/v0.7/0.7.7-v0.7-release-candidate-bundle
```

Expected result: matches may appear only in forbidden-scope or "not final"
contexts.

## Commands Not Run

No runtime/API/frontend/E2E/live Agent/full autonomous/external suite/product/
generation/release checks are run by this documentation-only bundle.

## Blocker Recording Rule

If any documentation, evidence-link, status-guard, scope-guard, or evaluator
check fails, record it in `review.md` and `release-candidate-summary.md` before
handoff to final closeout. Do not claim review complete while a P1 or
unresolved P2 remains.

## No Unverified Claims Rule

Do not claim runtime/API/frontend/E2E/live Agent/full autonomous/external
suite/product/generation/release checks passed. This release-candidate bundle
only summarizes evidence surfaces that are explicitly linked and checked by
the commands above.
