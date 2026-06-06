# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Test Scope

Testing must prove the active-backend deterministic legality boundary without
provider calls, checker execution, external validation, frontend work, or
Validation Client work.

## Focused Tests

Primary focused command after implementation:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_rule_linked_evolution_legality.py -q
```

The focused suite must cover:

- `WorldEventCandidate` rejects extra fields.
- legal candidate with matched rule, allowed operation, valid timing, public
  cause, public probability evidence, and public causality evidence is accepted.
- accepted candidate returns `WorldStateDiff` with changed parameter ids,
  public old/new values, matched rule id, and no direct private mutation.
- accepted apply-capable route updates only public in-memory world parameters
  covered by the accepted diff.
- accepted event/API behavior records public evolution evidence without raw
  prompt/provider/private markers.
- unknown rule refs are rejected.
- unknown parameter refs are rejected.
- operations not listed in the matched rule's `allowed_ops` are rejected.
- out-of-bounds values are rejected.
- timing outside current runtime tick/time window is rejected.
- candidate without public cause, probability evidence, or causality evidence
  is rejected.
- candidate containing private markers in ids, refs, summary, evidence,
  patches, or values is rejected without public echo.
- direct final fact and Agent private-state mutation candidates are rejected.
- direction-biased candidate may be accepted only when public rule, state,
  timing, probability, and causality checks pass.
- rejected candidates do not append canonical accepted events or mutate public
  state.
- snapshot/event-step/replay evidence remains consistent with accepted public
  state diff.

## Related Regression

Run related public surface regression:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_rule_linked_evolution_legality.py app/tests/test_world_rule_parameter_schema.py app/tests/test_world_direction_boundary.py app/tests/test_runtime_bounded_run.py app/tests/test_public_handoff_contract_api.py app/tests/test_world_params.py app/tests/test_event_api_compat.py app/tests/test_archive_snapshot_summary.py -q
```

This confirms compatibility with generated rule/parameter validation, natural
language direction, bounded runtime controls, and public manifest surfaces.
It also checks existing world params, event-step, and snapshot/archive
compatibility.

## Backend Regression

Run the backend test suite:

```text
cd backend && .venv/bin/python -m pytest app/tests -q
```

## Documentation Checks

Before and after documentation review:

```text
git diff --check
```

Run package file and mirror checks:

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality"); expected={"README","intent","contract","technical-design","test-plan","plan","review"}; names={p.name for p in root.glob("*.md")}; missing=[]; [missing.append(f"{base}.md") for base in sorted(expected) if f"{base}.md" not in names]; [missing.append(f"{base}.zh.md") for base in sorted(expected) if f"{base}.zh.md" not in names]; print("files", len(names)); print("missing", missing); raise SystemExit(1 if missing else 0)'
```

Run authorization/status scan:

```text
rg -n "implementation_authorized(:|：) yes|provider_live_call_authorized(:|：) yes|generated_result_creation_authorized(:|：) yes|external_validation_authorized(:|：) yes|checker_execution_authorized(:|：) yes|Status(:|：).*implementation complete" docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality
```

Before documentation review approval, this scan must return no premature
implementation-complete or live/external/checker authorization.

## Not Run In This Package

- Live provider calls.
- Generated-result creation.
- Checker execution or checker fixture validation.
- External validation or autonomous validation.
- Frontend or Validation Client tests.
- E2E tests.
- Agent smoke or autonomous tests.

These are unauthorized unless a later reviewed package explicitly authorizes
them.
