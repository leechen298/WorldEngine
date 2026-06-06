# Review

Chinese mirror: `review.zh.md`.

Status: implementation complete / verification passed

implementation_authorized: yes
provider_live_call_authorized: no
generated_result_creation_authorized: no
checker_execution_authorized: no
external_validation_authorized: no

## Changed Files

Documentation draft:

```text
docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/README.md
docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/README.zh.md
docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/intent.md
docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/intent.zh.md
docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/contract.md
docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/contract.zh.md
docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/technical-design.md
docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/technical-design.zh.md
docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/test-plan.md
docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/test-plan.zh.md
docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/plan.md
docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/plan.zh.md
docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/review.md
docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/review.zh.md
```

Runtime, schema, API, frontend, checker, fixture, generated-result, external
repository, and Validation Client files were not changed during documentation
drafting.

Current worktree note: the repository already contains pre-existing v0.9
backend/app implementation changes and earlier child-package files from this
goal state. The `0.9.9` documentation-stage scope in this review is limited to
the new `0.9.9` package documentation files listed above; it does not claim,
authorize, stage, or close any pre-existing non-`0.9.9` implementation
changes.

Implementation closeout:

```text
backend/app/schemas/external_projection.py
backend/app/core/external_projection.py
backend/app/api/routes/world.py
backend/app/api/app_factory.py
backend/app/tests/test_external_narrative_diagnostic_boundary.py
docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/README.md
docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/README.zh.md
docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/review.md
docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary/review.zh.md
docs/iterations/v0.9/CURRENT_STATE.md
docs/iterations/v0.9/CURRENT_STATE.zh.md
docs/iterations/v0.9/README.md
docs/iterations/v0.9/README.zh.md
docs/iterations/v0.9/CAMPAIGN_PLAN.md
docs/iterations/v0.9/CAMPAIGN_PLAN.zh.md
docs/iterations/v0.9/GOAL_RUNNER.md
docs/iterations/v0.9/GOAL_RUNNER.zh.md
docs/iterations/v0.9/review.md
docs/iterations/v0.9/review.zh.md
docs/iterations/v0.9/v0.9-plan.md
docs/iterations/v0.9/v0.9-plan.zh.md
```

## Commands Run

Documentation checks:

```text
git diff --check
```

Result: exit 0; no output.

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary"); expected={"README","intent","contract","technical-design","test-plan","plan","review"}; names={p.name for p in root.glob("*.md")}; missing=[]; [missing.append(f"{base}.md") for base in sorted(expected) if f"{base}.md" not in names]; [missing.append(f"{base}.zh.md") for base in sorted(expected) if f"{base}.zh.md" not in names]; print("files", len(names)); print("missing", missing); raise SystemExit(1 if missing else 0)'
```

Result: exit 0; `files 14`; `missing []`.

```text
rg -n "implementation_authorized(:|：) yes|provider_live_call_authorized(:|：) yes|generated_result_creation_authorized(:|：) yes|external_validation_authorized(:|：) yes|checker_execution_authorized(:|：) yes|Status(:|：).*implementation complete" docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary
```

Initial result before removing exact future-authorization wording from
`README.md`, `README.zh.md`, `plan.md`, and `plan.zh.md`: exit 0, matching
explanatory prose. After repair: exit 1; no output.

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary"); pairs=[("README.md","README.zh.md"),("intent.md","intent.zh.md"),("contract.md","contract.zh.md"),("technical-design.md","technical-design.zh.md"),("test-plan.md","test-plan.zh.md"),("plan.md","plan.zh.md"),("review.md","review.zh.md")]; missing=[str(root/x) for pair in pairs for x in pair if not (root/x).exists()]; bad=[]; [bad.append(str(root/b)+": missing mirrored status") for a,b in pairs if (root/a).exists() and (root/b).exists() and "Status:" in (root/a).read_text() and "Status：" not in (root/b).read_text()]; [bad.append(str(root/b)+": missing implementation authorization no") for a,b in pairs if (root/a).exists() and (root/b).exists() and "implementation_authorized: no" in (root/a).read_text() and "implementation_authorized: no" not in (root/b).read_text()]; print("missing", missing); print("bad", bad); raise SystemExit(1 if missing or bad else 0)'
```

Result: exit 0; `missing []`; `bad []`.

```text
rg -n "0\.9\.7 documentation gate complete|0\.9\.7.*implementation authorized|0\.9\.8.*Status: planned|0\.9\.8.*Status：planned|0\.9\.9.*Status: planned|0\.9\.9.*Status：planned|0\.9\.8-brain-inspired-agent-continuity-and-consolidation-evidence-implementation-authorized" docs/iterations/v0.9/v0.9-plan.md docs/iterations/v0.9/v0.9-plan.zh.md docs/iterations/v0.9/CURRENT_STATE.md docs/iterations/v0.9/CURRENT_STATE.zh.md docs/iterations/v0.9/README.md docs/iterations/v0.9/README.zh.md
```

Initial result before synchronizing parent `v0.9-plan.md` and
`v0.9-plan.zh.md`: exit 0, stale status matches. After repair: exit 1; no
output.

## Test Results

Documentation drafting did not run code tests because implementation was not
authorized at that stage.

Implementation closeout verification:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_external_narrative_diagnostic_boundary.py -q
```

Result: exit 0; `23 passed in 0.53s`.

```text
cd backend && .venv/bin/python -m pytest app/tests/test_external_narrative_diagnostic_boundary.py app/tests/test_agent_continuity_consolidation_evidence.py app/tests/test_event_api_compat.py app/tests/test_runtime_bounded_run.py app/tests/test_archive_snapshot_summary.py app/tests/test_public_handoff_contract_api.py app/tests/test_rule_linked_evolution_legality.py -q
```

Result: exit 0; `102 passed in 1.83s`.

```text
cd backend && .venv/bin/python -m pytest app/tests -q
```

Result: exit 0; `389 passed in 4.37s`.

```text
git diff --check
```

Result: exit 0; no output.

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary"); expected={"README","intent","contract","technical-design","test-plan","plan","review"}; names={p.name for p in root.glob("*.md")}; missing=[]; [missing.append(f"{base}.md") for base in sorted(expected) if f"{base}.md" not in names]; [missing.append(f"{base}.zh.md") for base in sorted(expected) if f"{base}.zh.md" not in names]; print("files", len(names)); print("missing", missing); raise SystemExit(1 if missing else 0)'
```

Result: exit 0; `files 14`; `missing []`.

## Compatibility Review

Draft contract requires additive compatibility with existing event, runtime,
snapshot/archive, world direction, rule-linked event legality, Agent
continuity, Agent memory, and public handoff surfaces.

Implementation compatibility review:

- Existing event, runtime, archive/snapshot, Agent continuity, and rule-linked
  legality response shapes remain additive-compatible.
- New projection and diagnostic endpoints are additive public surfaces.
- Accepted projection/diagnostic artifacts do not append canonical events,
  write Agent memory, mutate world state, or record in-world dialogue.
- Public event refs are checked against the event log; public snapshot refs
  are checked against the snapshot store.
- Agent continuity refs remain public type-only refs for this package and are
  prepared for later checker consumption.

## Scope Review

Draft scope is limited to future active-backend public narrative projection
and out-of-world diagnostic dialogue boundary evidence. Provider live calls,
generated-result creation, checker execution or fixture changes, external
validation, Validation Client changes, frontend UI, player-in-world chat,
narrative game content, diagnostic-to-memory bridges, durable scheduling, and
`backend/worldengine/` changes remain unauthorized.

Implementation scope review:

- Implementation stayed in `backend/app/` plus this package review/README and
  parent v0.9 route/status handoff docs.
- No `backend/worldengine/`, frontend, Validation Client, external
  repository, checker fixture, generated-result, durable scheduling,
  player-in-world chat, narrative game content, or diagnostic-to-memory bridge
  work was added.
- Live provider calls, generated-result creation, checker execution, and
  external validation were not run and remain unauthorized.

## Subagent Findings

Documentation/contract evaluator:

```text
agent: 019e9b28-a596-79f2-b414-6256cf0237e1
scope: read-only 0.9.9 documentation/contract/design/test-plan review
status: FAIL
```

Findings:

- P1: parent `v0.9-plan.md` and `v0.9-plan.zh.md` still carried stale
  `0.9.7` implementation-authorized and `0.9.8`/`0.9.9` planned statuses.
- P2: this review did not explicitly record that the dirty worktree contains
  pre-existing non-`0.9.9` backend implementation changes from earlier v0.9
  work.

Repairs:

- Synchronized parent `v0.9-plan.md` and `v0.9-plan.zh.md` to the current
  `0.9.8` complete / `0.9.9` documentation-review state.
- Added the current worktree note above to keep `0.9.9` documentation-stage
  scope distinct from pre-existing implementation changes.

Documentation/contract re-review:

```text
agent: 019e9b28-a596-79f2-b414-6256cf0237e1
scope: read-only 0.9.9 documentation/contract/design/test-plan re-review
status: PASS
```

Verdict: PASS with no P0/P1/P2/P3 findings. The evaluator recommended
authorizing only the active `0.9.9` implementation scope while keeping
provider live calls, generated-result creation, checker execution, external
validation, frontend, Validation Client, and `backend/worldengine/` work
unauthorized.

Implementation-scope evaluator:

```text
agent: 019e9b36-fdc3-73f0-97fc-d493a852612c
scope: read-only 0.9.9 implementation review
status: FAIL
```

Findings:

- P1: accepted projection/diagnostic artifacts could be source-less.
- P1: narrative or diagnostic text could claim canonical mutation while flags
  remained false.
- P1: HTTP validation redaction missed raw provider request/response variants.
- P2: schema-level private marker rejection was missing.
- P2: focused tests did not cover those negative cases.

Repairs:

- Projection and diagnostic helpers now require at least one public evidence
  ref.
- Helpers reject textual claims that canonical state was mutated, canonical
  events were appended, Agent memory was written, or in-world dialogue was
  recorded.
- External projection schemas now perform schema-level private marker
  rejection.
- HTTP validation-error sanitizer now redacts raw provider request/response
  marker variants.
- Focused tests now cover diagnostic extra fields, schema private marker
  validation, raw provider request loc redaction, empty refs, textual mutation
  claims, explicit canonical event append flags, and expanded marker variants.

Implementation re-review:

```text
agent: 019e9b36-fdc3-73f0-97fc-d493a852612c
scope: read-only 0.9.9 implementation re-review
status: PASS
```

Verdict: PASS with no P0/P1/P2/P3 findings. The evaluator reported that the
routes remain additive and non-mutating for projection/diagnostic surfaces,
accepted artifacts keep all canonical/event/memory/dialogue flags false, and
no frontend or `backend/worldengine/` changes were present in the scope check.

## Unresolved P1/P2/P3

- None after implementation repairs and closeout evidence update.

## Final Assessment

Implementation complete for the scoped active-backend `0.9.9` narrative
projection and diagnostic dialogue boundary work recorded in this package.

Final route:

```text
0.9.10-llm-backed-autonomous-checker-and-fixtures-documentation-package-needed
```
