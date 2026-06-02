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
 "docs/testing/results/2026-06-02-v0.7-code-review.md",
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

## V07-CR Blocker Gate

任何 final closeout 或 clean PASS  statement 前，必须读取 post-closeout code-review result：

```bash
rg -n "Status: review complete with blocking findings|### P1|### P2|V07-CR-0[1-5]" docs/testing/results/2026-06-02-v0.7-code-review.md
```

预期 gate result：

- 如果 code-review file 仍记录 blocking findings，则 final closeout 与 clean PASS 都被阻塞，
  直到 repair package 记录当前 session evidence，证明 V07-CR-01 到 V07-CR-05 已修复，
  或被 reviewer-approved rationale 明确降级。
- Clean PASS 前必须运行 L1 blocker regression：accepted/deferred P1/P2 report cases、
  private report markers、private manifest command/text、`private_application_state_summary`
  和 schema-valid/checker-invalid authority cases 必须全部由 focused checker tests 覆盖，
  或记录为 unresolved blockers。
- JSON parse、manifest CLI PASS、projection CLI PASS 或 `tools/testing` PASS 不能覆盖仍未解决的
  V07-CR P1/P2 findings。

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

- `tools/testing` 退出 `0`。
- Manifest 和 projection CLI checks 退出 `0`。
- JSON parse commands 退出 `0`。
- `git diff --check` 退出 `0`。
- Required `0.7.8` package docs、final-closeout record 和中文镜像存在。
- Final evidence references 指向 parent、已完成 child package reviews 和 post-closeout V07-CR
  code-review result。
- V07-CR blocker gate 已分类。如果 blockers 仍未解决，或缺少 L1 blocker regression evidence，
  final closeout 仍保持 blocked。
- Changed-file scope guard 退出 `0`，且 `out_of_scope_changed_or_untracked=0`。

## Commands Not Run

本 closeout 不运行 external validation suite、projection application validation、product-readiness checks、
runtime/API/frontend/E2E/live Agent/full autonomous/generation-quality checks 或 v0.8 checks。

## Blocker Recording Rule

任何 final verification command、docs completeness check、evidence-reference check、V07-CR
blocker gate、scope guard 或 evaluator checkpoint 失败，都必须在 parent status updates 前记录到
`review.md` 和 `final-closeout.md`。存在 P1、unresolved P2 或未执行的 L1 blocker regression 时，
不得标记 final closeout complete。

## No Unverified Claims Rule

不要声明 external validation suite PASS、projection application readiness、product readiness、
runtime/API/frontend/E2E/live Agent/full autonomous/generation-quality PASS 或 v0.8 readiness，除非
current-session evidence 明确覆盖该 surface。Checker/schema PASS 只支持对应 checker/schema surface。
