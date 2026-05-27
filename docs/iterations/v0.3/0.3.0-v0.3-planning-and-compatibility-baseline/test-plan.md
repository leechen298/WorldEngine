# Test Plan

Status: ready for review

## Scope

This package is documentation-only. It must not run backend or frontend tests
unless implementation files are accidentally changed.

## Required Commands

```bash
git status --short --branch
git diff --check
```

## v0.3 Document Existence Checks

```bash
test -f docs/iterations/v0.3/README.md
test -f docs/iterations/v0.3/v0.3-plan.md
test -f docs/iterations/v0.3/00-chatgpt-plan.md
test -f docs/iterations/v0.3/0.3.0-v0.3-planning-and-compatibility-baseline/README.md
```

## Documentation Status Checks

Use single-quoted patterns so backticks in Chinese status text are not
interpreted by the shell:

```bash
rg -n 'Status: planned / in progress|状态：`planned / in progress`|0\.3\.0|0\.3\.1|0\.3\.8|WorldSpec Loader and Runtime Bridge' docs/iterations/v0.3 docs/roadmap.md docs/roadmap.zh.md
```

If release placeholders are modified, run:

```bash
rg -n 'v0\.3|planned|not released|draft' docs/releases/v0.3.md docs/releases/v0.3.zh.md
```

## Forbidden Phrase Check

```bash
tmp_patterns="$(mktemp)"
printf '%s\n' \
  'v0\.3[[:space:]]complete' \
  'release[[:space:]]complete' \
  'Status:[[:space:]]released' \
  'Agent-in-World loop[[:space:]]implemented' \
  'world generation[[:space:]]implemented' \
  'external validation repository[[:space:]]created' \
  > "$tmp_patterns"
rg -n -f "$tmp_patterns" docs/iterations/v0.3 docs/releases/v0.3.md docs/releases/v0.3.zh.md
rc=$?
rm -f "$tmp_patterns"
test "$rc" -eq 1
```

This command should return no matches.

## Roadmap Status Acceptance Gate

Before final output, verify:

- `docs/roadmap.md` and `docs/roadmap.zh.md` no longer describe v0.2 as
  `planned / in progress`.
- v0.2 is described as final / closeout complete or equivalent wording.
- v0.3 remains planned / in progress, not released.
- v0.3 roadmap wording stays focused on WorldSpec Loader and Runtime Bridge.
- v0.4+ roadmap direction is not rewritten except for unavoidable wording
  consistency.

Suggested checks:

```bash
sed -n '15,24p' docs/roadmap.md
sed -n '16,25p' docs/roadmap.zh.md
rg -n '## v0\.3 - WorldSpec Loader and Runtime Bridge|Status: planned / in progress|状态：`planned / in progress`' docs/roadmap.md docs/roadmap.zh.md
```

If v0.2 still appears as planned / in progress in roadmap files after this
pass, record a P1 finding.

## Tests Not Run

Do not run backend or frontend tests because this package only changes
documentation and roadmap status wording.
