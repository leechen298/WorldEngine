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

运行 `0.7.5` 使用的 changed-file scope guard。

## Status Guard

搜索 release-candidate package 中是否有 accidental final closeout claims：

```bash
rg -n "final / closeout complete|v0.7 final|final release" docs/iterations/v0.7/0.7.7-v0.7-release-candidate-bundle
```

Expected result：matches 只能出现在 forbidden-scope 或 "not final" contexts。

## Commands Not Run

本 documentation-only bundle 不运行 runtime/API/frontend/E2E/live Agent/full autonomous/external
suite/product/generation/release checks。
