# Review 评审

状态：final / closeout complete；已记录 post-closeout code-review blockers

parent_implementation_authorized：no
active_child_package：无
active_child_implementation_authorized：no
active_child_evidence_execution_authorized：final verification 后已关闭

## Post-Closeout Code Review Status

`docs/testing/results/2026-06-02-v0.7-code-review.md` 记录在历史 `0.7.8` closeout
之后，并报告 3 个 P1、2 个 P2、1 个 P3。本 parent review 仍是历史 route/closeout
evidence，但不得用作 v0.7 clean pass、product PASS、external suite PASS、
projection readiness PASS，或 v0.7 已无 blocker 的证明。

已知 post-closeout code-review blockers 需要先通过窄范围 v0.7 repair package 处理，然后再尝试新的
clean-pass validation；除非 validation result 明确把它们记录为 blockers。

## Parent Review Completion

v0.7 parent documentation review 已完成，可用于 route selection。两个 current-session read-only
subagents 复核 parent package，未发现 P0/P1/P2/P3 blocker：

- Parent campaign evaluator：PASS。Evaluator 确认 parent route/status 一致、implementation
  authorization 关闭、child packages 仍只是 roadmap specs，并且选择 `0.7.0` 前没有 required fixes。
- Chinese mirror and file-scope evaluator：PASS。Evaluator 确认 mirror semantics、选择前没有 child
  package files、没有 pass/final overclaims，并且 parent review completion 没有 mirror blocker。

该 review completion 只授权选择并起草 documentation-only
`0.7.0-v0.7-planning-and-external-validation-boundary-baseline` child package。
它不授权 runtime、schema、API、frontend、backend test、checker、fixture、migration、external
repository、generated result 或 `backend/worldengine/` implementation changes。

## Parent-Only Scope Correction Before Child Selection

本 review 记录 `0.7.0` 被选择之前 parent-only review pass 中修正后的 v0.7 文档范围：

- 在 parent-only review 时，v0.7 的权威产物只有 version-level package。
- 在 parent-only review 时，planned child packages 只作为 `v0.7-plan.md` 中的路线图规格存在。
- Campaign 后续已完成 `0.7.0` 到 `0.7.8`。
- Final closeout 后没有 active v0.7 child package。
- Closeout 后的新工作必须创建新的 reviewed package，或从下一版本自己的 reviewed
  iteration package 开始。

## Changed Files 变更文件

Version-level v0.7 documentation files：

- `docs/iterations/v0.7/README.md`
- `docs/iterations/v0.7/README.zh.md`
- `docs/iterations/v0.7/v0.7-plan.md`
- `docs/iterations/v0.7/v0.7-plan.zh.md`
- `docs/iterations/v0.7/GOAL_RUNNER.md`
- `docs/iterations/v0.7/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.7/CURRENT_STATE.md`
- `docs/iterations/v0.7/CURRENT_STATE.zh.md`
- `docs/iterations/v0.7/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.7/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.7/review.md`
- `docs/iterations/v0.7/review.zh.md`

Removed from scope：

- earlier parent-only drafting pass 中提前创建的 `0.7.0` child package files 与空目录。当前
  `0.7.0` child package 是 parent review 完成后重新创建的。
- 提前创建的 `0.7.1` child package files 与空目录。

本次 drafting 不授权 runtime、schema、API、frontend、backend test、checker implementation、fixture、
migration、external repository、generated result 或 `backend/worldengine/` implementation files。

## Commands Run 已运行命令

本 section 中的 command evidence 属于 `0.7.0` 被选择前的 parent-only review pass。当前 `0.7.0`
child evidence 记录在 child package review 中。

```bash
git status --short --branch
```

结果：

```text
## v0.7-local
?? docs/iterations/v0.7/
```

```bash
git diff --check
```

结果：无输出，通过。

```bash
rmdir docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts
```

结果：无输出，通过。该命令删除了两个提前创建但已经为空的 child package directories。

```bash
python3 -c 'import subprocess
files=subprocess.check_output(["git","ls-files","--others","--exclude-standard","docs/iterations/v0.7"], text=True).splitlines()
print("untracked_files=" + str(len(files)))
raise SystemExit(1 if len(files) != 12 else 0)'
```

结果：

```text
untracked_files=12
```

```bash
find docs/iterations/v0.7 -mindepth 1 -maxdepth 2 -type d -print | sort
```

结果：无输出，通过。当前没有 child package directories。

```bash
find docs/iterations/v0.7 -mindepth 2 -type f | sort
```

结果：无输出，通过。当前没有 child package files。

```bash
python3 -c 'from pathlib import Path
parent=Path("docs/iterations/v0.7")
parent_docs=["README","v0.7-plan","GOAL_RUNNER","CURRENT_STATE","CAMPAIGN_PLAN","review"]
missing=[str(parent/(name+suffix)) for name in parent_docs for suffix in (".md",".zh.md") if not (parent/(name+suffix)).exists()]
print("missing=" + str(len(missing)))
raise SystemExit(1 if missing else 0)'
```

结果：

```text
missing=0
```

```bash
python3 -c 'from pathlib import Path
files=sorted(Path("docs/iterations/v0.7").rglob("*.md"))
trailing=[]
tabs=[]
child=[]
for path in files:
    if path.parent != Path("docs/iterations/v0.7"):
        child.append(str(path))
    for lineno,line in enumerate(path.read_text().splitlines(), 1):
        if line.rstrip(" \t") != line:
            trailing.append(f"{path}:{lineno}")
        if "\t" in line:
            tabs.append(f"{path}:{lineno}")
print("markdown_files=" + str(len(files)))
print("child_dir_files=" + str(len(child)))
print("trailing_whitespace=" + str(len(trailing)))
print("tab_lines=" + str(len(tabs)))
raise SystemExit(1 if trailing or tabs or child or len(files)!=12 else 0)'
```

结果：

```text
markdown_files=12
child_dir_files=0
trailing_whitespace=0
tab_lines=0
```

```bash
python3 -c 'from pathlib import Path
import re
required=["Package name:","Status:","Type:","Goal:","Why this exists:","Inputs / required reading:","Allowed changes:","Forbidden changes:","Expected deliverables:","Expected tests / verification:","Compatibility constraints:","Scope guardrails:","Exit criteria:","Handoff to next package:"]
lines=Path("docs/iterations/v0.7/v0.7-plan.md").read_text().splitlines()
heads=[(i,l) for i,l in enumerate(lines) if re.match(r"^### 0\.7\.[0-9]+ ", l)]
bad=[]
for idx,(start,head) in enumerate(heads):
    end=heads[idx+1][0] if idx+1 < len(heads) else len(lines)
    section="\n".join(lines[start:end])
    missing=[f for f in required if f not in section]
    if missing:
        bad.append((head, missing))
print("planned_package_count=" + str(len(heads)))
print("planned_package_missing_fields=" + str(len(bad)))
raise SystemExit(1 if bad or len(heads) != 9 else 0)'
```

结果：

```text
planned_package_count=9
planned_package_missing_fields=0
```

```bash
python3 -c 'import subprocess
allowed_prefixes=("docs/iterations/v0.7/",)
lines=subprocess.check_output(["git","status","--short"], text=True).splitlines()
bad=[]
for line in lines:
    if not line:
        continue
    path=line[3:]
    if path.startswith(allowed_prefixes):
        continue
    bad.append(line)
print("unexpected_status=" + str(len(bad)))
raise SystemExit(1 if bad else 0)'
```

结果：

```text
unexpected_status=0
```

```bash
python3 -c 'import subprocess
pattern=r"^Status: (review complete|final / closeout complete)|^状态：(review complete|final / closeout complete)|^implementation_authorized: yes|^Implementation authorization: yes"
proc=subprocess.run(["rg","-n",pattern,"docs/iterations/v0.7"], text=True, capture_output=True)
if proc.returncode == 1:
    print("unexpected_status_or_auth=0")
    raise SystemExit(0)
print("unexpected_status_or_auth=1")
print(proc.stdout, end="")
raise SystemExit(1)'
```

结果：

```text
unexpected_status_or_auth=0
```

```bash
python3 -c 'from pathlib import Path
patterns=["Child package documentation files","untracked_files=40","markdown_files=40","0.7.0 package docs","0.7.1 package docs","package docs and mirrors","planned / package docs pending"]
bad=[]
for path in [Path("docs/iterations/v0.7/review.md"), Path("docs/iterations/v0.7/review.zh.md"), Path("docs/iterations/v0.7/v0.7-plan.md"), Path("docs/iterations/v0.7/v0.7-plan.zh.md")]:
    in_fence=False
    for lineno,line in enumerate(path.read_text().splitlines(),1):
        if line.startswith("```"):
            in_fence=not in_fence
            continue
        if in_fence:
            continue
        if any(pattern in line for pattern in patterns):
            bad.append(f"{path}:{lineno}:{line}")
print("stale_child_doc_claims=" + str(len(bad)))
[print(item) for item in bad]
raise SystemExit(1 if bad else 0)'
```

结果：

```text
stale_child_doc_claims=0
```

## Test Results 测试结果

Documentation checks 已通过：

- `git diff --check`：通过。
- Untracked v0.7 docs count：`untracked_files=12`。
- Required v0.7 parent docs/mirrors check：`missing=0`。
- v0.7 parent Markdown count：`markdown_files=12`。
- 具体 child package directory/file count：`child_dir_files=0`，且没有 child directories 或 files。
- Planned-package field check：`planned_package_count=9` 且
  `planned_package_missing_fields=0`。
- Changed-file scope guard：`unexpected_status=0`。
- Status/authorization guard：`unexpected_status_or_auth=0`。
- Stale child-doc review claim search：`stale_child_doc_claims=0`。

Backend、frontend、API、E2E、Agent smoke、autonomous、external validation 和 runtime tests 未运行，因为本次
drafting 是 documentation-only，且没有修改 implementation files。

## Compatibility Review 兼容性评审

本次 drafting 仅修改 documentation。现有 runtime、schema、API、frontend、event、archive、params、Agent
loop、memory、generation、fixture、migration、checker 和 legacy behavior 均未改变。

历史 v0.6 evidence 只作为 handoff context 记录，不能作为当前 v0.7 PASS evidence。

## Scope Review 范围评审

Parent-only review 确认 child packages 在选择前只是路线图规格。当前 `CURRENT_STATE.md` 已记录
v0.7 为 final / closeout complete，没有 active child，也没有 implementation authorization。

`v0.7-plan.md` 中的 `0.7.x` sections 只是 roadmap planned package specs，不是 active child
package documents、implementation authorization 或 immutable execution scripts。未来 implementation 如果发现
design gap，必须停止实现，直到 active child contract/design/test-plan/plan/review 更新并完成复审。

本次 repair pass 没有留下 `docs/iterations/v0.7/**` 之外的文件修改。

## Subagent / Evaluator Evidence 证据

两个 read-only subagents 复核了本次 scope repair：

- English parent-doc reviewer 发现 `review.md` 中仍有 `0.7.0`/`0.7.1` child-doc stale claim
  的 P1；已通过把 review evidence 改为 parent-only scope 修复。
- Chinese mirror/file-tree reviewer 发现 `review.zh.md` 同类 P1 stale child-doc claim，以及 P2
  空 child directory residue；已通过重写中文 review evidence 并删除空目录修复。

修复后的 verification 确认没有 unresolved P1/P2/P3。

Later child-package review evidence：

- `0.7.0-v0.7-planning-and-external-validation-boundary-baseline`：review complete，
  documentation-only，implementation authorization closed，并已 hand off to `0.7.1`。
- `0.7.1-public-validation-and-projection-contracts`：review complete，documentation-only，
  implementation authorization closed，added reviewed public contracts under `docs/contracts/`，并已
  hand off to `0.7.2`。
- `0.7.2-validation-report-schema-and-redaction-checker`：reviewed child
  package docs 已存在，approved schema/checker/template/test scope 已实现，并且 package 已
  review complete。
- `0.7.3-contract-bundle-and-readiness-manifest`：reviewed child package docs
  已存在，approved manifest schema/json/checker/test scope 已实现，并且 package 已
  review complete。
- `0.7.4-projection-consumer-read-model-contracts`：reviewed child package
  docs 已存在，approved projection read-model contract/checker/test scope 已实现，并且
  package 已 review complete。
- `0.7.5-quality-regression-and-compatibility-evidence`：review complete，记录了
  evidence matrix 和累计 compatibility/scope evidence。
- `0.7.6-v0.7-evidence-and-compatibility-audit`：review complete，记录了 audit
  report 与 evidence compatibility findings。
- `0.7.7-v0.7-release-candidate-bundle`：review complete，记录了 release-candidate
  summary。
- `0.7.8-v0.7-final-closeout`：final verification、evaluator PASS 和 parent status
  updates 后 review complete / final closeout complete。
- Final parent-status evaluator：parent updates 后 PASS。Parent final status
  surfaces 已与 `0.7.8` final closeout 对齐，并保留 explicit exclusions。
- Final Chinese mirror evaluator：parent updates 后 PASS。Parent 和 `0.7.8`
  Chinese mirrors 对齐，且没有 stale selected-child、package-docs-needed 或
  pending-evaluator status。

## Unresolved Findings 未解决问题

- P1：无。
- P2：无。
- P3：无。

## Final Assessment 最终评估

v0.7 version-level documentation 和 `0.7.0` 到 `0.7.8` 全部 child packages 均已
review complete。`0.7.8-v0.7-final-closeout` 已通过 final verification 和 evaluator
review，parent status surfaces 已更新。v0.7 在 `CURRENT_STATE.md` 和 `0.7.8`
closeout evidence 记录的 explicit exclusions 下为 final / closeout complete。该 final
state 不授权 runtime、schema、API、frontend、test implementation、fixture、migration、
external repository、generated result 或 `backend/worldengine/` implementation work。
