# Review

Chinese mirror: `review.zh.md`.

Status: reviewed / ready for implementation

implementation_authorized: yes
provider_live_call_authorized: no
generated_result_creation_authorized: no
checker_execution_authorized: no
external_validation_authorized: no

## Changed Files

Documentation draft:

```text
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/README.md
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/README.zh.md
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/intent.md
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/intent.zh.md
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/contract.md
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/contract.zh.md
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/technical-design.md
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/technical-design.zh.md
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/test-plan.md
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/test-plan.zh.md
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/plan.md
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/plan.zh.md
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/review.md
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/review.zh.md
```

Runtime, schema, API, frontend, checker, fixture, generated-result, external
repository, and Validation Client files were not changed during documentation
drafting.

## Commands Run

Documentation checks:

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality"); expected={"README","intent","contract","technical-design","test-plan","plan","review"}; names={p.name for p in root.glob("*.md")}; missing=[]; [missing.append(f"{base}.md") for base in sorted(expected) if f"{base}.md" not in names]; [missing.append(f"{base}.zh.md") for base in sorted(expected) if f"{base}.zh.md" not in names]; print("files", len(names)); print("missing", missing); raise SystemExit(1 if missing else 0)'
```

Result: exit 0; `files 14`; `missing []`.

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality"); pairs=[("README.md","README.zh.md"),("intent.md","intent.zh.md"),("contract.md","contract.zh.md"),("technical-design.md","technical-design.zh.md"),("test-plan.md","test-plan.zh.md"),("plan.md","plan.zh.md"),("review.md","review.zh.md")]; missing=[str(root/x) for pair in pairs for x in pair if not (root/x).exists()]; bad=[]; [bad.append(str(root/b)+": missing mirrored status") for a,b in pairs if (root/a).exists() and (root/b).exists() and "Status:" in (root/a).read_text() and "Status：" not in (root/b).read_text()]; [bad.append(str(root/b)+": missing implementation authorization no") for a,b in pairs if (root/a).exists() and (root/b).exists() and "implementation_authorized: no" in (root/a).read_text() and "implementation_authorized: no" not in (root/b).read_text()]; print("missing", missing); print("bad", bad); raise SystemExit(1 if missing or bad else 0)'
```

Result: exit 0; `missing []`; `bad []`.

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality"); combined="\n".join(path.read_text() for path in root.glob("*.md")); required=["implementation_authorized: no","provider_live_call_authorized: no","generated_result_creation_authorized: no","checker_execution_authorized: no","external_validation_authorized: no","WorldEventCandidate","WorldEventLegalityResult","WorldStateDiff","WorldEvolutionEvidence","direction-biased","/world/event-steps","/world/params","0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence"]; missing=[term for term in required if term not in combined]; print("missing", missing); raise SystemExit(1 if missing else 0)'
```

Initial result before adding the exact handoff id: exit 1;
`missing ['0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence']`.
After repair: exit 0; `missing []`.

```text
rg -n "implementation_authorized(:|：) yes|provider_live_call_authorized(:|：) yes|generated_result_creation_authorized(:|：) yes|external_validation_authorized(:|：) yes|checker_execution_authorized(:|：) yes|Status(:|：).*implementation complete" docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality
```

Initial result before removing future exact authorization strings: exit 0,
matching future-authorization prose in `README.md`, `README.zh.md`,
`plan.md`, and `plan.zh.md`. After repair: exit 1, no output. No premature
implementation, live provider, generated-result, checker, or external
authorization remains in the draft.

```text
git diff --check
```

Result: exit 0, no output.

Post-review Chinese mirror repair checks:

```text
rg -n --glob '*.zh.md' --glob '!**/review*.md' "public generated|deterministic public|Implementation 必须|accepted parameter changes|legal event acceptance|illegal event rejection|focused backend/API tests|active backend scope|existing public|mostly English|documentation package drafting" docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality
```

Result after Chinese mirror rewrite: exit 1, no output.

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality"); pairs=[("README.md","README.zh.md"),("intent.md","intent.zh.md"),("contract.md","contract.zh.md"),("technical-design.md","technical-design.zh.md"),("test-plan.md","test-plan.zh.md"),("plan.md","plan.zh.md"),("review.md","review.zh.md")]; missing=[str(root/x) for pair in pairs for x in pair if not (root/x).exists()]; bad=[]; [bad.append(str(root/b)+": missing mirrored status") for a,b in pairs if (root/a).exists() and (root/b).exists() and "Status:" in (root/a).read_text() and "Status：" not in (root/b).read_text()]; [bad.append(str(root/b)+": missing implementation authorization no") for a,b in pairs if (root/a).exists() and (root/b).exists() and "implementation_authorized: no" in (root/a).read_text() and "implementation_authorized: no" not in (root/b).read_text()]; print("missing", missing); print("bad", bad); raise SystemExit(1 if missing or bad else 0)'
```

Result after Chinese mirror rewrite: exit 0; `missing []`; `bad []`.

```text
git diff --check
```

Result after Chinese mirror rewrite: exit 0, no output.

P3 terminology repair checks:

```text
rg -n "红action" docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality
```

Result after repair: exit 1, no output.

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality"); pairs=[("README.md","README.zh.md"),("intent.md","intent.zh.md"),("contract.md","contract.zh.md"),("technical-design.md","technical-design.zh.md"),("test-plan.md","test-plan.zh.md"),("plan.md","plan.zh.md"),("review.md","review.zh.md")]; missing=[str(root/x) for pair in pairs for x in pair if not (root/x).exists()]; bad=[]; [bad.append(str(root/b)+": missing mirrored status") for a,b in pairs if (root/a).exists() and (root/b).exists() and "Status:" in (root/a).read_text() and "Status：" not in (root/b).read_text()]; [bad.append(str(root/b)+": missing implementation authorization no") for a,b in pairs if (root/a).exists() and (root/b).exists() and "implementation_authorized: no" in (root/a).read_text() and "implementation_authorized: no" not in (root/b).read_text()]; print("missing", missing); print("bad", bad); raise SystemExit(1 if missing or bad else 0)'
```

Result before implementation authorization update: exit 0; `missing []`;
`bad []`.

```text
rg -n --glob '*.zh.md' --glob '!**/review*.md' "public generated|deterministic public|Implementation 必须|accepted parameter changes|legal event acceptance|illegal event rejection|focused backend/API tests|active backend scope|existing public|mostly English|documentation package drafting|红action" docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality
```

Result after repair: exit 1, no output.

```text
git diff --check
```

Result after repair: exit 0, no output.

## Test Results

Code tests were not run during documentation drafting because implementation
is not authorized yet.

## Compatibility Review

Draft contract requires additive compatibility with existing event, runtime,
generated rule/parameter, world direction, director-guidance, and public
handoff surfaces.

## Scope Review

Draft scope is limited to future active-backend deterministic rule-linked
event legality and state-diff evidence. Provider live calls,
generated-result creation, checker execution or fixture changes, external
validation, Validation Client changes, frontend UI, Agent continuity,
narrative projection, diagnostic dialogue, durable scheduling, and
`backend/worldengine/` changes remain unauthorized.

## Subagent Findings

Requirements extraction subagent:

```text
agent: 019e9944-7117-7bf0-98e6-2d8da75f529e
scope: read-only 0.9.7 requirements extraction
status: complete
```

The subagent confirmed the active route, required file set, and core links to
`0.9.3`, `0.9.5`, `0.9.6`, and existing public event surfaces. It flagged
risks that this draft addresses:

- checker support must be limited to public artifact shape because checker
  execution and fixtures belong to later packages.
- legality must be based on public rule/state evidence, not hidden prose
  adjudication.
- accepted state mutation must have public diff/replay evidence.
- direction must not bypass rules into direct final facts or Agent private
  mutation.
- tests must include event, runtime, direction, world-param, and snapshot
  compatibility.

Initial documentation/contract evaluator:

```text
agent: 019e994d-2433-7433-8942-8a83dbc9aa0b
scope: read-only 0.9.7 documentation/contract review
status: FAIL
```

Verdict: FAIL for clean documentation/contract approval with one P2.

- P2: Chinese mirrors were semantically aligned but were too mixed-English for
  the Chinese mirror quality rule in `docs/iterations/AGENTS.md`.

Local repair rewrote Chinese mirrors into natural Chinese prose while
preserving technical identifiers, API routes, field names, status values, and
authorization semantics.

Documentation/contract re-review:

```text
agent: 019e994d-2433-7433-8942-8a83dbc9aa0b
scope: read-only 0.9.7 documentation/contract re-review
status: PASS
```

Verdict: PASS with no P0/P1/P2 findings. The evaluator noted one non-blocking
P3 for the unnatural Chinese term `红action`; local repair replaced it with
natural Chinese `脱敏`.

## Unresolved P1/P2/P3

- None.

## Final Assessment

Documentation gate complete. Implementation is authorized only for the scoped
active-backend `0.9.7` rule-linked evolution and event-legality work recorded
in this package.

Provider live calls, generated-result creation, checker execution or fixture
changes, external validation, Validation Client changes, frontend UI, Agent
continuity, narrative projection, diagnostic dialogue, durable scheduling, and
`backend/worldengine/` changes remain unauthorized.

## Implementation Closeout Update

Status: implementation complete / verification passed

### Changed Files

Scoped `0.9.7` implementation changed or added:

```text
backend/app/api/app_factory.py
backend/app/api/routes/world.py
backend/app/core/rule_linked_evolution.py
backend/app/schemas/world_evolution.py
backend/app/tests/test_rule_linked_evolution_legality.py
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/README.md
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/README.zh.md
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/review.md
docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality/review.zh.md
```

Other v0.9 files are already modified in the current worktree from earlier
v0.9 child work and are not claimed as new `0.9.7` implementation changes
except where parent route/status handoff is updated after this closeout.

### Implementation Summary

- Added `WorldEventCandidate`, `WorldParameterPatch`,
  `WorldEventLegalityResult`, `WorldEventLegalityDiagnostic`,
  `WorldStateDiff`, `WorldEvolutionEvidence`, and API request/response
  schemas with `extra="forbid"`.
- Added deterministic rule-linked legality evaluation over
  `GeneratedRuleParameterSet`, current public params, runtime tick/world time,
  constraints, probability evidence, causality evidence, public cause refs,
  and optional queued direction refs.
- Added additive public endpoint
  `POST /worlds/{world_id}/evolution/evaluate-event` and manifest exposure.
- Accepted apply requests update only public in-memory `WorldState` parameter
  paths covered by the accepted diff and append `world.evolution.accepted`
  with public replay/evolution evidence.
- Rejected candidates return public diagnostics and do not append accepted
  events or mutate public state.
- Extended validation-error redaction so private marker field names such as
  `private_goal` are redacted from public HTTP validation errors.

### Commands Run

```text
cd backend && .venv/bin/python -m pytest app/tests/test_rule_linked_evolution_legality.py -q
```

Initial implementation result: exit 0; `17 passed in 0.52s`.

After implementation-scope evaluator findings were repaired:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_rule_linked_evolution_legality.py -q
```

Result: exit 0; `19 passed in 0.50s`.

```text
cd backend && .venv/bin/python -m pytest app/tests/test_rule_linked_evolution_legality.py app/tests/test_world_rule_parameter_schema.py app/tests/test_world_direction_boundary.py app/tests/test_runtime_bounded_run.py app/tests/test_public_handoff_contract_api.py app/tests/test_world_params.py app/tests/test_event_api_compat.py app/tests/test_archive_snapshot_summary.py -q
```

Initial related regression result: exit 0; `83 passed in 1.36s`.

After evaluator repair:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_rule_linked_evolution_legality.py app/tests/test_world_rule_parameter_schema.py app/tests/test_world_direction_boundary.py app/tests/test_runtime_bounded_run.py app/tests/test_public_handoff_contract_api.py app/tests/test_world_params.py app/tests/test_event_api_compat.py app/tests/test_archive_snapshot_summary.py -q
```

Result: exit 0; `85 passed in 1.36s`.

```text
cd backend && .venv/bin/python -m pytest app/tests -q
```

Initial backend regression result: exit 0; `334 passed in 3.35s`.

After evaluator repair:

```text
cd backend && .venv/bin/python -m pytest app/tests -q
```

Result: exit 0; `336 passed in 3.31s`.

```text
git diff --check
```

Result: exit 0; no output.

Package file check:

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality"); expected={"README","intent","contract","technical-design","test-plan","plan","review"}; names={p.name for p in root.glob("*.md")}; missing=[]; [missing.append(f"{base}.md") for base in sorted(expected) if f"{base}.md" not in names]; [missing.append(f"{base}.zh.md") for base in sorted(expected) if f"{base}.zh.md" not in names]; print("files", len(names)); print("missing", missing); raise SystemExit(1 if missing else 0)'
```

Result: exit 0; `files 14`; `missing []`.

Unauthorized authorization scan:

```text
rg -n "provider_live_call_authorized(:|：) yes|generated_result_creation_authorized(:|：) yes|external_validation_authorized(:|：) yes|checker_execution_authorized(:|：) yes" docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality
```

Result: exit 1; no output.

### Implementation-Scope Evaluator

First implementation evaluator:

```text
agent: 019e9acb-95eb-7481-947e-0ac6604b4490
scope: read-only 0.9.7 implementation review
status: FAIL
```

Findings:

- P1: direct-final and Agent-private mutation checks did not scan all
  candidate surfaces, including refs, probability/causality evidence, and
  patch values.
- P1: package `review.md` and `review.zh.md` still contained only
  documentation-stage evidence and did not close the implementation contract.
- P2: HTTP validation redaction still echoed private extra-field names such as
  `private_goal` in validation-error `loc`.

Repairs:

- `_direct_final_fact_diagnostics` now recursively scans the full public
  candidate structure returned by `candidate.model_dump()`.
- focused tests now cover direct-final/private-state markers hidden in
  probability evidence, causality evidence, and patch values.
- `_PRIVATE_VALIDATION_MARKERS` now includes underscore variants including
  `private_goal`, `private_memory`, `private_prompt`, and
  `private_evaluator_data`.
- focused tests now cover private extra-field names in HTTP validation errors.
- implementation closeout evidence is recorded in this section.

Final implementation evaluator:

```text
agent: 019e9acb-95eb-7481-947e-0ac6604b4490
scope: read-only 0.9.7 implementation re-review
status: PASS
```

Verdict: PASS with no P0/P1/P2 findings. The evaluator reported one
non-blocking P3 because this review still contained a pending final re-review
placeholder before this update.

### Compatibility Review

- Existing `/world/events` and `/world/event-steps` response shapes remain
  compatible; `Event` required fields were not changed and empty `refs`
  serialization remains unchanged.
- Existing `/world/params` and `/world/params/apply` behavior remains
  compatible; `0.9.7` does not reuse `/world/params/apply` as an event
  legality entrypoint.
- Existing runtime bounded-run, world direction, generated rule/parameter,
  public manifest, snapshot/archive, and event API compatibility suites pass.
- Generated rule/parameter schemas do not grant runtime writable paths by
  themselves; `0.9.7` evaluates rule-linked public paths per request and
  applies only accepted diff-covered public parameter patches.

### Scope Review

No live provider calls, generated-result creation, checker execution,
checker fixture changes, external validation, Validation Client changes,
frontend UI changes, Agent continuity, narrative projection, diagnostic
dialogue, durable scheduling, deployment infrastructure, or
`backend/worldengine/` changes were made for this package.

### Unresolved P1/P2/P3

- None.

### Final Route

Implementation complete. Handoff goes to
`0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence`
documentation-package creation/review. Evidence execution, live provider
calls, generated-result creation, checker execution, external validation,
Agent continuity implementation, frontend UI, durable scheduling,
Validation Client changes, and `backend/worldengine/` changes remain
unauthorized.
