# Review

Status: implementation complete / ready for implementation review

## Implementation Review Fix Closeout

### Changed Files

| File | Change |
|---|---|
| `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/review.md`, `review.zh.md` | Fixed P1 stale implementation evidence by recording the committed checkpoint and adding omitted `docs/iterations/v0.2/findings.md` changed-file evidence. |

### Commands Run

```bash
git log --oneline --decorate -8
git diff --check
sed '/^```bash$/,/^```$/d' docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/review.md docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/review.zh.md | rg -n 'No checkpoint commit|handoff is blocked|未创建 checkpoint|仍被阻塞'
git show --name-only --oneline --no-renames --format='%h %s' HEAD
git status --short --branch
```

### Test Results

- `git diff --check` exited `0`; no whitespace errors.
- Stale checkpoint-blocker text sweep, excluding fenced command blocks, exited
  `1` with no matches.
- `git show --name-only --oneline --no-renames --format='%h %s' HEAD`
  exited `0`; commit `19282d9` includes `docs/iterations/v0.2/findings.md`.
- Backend tests were not run for this fix because only review evidence
  documentation changed.

### Remaining Risks

- P1: none.
- P2: detailed v0.2 plan status still marks 0.2.7 as `ready for review`
  while the milestone index marks it `review complete`; this remains deferred
  to 0.2.9.

## Implementation Closeout

### Changed Files

| File | Change |
|---|---|
| `docs/contracts/event-ref-contract.md` | Added the v0.2 EventRef and Event.refs contract with field semantics, validation behavior, compatibility guarantees, event-local limits, and non-goals. |
| `backend/app/tests/test_event_schema_compat.py` | Added focused coverage proving EventRef accepts free-form metadata without interpretation. |
| `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/review.md`, `review.zh.md` | Added implementation closeout evidence. |
| `docs/iterations/v0.2/findings.md` | Recorded the deferred 0.2.7 milestone status synchronization finding for 0.2.9 follow-up. |

No schema code changes were required. The current EventRef and Event.refs
schema already preserves optional refs, default refs, non-empty id/kind
validation, default metadata, nested event containers, and model dump /
validate round trips.

### Commands Run

```bash
git status --short --branch
git diff --check
cd backend && .venv/bin/python -m pytest app/tests/test_event_schema_compat.py -q
make check-backend
backend/.venv/bin/python - <<'PY'
from pathlib import Path
import base64
encoded = b'aGlzdG9yaWNhbC1jaGlsZC1jZWxsCmhpc3RvcmljYWwgYXJlYQpoaXN0b3JpY2FsLW5lc3RlZC1lbnRpdHkKaGlzdG9yaWNhbCBvYmplY3QKaGlzdG9yaWNhbCBhY3Rvcgpjb25jcmV0ZSBkZW1vIHN1cmZhY2UKY29uY3JldGUgcHJvZHVjdCBzdXJmYWNlCmhpc3RvcmljYWwgY29uY3JldGUgZml4dHVyZQo='
Path('/tmp/worldengine-0.2.8-anchor-patterns.txt').write_text(base64.b64decode(encoded).decode('utf-8'))
PY
rg -n -i -f /tmp/worldengine-0.2.8-anchor-patterns.txt docs/contracts/event-ref-contract.md backend/app/tests/test_event_schema_compat.py docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/review.md docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/review.zh.md
git add docs/contracts/event-ref-contract.md backend/app/tests/test_event_schema_compat.py docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/review.md docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/review.zh.md
```

The temporary anchor pattern file was created under `/tmp` and was not
tracked. The encoded command payload intentionally avoids writing concrete
pattern lists into tracked review evidence.

### Test Results

- `git status --short --branch` exited `0`; branch `v0.2` was ahead of
  `origin/v0.2` by 5 commits and showed this package's modified event test,
  modified review files, untracked `docs/contracts/event-ref-contract.md`, and
  pre-existing untracked `docs/iterations/v0.2/findings.md`.
- `git diff --check` exited `0`; no whitespace errors.
- `cd backend && .venv/bin/python -m pytest app/tests/test_event_schema_compat.py -q`
  exited `0`; result: `10 passed in 0.05s`.
- `make check-backend` exited `0`.
- Concrete demo anchor sweep over the touched contract doc, focused event
  test, and review evidence exited `1` with no matches.
- `git add ...` initially exited `128` in the implementation session because
  that sandbox could not create `.git/index.lock` (`Operation not permitted`);
  the implementation checkpoint was later committed as `19282d9`.
- Full backend app tests were not run because event schema code did not
  change.
- Recursive schema tests were not run because shared schema behavior and
  recursive schema imports were not touched.

### Compatibility Review

Runtime behavior, event log behavior, payload behavior, API response shapes,
frontend behavior, fixtures, migrations, and legacy `backend/worldengine/`
behavior were not changed. `Event.refs` remains optional and defaults to `[]`;
existing events without refs continue to validate. EventRef validation behavior
is unchanged.

### Scope Review

Implementation stayed inside 0.2.8 scope:

- added the approved EventRef contract document.
- added one focused, domain-neutral event schema compatibility test.
- updated only this package's review evidence files and the deferred findings
  register.
- did not add a resolver, causality engine, runtime bridge, memory behavior,
  projection behavior, generation, frontend work, fixtures, migrations,
  external repository, API route, or `backend/worldengine/` change.

### Unresolved Findings

- P1: none.
- P2: detailed v0.2 plan status still marks 0.2.7 as `ready for review`
  while the milestone index marks it `review complete`; this was identified
  by documentation review and deferred to 0.2.9.
- P3: none.

### Final Assessment

0.2.8 implementation is complete and ready for implementation review. The
implementation checkpoint exists as commit `19282d9`.

## Changed Files

| File | Change |
|---|---|
| `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/**` | Added documentation-stage package docs with English and Chinese mirrors. |
| `docs/iterations/v0.2/README.md`, `README.zh.md` | Updated 0.2.8 package status to `ready for review`. |
| `docs/iterations/v0.2/v0.2-plan.md`, `v0.2-plan.zh.md` | Updated 0.2.8 package status to `ready for review`. |
| `docs/contracts/event-ref-contract.md` | Added the v0.2 EventRef and Event.refs contract. |
| `backend/app/tests/test_event_schema_compat.py` | Added focused free-form metadata compatibility coverage. |
| `docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/review.md`, `review.zh.md` | Added implementation-stage evidence. |
| `docs/iterations/v0.2/findings.md` | Recorded the deferred 0.2.7 milestone status synchronization finding for 0.2.9 follow-up. |

## Commands Run

```bash
git status --short --branch
sed -n '1,220p' /Users/leechen/projects/WorldEnginProjects/WorldEngine/.agents/skills/worldengine-iteration-docs/SKILL.md
rg --files -g 'AGENTS.md' -g 'CLAUDE.md' -g 'AGENTS.zh.md' -g 'README.md' docs/iterations docs
find docs/iterations -maxdepth 3 -type f | sort
sed -n '1,220p' AGENTS.md
sed -n '1,220p' CLAUDE.md
sed -n '1,260p' docs/iterations/README.md
sed -n '1,260p' docs/project-north-star.md
sed -n '1,260p' docs/product-model.md
sed -n '1,260p' docs/scope-boundaries.md
sed -n '1,260p' docs/roadmap.md
sed -n '1,320p' docs/iterations/v0.2/README.md
sed -n '1,340p' docs/iterations/v0.2/v0.2-plan.md
sed -n '1,340p' docs/iterations/v0.2/00-chatgpt-plan.md
sed -n '1,260p' docs/iterations/v0.2/v0.2-plan.zh.md
sed -n '1,220p' docs/iterations/v0.2/README.zh.md
sed -n '1,260p' backend/app/schemas/event.py
sed -n '1,300p' backend/app/tests/test_event_schema_compat.py
sed -n '1,260p' docs/backend-implementation.md
sed -n '1,260p' docs/current-implementation.md
find docs/contracts -maxdepth 1 -type f -print
mkdir -p docs/iterations/v0.2/0.2.8-event-reference-contract-hardening
for f in README intent contract technical-design test-plan plan review; do test -f "docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/$f.md" && test -f "docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/$f.zh.md" || exit 1; done; find docs/iterations/v0.2/0.2.8-event-reference-contract-hardening -maxdepth 1 -type f | wc -l
rg -n 'Status: ready for review|状态：`ready for review`|0\.2\.8-event-reference-contract-hardening' docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/README.md docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/README.zh.md docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md
git diff --check
rg -n '[[:blank:]]$' docs/iterations/v0.2/0.2.8-event-reference-contract-hardening docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md
git diff --name-only
git diff --stat
sed -n '1,220p' /Users/leechen/projects/WorldEnginProjects/WorldEngine/.agents/skills/worldengine-iteration-dev/SKILL.md
sed -n '1,240p' AGENTS.md
sed -n '1,240p' CLAUDE.md
sed -n '1,240p' docs/iterations/README.md
sed -n '1,520p' docs/iterations/v0.2/v0.2-plan.md
sed -n '1,220p' docs/iterations/v0.2/README.md
sed -n '1,220p' docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/README.md
sed -n '1,260p' /Users/leechen/projects/WorldEnginProjects/WorldEngine/.agent-runs/20260526-202736-v0.2-0.2.8-event-reference-contract-hardening/docs-review.md
sed -n '1,260p' docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/intent.md
sed -n '1,320p' docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/contract.md
sed -n '1,320p' docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/technical-design.md
sed -n '1,320p' docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/test-plan.md
sed -n '1,360p' docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/plan.md
sed -n '1,360p' docs/iterations/v0.2/0.2.8-event-reference-contract-hardening/review.md
sed -n '1,260p' docs/backend-implementation.md
sed -n '1,260p' docs/current-implementation.md
sed -n '1,280p' docs/scope-boundaries.md
sed -n '1,280p' backend/app/schemas/event.py
sed -n '1,360p' backend/app/tests/test_event_schema_compat.py
find docs/contracts -maxdepth 1 -type f -print | sort
sed -n '1,260p' docs/contracts/entity-ref-contract.md
sed -n '1,260p' docs/contracts/worldcell-contract.md
sed -n '1,260p' docs/contracts/worldspec-contract.md
```

## Test Results

- `git status --short --branch` exited `0`; branch `v0.2` is ahead of
  `origin/v0.2` by 4 commits and showed only v0.2 iteration docs modified
  plus the untracked 0.2.8 package directory.
- English / Chinese mirror file check passed for the seven required package
  document names.
- File count check found 14 package documents: seven English files and seven
  Chinese mirrors.
- Status checks confirmed this package README, the Chinese README mirror, the
  v0.2 milestone index, and the v0.2 plan docs mark 0.2.8 as
  `ready for review`.
- `git diff --check` exited `0`; no whitespace errors were found in tracked
  diffs.
- Trailing-whitespace grep over the new package docs and touched v0.2 status
  docs exited `1` with no matches.
- `git diff --name-only` and `git diff --stat` showed only the four tracked
  v0.2 status docs; the new package docs remain untracked until staged by a
  later commit workflow.

Backend and frontend tests were not run because this pass only prepares the
iteration package documentation and updates milestone planning docs. No
runtime, schema, API, frontend, fixture, migration, or test implementation
files were intentionally modified.

## Compatibility Review

No runtime behavior, API response shape, schema behavior, frontend behavior,
fixture behavior, migration behavior, or legacy `backend/worldengine/`
behavior is changed by this documentation-stage pass.

The planned implementation contract preserves additive event compatibility
unless a future documentation review explicitly approves a breaking change.

## Scope Review

This pass stayed inside documentation-stage scope:

- created only the 0.2.8 package documents.
- synchronized v0.2 status documentation for the new 0.2.8 review gate.
- did not create the contract deliverable under `docs/contracts/`.
- did not implement schema, runtime, API, frontend, fixture, migration, or
  test changes.

## Assumptions

- `docs/iterations/v0.2/README.md` is the milestone index referenced by the
  task.
- Updating `docs/iterations/v0.2/v0.2-plan.md` as well as the milestone index
  is required status synchronization.

## Unresolved Findings

- P1: none.
- P2: detailed v0.2 plan status still marks 0.2.7 as `ready for review`
  while the milestone index marks it `review complete`; this was identified
  by documentation review and deferred to 0.2.9.
- P3: none.

## Final Assessment

implementation complete; see implementation closeout above
