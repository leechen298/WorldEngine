# Test Plan

Status: review complete

## Documentation Checks

Run:

```bash
git status --short --branch
git diff --check
python3 -c "from pathlib import Path; parent=Path('docs/iterations/v0.6'); child=parent/'0.6.0-v0.6-planning-and-generation-boundary-baseline'; parent_docs=['README','v0.6-plan','GOAL_RUNNER','CURRENT_STATE','CAMPAIGN_PLAN','review']; child_docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[]; missing += [str(parent/(name+suffix)) for name in parent_docs for suffix in ('.md','.zh.md') if not (parent/(name+suffix)).exists()]; missing += [str(child/(name+suffix)) for name in child_docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
python3 -c 'from pathlib import Path
import re
required=["Package name:","Status:","Type:","Goal:","Why this exists:","Inputs / required reading:","Allowed changes:","Forbidden changes:","Expected deliverables:","Expected tests / verification:","Compatibility constraints:","Scope guardrails:","Exit criteria:","Handoff to next package:"]
lines=Path("docs/iterations/v0.6/v0.6-plan.md").read_text().splitlines()
heads=[(i,l) for i,l in enumerate(lines) if re.match(r"^### 0\.6\.[0-9]+ ", l)]
bad=[]
for idx,(start,head) in enumerate(heads):
    end=heads[idx+1][0] if idx+1 < len(heads) else len(lines)
    section="\n".join(lines[start:end])
    missing=[f for f in required if f not in section]
    if missing:
        bad.append((head, missing))
print("planned_package_missing_fields=" + str(len(bad)))
for head, missing in bad:
    print(head + " missing " + ", ".join(missing))
raise SystemExit(1 if bad else 0)'
```

Expected:

- `git diff --check` exits `0`.
- required docs/mirrors check prints `missing=0`.
- planned package field check prints `planned_package_missing_fields=0`.

## Scope Guard

Run a scope guard that confirms current work only contains this package's v0.6
docs:

```bash
python3 -c "import subprocess; allowed_prefixes=('docs/iterations/v0.6/',); lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[];
for line in lines:
    if not line:
        continue
    path=line[3:]
    if path.startswith(allowed_prefixes):
        continue
    bad.append(line)
print('unexpected_status=' + str(len(bad))); [print(item) for item in bad]; raise SystemExit(1 if bad else 0)"
```

Expected: `unexpected_status=0`.

## Mirror Quality Check

Run:

```bash
python3 -c 'from pathlib import Path
import re
bad=[]
for path in Path("docs/iterations/v0.6").rglob("*.zh.md"):
    in_fence=False
    for lineno,line in enumerate(path.read_text().splitlines(),1):
        if line.startswith("```"):
            in_fence=not in_fence
            continue
        if in_fence or not line.startswith("#"):
            continue
        text=line.lstrip("#").strip()
        has_latin=bool(re.search(r"[A-Za-z]", text))
        has_cjk=bool(re.search(r"[\u4e00-\u9fff]", text))
        code_like=text.startswith("`") or text.startswith("0.6.") or "`" in text
        if has_latin and not has_cjk and not code_like:
            bad.append(f"{path}:{lineno}:{line}")
print("generic_english_only_headings=" + str(len(bad)))
for item in bad:
    print(item)
raise SystemExit(1 if bad else 0)'
```

Expected: `generic_english_only_headings=0`.

## Commands Not Run

Backend, frontend, API, E2E, runtime, Agent smoke, autonomous validation,
build, fixture, migration, and external validation commands are not run for
`0.6.0` because this package is documentation-only and does not change those
implementation surfaces.

## Blocker Recording Rule

If documentation checks fail, record the exact command, exit status, and
failure summary in `review.md`. Do not mark this package review complete until
the failure is fixed or explicitly classified.

If evaluator tooling is unavailable or not authorized, record that status in
`review.md` and keep implementation authorization closed.

## No Unverified Claims Rule

Only commands actually run in the current session may be recorded as passed.
Historical v0.5 evidence may be cited only as handoff evidence.
