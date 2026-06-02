# Test Plan

## Documentation Gate Checks

Implementation authorization 前运行：

```bash
git status --short --branch
git diff --check
python3 -c 'from pathlib import Path
pkg=Path("docs/iterations/v0.7/0.7.4-projection-consumer-read-model-contracts")
names=["README","intent","contract","technical-design","test-plan","plan","review"]
missing=[str(pkg/(name+suffix)) for name in names for suffix in (".md",".zh.md") if not (pkg/(name+suffix)).exists()]
print("missing_0_7_4_docs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
```

Expected results：

- Required `0.7.4` package docs 与中文镜像存在。
- Changed/untracked files 留在 cumulative v0.7 scope 内，包含 completed child packages
  和当前 `0.7.4` docs。
- Implementation authorization remains closed until evaluator approval。

## Focused Implementation Tests

Implementation 后运行：

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_projection_read_model_contract.py
backend/.venv/bin/python tools/testing/validate_projection_read_model_contract.py docs/contracts/projection-read-model-schema.json
```

Expected results：

- Valid projection read-model contract passes。
- Missing required families fail for `runtime_summary`、`event_timeline_summary`、
  `agent_loop_summary`、`memory_context_summary`、`generation_readiness_summary`、
  `readiness_manifest_summary` 和 `redacted_report_summary`。
- Non-read-only families fail。
- Write capability markers fail。
- Forbidden private-detail markers fail。
- V07-CR-04 regression case 会失败：即使字段以 `_summary` 结尾，只要字段名是
  `private_application_state_summary`，也必须被拒绝。
- Forbidden field terms 至少包含 `private`、`application_state`、`prompt`、
  `transcript`、raw memory internals 和 event payload leakage。
- Schema parse alone 不是 projection readiness。如果 schema shape 接受了违反这些语义规则的
  case，projection checker 必须拒绝它，或者 schema 必须先收紧后才能 closeout。
- CLI exits `0` for valid contract and `1` for invalid contract。

## Regression / Scope Checks

Implementation 后运行：

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_readiness_manifest.py
git diff --check
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

## Commands Not Run

Backend runtime tests、frontend tests、API smoke、E2E、Agent smoke live run、
full autonomous runner、external validation suite、projection application validation 和 release checks
不要求，除非 implementation touches those surfaces。

## Blocker Recording Rule

任何 documentation gate、focused test、scope guard、evaluator checkpoint 或 compatibility
check 失败，都必须在 closeout 前记录到 `review.md`。

## No Unverified Claims Rule

不要从 schema/checker tests 推断 projection app readiness、product readiness、external
consumer PASS、runtime/API/frontend PASS 或 v0.8 readiness。
