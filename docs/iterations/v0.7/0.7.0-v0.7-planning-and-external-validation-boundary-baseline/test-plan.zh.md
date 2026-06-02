# Test Plan

## Documentation Checks

Run:

```bash
git status --short --branch
git diff --check
python3 -c 'from pathlib import Path
pkg=Path("docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline")
names=["README","intent","contract","technical-design","test-plan","plan","review"]
missing=[str(pkg/(name+suffix)) for name in names for suffix in (".md",".zh.md") if not (pkg/(name+suffix)).exists()]
print("missing_child_docs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
python3 -c 'from pathlib import Path
checks={
"docs/iterations/v0.7/README.md":["Status: in progress / 0.7.1 child selected","- Status: review complete","- Status: selected / child docs not created"],
"docs/iterations/v0.7/README.zh.md":["状态：in progress / 0.7.1 child selected","- 状态：review complete","- 状态：selected / child docs not created"],
"docs/iterations/v0.7/v0.7-plan.md":["Status: in progress / 0.7.1 child selected","Status: review complete","Status: selected / child docs not created"],
"docs/iterations/v0.7/v0.7-plan.zh.md":["状态：in progress / 0.7.1 child selected","Status：review complete","Status：selected / child docs not created"],
"docs/iterations/v0.7/CURRENT_STATE.md":["Current route: `0.7.1-documentation-package-needed`","Implementation authorization: no","0.7.0-v0.7-planning-and-external-validation-boundary-baseline: review complete","0.7.1-public-validation-and-projection-contracts: selected / child docs not created"],
"docs/iterations/v0.7/CURRENT_STATE.zh.md":["Current route：`0.7.1-documentation-package-needed`","Implementation authorization：no","0.7.0-v0.7-planning-and-external-validation-boundary-baseline: review complete","0.7.1-public-validation-and-projection-contracts: selected / child docs not created"],
"docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline/README.md":["Status: review complete"],
"docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline/README.zh.md":["状态：review complete"]}
bad=[]
for file,terms in checks.items():
    text=Path(file).read_text()
    for term in terms:
        if term not in text:
            bad.append(file + " missing " + term)
print("status_check_failures=" + str(len(bad)))
print("\n".join(bad))
raise SystemExit(1 if bad else 0)'
python3 -c 'import subprocess
allowed_prefix="docs/iterations/v0.7/"
tracked=subprocess.check_output(["git","diff","--name-only"], text=True).splitlines()
untracked=subprocess.check_output(["git","ls-files","--others","--exclude-standard"], text=True).splitlines()
files=tracked+untracked
bad=[p for p in files if not p.startswith(allowed_prefix)]
print("changed_or_untracked=" + str(len(files)))
print("out_of_scope_changed_or_untracked=" + str(len(bad)))
print("\n".join(bad))
raise SystemExit(1 if bad else 0)'
python3 -c 'from pathlib import Path
root=Path("docs/iterations/v0.7")
files=sorted(root.rglob("*.md"))
trailing=[]
tabs=[]
for path in files:
    for lineno,line in enumerate(path.read_text().splitlines(),1):
        if line.rstrip(" \t") != line:
            trailing.append(f"{path}:{lineno}")
        if "\t" in line:
            tabs.append(f"{path}:{lineno}")
print("markdown_files=" + str(len(files)))
print("trailing_whitespace=" + str(len(trailing)))
print("tab_lines=" + str(len(tabs)))
raise SystemExit(1 if trailing or tabs or len(files)!=26 else 0)'
python3 -c 'from pathlib import Path
import re
bad=[]
for path in Path("docs/iterations/v0.7").rglob("*.md"):
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

Expected results:

- Required `0.7.0` child docs 和 Chinese mirrors 存在。
- Parent docs 标记 `0.7.0` review complete，并 route 到 `0.7.1` package creation，同时保持
  implementation authorization closed。
- 本 package changes 不包含 runtime、schema、API、frontend、backend test、checker implementation、
  fixture、migration、external repository、generated result 或 `backend/worldengine/`
  implementation file。
- 任何 `docs/iterations/v0.7/**` 之外预先存在的 dirty file 都明确记录为 outside this package
  scope。
- 没有缺少 current-session evidence 的 positive v0.7 pass/final/release/product/projection/
  external-suite claim。

## Subagent / Evaluator Checks

在标记本 package review complete 前，至少使用一个 read-only documentation evaluator。Evaluator 应检查：

- package document completeness。
- parent/child status consistency。
- implementation authorization remains closed。
- scope boundaries 和 forbidden changes 保持。
- Chinese mirrors 不弱化 status、scope、authorization 或 final assessment semantics。

## Runtime / Code Tests

Backend、frontend、API、E2E、Agent smoke、autonomous、external validation 和 runtime tests 对本 package
不要求运行，因为它是 documentation-only，且不得改变 implementation files。

如果出现任何 implementation file changes，停止并记录 P1 scope failure，不要用运行 implementation tests
代替 scope compliance。

## Acceptance Criteria

- Documentation checks pass。
- Required evaluator review 没有 P0/P1 且没有 blocking P2。
- `review.md` and `review.zh.md` 记录 changed files、commands、results、compatibility review、
  scope review、findings 和 final assessment。
- Parent and child status surfaces 在 route 和 authorization 上一致。
- 没有 unresolved P1/P2。

## Not Run

Code tests intentionally not run unless a future package authorizes implementation changes。本 package 记录该理由，
而不是声明 implementation behavior passed。
