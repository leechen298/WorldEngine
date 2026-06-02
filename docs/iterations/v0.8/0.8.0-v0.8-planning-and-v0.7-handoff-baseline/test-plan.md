# Test Plan

## Exact Commands To Run

```bash
git status --short --branch
```

Expected result: changed/untracked files are limited to authorized
`docs/iterations/v0.8/**` documentation surfaces.

```bash
git diff --check
```

Expected result: exit `0` with no output.

```bash
python3 -c 'from pathlib import Path
pkg=Path("docs/iterations/v0.8/0.8.0-v0.8-planning-and-v0.7-handoff-baseline")
names=["README","intent","contract","technical-design","test-plan","plan","review"]
missing=[str(pkg/(name+suffix)) for name in names for suffix in (".md",".zh.md") if not (pkg/(name+suffix)).exists()]
print("missing_child_docs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
```

Expected result: `missing_child_docs=0`.

```bash
python3 -c 'from pathlib import Path
checks={
"docs/iterations/v0.8/README.md":["Status: in progress / 0.8.1 child selected","0.8.0-v0.8-planning-and-v0.7-handoff-baseline: review complete","0.8.1-minimum-working-state-contract: selected / child docs not created"],
"docs/iterations/v0.8/README.zh.md":["状态：in progress / 0.8.1 child selected","0.8.0-v0.8-planning-and-v0.7-handoff-baseline: review complete","0.8.1-minimum-working-state-contract: selected / child docs not created"],
"docs/iterations/v0.8/v0.8-plan.md":["Status: in progress / 0.8.1 child selected","Status: review complete","Status: selected / child docs not created"],
"docs/iterations/v0.8/v0.8-plan.zh.md":["状态：in progress / 0.8.1 child selected","Status：review complete","Status：selected / child docs not created"],
"docs/iterations/v0.8/CURRENT_STATE.md":["Current route: `0.8.1-documentation-package-needed`","Implementation authorization: no","Evidence execution authorization: no","0.8.0-v0.8-planning-and-v0.7-handoff-baseline: review complete","0.8.1-minimum-working-state-contract: selected / child docs not created"],
"docs/iterations/v0.8/CURRENT_STATE.zh.md":["Current route：`0.8.1-documentation-package-needed`","Implementation authorization：no","Evidence execution authorization：no","0.8.0-v0.8-planning-and-v0.7-handoff-baseline: review complete","0.8.1-minimum-working-state-contract: selected / child docs not created"],
"docs/iterations/v0.8/0.8.0-v0.8-planning-and-v0.7-handoff-baseline/README.md":["Status: review complete"],
"docs/iterations/v0.8/0.8.0-v0.8-planning-and-v0.7-handoff-baseline/README.zh.md":["状态：review complete"]}
bad=[]
for file,terms in checks.items():
    text=Path(file).read_text()
    for term in terms:
        if term not in text:
            bad.append(file + " missing " + term)
print("status_check_failures=" + str(len(bad)))
print("\n".join(bad))
raise SystemExit(1 if bad else 0)'
```

Expected result: `status_check_failures=0`.

```bash
python3 -c 'import subprocess
allowed_prefix="docs/iterations/v0.8/"
tracked=subprocess.check_output(["git","diff","--name-only"], text=True).splitlines()
untracked=subprocess.check_output(["git","ls-files","--others","--exclude-standard"], text=True).splitlines()
files=tracked+untracked
bad=[p for p in files if not p.startswith(allowed_prefix)]
print("changed_or_untracked=" + str(len(files)))
print("out_of_scope_changed_or_untracked=" + str(len(bad)))
print("\n".join(bad))
raise SystemExit(1 if bad else 0)'
```

Expected result: `out_of_scope_changed_or_untracked=0`.

```bash
python3 -c 'from pathlib import Path
root=Path("docs/iterations/v0.8")
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
raise SystemExit(1 if trailing or tabs else 0)'
```

Expected result: `trailing_whitespace=0` and `tab_lines=0`.

```bash
python3 -c 'from pathlib import Path
import re
bad=[]
for path in Path("docs/iterations/v0.8").rglob("*.md"):
    if path.name.startswith("test-plan"):
        continue
    lines=path.read_text().splitlines()
    for lineno,line in enumerate(lines,1):
        if re.match(r"^(implementation_authorized|Implementation authorization)[：:] yes$", line):
            bad.append(f"{path}:{lineno}: implementation authorization yes")
        if re.match(r"^(evidence_execution_authorized|Evidence execution authorization)[：:] yes$", line):
            bad.append(f"{path}:{lineno}: evidence execution authorization yes")
        positive=["external validation PASS","external consumer PASS","minimum working-state PASS","product readiness passed","runtime behavior passed","API behavior passed","frontend behavior passed","E2E passed","Agent smoke passed","autonomous runner or autonomous suite passed","v0.8 readiness passed"]
        context=" ".join(lines[max(0,lineno-20):lineno+1]).lower()
        nonclaim=["not claim","non-claim","nonclaims","不声明","不得","do not","must not","does not","does not prove","no ","without claiming","without current-session evidence","不证明","不能","过度声明","current exclusions","当前 v0.8 documentation 不声明","当前 v0.8 文档不声明"]
        for phrase in positive:
            if phrase in line and not any(marker in context for marker in nonclaim):
                bad.append(f"{path}:{lineno}: possible positive claim {phrase}")
print("claim_guard_failures=" + str(len(bad)))
print("\n".join(bad))
raise SystemExit(1 if bad else 0)'
```

Expected result: `claim_guard_failures=0`.

```bash
rg -n 'v0\.7 post-closeout (P1/P2 )?blockers must be repaired|until they are repaired|code-review blockers recorded|blocking findings' docs/iterations/v0.8 --glob '!review*.md' --glob '!test-plan*.md'
```

Expected result: exit `1` with no stale unresolved-blocker wording in active
v0.8 docs outside review history and test-plan command examples.

## Commands Not Run And Why

Backend, frontend, API, E2E, Agent smoke, autonomous, external validation, and
runtime tests are not run for this package because it is documentation-only and
does not authorize implementation or evidence execution.

## Blocker Recording Rule

Any failed documentation check, missing mirror, out-of-scope changed file,
stale v0.7 blocker wording, positive readiness claim, or evaluator P1/P2 must
be recorded as a blocker in `review.md` before handoff.

## No Unverified Claims Rule

This package may report documentation checks run in the current session. It
must not claim runtime/API/frontend/E2E/Agent/autonomous/external validation,
minimum working-state, product, or release behavior passed.
