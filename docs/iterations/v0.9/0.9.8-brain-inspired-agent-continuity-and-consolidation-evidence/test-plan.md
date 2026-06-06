# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Test Scope

Testing must prove the active-backend public Agent continuity and
consolidation evidence boundary without provider calls, checker execution,
external validation, frontend work, or Validation Client work.

## Focused Tests

Primary focused command after implementation:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_agent_continuity_consolidation_evidence.py -q
```

The focused suite must cover:

- continuity request/schema rejects extra fields.
- accepted observe/intent/action/no-intent/wait/rest/sleep/consolidating/reacting states.
- accepted continuity artifact includes public Agent id, tick/world time,
  public summary refs, state, evidence refs, and redaction status.
- accepted event reaction evidence references public canonical events.
- accepted autonomous action evidence references public Agent action and
  action-result events and records WorldEngine-owned provenance.
- consolidation phase may span multiple ticks and records bounded start/end
  tick/time evidence.
- short-term to long-term summary evidence is represented by public refs, not
  private memory payloads.
- personality/skill summaries are stable or bounded-drift refs, not automatic
  per-tick mutation.
- client-scripted autonomy evidence is rejected and does not append accepted
  Agent autonomy events.
- candidate evidence containing raw thought, chain-of-thought, private memory,
  private goals, hidden context, raw prompts, provider traces, API keys, or
  private evaluator data is rejected without public echo.
- accepted continuity/consolidation event payloads contain no private markers.
- public manifest/OpenAPI exposure is additive if a route is added.
- compatibility with existing Agent loop action events, v0.5 memory surfaces,
  runtime, events, snapshots/archive, world direction, and 0.9.7 legality
  surfaces.

## Related Regression

Run related public surface regression:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_agent_continuity_consolidation_evidence.py app/tests/test_agent_loop*.py app/tests/test_agent_memory*.py app/tests/test_event_api_compat.py app/tests/test_runtime_bounded_run.py app/tests/test_archive_snapshot_summary.py app/tests/test_public_handoff_contract_api.py app/tests/test_rule_linked_evolution_legality.py -q
```

If glob expansion does not match existing tests in the current shell, replace
the glob entries with the concrete current Agent loop and memory test files.

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
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence"); expected={"README","intent","contract","technical-design","test-plan","plan","review"}; names={p.name for p in root.glob("*.md")}; missing=[]; [missing.append(f"{base}.md") for base in sorted(expected) if f"{base}.md" not in names]; [missing.append(f"{base}.zh.md") for base in sorted(expected) if f"{base}.zh.md" not in names]; print("files", len(names)); print("missing", missing); raise SystemExit(1 if missing else 0)'
```

Run authorization/status scan:

```text
rg -n "implementation_authorized(:|：) yes|provider_live_call_authorized(:|：) yes|generated_result_creation_authorized(:|：) yes|external_validation_authorized(:|：) yes|checker_execution_authorized(:|：) yes|Status(:|：).*implementation complete" docs/iterations/v0.9/0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence
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

These are unauthorized unless this or a later reviewed package explicitly
authorizes them.
