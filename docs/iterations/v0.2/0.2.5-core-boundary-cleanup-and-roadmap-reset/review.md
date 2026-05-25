# Review

Status: review complete

## Changed Files

| File | Change |
|---|---|
| `AGENTS.md`, `AGENTS.zh.md` | Replaced concrete projection wording with external consumer boundaries and added hard rules for generic core scope. |
| `CLAUDE.md`, `CLAUDE.zh.md` | Mirrored the agent guidance cleanup for the existing Claude entry files. |
| `README.md`, `README.zh.md` | Removed the concrete reference-world limitation and described external projection applications as consumers. |
| `docs/project-north-star.md`, `docs/project-north-star.zh.md` | Replaced first concrete user-surface wording with external projection application guidance. |
| `docs/product-model.md`, `docs/product-model.zh.md` | Removed concrete product-surface wording and kept product surfaces as public consumers. |
| `docs/scope-boundaries.md`, `docs/scope-boundaries.zh.md` | Added explicit core-vs-external fixture and validation boundaries. |
| `docs/roadmap.md`, `docs/roadmap.zh.md` | Reset v0.2.5 through v0.8 around generic engine and external consumer milestones. |
| `docs/architecture.md`, `docs/architecture.zh.md` | Replaced concrete fixture direction with generic schema smoke validation. |
| `docs/glossary.md`, `docs/glossary.zh.md` | Replaced concrete reference-world vocabulary with external validation world and projection consumer terms. |
| `docs/releases/v0.2.md`, `docs/releases/v0.2.zh.md` | Updated planned capability and non-goal wording for generic schema smoke and external boundaries. |
| `docs/iterations/v0.2/README.md`, `docs/iterations/v0.2/README.zh.md` | Marked 0.2.4 as historical and 0.2.5 as review complete. |
| `docs/iterations/v0.2/v0.2-plan.md`, `docs/iterations/v0.2/v0.2-plan.zh.md` | Replaced legacy fixture direction with 0.2.5 cleanup and 0.2.6 generic closeout planning. |
| `docs/iterations/v0.2/0.2.4-worldspec-reference-fixture/README.md`, `README.zh.md` | Added historical artifact notes that supersede the concrete fixture direction. |
| `docs/iterations/v0.2/0.2.5-core-boundary-cleanup-and-roadmap-reset/README.md` | Synchronized status and checklist to review complete. |
| `backend/data/world_specs/tiny_village.world.json` | Deleted the concrete external-world fixture. |
| `backend/app/tests/test_worldspec_fixture.py` | Deleted the concrete fixture test. |
| `backend/app/tests/test_worldspec_schema_smoke.py` | Added domain-neutral in-memory WorldSpec schema smoke tests. |
| `backend/app/tests/test_world_cell_schema.py` | Replaced a concrete invalid `kind` value with a domain-neutral invalid value. |
| `docs/external-fixture-boundary.md` | Added the external fixture and validation consumer boundary guide. |
| `docs/validation-report-template.md` | Added a redacted validation report template using `redacted target id`. |
| `docs/iterations/v0.2/0.2.5-core-boundary-cleanup-and-roadmap-reset/review.md` | Recorded implementation closeout evidence. |
| `docs/current-implementation.md`, `docs/current-implementation.zh.md` | Follow-up docs polish replaced the stale `game surface` limitation with external projection application consumer wording. |
| `docs/iterations/v0.2/0.2.5-core-boundary-cleanup-and-roadmap-reset/README.md` | Follow-up docs polish clarified that the planning-only scope text describes the initial pass and that implementation closeout evidence is in this review. |

## Commands Run

```bash
git status --short --branch
sed -n '1,220p' docs/iterations/v0.2/0.2.5-core-boundary-cleanup-and-roadmap-reset/README.md
sed -n '1,220p' docs/iterations/v0.2/0.2.5-core-boundary-cleanup-and-roadmap-reset/intent.md
sed -n '1,260p' docs/iterations/v0.2/0.2.5-core-boundary-cleanup-and-roadmap-reset/contract.md
sed -n '1,240p' docs/iterations/v0.2/0.2.5-core-boundary-cleanup-and-roadmap-reset/technical-design.md
sed -n '1,220p' docs/iterations/v0.2/0.2.5-core-boundary-cleanup-and-roadmap-reset/test-plan.md
sed -n '1,220p' docs/iterations/v0.2/0.2.5-core-boundary-cleanup-and-roadmap-reset/plan.md
sed -n '1,220p' docs/iterations/v0.2/0.2.5-core-boundary-cleanup-and-roadmap-reset/review.md
rg -n "tiny|Tiny|tiny_village|village|Village|village-like|reference village|Reference Village World|reference world|first game surface|electronic-pet|electronic pet|workshop|square|notice-board|workbench|villager" .
rg -n "tiny|Tiny|tiny_village|village|Village|village-like|reference village|Reference Village World|reference world|first game surface|electronic-pet|electronic pet|workshop|square|notice-board|workbench|villager" AGENTS.md AGENTS.zh.md CLAUDE.md CLAUDE.zh.md README.md README.zh.md docs/project-north-star.md docs/project-north-star.zh.md docs/product-model.md docs/product-model.zh.md docs/scope-boundaries.md docs/scope-boundaries.zh.md docs/roadmap.md docs/roadmap.zh.md docs/architecture.md docs/architecture.zh.md docs/glossary.md docs/glossary.zh.md docs/releases/v0.2.md docs/releases/v0.2.zh.md docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md backend/app/tests backend/data
git diff --check
make check-backend
cd backend && .venv/bin/python -m pytest app/tests/test_worldspec_schema_smoke.py -q
cd backend && .venv/bin/python -m pytest app/tests -q
git diff --name-status
git diff --stat
git status --short --branch
rg -n "No game surface|还没有 game surface|This documentation-planning pass creates only this iteration package" docs/current-implementation.md docs/current-implementation.zh.md docs/iterations/v0.2/0.2.5-core-boundary-cleanup-and-roadmap-reset/README.md
git diff --check
```

## Test Results

- `git diff --check` exited `0`; no whitespace errors.
- `make check-backend` exited `0`; backend virtual environment exists.
- `cd backend && .venv/bin/python -m pytest app/tests/test_worldspec_schema_smoke.py -q`
  exited `0`; result: `4 passed in 0.08s`.
- `cd backend && .venv/bin/python -m pytest app/tests -q` exited `0`; result:
  `91 passed in 0.94s`.
- Frontend tests were not run because this package did not modify frontend
  files and the contract forbids frontend dashboard changes.
- Follow-up docs polish: `git diff --check` exited `0`; the targeted stale-text
  grep for `No game surface`, `还没有 game surface`, and the obsolete
  planning-only Scope sentence exited with no matches.

## Grep Residuals

Full repository grep still reports allowed residuals in these categories:

- Dependency false positives: `frontend/pnpm-lock.yaml` package names such as
  `tinybench`, `tinyexec`, `tinypool`, `tinyrainbow`, `tinyspy`, and
  `@ctrl/tinycolor`.
- Historical release artifacts: `docs/releases/v0.1.md` and
  `docs/releases/v0.1.zh.md`.
- Historical iteration artifacts and review evidence:
  `docs/iterations/v0.1/**`, `docs/iterations/v0.2/0.2.1-*`,
  `docs/iterations/v0.2/0.2.2-*`, `docs/iterations/v0.2/0.2.3-*`, and
  `docs/iterations/v0.2/0.2.4-worldspec-reference-fixture/**`.
- 0.2.5 cleanup-scope mentions:
  `docs/iterations/v0.2/0.2.5-core-boundary-cleanup-and-roadmap-reset/**`.

The targeted active-docs/tests/fixtures grep over `AGENTS*`, `CLAUDE*`,
`README*`, current project direction docs, v0.2 active index/plan docs,
`backend/app/tests`, and `backend/data` exited with no matches. Active docs,
active tests, and active fixtures no longer retain concrete Demo-world
semantic anchors.

## Compatibility Review

Generic schema contracts are preserved. `WorldCell`, `WorldSpec`, `EntityRef`,
and `EventRef` were not deleted or narrowed. Runtime behavior, API routes,
API response shapes, production event log storage, frontend dashboard behavior,
and `backend/worldengine/` behavior were not changed.

The test cleanup removes concrete fixture data and replaces concrete fixture
assertions with in-memory, domain-neutral schema smoke coverage. No production
WorldSpec loader was added.

## Scope Review

Implementation stayed inside the 0.2.5 contract:

- cleaned active documentation anchors.
- reset active roadmap language.
- marked 0.2.4 as historical in the package README files.
- deleted concrete fixture data.
- replaced concrete fixture tests with generic schema smoke tests.
- added external fixture and redacted validation report docs.
- updated this review evidence.

No external fixture repository, external validation repository, loader, runtime
bridge, Agent loop, memory/self-continuity implementation, world generation,
frontend work, API work, event storage change, generic schema deletion, or new
concrete world was introduced.

## Unresolved Findings

- P1: none.
- P2: none. The follow-up docs polish resolved the stale
  `docs/current-implementation*` wording and the 0.2.5 README planning-pass
  wording.
- P3: none.

## Final Assessment

0.2.5 implementation is review complete. The WorldEngine core repository no
longer has active concrete Demo-world anchors in current docs, tests, or
fixtures; the roadmap is reset around generic engine and external consumer
milestones; and the focused and full backend tests pass in the current session.
