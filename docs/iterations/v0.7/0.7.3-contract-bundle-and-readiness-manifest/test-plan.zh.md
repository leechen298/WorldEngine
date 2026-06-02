# Test Plan

## Documentation Gate Checks

Implementation authorization 前运行：

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

Expected results：

- Required `0.7.3` package docs 与中文镜像存在。
- Changed/untracked files 留在 cumulative v0.7 scope 内，包含 completed child packages
  和当前 `0.7.3` docs。
- Implementation authorization remains closed until evaluator approval。

## Focused Implementation Tests

Implementation 后运行：

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_readiness_manifest.py
backend/.venv/bin/python tools/testing/validate_readiness_manifest.py docs/contracts/v0.7-readiness-manifest.json
```

Expected results：

- Valid manifest passes。
- Missing required fields fail。
- Required public contract/schema/template references 会被强制校验。
- Unsupported claim values fail。
- Absolute paths 和 parent traversal 会失败。
- Forbidden synthetic private-detail markers 会失败。
- CLI 对 valid manifests 返回 `0`，对 invalid manifests 返回 `1`。

## Regression / Scope Checks

Implementation 后运行：

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

Expected results：

- Focused manifest tests 通过。
- Existing external validation report checker tests 通过。
- Changed/untracked files 留在 approved cumulative scope 内。
- `git diff --check` 通过。

## Commands Not Run

Backend runtime tests、frontend tests、API smoke、E2E、Agent smoke live run、
full autonomous runner、external validation suite、projection application validation
和 release checks 不要求，除非 implementation 触及这些 surfaces。

## Blocker Recording Rule

任何 documentation gate、focused manifest test、adjacent report-checker regression、
scope guard、evaluator checkpoint 或 compatibility check 失败，都必须在 closeout 前记录到
`review.md`。

## No Unverified Claims Rule

不要从 manifest checker tests 推断 external suite PASS、projection readiness、product
readiness、runtime/API/frontend PASS 或 release readiness。
