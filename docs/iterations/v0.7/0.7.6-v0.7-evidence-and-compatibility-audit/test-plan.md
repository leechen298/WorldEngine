# Test Plan

## Documentation And Traceability Checks

```bash
git diff --check
python3 -c 'from pathlib import Path
pkg=Path("docs/iterations/v0.7/0.7.6-v0.7-evidence-and-compatibility-audit")
names=["README","intent","contract","technical-design","test-plan","plan","review","audit-report"]
missing=[str(pkg/(name+suffix)) for name in names for suffix in (".md",".zh.md") if not (pkg/(name+suffix)).exists()]
print("missing_0_7_6_docs=" + str(len(missing)))
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
]
missing=[p for p in paths if not Path(p).exists()]
print("missing_v0_7_evidence_refs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
```

Run the changed-file scope guard used by `0.7.5`.

## Commands Not Run

No runtime/API/frontend/E2E/live Agent/full autonomous/external suite/product/
generation/release checks are run by this documentation-only audit.

## Expected Result

All documentation, traceability, formatting, and scope checks pass, or the
audit records blockers before closeout.
