# Review

Status: campaign ready / unverified restart

## FINAL_STATUS

route_status: CAMPAIGN_READY
evidence_status: unverified restart; prior `02` pass is archived evidence only
next_action: `/goal 完成 v0.2-post-closeout` starts full campaign at `01-e2e-validation-plan`
active_package: `01-e2e-validation-plan`
implementation_authorized: child_contract_controlled
blocking_findings: none for campaign restart routing
open_findings: `v0.2-post-closeout-P2-001`
last_verified_at: 2026-05-29
evidence_commit: archived only; current campaign evidence not yet produced
commands_run: documentation routing and adaptive workflow checks only in the current Goal Campaign updates; see package reviews for archived validation commands
commands_not_run: campaign execution; autonomous validation; final bundle synthesis; backend tests; API smoke; E2E

## Adaptive Child Workflow Update

Date: 2026-05-29

Changed files:

- `docs/iterations/AGENTS.md`, `docs/iterations/AGENTS.zh.md`: clarify that
  `GOAL_RUNNER.md` owns adaptive gate selection and risk-based gate order.
- `README.md`, `README.zh.md`: update the one-sentence goal interpretation so
  each child selects gates by child type, contract, and risk instead of
  following one fixed phase list.
- `GOAL_RUNNER.md`, `GOAL_RUNNER.zh.md`: replace the rigid child package cycle
  with an adaptive package cycle, package-shape gate selection, optional
  subagent / evaluator guidance, and verification escalation rules.
- `CAMPAIGN_PLAN.md`, `CAMPAIGN_PLAN.zh.md`: replace the fixed child cycle with
  workflow selection by planning, validation, implementation, autonomous
  validation, or final-bundle child type.
- `review.md`, `review.zh.md`: record this adaptive workflow update and
  closeout evidence.

Commands run for this adaptive workflow update:

```bash
git status --short --branch
git diff --name-only
git diff --check
rg -n "Adaptive Child|adaptive gate|risk-based|gate-selection|evaluator-review|verification-escalation|Workflow selection|Subagent|subagent|evaluator|P0 / P1|full child-package cycle" docs/iterations/v0.2-post-closeout/GOAL_RUNNER.md docs/iterations/v0.2-post-closeout/GOAL_RUNNER.zh.md docs/iterations/v0.2-post-closeout/CAMPAIGN_PLAN.md docs/iterations/v0.2-post-closeout/CAMPAIGN_PLAN.zh.md docs/iterations/v0.2-post-closeout/README.md docs/iterations/v0.2-post-closeout/README.zh.md docs/iterations/AGENTS.md docs/iterations/AGENTS.zh.md
rg -n "Child Package Cycle|Child Cycle|fixed phase list|rigid phase list|strongest cycle" docs/iterations/v0.2-post-closeout/GOAL_RUNNER.md docs/iterations/v0.2-post-closeout/GOAL_RUNNER.zh.md docs/iterations/v0.2-post-closeout/CAMPAIGN_PLAN.md docs/iterations/v0.2-post-closeout/CAMPAIGN_PLAN.zh.md
rg -n "[[:blank:]]$" AGENTS.md AGENTS.zh.md docs/iterations/AGENTS.md docs/iterations/AGENTS.zh.md docs/iterations/v0.2-post-closeout
for f in $(find docs/iterations/v0.2-post-closeout -type f -name '*.md' ! -name '*.zh.md' -print); do zh="${f%.md}.zh.md"; test -f "$zh" || echo "$f"; done
```

Results:

- `git diff --check` exited `0`.
- Adaptive workflow keyword search found the expected goal-runner, campaign
  plan, README, and iteration-AGENTS entries.
- Legacy-cycle wording search found only the intentional replacement headings
  and guard wording that says not to run a fixed / rigid phase list blindly.
- Trailing-whitespace search exited `1` with no output.
- English / Chinese mirror loop exited `0` and printed only the pre-existing
  `docs/iterations/v0.2-post-closeout/findings.md`, which has no mirror by
  existing package convention.
- `git status --short --branch` still shows the pre-existing untracked
  `docs/iterations/v0.2-post-closeout.zip`. It also shows the new
  `CAMPAIGN_PLAN.md` and `CAMPAIGN_PLAN.zh.md`, which are in-scope campaign
  routing docs and are listed in this review.
- Backend tests, API smoke, E2E, autonomous validation, and final bundle
  synthesis were not run because this update only changes routing documents.

## Goal Campaign Restart Update

Date: 2026-05-29

Changed files:

- `AGENTS.md`, `AGENTS.zh.md`: add package-discovery guidance for `完成
  <iteration-package>` goals.
- `docs/iterations/AGENTS.md`, `docs/iterations/AGENTS.zh.md`: add the Codex
  Goal Campaign standard and file ownership model.
- `README.md`, `README.zh.md`: add `Goal Entry`, reset the package to
  `campaign ready / unverified restart`, and point one-sentence goals to
  `GOAL_RUNNER.md`, `CURRENT_STATE.md`, and `CAMPAIGN_PLAN.md`.
- `CURRENT_STATE.md`, `CURRENT_STATE.zh.md`: reset active child routing to
  `01-e2e-validation-plan` and mark prior pass evidence as archived only.
- `CAMPAIGN_PLAN.md`, `CAMPAIGN_PLAN.zh.md`: add the full campaign child
  sequence, child cycle, implementation authorization rule, exit criteria, and
  hard stops.
- `GOAL_RUNNER.md`, `GOAL_RUNNER.zh.md`: convert from one-package validation
  routing into a full campaign state machine with child cycles, review loops,
  implementation authorization, repair loops, and closeout gates.
- `validation-master-plan.md`, `validation-master-plan.zh.md`: align current
  route snapshot and default route with the campaign restart.
- child package `review.md` / `review.zh.md` files: mark earlier statuses as
  restart-ready, archived-only, or not executed in the current campaign.
- child package README / status files, especially
  `02-e2e-validation-execution/{intent,contract,execution-plan,e2e-validation-report}.md`
  and mirrors: mark 2026-05-29 pass evidence as archived rather than current
  campaign completion evidence.

Commands run for this campaign routing update:

```bash
git status --short
git diff --name-only
git diff --check
test -f docs/iterations/v0.2-post-closeout/CAMPAIGN_PLAN.md
test -f docs/iterations/v0.2-post-closeout/CAMPAIGN_PLAN.zh.md
rg -n "Goal Entry|完成 v0\\.2-post-closeout|CAMPAIGN_PLAN|full campaign|campaign ready|unverified_restart|RESTART_READY|NOT_EXECUTED_CURRENT_CAMPAIGN|ARCHIVED_EVIDENCE_ONLY|implementation_authorized|Closeout Consistency Gate" docs/iterations/v0.2-post-closeout AGENTS.md AGENTS.zh.md docs/iterations/AGENTS.md docs/iterations/AGENTS.zh.md
for f in $(find docs/iterations/v0.2-post-closeout -type f -name '*.md' ! -name '*.zh.md' -print); do zh="${f%.md}.zh.md"; test -f "$zh" || echo "$f"; done
rg -n '[[:blank:]]$' AGENTS.md AGENTS.zh.md docs/iterations/AGENTS.md docs/iterations/AGENTS.zh.md docs/iterations/v0.2-post-closeout
```

Results:

- `git diff --check` exited `0`.
- `CAMPAIGN_PLAN.md` and `CAMPAIGN_PLAN.zh.md` existence checks exited `0`.
- Campaign keyword search found the expected goal entry, state-machine,
  restart, archived-evidence, implementation authorization, and closeout gate
  terms.
- English / Chinese mirror loop exited `0` and printed only the pre-existing
  `docs/iterations/v0.2-post-closeout/findings.md`, which has no mirror by
  existing package convention.
- Trailing-whitespace search exited `1` with no output.
- `git status --short` also shows the pre-existing untracked
  `docs/iterations/v0.2-post-closeout.zip`; this file was not modified by this
  campaign update and is not part of the tracked diff.

## Goal Runner Routing Update

Date: 2026-05-29

Changed files:

- `CURRENT_STATE.md`, `CURRENT_STATE.zh.md`: add the current one-package
  routing snapshot for `/goal`.
- `GOAL_RUNNER.md`, `GOAL_RUNNER.zh.md`: add `/goal` execution modes, route
  statuses, hard stops, and per-package closeout rules.
- `README.md`, `README.zh.md`: replace the stale documentation-only opening
  with the current routing note and add the new routing deliverables.
- `validation-master-plan.md`, `validation-master-plan.zh.md`: add the current
  routing snapshot and default next route.
- `review.md`, `review.zh.md`, and child package `review.md` / `review.zh.md`
  files: add `FINAL_STATUS` blocks.

Commands run for this routing update:

```bash
git diff --check
rg -n "GOAL_RUNNER|CURRENT_STATE|FINAL_STATUS|PACKAGE_COMPLETE|NEEDS_USER_INPUT|NOT_EXECUTED|BLOCKED|FAILED" docs/iterations/v0.2-post-closeout
rg -n "do not modify implementation|does not reopen v0.2|not executed|passed|blocked|failed|v0.4" docs/iterations/v0.2-post-closeout
git diff --name-only
test -f docs/iterations/v0.2-post-closeout/CURRENT_STATE.md
test -f docs/iterations/v0.2-post-closeout/CURRENT_STATE.zh.md
test -f docs/iterations/v0.2-post-closeout/GOAL_RUNNER.md
test -f docs/iterations/v0.2-post-closeout/GOAL_RUNNER.zh.md
git status --short --branch
```

Results:

- `git diff --check` exited `0`.
- Required routing file existence checks exited `0`.
- Routing keyword search found the expected current-state, runner, and
  `FINAL_STATUS` entries.
- Status / scope wording search found the expected validation status and guard
  terms.
- No runtime, schema, API, frontend, backend test, fixture, migration, or
  external repository file was modified by this routing update.
- Backend tests, API smoke, E2E, autonomous validation, and final bundle
  synthesis were not run because this update only organizes validation routing
  documents.

## Changed Files

| File | Change |
|---|---|
| `docs/validation/README.md`, `README.zh.md` | Removed the obsolete validation index files after moving the package under `docs/iterations/`. |
| `docs/iterations/v0.2-post-closeout/README.md`, `README.zh.md` | Added package overview, scope, status, deliverables, and mirror. |
| `docs/iterations/v0.2-post-closeout/validation-master-plan.md`, `.zh.md` | Added master validation control plan and mirror. |
| `docs/iterations/v0.2-post-closeout/validation-report-template.md`, `.zh.md` | Added post-closeout report template and mirror. |
| `docs/iterations/v0.2-post-closeout/01-e2e-validation-plan/**` | Added E2E / integration / API smoke planning package with mirrors. |
| `docs/iterations/v0.2-post-closeout/02-e2e-validation-execution/**` | Added execution template package with mirrors. |
| `docs/iterations/v0.2-post-closeout/03-codex-autonomous-validation-plan/**` | Added Codex autonomous validation planning package with mirrors. |
| `docs/iterations/v0.2-post-closeout/04-codex-autonomous-validation-execution/**` | Added Codex autonomous execution template package with mirrors. |
| `docs/iterations/v0.2-post-closeout/05-final-validation-bundle/**` | Added final validation bundle template package with mirrors. |
| `docs/iterations/v0.2-post-closeout/review.md`, `.zh.md` | Added top-level package review evidence and mirror. |

## Commands Run

```bash
git status --short --branch
git diff --check
test -f docs/iterations/v0.2-post-closeout/README.md
test -f docs/iterations/v0.2-post-closeout/README.zh.md
test -f docs/iterations/v0.2-post-closeout/validation-master-plan.md
test -f docs/iterations/v0.2-post-closeout/validation-master-plan.zh.md
test -f docs/iterations/v0.2-post-closeout/01-e2e-validation-plan/test-plan.md
test -f docs/iterations/v0.2-post-closeout/01-e2e-validation-plan/test-plan.zh.md
test -f docs/iterations/v0.2-post-closeout/03-codex-autonomous-validation-plan/test-plan.md
test -f docs/iterations/v0.2-post-closeout/03-codex-autonomous-validation-plan/test-plan.zh.md
test -f docs/iterations/v0.2-post-closeout/05-final-validation-bundle/final-validation-bundle.md
test -f docs/iterations/v0.2-post-closeout/05-final-validation-bundle/final-validation-bundle.zh.md
test ! -e docs/validation
rg -n -e 'E2E pas''sed' -e 'Codex autonomous validation pas''sed' -e 'v0.2 revali''dated' -e 'Status: pas''sed' -e 'final assessment: pas''sed' docs/iterations/v0.2-post-closeout
rg -n -e 'v0\.3-lco''al' -e 'v0\.3-loc''al' -e 'Observed bra''nch' docs/iterations/v0.2-post-closeout
find docs/iterations/v0.2-post-closeout -type f -name '*.md' ! -name '*.zh.md' -print | while read -r f; do zh="${f%.md}.zh.md"; test -f "$zh" || echo "$f"; done
rg -n '[[:blank:]]$' docs/iterations/v0.2-post-closeout
rg -n 'docs/validation/v0\.2-post-closeout' docs/iterations/v0.2-post-closeout
rg -n -e 'live under `docs/vali''dation/`' -e '位于 `docs/vali''dation/`' docs/iterations/v0.2-post-closeout
git status --porcelain=v1 -uall | rg -v '^( M docs/iterations/AGENTS(\.zh)?\.md|\?\? docs/iterations/v0\.2-post-closeout/)'
```

## Test Results

- `git diff --check` exited `0`.
- Required English and Chinese file checks exited `0`.
- Removed validation index directory check exited `0`.
- Forbidden success wording search exited `1` with no output.
- Hardcoded observed branch search exited `1` with no output.
- English / Chinese mirror presence loop exited `0` with no output.
- Trailing-whitespace search exited `1` with no output.
- Stale old package path search exited `1` with no output.
- Stale `docs/validation/` governance wording search exited `1` with no
  output.
- Changed-file scope guard exited `1` with no output after allowing the
  separately modified `docs/iterations/AGENTS*` rule files and this package.
- Backend, frontend, E2E, API smoke, runtime, schema execution, fixture, and
  migration checks were not run because this is a documentation-only package.

## Compatibility Review

No runtime, schema, API, frontend, backend test, fixture, migration, or legacy
path behavior changed.

## Scope Review

This package creates post-closeout validation planning and templates only. It
does not reopen v0.2, does not change v0.2 final / complete status, and does
not claim independent validation has run.

The active package location is `docs/iterations/v0.2-post-closeout/`. The
obsolete `docs/validation/` index files were removed so the package has a
single iteration-docs entrypoint.

The working tree also contains separately modified `docs/iterations/AGENTS.md`
and `docs/iterations/AGENTS.zh.md` rule files. This package consumes those
rules but does not modify them.

## Unresolved P1/P2/P3

- P1: none.
- P2: none.
- P3: none.

## Final Assessment

Ready for human / ChatGPT review.
