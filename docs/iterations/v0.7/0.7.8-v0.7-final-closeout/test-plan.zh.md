# Test Plan

## Final Verification Commands

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

运行 docs/evidence link checks：

```bash
python3 -c 'from pathlib import Path
pkg=Path("docs/iterations/v0.7/0.7.8-v0.7-final-closeout")
names=["README","intent","contract","technical-design","test-plan","plan","review","final-closeout"]
missing=[str(pkg/(name+suffix)) for name in names for suffix in (".md",".zh.md") if not (pkg/(name+suffix)).exists()]
print("missing_0_7_8_docs=" + str(len(missing)))
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
 "docs/iterations/v0.7/0.7.7-v0.7-release-candidate-bundle/review.md",
 "docs/iterations/v0.7/0.7.7-v0.7-release-candidate-bundle/release-candidate-summary.md",
]
missing=[p for p in paths if not Path(p).exists()]
print("missing_v0_7_final_refs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
```

运行 `0.7.5` 使用的 changed-file scope guard。

## Commands Not Run

本 closeout 不运行 external validation suite、projection application validation、product-readiness checks、
runtime/API/frontend/E2E/live Agent/full autonomous/generation-quality checks 或 v0.8 checks。
