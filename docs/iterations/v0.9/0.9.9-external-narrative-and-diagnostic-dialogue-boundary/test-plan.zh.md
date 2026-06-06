# Test Plan

英文原文：`test-plan.md`。

## Test Scope

Testing 必须证明 active-backend public narrative projection 和 out-of-world diagnostic boundary，
不得使用 provider calls、checker execution、external validation、frontend work 或 Validation Client work。

## Focused Tests

Implementation 后的 primary focused command：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_external_narrative_diagnostic_boundary.py -q
```

Focused suite 必须覆盖：

- projection request/schema rejects extra fields。
- diagnostic request/schema rejects extra fields。
- accepted narrative projection artifact 包含 public world id、public source refs、provenance、
  redaction status，并且所有 mutation flags 为 false。
- accepted diagnostic dialogue artifact 包含 public world id、Agent id、public question/response
  summaries、evidence refs、provenance、redaction status，并且所有 mutation flags 为 false。
- projection 只使用 public events、snapshots 和 Agent continuity refs 作为 sources。
- diagnostic dialogue 默认保持在 world timeline 和 Agent memory 之外。
- 声称 canonical state mutation、canonical event append、Agent memory write 或 in-world dialogue
  recording 的 requests 会被 rejected。
- 包含 raw thought、chain-of-thought、private memory、private goals、hidden context、raw prompts、
  provider traces、API keys、authorization headers、secrets 或 private evaluator data 的 candidate
  evidence 会被 rejected，且不 public echo。
- accepted projection/diagnostic payloads 不包含 private markers。
- 如添加 route，public manifest/OpenAPI exposure 是 additive。
- 与 existing events、snapshots/archive、Agent continuity、runtime、world direction 和 0.9.7 legality
  surfaces 兼容。

## Related Regression

Run related public surface regression：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_external_narrative_diagnostic_boundary.py app/tests/test_agent_continuity_consolidation_evidence.py app/tests/test_event_api_compat.py app/tests/test_runtime_bounded_run.py app/tests/test_archive_snapshot_summary.py app/tests/test_public_handoff_contract_api.py app/tests/test_rule_linked_evolution_legality.py -q
```

## Backend Regression

Run the backend test suite：

```text
cd backend && .venv/bin/python -m pytest app/tests -q
```

## Documentation Checks

Documentation review 前后运行：

```text
git diff --check
```

Run package file and mirror checks：

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary"); expected={"README","intent","contract","technical-design","test-plan","plan","review"}; names={p.name for p in root.glob("*.md")}; missing=[]; [missing.append(f"{base}.md") for base in sorted(expected) if f"{base}.md" not in names]; [missing.append(f"{base}.zh.md") for base in sorted(expected) if f"{base}.zh.md" not in names]; print("files", len(names)); print("missing", missing); raise SystemExit(1 if missing else 0)'
```

Run authorization/status scan：

```text
rg -n "implementation_authorized(:|：) yes|provider_live_call_authorized(:|：) yes|generated_result_creation_authorized(:|：) yes|external_validation_authorized(:|：) yes|checker_execution_authorized(:|：) yes|Status(:|：).*implementation complete" docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary
```

Documentation review approval 前，这个 scan 必须没有 premature implementation-complete 或
live/external/checker authorization。

## Not Run In This Package

- Live provider calls。
- Generated-result creation。
- Checker execution 或 checker fixture validation。
- External validation 或 autonomous validation。
- Frontend 或 Validation Client tests。
- E2E tests。

除非本包或后续 reviewed package 明确授权，否则这些都不授权。
