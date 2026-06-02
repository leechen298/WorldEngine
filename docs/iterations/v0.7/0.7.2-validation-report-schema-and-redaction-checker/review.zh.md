# Review

Status: review complete
implementation_authorized: yes

## 变更文件

预期 package 文件：

- `docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/README.md`
- `docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/intent.md`
- `docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/contract.md`
- `docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/technical-design.md`
- `docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/test-plan.md`
- `docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/plan.md`
- `docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/review.md`
- 每个 package 文档对应的中文镜像。

授权后预期实现文件：

- `docs/testing/external-validation-report-schema.json`
- `docs/validation-report-template.md`
- `tools/testing/validate_external_validation_report.py`
- `tools/testing/test_validate_external_validation_report.py`

## 已运行命令

```bash
git status --short --branch
```

结果：通过。Changed/untracked 集合只包含 v0.7 campaign docs、两个继承自
`0.7.1` 的 public contract docs，以及新的 `0.7.2` package docs。

```bash
git diff --check
```

结果：通过，无输出。

```bash
python3 -c 'from pathlib import Path
pkg=Path("docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker")
names=["README","intent","contract","technical-design","test-plan","plan","review"]
missing=[str(pkg/(name+suffix)) for name in names for suffix in (".md",".zh.md") if not (pkg/(name+suffix)).exists()]
print("missing_0_7_2_docs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
```

结果：

```text
missing_0_7_2_docs=0
```

```bash
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

结果：

```text
changed_or_untracked=56
out_of_scope_changed_or_untracked=0
```

两个 `docs/contracts/` 文件是同一 campaign 工作树里继承的 `0.7.1` artifacts。
它们允许出现在 cumulative scope guard 中，但不是当前 `0.7.2` write targets。

```bash
python3 -c 'from pathlib import Path
files=list(Path("docs/iterations/v0.7").rglob("*.md"))+[Path("docs/contracts/external-validation-readiness-contract.md"),Path("docs/contracts/projection-consumer-contract.md")]
trailing=[]
tabs=[]
for path in files:
    for lineno,line in enumerate(path.read_text().splitlines(),1):
        if line.rstrip(" \t") != line:
            trailing.append(f"{path}:{lineno}")
        if "\t" in line:
            tabs.append(f"{path}:{lineno}")
print("checked_files=" + str(len(files)))
print("trailing_whitespace=" + str(len(trailing)))
print("tab_lines=" + str(len(tabs)))
print("\n".join(trailing+tabs))
raise SystemExit(1 if trailing or tabs else 0)'
```

结果：

```text
checked_files=56
trailing_whitespace=0
tab_lines=0
```

```bash
python3 -c 'from pathlib import Path
import re
bad=[]
for path in list(Path("docs/iterations/v0.7").rglob("*.md"))+[Path("docs/contracts/external-validation-readiness-contract.md"),Path("docs/contracts/projection-consumer-contract.md")]:
    lines=path.read_text().splitlines()
    for lineno,line in enumerate(lines,1):
        if re.match(r"^(implementation_authorized|Implementation authorization)[：:] yes$", line):
            bad.append(f"{path}:{lineno}: implementation authorization yes")
        for phrase in ["external validation suite passed.", "projection application readiness passed.", "product readiness passed."]:
            if line.strip() == phrase:
                prev="\n".join(lines[max(0,lineno-5):lineno])
                if "No current v0.7 evidence claims" not in prev:
                    bad.append(f"{path}:{lineno}: positive claim {phrase}")
print("claim_guard_failures=" + str(len(bad)))
print("\n".join(bad))
raise SystemExit(1 if bad else 0)'
```

记录 implementation authorization 之前的结果：

```text
claim_guard_failures=0
```

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_external_validation_report.py
```

结果：

```text
21 passed
```

```bash
backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_smoke_result.py tools/testing/test_validate_agent_autonomous_result.py
```

结果：

```text
34 passed
```

```bash
backend/.venv/bin/python -m json.tool docs/testing/external-validation-report-schema.json
```

结果：通过。Schema JSON 可以正常解析。

```bash
python3 -c 'from pathlib import Path
bad=[]
for path in [Path("tools/testing/test_validate_external_validation_report.py")]:
    text=path.read_text()
    for term in ["SENTINEL_PRIVATE_PATH", "SENTINEL_UI_SELECTOR", "SENTINEL_HIDDEN_RESET_API", "SENTINEL_ORACLE_INTERNAL", "SENTINEL_SEED_DATA", "SENTINEL_PRIVATE_TRANSCRIPT", "SENTINEL_EXTERNAL_EVENT_PAYLOAD"]:
        if term not in text:
            bad.append(f"missing synthetic marker coverage: {term}")
    for forbidden in ["/Users/", "data-testid", "xpath=", "http://localhost"]:
        if forbidden in text:
            bad.append(f"test contains forbidden concrete marker: {forbidden}")
print("synthetic_marker_guard_failures=" + str(len(bad)))
print("\n".join(bad))
raise SystemExit(1 if bad else 0)'
```

结果：

```text
synthetic_marker_guard_failures=0
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
changed_or_untracked=60
out_of_scope_changed_or_untracked=0
```

## 测试结果

Documentation-gate checks 已通过：

- `git diff --check`：通过。
- Required `0.7.2` docs and mirrors：`missing_0_7_2_docs=0`。
- Cumulative documentation scope guard：`changed_or_untracked=56`，
  `out_of_scope_changed_or_untracked=0`。
- Markdown formatting：`checked_files=56`，`trailing_whitespace=0`，
  `tab_lines=0`。
- Pre-authorization claim guard：`claim_guard_failures=0`。
- Focused external validation report checker tests：`21 passed`。
- Existing Agent smoke/autonomous saved-result checker regression tests：
  `34 passed`。
- Schema JSON parse：通过。
- Synthetic marker guard：`synthetic_marker_guard_failures=0`。
- Implementation scope guard：`changed_or_untracked=60`，
  `out_of_scope_changed_or_untracked=0`。

Backend runtime tests、frontend tests、API smoke、E2E、Agent smoke live run、
full autonomous runner、external validation suite、projection application validation
和 release checks 未运行；它们不在本 package 范围内，不能从 checker tests 推断为已通过。

## Subagent / Evaluator Evidence

Documentation/contract evaluator：PASS_WITH_FINDINGS。

- P0/P1：无。
- P2：中文镜像偏英文。已在授权前修复被点名的 `README.zh.md` 和
  `review.zh.md` 相关表述；保留的英文主要是 contract/status identifiers。
- P2：scope guard 允许累计工作树里的 `0.7.1` contract docs。已补充说明：
  这些文件是 inherited campaign artifacts，不是当前 `0.7.2` write targets。
- P3：leaked-detail tests 只能使用 synthetic sentinel strings，不能使用真实
  private paths、selectors、oracle internals、transcripts 或 consumer details。
  已接受并作为 implementation guardrail。
- Verdict：本证据记录后可以开始实现。

Chinese mirror/scope evaluator：PASS_WITH_FINDINGS。

- P0/P1/P2：无。
- P3：parent status surfaces 起初仍写着 `0.7.2` docs 未创建。已在授权更新中修复；
  closeout 后 parent status now routes to `0.7.3`。
- 确认英文/中文镜像保留 status、type、goal、allowed/forbidden scope、
  implementation authorization、review gates、test plan、stop conditions 和
  final assessment 语义。
- 确认没有 product、external validation suite 或 projection readiness PASS overclaim。

Implementation-scope/code-review evaluator：initial FAIL，已修复。

- P1：`pass` reports 曾接受 `status: deferred` 的 P1/P2 findings。已修复为
  pass reports 只把 `accepted` 和 `resolved` 视为非阻塞，并补充 deferred P1/P2
  focused regression test。
- P2：implementation results 记录前，review evidence 已过期。已在本 review update 修复。
- 修复后复跑证据：focused checker tests `21 passed`；existing saved-result checker
  tests `34 passed`；`git diff --check` 通过；schema JSON parse 通过；implementation
  scope guard 报告 `out_of_scope_changed_or_untracked=0`。

Validation-evidence / closeout evaluator：initial FAIL，已修复。

- P1/P2：implementation evidence、checklist、parent route 和 closeout status 尚未记录。
  已通过更新本 review、package README 和 parent v0.7 route/status surfaces 修复。
- P3：已明确 checker tests 不代表 external suite PASS、product readiness、
  projection readiness、runtime/API/frontend PASS、live Agent smoke 或 full autonomous validation。

Final implementation-scope/code-review re-review：PASS。

- P0/P1/P2/P3：无。
- 确认 deferred P1/P2 blocker 已修复。
- 确认 focused checker tests `21 passed`、existing saved-result checker tests
  `34 passed`、schema JSON parse 通过、`git diff --check` 通过、scope guard
  为 `changed_or_untracked=60` / `out_of_scope_changed_or_untracked=0`，
  synthetic marker guard 为 `synthetic_marker_guard_failures=0`。

Final validation-evidence / closeout re-review：PASS。

- P0/P1/P2/P3：无。
- 确认 child status 为 `review complete`，parent status route 到
  `0.7.3-package-docs-needed`，`0.7.3` implementation authorization closed，
  且没有把 focused checker evidence 夸大成 external suite PASS、product readiness、
  projection readiness、runtime/API/frontend PASS、live Agent smoke 或 full autonomous validation。

## 兼容性评审

计划中的实现只会落在新的 schema/checker/test 路径，以及一个增量模板更新。
Runtime、API、frontend、persistence、migrations、generated results、external
repositories 和 `backend/worldengine/` 都不在本包范围内。

Existing Agent smoke/autonomous saved-result schemas 和 checkers 必须保持兼容。
当前 session 已运行它们的 focused checker tests，并通过。

## 范围评审

Changed/untracked file set 留在累计 v0.7 campaign scope 内。
`docs/contracts/external-validation-readiness-contract.md` 和
`docs/contracts/projection-consumer-contract.md` 是继承的 `0.7.1` artifacts；
`0.7.2` 不得编辑它们。

## 未解决发现

- P1：无。
- P2：无。
- P3：无。Leaked-detail tests 使用 synthetic sentinel strings，没有引入真实
  private paths、UI selectors、external-world details、oracle internals、
  transcripts 或 event payloads。

## 最终评估

`0.7.2-validation-report-schema-and-redaction-checker` 已 review complete。它实现了
approved report schema、checker、focused tests 和 template alignment，并把
machine-checkable redacted report semantics 交接给
`0.7.3-contract-bundle-and-readiness-manifest`。
