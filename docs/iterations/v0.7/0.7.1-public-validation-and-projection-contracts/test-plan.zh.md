# Test Plan

## Documentation Checks

Run:

```bash
git status --short --branch
git diff --check
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

Expected results:

- Required `0.7.1` package docs and Chinese mirrors exist。
- Two public contract docs exist。
- Changed/untracked files stay inside the documentation-only scope。
- Contract docs include forbidden-detail and redaction boundaries。
- Implementation authorization remains closed。

## Runtime / Code Tests

Backend、frontend、API、E2E、Agent smoke、autonomous、external validation 和 runtime tests are not run
because this package is documentation-only and must not change implementation files。

## Blocker Recording Rule

任何 documentation check、scope guard、contract guard 或 evaluator review 失败，都必须记录到
`review.md`，并且在 blocker 被修复或被 active contract 明确接受前，不得标记 package 为
`review complete`。

## No Unverified Claims Rule

不要声明 runtime、API、frontend、E2E、Agent smoke、autonomous、external validation、
projection readiness、product readiness 或 release behavior passed。本 package 只能基于实际运行并记录到
`review.md` 的命令，声明 documentation 与 public contract readiness。

## Acceptance Criteria

- Documentation checks pass。
- Read-only documentation evaluator reports no P0/P1 and no blocking P2。
- `review.md` and `review.zh.md` record changed files、commands、test results、compatibility review、
  scope review、findings 和 final assessment。
- `0.7.2` authorization criteria are explicit。
- No unresolved P1/P2 remains。
