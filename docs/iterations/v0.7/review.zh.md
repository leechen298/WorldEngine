# Review 评审

状态：planned / ready for review

implementation_authorized：no

## 范围修正

本 review 记录修正后的 v0.7 文档范围：

- 当前 v0.7 的权威产物只有 version-level package。
- Planned child packages 只作为 `v0.7-plan.md` 中的路线图规格存在。
- 当前没有任何具体 child package directory 是权威、active 或 execution-approved。
- 未来启动 child package 时，必须当时创建或确认该 child 的完整 document set，并通过
  review 后才能 implementation。

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

- 提前创建的 `0.7.0` child package files 与空目录。
- 提前创建的 `0.7.1` child package files 与空目录。

本次 drafting 不授权 runtime、schema、API、frontend、backend test、checker implementation、fixture、
migration、external repository、generated result 或 `backend/worldengine/` implementation files。

## Commands Run 已运行命令

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

v0.7 parent docs 已明确 child packages 只是路线图规格。`CURRENT_STATE.md` 记录没有 active
child package，也没有 implementation authorization。

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

## Unresolved Findings 未解决问题

- P1：无。
- P2：无。
- P3：child package document sets 按设计留到未来处理。每个未来 child 都必须在启动时创建或确认，
  并完成 review。

## Final Assessment 最终评估

v0.7 version-level documentation 作为 parent package 已 ready for review。当前没有任何具体
child package directory 是权威、review-complete 或 implementation-authorized。
