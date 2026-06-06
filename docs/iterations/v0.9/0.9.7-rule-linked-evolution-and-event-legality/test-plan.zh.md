# 测试计划

英文原文：`test-plan.md`。

## 测试范围

测试必须证明 active-backend 的 deterministic legality boundary。不得执行 provider calls、checker execution、external validation、frontend work 或 Validation Client work。

## Focused 测试

实现后的 primary focused command：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_rule_linked_evolution_legality.py -q
```

Focused suite 必须覆盖：

- `WorldEventCandidate` rejects extra fields。
- Legal candidate 在 matched rule、allowed operation、valid timing、public cause、public probability evidence 和 public causality evidence 都存在时被 accepted。
- Accepted candidate 返回 `WorldStateDiff`，包含 changed parameter ids、public old/new values、matched rule id，且无 direct private mutation。
- Accepted apply-capable route 只更新 accepted diff 覆盖的 public in-memory world parameters。
- Accepted event/API behavior 记录 public evolution evidence，不含 raw prompt/provider/private markers。
- Unknown rule refs 被 rejected。
- Unknown parameter refs 被 rejected。
- 不在 matched rule `allowed_ops` 内的 operations 被 rejected。
- Out-of-bounds values 被 rejected。
- 超出 current runtime tick/time window 的 timing 被 rejected。
- 缺少 public cause、probability evidence 或 causality evidence 的 candidate 被 rejected。
- Candidate 在 ids、refs、summary、evidence、patches 或 values 中含 private markers 时被 rejected，且不 public echo。
- Direct final fact 和 Agent private-state mutation candidates 被 rejected。
- Direction-biased candidate 只有在 public rule、state、timing、probability 和 causality checks 通过时才可 accepted。
- Rejected candidates 不 append canonical accepted events，也不 mutate public state。
- Snapshot/event-step/replay evidence 与 accepted public state diff 保持一致。

## 相关回归

运行 related public surface regression：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_rule_linked_evolution_legality.py app/tests/test_world_rule_parameter_schema.py app/tests/test_world_direction_boundary.py app/tests/test_runtime_bounded_run.py app/tests/test_public_handoff_contract_api.py app/tests/test_world_params.py app/tests/test_event_api_compat.py app/tests/test_archive_snapshot_summary.py -q
```

这组测试确认 generated rule/parameter validation、natural language direction、bounded runtime controls、public manifest surfaces、existing world params、event-step 和 snapshot/archive compatibility 没有被破坏。

## 后端回归

运行 backend test suite：

```text
cd backend && .venv/bin/python -m pytest app/tests -q
```

## 文档检查

Documentation review 前后运行：

```text
git diff --check
```

运行 package file 和 mirror checks：

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality"); expected={"README","intent","contract","technical-design","test-plan","plan","review"}; names={p.name for p in root.glob("*.md")}; missing=[]; [missing.append(f"{base}.md") for base in sorted(expected) if f"{base}.md" not in names]; [missing.append(f"{base}.zh.md") for base in sorted(expected) if f"{base}.zh.md" not in names]; print("files", len(names)); print("missing", missing); raise SystemExit(1 if missing else 0)'
```

运行 authorization/status scan：

```text
rg -n "implementation_authorized(:|：) yes|provider_live_call_authorized(:|：) yes|generated_result_creation_authorized(:|：) yes|external_validation_authorized(:|：) yes|checker_execution_authorized(:|：) yes|Status(:|：).*implementation complete" docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality
```

Documentation review approval 前，此 scan 不得出现 premature implementation-complete 或 live/external/checker authorization。

## 本包不运行

- Live provider calls。
- Generated-result creation。
- Checker execution 或 checker fixture validation。
- External validation 或 autonomous validation。
- Frontend 或 Validation Client tests。
- E2E tests。
- Agent smoke 或 autonomous tests。

除非后续 reviewed package 明确授权，否则这些工作未授权。
