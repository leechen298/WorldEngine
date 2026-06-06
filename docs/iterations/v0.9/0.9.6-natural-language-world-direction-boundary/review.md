# Review

Chinese mirror: `review.zh.md`.

Status: implementation complete / focused verification passed / evaluator PASS

implementation_authorized: yes
provider_live_call_authorized: no
generated_result_creation_authorized: no
external_validation_authorized: no

## Changed Files

Documentation draft:

```text
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/README.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/README.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/intent.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/intent.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/contract.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/contract.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/technical-design.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/technical-design.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/test-plan.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/test-plan.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/plan.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/plan.zh.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/review.md
docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary/review.zh.md
```

Implementation files:

```text
backend/app/schemas/world_direction.py
backend/app/api/routes/world.py
backend/app/tests/test_world_direction_boundary.py
```

## Commands Run

Documentation checks:

```text
git diff --check
```

Result: exit 0, no output.

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary"); expected={"README","intent","contract","technical-design","test-plan","plan","review"}; names={p.name for p in root.glob("*.md")}; missing=[]; [missing.append(f"{base}.md") for base in sorted(expected) if f"{base}.md" not in names]; [missing.append(f"{base}.zh.md") for base in sorted(expected) if f"{base}.zh.md" not in names]; print("files", len(names)); print("missing", missing); raise SystemExit(1 if missing else 0)'
```

Result: exit 0; `files 14`; `missing []`.

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary"); combined="\n".join(path.read_text() for path in root.glob("*.md")); required=["implementation_authorized: no","provider_live_call_authorized: no","generated_result_creation_authorized: no","external_validation_authorized: no","WorldDirectionRequest","WorldDirectionQueueItem","direct_final_fact","agent_private_state_mutation","rule_bypass","/worlds/{world_id}/director-guidance","0.9.7-rule-linked-evolution-and-event-legality"]; missing=[term for term in required if term not in combined]; print("missing", missing); raise SystemExit(1 if missing else 0)'
```

Result: exit 0; `missing []`.

```text
rg -n "implementation_authorized(:|：) yes|provider_live_call_authorized(:|：) yes|generated_result_creation_authorized(:|：) yes|external_validation_authorized(:|：) yes|Status(:|：).*implementation complete|Status(:|：).*ready for implementation" docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary
```

Result before documentation gate approval: exit 1, no output. No implementation
authorization or live/external authorization was recorded in the initial draft.

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary"); pairs=[("README.md","README.zh.md"),("intent.md","intent.zh.md"),("contract.md","contract.zh.md"),("technical-design.md","technical-design.zh.md"),("test-plan.md","test-plan.zh.md"),("plan.md","plan.zh.md"),("review.md","review.zh.md")]; missing=[str(root/x) for pair in pairs for x in pair if not (root/x).exists()]; bad=[]; [bad.append(str(root/b)+": missing mirrored status") for a,b in pairs if (root/a).exists() and (root/b).exists() and "Status:" in (root/a).read_text() and "Status：" not in (root/b).read_text()]; [bad.append(str(root/b)+": missing implementation authorization no") for a,b in pairs if (root/a).exists() and (root/b).exists() and "implementation_authorized: no" in (root/a).read_text() and "implementation_authorized: no" not in (root/b).read_text()]; print("missing", missing); print("bad", bad); raise SystemExit(1 if missing or bad else 0)'
```

Result: exit 0; `missing []`; `bad []`.

After evaluator PASS, `implementation_authorized: yes` was recorded for this
package only. Provider live-call, generated-result, and external validation
authorization remain `no`.

Focused implementation test:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py -q
```

Initial RED result: exit 2, expected import failure for missing
`app.schemas.world_direction`.

GREEN result after implementation: exit 0; `6 passed in 0.30s`.

Related public surface regression:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py app/tests/test_world_rule_parameter_schema.py app/tests/test_worldview_fidelity_evaluation.py -q
```

Result: exit 0; `40 passed in 0.65s`.

Backend regression:

```text
cd backend && .venv/bin/python -m pytest app/tests -q
```

Result: exit 0; `303 passed in 2.87s`.

Implementation review repair RED:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py -q
```

Result after adding evaluator-gap tests: exit 1; `4 failed, 11 passed in 0.52s`.
The failing tests covered private marker leakage through `public_context` keys
and `branch_id`, unreachable `future_evaluation_hint`, and classification
precedence for public rule constraints.

Implementation review repair focused GREEN:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py -q
```

Result: exit 0; `15 passed in 0.43s`.

Implementation review repair related public surface regression:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py app/tests/test_world_rule_parameter_schema.py app/tests/test_worldview_fidelity_evaluation.py -q
```

Result: exit 0; `49 passed in 0.80s`.

Implementation review repair backend regression:

```text
cd backend && .venv/bin/python -m pytest app/tests -q
```

Result: exit 0; `312 passed in 2.99s`.

Implementation re-review repair RED:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py -q
```

Result after adding documented-private-evidence tests: exit 1;
`3 failed, 17 passed in 0.54s`. The failing tests covered documented
anti-leak terms `raw prompt`, `raw provider response`, and
`private evaluator data` across `branch_id`, `public_context` keys, and
`instruction_text`.

Implementation re-review repair focused GREEN:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py -q
```

Result: exit 0; `20 passed in 0.52s`.

Implementation re-review repair related public surface regression:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py app/tests/test_world_rule_parameter_schema.py app/tests/test_worldview_fidelity_evaluation.py -q
```

Result: exit 0; `54 passed in 0.88s`.

Implementation re-review repair backend regression:

```text
cd backend && .venv/bin/python -m pytest app/tests -q
```

Result: exit 0; `317 passed in 3.09s`.

```text
git diff --check
```

Result after second repair: exit 0, no output.

## Test Results

Focused, related public surface, and backend regression tests passed after the
implementation review repairs as recorded above. Provider, checker, external
validation, generated-result, E2E, autonomous, frontend, and Validation Client
tests were not run because this package does not authorize them.

## Compatibility Review

Implementation adds an additive public `/worlds/{world_id}/direction` surface
and preserves existing benign `/worlds/{world_id}/director-guidance` behavior,
public handoff behavior, event listing, runtime controls, rule-parameter
schemas, and fidelity helpers under focused and related regression tests.

## Scope Review

Implementation stayed scoped to active-backend public direction schema,
world-route API behavior, and focused backend tests. It did not add live
provider calls, generated-result creation, checker execution, external
validation, Validation Client code, frontend UI, durable scheduling, event
legality/final adjudication, Agent continuity, or `backend/worldengine/`
changes.

## Subagent Findings

Read-only documentation/contract evaluator:

```text
agent: 019e98f6-7cf2-7b12-842e-1cd4991c608b
scope: 0.9.6 docs/contract/design/test-plan/mirror review only
status: PASS
```

Verdict: PASS with no P0/P1/P2/P3 findings.

The evaluator confirmed:

- required mixed-package docs and Chinese mirrors exist.
- package status and authorizations were closed before review.
- the contract is coherent with the parent v0.9 route and `v0.9-plan.md`.
- implementation scope is specific enough to authorize after local review
  updates.
- the package preserves the boundary between queued world-level guidance and
  out-of-scope event legality or direct mutation.

Initial implementation-scope evaluator:

```text
agent: 019e9900-d096-7cc1-b1e3-05ad9b54b588
scope: 0.9.6 implementation review only
status: FAIL
```

Verdict: FAIL with one P1 and one P2.

- P1: user-controlled `public_context` keys and `branch_id` could leak private
  markers through public responses or event payloads because classification
  checked only `instruction_text`.
- P2: evaluator-gap tests were insufficient and `future_evaluation_hint` was
  unreachable in deterministic classification.

Local repair added tests for private-marker redaction across
`instruction_text`, `branch_id`, and `public_context` keys; reachable allowed
categories; rule bypass; Agent goal mutation; timing; and existing
director-guidance compatibility. Implementation now classifies across all
public request fields, redacts event field echoes when redaction is required,
and exposes the missing future-evaluation category.

First implementation-scope re-review:

```text
agent: 019e9900-d096-7cc1-b1e3-05ad9b54b588
scope: 0.9.6 implementation re-review only
status: FAIL
```

Verdict: FAIL with one P1 and one P3.

- P1: the private marker vocabulary omitted documented anti-leak terms
  `raw prompt`, `raw provider response`, and `private evaluator data`.
- P3: focused tests did not assert `inventory_injection` and
  `relationship_override` forbidden categories.

Local second repair added tests for the documented anti-leak terms across
`branch_id`, `public_context` keys, and `instruction_text`; added coverage for
the remaining forbidden categories; and extended the marker vocabulary with
space and underscore forms for the documented raw/private evidence terms.

Second implementation-scope re-review:

```text
agent: 019e9900-d096-7cc1-b1e3-05ad9b54b588
scope: 0.9.6 implementation second re-review only
status: PASS
```

Verdict: PASS with no P0/P1/P2/P3 findings.

The evaluator confirmed that the marker vocabulary covers documented
anti-leak terms, classification checks `instruction_text`, `branch_id`, and
`public_context` keys, redacted public/event echoes are blanked, focused tests
cover documented anti-leak terms plus the remaining forbidden categories, and
`future_evaluation_hint` remains reachable.

## Unresolved P1/P2/P3

- None.

## Final Assessment

Documentation gate complete. Implementation completed for the reviewed
`0.9.6` scope. Focused, related public-surface, backend regression, and
`git diff --check` verification passed, and implementation-scope evaluator
re-review passed with no P0/P1/P2/P3 findings.

Provider live calls, generated-result creation, checker execution, external
validation, Validation Client changes, frontend UI, event legality, Agent
continuity, durable scheduling, and `backend/worldengine/` changes remain
unauthorized.
