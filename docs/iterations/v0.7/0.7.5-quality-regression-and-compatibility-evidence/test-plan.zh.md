# Test Plan

## Documentation Gate Checks

Evidence execution authorization 前运行：

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

Expected results：

- Required `0.7.5` package docs 和中文镜像存在。
- Changed/untracked files 留在 cumulative v0.7 scope 内，包含 completed child packages 和当前
  `0.7.5` docs。
- Evidence execution remains closed until evaluator approval。

## In-Scope Evidence Commands

Evidence execution authorization 后运行：

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

再运行下方 regression section 中的 changed-file scope guard。

Expected results：

- `tools/testing` checker regression 退出 `0`。
- Readiness manifest CLI 对当前 manifest 退出 `0`。
- Projection read-model CLI 对当前 projection schema 退出 `0`。
- JSON parse commands 退出 `0`。
- `git diff --check` 退出 `0`。
- Changed-file scope guard 退出 `0`，且 `out_of_scope_changed_or_untracked=0`。
- 任何 pass claim 仅限这些 checker/schema/scope surfaces。

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

Backend runtime tests、API smoke、frontend tests、frontend build、browser E2E、live Agent
smoke、full autonomous runner/full suite、external validation suite、projection application validation、
product-readiness checks、generation-quality checks 和 release checks 不要求，除非 reviewed package
scope 明确扩展。

## Blocker Recording Rule

任何 in-scope command 失败，都必须在 closeout 前记录到 `review.md` 和
`evidence-matrix.md`。不得在本 package 内修复 implementation code。

## No Unverified Claims Rule

不要从 checker 或 JSON parse output 推断 runtime/API/frontend/E2E/live Agent/full autonomous/
external suite/projection application/product/generation/release readiness。必须在 `review.md` 和
`evidence-matrix.md` 中明确记录每个 not-run surface。
