# Test Plan

英文原文：`test-plan.md`。

## Test Scope

Testing 必须证明 active-backend 的 public Agent continuity and consolidation evidence boundary。不得执行 provider calls、checker execution、external validation、frontend work 或 Validation Client work。

## Focused Tests

Implementation 后的 primary focused command：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_agent_continuity_consolidation_evidence.py -q
```

Focused suite 必须覆盖：

- continuity request/schema rejects extra fields。
- accepted observe/intent/action/no-intent/wait/rest/sleep/consolidating/reacting states。
- accepted continuity artifact 包含 public Agent id、tick/world time、public summary refs、state、evidence refs 和 redaction status。
- accepted event reaction evidence 引用 public canonical events。
- accepted autonomous action evidence 引用 public Agent action 和 action-result events，并记录 WorldEngine-owned provenance。
- consolidation phase 可以跨多个 ticks，并记录 bounded start/end tick/time evidence。
- short-term to long-term summary evidence 以 public refs 表示，而不是 private memory payloads。
- personality/skill summaries 是 stable 或 bounded-drift refs，不是 automatic per-tick mutation。
- client-scripted autonomy evidence 被拒绝，且不 append accepted Agent autonomy events。
- 包含 raw thought、chain-of-thought、private memory、private goals、hidden context、raw prompts、provider traces、API keys 或 private evaluator data 的 candidate evidence 被拒绝且不 public echo。
- accepted continuity/consolidation event payloads 不包含 private markers。
- 如果添加 route，public manifest/OpenAPI exposure 是 additive。
- 与 existing Agent loop action events、v0.5 memory surfaces、runtime、events、snapshots/archive、world direction 和 0.9.7 legality surfaces 兼容。

## Related Regression

运行 related public surface regression：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_agent_continuity_consolidation_evidence.py app/tests/test_agent_loop*.py app/tests/test_agent_memory*.py app/tests/test_event_api_compat.py app/tests/test_runtime_bounded_run.py app/tests/test_archive_snapshot_summary.py app/tests/test_public_handoff_contract_api.py app/tests/test_rule_linked_evolution_legality.py -q
```

如果当前 shell 的 glob expansion 没有匹配 existing tests，则用当前具体 Agent loop 和 memory test files 替换 glob entries。

## Backend Regression

运行 backend test suite：

```text
cd backend && .venv/bin/python -m pytest app/tests -q
```

## Documentation Checks

Documentation review 前后运行：

```text
git diff --check
```

运行 package file and mirror checks：

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence"); expected={"README","intent","contract","technical-design","test-plan","plan","review"}; names={p.name for p in root.glob("*.md")}; missing=[]; [missing.append(f"{base}.md") for base in sorted(expected) if f"{base}.md" not in names]; [missing.append(f"{base}.zh.md") for base in sorted(expected) if f"{base}.zh.md" not in names]; print("files", len(names)); print("missing", missing); raise SystemExit(1 if missing else 0)'
```

运行 authorization/status scan：

```text
rg -n "implementation_authorized(:|：) yes|provider_live_call_authorized(:|：) yes|generated_result_creation_authorized(:|：) yes|external_validation_authorized(:|：) yes|checker_execution_authorized(:|：) yes|Status(:|：).*implementation complete" docs/iterations/v0.9/0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence
```

Documentation review approval 前，此 scan 不得返回 premature implementation-complete 或 live/external/checker authorization。

## Not Run In This Package

- Live provider calls。
- Generated-result creation。
- Checker execution 或 checker fixture validation。
- External validation 或 autonomous validation。
- Frontend 或 Validation Client tests。
- E2E tests。

除非本包或后续 reviewed package 明确授权，否则这些都不运行。
