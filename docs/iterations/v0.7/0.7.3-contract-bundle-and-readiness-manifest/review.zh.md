# Review

Status: review complete
implementation_authorized: yes

## 变更文件

预期 package 文件：

- `docs/iterations/v0.7/0.7.3-contract-bundle-and-readiness-manifest/README.md`
- `docs/iterations/v0.7/0.7.3-contract-bundle-and-readiness-manifest/intent.md`
- `docs/iterations/v0.7/0.7.3-contract-bundle-and-readiness-manifest/contract.md`
- `docs/iterations/v0.7/0.7.3-contract-bundle-and-readiness-manifest/technical-design.md`
- `docs/iterations/v0.7/0.7.3-contract-bundle-and-readiness-manifest/test-plan.md`
- `docs/iterations/v0.7/0.7.3-contract-bundle-and-readiness-manifest/plan.md`
- `docs/iterations/v0.7/0.7.3-contract-bundle-and-readiness-manifest/review.md`
- 每个 package document 对应的中文镜像。

授权后预期实现文件：

- `docs/contracts/v0.7-readiness-manifest-schema.json`
- `docs/contracts/v0.7-readiness-manifest.json`
- `tools/testing/validate_readiness_manifest.py`
- `tools/testing/test_validate_readiness_manifest.py`

## 已运行命令

```bash
git diff --check
```

结果：通过，无输出。

```bash
python3 -c 'from pathlib import Path
pkg=Path("docs/iterations/v0.7/0.7.3-contract-bundle-and-readiness-manifest")
names=["README","intent","contract","technical-design","test-plan","plan","review"]
missing=[str(pkg/(name+suffix)) for name in names for suffix in (".md",".zh.md") if not (pkg/(name+suffix)).exists()]
print("missing_0_7_3_docs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
```

结果：

```text
missing_0_7_3_docs=0
```

```bash
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

结果：

```text
changed_or_untracked=74
out_of_scope_changed_or_untracked=0
```

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_readiness_manifest.py
```

结果：

```text
13 passed
```

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_external_validation_report.py
```

结果：

```text
21 passed
```

```bash
backend/.venv/bin/python tools/testing/validate_readiness_manifest.py docs/contracts/v0.7-readiness-manifest.json
```

结果：

```text
PASS: validated readiness manifest at docs/contracts/v0.7-readiness-manifest.json
```

```bash
backend/.venv/bin/python -m json.tool docs/contracts/v0.7-readiness-manifest-schema.json
backend/.venv/bin/python -m json.tool docs/contracts/v0.7-readiness-manifest.json
```

结果：通过。两个 JSON 文件均可正常解析。

```bash
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

结果：

```text
changed_or_untracked=78
out_of_scope_changed_or_untracked=0
```

```bash
python3 -c 'from pathlib import Path
bad=[]
for path in [Path("tools/testing/test_validate_readiness_manifest.py")]:
    text=path.read_text()
    for term in ["SENTINEL_PRIVATE_PATH"]:
        if term not in text:
            bad.append(f"missing synthetic marker coverage: {term}")
    for forbidden in ["/Users/", "data-testid", "xpath=", "http://localhost"]:
        if forbidden in text:
            bad.append(f"test contains forbidden concrete marker: {forbidden}")
print("manifest_synthetic_marker_guard_failures=" + str(len(bad)))
print("\n".join(bad))
raise SystemExit(1 if bad else 0)'
```

结果：

```text
manifest_synthetic_marker_guard_failures=0
```

## 测试结果

Documentation-gate checks 已通过：

- `git diff --check`：通过。
- Required `0.7.3` docs and mirrors：`missing_0_7_3_docs=0`。
- Documentation scope guard：`changed_or_untracked=74`，
  `out_of_scope_changed_or_untracked=0`。
- Focused readiness manifest checker tests：`13 passed`。
- Existing external validation report checker regression tests：`21 passed`。
- Readiness manifest CLI validation：通过。
- Manifest schema and manifest JSON parse：通过。
- Implementation scope guard：`changed_or_untracked=78`，
  `out_of_scope_changed_or_untracked=0`。
- Synthetic marker guard：`manifest_synthetic_marker_guard_failures=0`。

Backend runtime tests、frontend tests、API smoke、E2E、Agent smoke live run、
full autonomous runner、external validation suite、projection application validation
和 release checks 未运行；它们不在本 package 范围内，不能从 manifest checker tests 推断为已通过。

## Subagent / Evaluator Evidence

Documentation/contract evaluator：PASS_WITH_FINDINGS。

- P0/P1/P2：修复后无。
- P3：中文镜像仍保留部分英文状态、命令、字段名和 contract terms。因门禁语义已同步，接受为非阻断。
- 确认 required public surface paths、evidence status whitelist、PASS-like evidence
  rejection rule、blocker recording rule 和 implementation authorization gate 可 review。
- Verdict：本证据记录后可以开始实现。

Chinese mirror/scope evaluator：PASS_WITH_FINDINGS。

- P0/P1/P2：无。
- P3：parent status 起初仍写着 `0.7.3` docs 未创建。已在授权更新中修复；
  closeout 后 parent status now routes to `0.7.4`。
- 确认 mirror semantics、scope guard、format guard 和 overclaim guard。

Implementation-scope/code-review evaluator：PASS_WITH_FINDINGS。

- P0/P1：无。
- P2：implementation results 记录前，review evidence 已过期。已在本 review update 修复。
- 确认 implementation 留在 approved scope 内，required public paths 已包含，PASS-like
  evidence statuses 会被拒绝，private-detail markers 使用 synthetic markers，且没有
  runtime/API/frontend/`backend/worldengine` changes。

Validation-evidence / closeout evaluator：initial FAIL，已修复。

- P1/P2：implementation evidence、checklist、parent route 和 closeout status 尚未记录。
  已通过更新本 review、package README 和 parent v0.7 route/status surfaces 修复。
- P3：已明确 manifest tests 和 CLI validation 不代表 external suite PASS、product
  readiness、projection readiness、runtime/API/frontend PASS、live Agent smoke 或 full autonomous validation。

Final implementation-scope/code-review re-review：PASS。

- P0/P1/P2/P3：无。
- 确认 manifest required public paths 已包含，PASS-like evidence statuses 会被拒绝，
  scope guard 为 `changed_or_untracked=78` / `out_of_scope_changed_or_untracked=0`，
  且没有 runtime/API/frontend 或 `backend/worldengine` files changed。

Final validation-evidence / closeout re-review：PASS。

- P0/P1/P2/P3：无。
- 确认 child status 为 `review complete`，parent status route 到
  `0.7.4-package-docs-needed`，`0.7.4` implementation authorization closed，
  且没有把 manifest checker evidence 夸大成 external suite PASS、product readiness、
  projection readiness、runtime/API/frontend PASS、live Agent smoke 或 full autonomous validation。

## 兼容性评审

Implementation isolated to new manifest schema、manifest、checker 和 test files。
Runtime、API、frontend、persistence、migrations、generated results、external repositories
和 `backend/worldengine/` 都不在本包范围内。

## 范围评审

Changed/untracked set 留在 cumulative v0.7 scope 内。当前 `0.7.3` implementation 只触及
approved manifest schema/json/checker/test files。

## 未解决发现

- P1：无。
- P2：无。
- P3：无。中文镜像中保留的英文主要是 field names、commands 或 reviewed taxonomy values。

## 最终评估

`0.7.3-contract-bundle-and-readiness-manifest` 已 review complete。它实现了 approved
readiness manifest schema、manifest、checker 和 focused tests，并把 public contract
discovery semantics 交接给 `0.7.4-projection-consumer-read-model-contracts`。
