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

运行完整的 cumulative v0.7 changed-file scope guard：

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

Expected results：

- `git diff --check` 退出 `0`。
- Required `0.7.7` package docs、release-candidate summary 和中文镜像存在。
- Release-candidate evidence references 指向 parent 与已完成 child package reviews。
- Changed-file scope guard 退出 `0`，且 `out_of_scope_changed_or_untracked=0`。
- Status guard matches 只能出现在 forbidden-scope 或 "not final" contexts。

## Status Guard

搜索 release-candidate package 中是否有 accidental final closeout claims：

```bash
rg -n "final / closeout complete|v0.7 final|final release" docs/iterations/v0.7/0.7.7-v0.7-release-candidate-bundle
```

Expected result：matches 只能出现在 forbidden-scope 或 "not final" contexts。

## Commands Not Run

本 documentation-only bundle 不运行 runtime/API/frontend/E2E/live Agent/full autonomous/external
suite/product/generation/release checks。

## Blocker Recording Rule

任何 documentation、evidence-link、status-guard、scope-guard 或 evaluator check 失败，都必须在
handoff to final closeout 前记录到 `review.md` 和 `release-candidate-summary.md`。存在 P1 或
unresolved P2 时，不得声明 review complete。

## No Unverified Claims Rule

不要声明 runtime/API/frontend/E2E/live Agent/full autonomous/external suite/product/generation/release
checks passed。本 release-candidate bundle 只总结由上述命令明确链接并检查的 evidence surfaces。
