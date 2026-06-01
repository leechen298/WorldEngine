# Review

Status: planned / ready for review

implementation_authorized: no

## Scope Correction

This review records the corrected v0.7 documentation scope:

- The current authoritative v0.7 artifact is the version-level package only.
- Planned child packages exist only as route-map specifications in
  `v0.7-plan.md`.
- No concrete child package directory is currently authoritative, active, or
  execution-approved.
- Future child package work must create or confirm that child package's full
  document set at the time the child starts, then pass review before
  implementation.

## Changed Files

Version-level v0.7 documentation files:

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

Removed from scope:

- Premature `0.7.0` child package files and empty directory.
- Premature `0.7.1` child package files and empty directory.

No runtime, schema, API, frontend, backend test, checker implementation,
fixture, migration, external repository, generated result, or
`backend/worldengine/` implementation files are authorized by this drafting
pass.

## Commands Run

```bash
git status --short --branch
```

Result:

```text
## v0.7-local
?? docs/iterations/v0.7/
```

```bash
git diff --check
```

Result: passed with no output.

```bash
rmdir docs/iterations/v0.7/0.7.0-v0.7-planning-and-external-validation-boundary-baseline docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts
```

Result: passed with no output. This removed two empty premature child package
directories after their files had already been deleted.

```bash
python3 -c 'import subprocess
files=subprocess.check_output(["git","ls-files","--others","--exclude-standard","docs/iterations/v0.7"], text=True).splitlines()
print("untracked_files=" + str(len(files)))
raise SystemExit(1 if len(files) != 12 else 0)'
```

Result:

```text
untracked_files=12
```

```bash
find docs/iterations/v0.7 -mindepth 1 -maxdepth 2 -type d -print | sort
```

Result: passed with no output. No child package directories remain.

```bash
find docs/iterations/v0.7 -mindepth 2 -type f | sort
```

Result: passed with no output. No child package files remain.

```bash
python3 -c 'from pathlib import Path
parent=Path("docs/iterations/v0.7")
parent_docs=["README","v0.7-plan","GOAL_RUNNER","CURRENT_STATE","CAMPAIGN_PLAN","review"]
missing=[str(parent/(name+suffix)) for name in parent_docs for suffix in (".md",".zh.md") if not (parent/(name+suffix)).exists()]
print("missing=" + str(len(missing)))
raise SystemExit(1 if missing else 0)'
```

Result:

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

Result:

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

Result:

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

Result:

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

Result:

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

Result:

```text
stale_child_doc_claims=0
```

## Test Results

Documentation checks passed:

- `git diff --check`: passed.
- Untracked v0.7 docs count: `untracked_files=12`.
- Required v0.7 parent docs/mirrors check: `missing=0`.
- v0.7 parent Markdown count: `markdown_files=12`.
- Concrete child package directory and file count: `child_dir_files=0`, with no
  child directories or files remaining.
- Planned-package field check: `planned_package_count=9` and
  `planned_package_missing_fields=0`.
- Changed-file scope guard: `unexpected_status=0`.
- Status/authorization guard: `unexpected_status_or_auth=0`.
- Stale child-doc review claim search: `stale_child_doc_claims=0`.

Backend, frontend, API, E2E, Agent smoke, autonomous, external validation, and
runtime tests were not run for this drafting pass because it is
documentation-only and does not modify implementation files.

## Compatibility Review

This drafting pass is documentation-only. Existing runtime, schema, API,
frontend, event, archive, params, Agent loop, memory, generation, fixture,
migration, checker, and legacy behavior are unchanged.

Historical v0.6 evidence is recorded only as handoff context. It is not
current v0.7 PASS evidence.

## Scope Review

The v0.7 parent docs now explicitly state that child packages are route-map
specifications only. `CURRENT_STATE.md` records no active child package and no
implementation authorization.

The `0.7.x` sections in `v0.7-plan.md` are roadmap planned package specs only.
They are not active child package documents, implementation authorization, or
immutable execution scripts. Future implementation must stop on a design gap
until the active child contract/design/test-plan/plan/review are updated and
reviewed.

No files outside `docs/iterations/v0.7/**` remain modified by this repair pass.

## Subagent / Evaluator Evidence

Two read-only subagents reviewed the scope repair:

- English parent-doc reviewer found a P1 stale `0.7.0`/`0.7.1` child-doc claim
  in `review.md`; fixed by rewriting the review evidence to parent-only scope.
- Chinese mirror/file-tree reviewer found the same P1 stale child-doc claim in
  `review.zh.md` and a P2 empty-child-directory residue; fixed by rewriting the
  Chinese review evidence and removing the empty directories.

Post-fix verification confirms no unresolved P1/P2/P3 remain.

## Unresolved Findings

- P1: none.
- P2: none.
- P3: child package document sets remain future work by design. Each future
  child must be created or confirmed and reviewed at the time that child
  starts.

## Final Assessment

The v0.7 version-level documentation is ready for review as a parent package
only. No concrete child package directory is currently authoritative,
review-complete, or implementation-authorized.
