# Review

Status: review complete
implementation_authorized: no

## Changed Files

Expected package files:

- `docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/README.md`
- `docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/intent.md`
- `docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/contract.md`
- `docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/technical-design.md`
- `docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/test-plan.md`
- `docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/plan.md`
- `docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts/review.md`
- Chinese mirrors for each package document.

Expected public contract docs:

- `docs/contracts/external-validation-readiness-contract.md`
- `docs/contracts/projection-consumer-contract.md`

## Commands Run

```bash
git status --short --branch
```

Result: passed. The changed/untracked set is limited to v0.7 documentation
surfaces and the two approved public contract documents.

```bash
git diff --check
```

Result: passed with no output.

```bash
python3 -c 'from pathlib import Path
pkg=Path("docs/iterations/v0.7/0.7.1-public-validation-and-projection-contracts")
names=["README","intent","contract","technical-design","test-plan","plan","review"]
missing=[str(pkg/(name+suffix)) for name in names for suffix in (".md",".zh.md") if not (pkg/(name+suffix)).exists()]
for file in ["docs/contracts/external-validation-readiness-contract.md","docs/contracts/projection-consumer-contract.md"]:
    if not Path(file).exists():
        missing.append(file)
print("missing_0_7_1_docs=" + str(len(missing)))
print("\n".join(missing))
raise SystemExit(1 if missing else 0)'
```

Result:

```text
missing_0_7_1_docs=0
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

Result:

```text
changed_or_untracked=42
out_of_scope_changed_or_untracked=0
```

```bash
python3 -c 'from pathlib import Path
bad=[]
for path in [Path("docs/contracts/external-validation-readiness-contract.md"),Path("docs/contracts/projection-consumer-contract.md")]:
    text=path.read_text().lower()
    for term in ["character name", "location name", "story rule", "seed data", "ui selector", "oracle internal", "private fixture"]:
        if term not in text:
            bad.append(f"{path}: missing forbidden/redaction term {term}")
print("contract_guard_failures=" + str(len(bad)))
print("\n".join(bad))
raise SystemExit(1 if bad else 0)'
```

Result:

```text
contract_guard_failures=0
```

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
raise SystemExit(1 if trailing or tabs else 0)'
```

Result:

```text
checked_files=42
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

Result:

```text
claim_guard_failures=0
```

## Test Results

Documentation checks passed:

- `git diff --check`: passed.
- Required package and public contract docs: `missing_0_7_1_docs=0`.
- Scope guard: `changed_or_untracked=42`,
  `out_of_scope_changed_or_untracked=0`.
- Contract forbidden-detail/redaction guard: `contract_guard_failures=0`.
- Markdown formatting: `checked_files=42`, `trailing_whitespace=0`,
  `tab_lines=0`.
- Authorization and positive-claim guard: `claim_guard_failures=0`.

Backend, frontend, API, E2E, Agent smoke, autonomous, external validation, and
runtime tests are not run because this package is documentation-only and does
not authorize implementation changes.

## Subagent / Evaluator Evidence

Documentation/contract evaluator: PASS_WITH_FINDINGS.

- P0/P1: none.
- P2 parent v0.7 status surfaces stale while `0.7.1` docs exist. Fixed by
  marking `0.7.1` review complete and routing parent state to `0.7.2`.
- P3 `docs/validation-report-template.md` currently lists only
  `pass / fail / blocked`, while the new readiness contract adds `skipped`
  and `out_of_scope`. Carried as a `0.7.2` handoff: the report
  schema/template/checker alignment must be handled in
  `0.7.2-validation-report-schema-and-redaction-checker`.
- Confirmed package docs, public contracts, taxonomy, redaction rules,
  compatibility requirements, and `0.7.2` authorization criteria are
  reviewable.
- Confirmed no implementation authorization, no product/projection app
  readiness claim, and no concrete external/private consumer details.

Chinese mirror/scope evaluator: PASS_WITH_FINDINGS.

- P2 pending review evidence in `review.md` / `review.zh.md`. Fixed by
  recording command evidence, compatibility review, scope review, evaluator
  evidence, and final assessment.
- P3 parent status still said `0.7.1` docs were not created. Fixed by routing
  parent state to `0.7.2`.
- Confirmed mirrors preserve status, type, goal, scope, forbidden changes,
  compatibility, authorization criteria, findings, and final assessment
  semantics.
- Confirmed changed/untracked scope stays inside `docs/iterations/v0.7/**`
  plus the two approved public contract docs.

## Compatibility Review

This package is documentation-only. Existing runtime, schema, API, frontend,
event, archive, params, Agent loop, memory, generation, fixture, migration,
checker, and legacy behavior are unchanged.

`docs/contracts/external-fixture-runner-contract.md` remains compatible. The
new readiness contract additively defines readiness taxonomy and report
semantics without changing the existing runner contract.

## Scope Review

The changed/untracked file set stays inside `docs/iterations/v0.7/**` and the
two approved public contract docs. No runtime, schema, API, frontend, backend
test, checker implementation, fixture, migration, external repository,
generated result, or `backend/worldengine/` implementation file is modified by
this package.

## Unresolved Findings

- P1: none.
- P2: none.
- P3: `0.7.2` must align `docs/validation-report-template.md` and any
  future schema/checker with the new `skipped` and `out_of_scope` report
  status semantics.

## Final Assessment

`0.7.1-public-validation-and-projection-contracts` is review complete. It
hands off reviewed external-validation readiness semantics, projection
consumer boundaries, readiness taxonomy, redaction rules, and `0.7.2`
authorization criteria to
`0.7.2-validation-report-schema-and-redaction-checker`.
