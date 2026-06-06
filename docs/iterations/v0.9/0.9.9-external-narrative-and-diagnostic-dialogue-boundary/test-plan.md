# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Test Scope

Testing must prove the active-backend public narrative projection and
out-of-world diagnostic boundary without provider calls, checker execution,
external validation, frontend work, or Validation Client work.

## Focused Tests

Primary focused command after implementation:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_external_narrative_diagnostic_boundary.py -q
```

The focused suite must cover:

- projection request/schema rejects extra fields.
- diagnostic request/schema rejects extra fields.
- accepted narrative projection artifact includes public world id, public
  source refs, provenance, redaction status, and all mutation flags false.
- accepted diagnostic dialogue artifact includes public world id, Agent id,
  public question/response summaries, evidence refs, provenance, redaction
  status, and all mutation flags false.
- projection uses only public events, snapshots, and Agent continuity refs as
  sources.
- diagnostic dialogue remains outside world timeline and Agent memory by
  default.
- requests that claim canonical state mutation, canonical event append, Agent
  memory write, or in-world dialogue recording are rejected.
- candidate evidence containing raw thought, chain-of-thought, private memory,
  private goals, hidden context, raw prompts, provider traces, API keys,
  authorization headers, secrets, or private evaluator data is rejected without
  public echo.
- accepted projection/diagnostic payloads contain no private markers.
- public manifest/OpenAPI exposure is additive if routes are added.
- compatibility with existing events, snapshots/archive, Agent continuity,
  runtime, world direction, and 0.9.7 legality surfaces.

## Related Regression

Run related public surface regression:

```text
cd backend && .venv/bin/python -m pytest app/tests/test_external_narrative_diagnostic_boundary.py app/tests/test_agent_continuity_consolidation_evidence.py app/tests/test_event_api_compat.py app/tests/test_runtime_bounded_run.py app/tests/test_archive_snapshot_summary.py app/tests/test_public_handoff_contract_api.py app/tests/test_rule_linked_evolution_legality.py -q
```

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
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary"); expected={"README","intent","contract","technical-design","test-plan","plan","review"}; names={p.name for p in root.glob("*.md")}; missing=[]; [missing.append(f"{base}.md") for base in sorted(expected) if f"{base}.md" not in names]; [missing.append(f"{base}.zh.md") for base in sorted(expected) if f"{base}.zh.md" not in names]; print("files", len(names)); print("missing", missing); raise SystemExit(1 if missing else 0)'
```

Run authorization/status scan:

```text
rg -n "implementation_authorized(:|：) yes|provider_live_call_authorized(:|：) yes|generated_result_creation_authorized(:|：) yes|external_validation_authorized(:|：) yes|checker_execution_authorized(:|：) yes|Status(:|：).*implementation complete" docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary
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
