# Test Plan

## Documentation Gate Checks

Implementation authorization 前运行：

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

预期结果：

- Required `0.7.2` package docs 与中文镜像存在。
- Changed/untracked files 留在累计 documentation-gate scope 内。其中两个
  `docs/contracts/` 文件是同一 campaign 工作树里继承的 `0.7.1` artifacts；
  `0.7.2` 不得编辑它们。
- Implementation authorization 在 evaluator approval 前保持关闭。

## Focused Implementation Tests

Implementation 后运行：

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_external_validation_report.py
python3 tools/testing/validate_external_validation_report.py <valid-report-json>
python3 tools/testing/validate_external_validation_report.py <invalid-report-json>
```

预期结果：

- Valid redacted `pass` report 不产生 validation errors。
- Missing required fields 会失败。
- Unsupported status 会失败。
- `pass` 要求 `redaction_confirmed: true`。
- `pass` 会拒绝 unresolved P1/P2 findings。
- `blocked`、`skipped`、`out_of_scope` 必须包含 explicit reasons，且不能被当作
  pass。
- Forbidden detail review flags 设为 true 时会失败。
- Generic leaked-detail markers 会失败。
- V07-CR-01 regression cases 会失败：`status=pass` 且 P1 或 P2 findings 的
  finding status 为 `accepted`、`deferred` 或其他未 closed 状态。
- V07-CR-02 regression cases 会失败：真实 private paths，如
  `/Users/alice/private-suite/run.py`、`file://` local paths、
  `data-testid=submit-button`、CSS selector details、hidden reset hooks、
  private oracles、transcripts、seed data 和 event payload markers。
- 必须包含 schema-valid 但 checker-invalid 的 accepted P1/P2 和 redaction leak examples。
  JSON Schema 形状校验不是 semantic PASS 来源；report checker 是这些 cases 的语义权威。
- CLI 对 valid reports 返回 `0`，对 invalid reports 返回 `1`。

## Regression / Scope Checks

Implementation 后运行：

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

预期结果：

- Focused checker tests 通过。
- 如果 shared testing expectations 可能受影响，existing Agent smoke/autonomous
  checker tests 通过。
- Changed/untracked files 留在 approved cumulative scope 内。两个 `docs/contracts/`
  文件仍是继承的 `0.7.1` artifacts，不是当前 `0.7.2` write targets。
- `git diff --check` 通过。

## Commands Not Run

Backend runtime tests、frontend tests、API smoke、E2E、Agent smoke live run、
full autonomous runner、external validation suite、projection application validation
和 release checks 对本 package 不要求，除非后续 review 发现 implementation touched those surfaces。

## Blocker Recording Rule

任何 required focused test、scope guard、evaluator checkpoint 或 compatibility check
失败，都必须在 closeout 前记录到 `review.md`。

## No Unverified Claims Rule

只有当前 session 实际运行的 commands 可以记录为 passed。不要从 schema/checker tests
推断 external validation readiness、projection readiness、product readiness 或
runtime/API/frontend PASS。
