# Test Plan

Status: review complete

## Documentation Checks

Run:

```bash
git status --short --branch
git diff --check
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics'); required=['WorldGenerationRequest','WorldTemplate','GenerationPlan','GeneratedWorldSpec','GenerationMetadata','GenerationPreview','RegenerationRequest','diagnostics','implementation_authorized: no']; bad=[]; text='\\n'.join(path.read_text() for path in child.glob('*.md')); [bad.append(term) for term in required if term not in text]; print('missing_required_terms=' + str(len(bad))); [print(term) for term in bad]; raise SystemExit(1 if bad else 0)"
python3 -c "import subprocess; allowed_prefixes=('docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics/',); lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[]; [bad.append(line) for line in lines if line and not line[3:].startswith(allowed_prefixes)]; print('unexpected_status=' + str(len(bad))); [print(item) for item in bad]; raise SystemExit(1 if bad else 0)"
```

Expected:

- `git diff --check` exits `0`.
- required docs/mirrors check prints `missing=0`.
- required term check prints `missing_required_terms=0`.
- scope guard prints `unexpected_status=0` before parent status files are
  updated.

After parent status files are updated, rerun the scope guard with
`docs/iterations/v0.6/` as the allowed prefix and expect `unexpected_status=0`.

## Mirror Quality Check

Run:

```bash
python3 -c 'from pathlib import Path
import re
bad=[]
for path in Path("docs/iterations/v0.6/0.6.1-world-generation-contracts-and-template-semantics").glob("*.zh.md"):
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

## Status Consistency Check

After evaluator evidence is recorded and parent status files are updated,
search for the reviewed handoff:

```bash
rg -n "0\\.6\\.1-world-generation-contracts-and-template-semantics: review complete|0\\.6\\.2-template-catalog-and-deterministic-generator-core|implementation_authorized: no" docs/iterations/v0.6
```

Expected: status surfaces agree on the active or next child, and
implementation authorization remains closed.

## Commands Not Run

Backend, frontend, API, E2E, runtime, Agent smoke, autonomous validation,
build, fixture, migration, and external validation commands are not run for
`0.6.1` because this package is documentation-only and changes no
implementation surfaces.

## Blocker Recording Rule

If documentation checks fail, record the exact command, exit status, and
failure summary in `review.md`. Do not mark this package review complete until
the failure is fixed or explicitly classified.

If the documentation evaluator is unavailable or reports blocking P1/P2, keep
status at `planned / ready for review` or record the blocker. Do not mark
`implementation_authorized: yes`.

## No Unverified Claims Rule

Only commands actually run in the current session may be recorded as passed.
Do not record backend, frontend, API, E2E, runtime, Agent smoke, autonomous,
build, release, product-readiness, or generated-world quality claims as
passed unless those commands or flows were actually executed and are in scope.
