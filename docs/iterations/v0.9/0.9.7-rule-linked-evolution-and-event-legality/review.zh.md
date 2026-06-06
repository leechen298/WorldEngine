# Review

英文原文：`review.md`。

Status：reviewed / ready for implementation

implementation_authorized: yes
provider_live_call_authorized: no
generated_result_creation_authorized: no
checker_execution_authorized: no
external_validation_authorized: no

## 变更文件

Documentation draft：

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

Documentation drafting 期间没有修改 runtime、schema、API、frontend、checker、fixture、generated-result、external repository 或 Validation Client files。

## 已运行命令

Documentation checks：

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality"); expected={"README","intent","contract","technical-design","test-plan","plan","review"}; names={p.name for p in root.glob("*.md")}; missing=[]; [missing.append(f"{base}.md") for base in sorted(expected) if f"{base}.md" not in names]; [missing.append(f"{base}.zh.md") for base in sorted(expected) if f"{base}.zh.md" not in names]; print("files", len(names)); print("missing", missing); raise SystemExit(1 if missing else 0)'
```

结果：exit 0；`files 14`；`missing []`。

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality"); pairs=[("README.md","README.zh.md"),("intent.md","intent.zh.md"),("contract.md","contract.zh.md"),("technical-design.md","technical-design.zh.md"),("test-plan.md","test-plan.zh.md"),("plan.md","plan.zh.md"),("review.md","review.zh.md")]; missing=[str(root/x) for pair in pairs for x in pair if not (root/x).exists()]; bad=[]; [bad.append(str(root/b)+": missing mirrored status") for a,b in pairs if (root/a).exists() and (root/b).exists() and "Status:" in (root/a).read_text() and "Status：" not in (root/b).read_text()]; [bad.append(str(root/b)+": missing implementation authorization no") for a,b in pairs if (root/a).exists() and (root/b).exists() and "implementation_authorized: no" in (root/a).read_text() and "implementation_authorized: no" not in (root/b).read_text()]; print("missing", missing); print("bad", bad); raise SystemExit(1 if missing or bad else 0)'
```

结果：exit 0；`missing []`；`bad []`。

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality"); combined="\n".join(path.read_text() for path in root.glob("*.md")); required=["implementation_authorized: no","provider_live_call_authorized: no","generated_result_creation_authorized: no","checker_execution_authorized: no","external_validation_authorized: no","WorldEventCandidate","WorldEventLegalityResult","WorldStateDiff","WorldEvolutionEvidence","direction-biased","/world/event-steps","/world/params","0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence"]; missing=[term for term in required if term not in combined]; print("missing", missing); raise SystemExit(1 if missing else 0)'
```

添加 exact handoff id 前初次结果：exit 1；`missing ['0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence']`。修复后：exit 0；`missing []`。

```text
rg -n "implementation_authorized(:|：) yes|provider_live_call_authorized(:|：) yes|generated_result_creation_authorized(:|：) yes|external_validation_authorized(:|：) yes|checker_execution_authorized(:|：) yes|Status(:|：).*implementation complete" docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality
```

移除 future exact authorization strings 前初次结果：exit 0，匹配 `README.md`、`README.zh.md`、`plan.md` 和 `plan.zh.md` 中的 future-authorization prose。修复后：exit 1，无输出。Draft 中没有 premature implementation、live provider、generated-result、checker 或 external authorization。

```text
git diff --check
```

结果：exit 0，无输出。

评审后中文镜像修复检查：

```text
rg -n --glob '*.zh.md' --glob '!**/review*.md' "public generated|deterministic public|Implementation 必须|accepted parameter changes|legal event acceptance|illegal event rejection|focused backend/API tests|active backend scope|existing public|mostly English|documentation package drafting" docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality
```

中文镜像重写后结果：exit 1，无输出。

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality"); pairs=[("README.md","README.zh.md"),("intent.md","intent.zh.md"),("contract.md","contract.zh.md"),("technical-design.md","technical-design.zh.md"),("test-plan.md","test-plan.zh.md"),("plan.md","plan.zh.md"),("review.md","review.zh.md")]; missing=[str(root/x) for pair in pairs for x in pair if not (root/x).exists()]; bad=[]; [bad.append(str(root/b)+": missing mirrored status") for a,b in pairs if (root/a).exists() and (root/b).exists() and "Status:" in (root/a).read_text() and "Status：" not in (root/b).read_text()]; [bad.append(str(root/b)+": missing implementation authorization no") for a,b in pairs if (root/a).exists() and (root/b).exists() and "implementation_authorized: no" in (root/a).read_text() and "implementation_authorized: no" not in (root/b).read_text()]; print("missing", missing); print("bad", bad); raise SystemExit(1 if missing or bad else 0)'
```

中文镜像重写后结果：exit 0；`missing []`；`bad []`。

```text
git diff --check
```

中文镜像重写后结果：exit 0，无输出。

P3 terminology repair checks：

```text
rg -n "红action" docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality
```

修复后结果：exit 1，无输出。

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality"); pairs=[("README.md","README.zh.md"),("intent.md","intent.zh.md"),("contract.md","contract.zh.md"),("technical-design.md","technical-design.zh.md"),("test-plan.md","test-plan.zh.md"),("plan.md","plan.zh.md"),("review.md","review.zh.md")]; missing=[str(root/x) for pair in pairs for x in pair if not (root/x).exists()]; bad=[]; [bad.append(str(root/b)+": missing mirrored status") for a,b in pairs if (root/a).exists() and (root/b).exists() and "Status:" in (root/a).read_text() and "Status：" not in (root/b).read_text()]; [bad.append(str(root/b)+": missing implementation authorization no") for a,b in pairs if (root/a).exists() and (root/b).exists() and "implementation_authorized: no" in (root/a).read_text() and "implementation_authorized: no" not in (root/b).read_text()]; print("missing", missing); print("bad", bad); raise SystemExit(1 if missing or bad else 0)'
```

implementation authorization update 前结果：exit 0；`missing []`；`bad []`。

```text
rg -n --glob '*.zh.md' --glob '!**/review*.md' "public generated|deterministic public|Implementation 必须|accepted parameter changes|legal event acceptance|illegal event rejection|focused backend/API tests|active backend scope|existing public|mostly English|documentation package drafting|红action" docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality
```

修复后结果：exit 1，无输出。

```text
git diff --check
```

修复后结果：exit 0，无输出。

## 测试结果

Documentation drafting 阶段未运行 code tests，因为 implementation 尚未授权。

## 兼容性审查

Draft contract 要求与 existing event、runtime、generated rule/parameter、world direction、director-guidance 和 public handoff surfaces 保持 additive compatibility。

## 范围审查

Draft scope 限定为 future active-backend deterministic rule-linked event legality 和 state-diff evidence。Provider live calls、generated-result creation、checker execution 或 fixture changes、external validation、Validation Client changes、frontend UI、Agent continuity、narrative projection、diagnostic dialogue、durable scheduling 和 `backend/worldengine/` changes 仍未授权。

## Subagent 发现

Requirements extraction subagent：

```text
agent: 019e9944-7117-7bf0-98e6-2d8da75f529e
scope: read-only 0.9.7 requirements extraction
status: complete
```

Subagent 确认 active route、required file set，以及与 `0.9.3`、`0.9.5`、`0.9.6` 和既有公开事件 surface 的核心连接。它提示的风险已在 draft 中处理：

- checker support 必须限定为 public artifact shape，因为 checker execution 和 fixtures 属于后续 packages。
- legality 必须基于 public rule/state evidence，而不是 hidden prose adjudication。
- accepted state mutation 必须有 public diff/replay evidence。
- direction 不得绕过 rules 变成 direct final facts 或 Agent private mutation。
- tests 必须包含 event、runtime、direction、world-param 和 snapshot compatibility。

初次 documentation/contract evaluator：

```text
agent: 019e994d-2433-7433-8942-8a83dbc9aa0b
scope: read-only 0.9.7 documentation/contract review
status: FAIL
```

Verdict：FAIL for clean documentation/contract approval，有一个 P2。

- P2：中文镜像语义对齐，但对 `docs/iterations/AGENTS.md` 的中文镜像质量规则来说，英中混写过多。

本地修复已将中文镜像重写为自然中文说明，同时保留技术标识、API routes、field names、status values 和授权语义。

Documentation/contract re-review：

```text
agent: 019e994d-2433-7433-8942-8a83dbc9aa0b
scope: read-only 0.9.7 documentation/contract re-review
status: PASS
```

Verdict：PASS，无 P0/P1/P2 findings。Evaluator 记录了一个非阻塞 P3：中文词语 `红action`
不自然；本地修复已将其替换为自然中文 `脱敏`。

## 未解决 P1/P2/P3

- 无。

## 最终评估

Documentation gate complete。Implementation 仅授权本包记录的 scoped active-backend `0.9.7`
rule-linked evolution and event-legality work。

Provider live calls、generated-result creation、checker execution 或 fixture changes、
external validation、Validation Client changes、frontend UI、Agent continuity、narrative
projection、diagnostic dialogue、durable scheduling 和 `backend/worldengine/` changes 仍未授权。

## Implementation Closeout Update

Status：implementation complete / verification passed

### Changed Files

Scoped `0.9.7` implementation changed or added：

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

当前 worktree 中还有早前 v0.9 child work 留下的其他 modified/untracked files。本节不把这些旧改动声明为新的 `0.9.7` implementation changes，除非后续只做 parent route/status handoff 更新。

### Implementation Summary

- 新增 `WorldEventCandidate`、`WorldParameterPatch`、`WorldEventLegalityResult`、`WorldEventLegalityDiagnostic`、`WorldStateDiff`、`WorldEvolutionEvidence` 以及 API request/response schemas，并使用 `extra="forbid"`。
- 新增 deterministic rule-linked legality evaluation，输入包括 `GeneratedRuleParameterSet`、当前公开 params、runtime tick/world time、constraints、probability evidence、causality evidence、public cause refs，以及可选 queued direction refs。
- 新增 additive public endpoint：`POST /worlds/{world_id}/evolution/evaluate-event`，并加入 manifest exposure。
- Accepted apply requests 只更新 accepted diff 覆盖的 public in-memory `WorldState` parameter paths，并追加带 public replay/evolution evidence 的 `world.evolution.accepted` event。
- Rejected candidates 只返回 public diagnostics，不追加 accepted events，也不 mutate public state。
- 扩展 validation-error redaction，确保 `private_goal` 等 private marker field names 不会出现在 public HTTP validation errors 中。

### Commands Run

```text
cd backend && .venv/bin/python -m pytest app/tests/test_rule_linked_evolution_legality.py -q
```

Initial implementation result：exit 0；`17 passed in 0.52s`。

Implementation-scope evaluator findings 修复后：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_rule_linked_evolution_legality.py -q
```

Result：exit 0；`19 passed in 0.50s`。

```text
cd backend && .venv/bin/python -m pytest app/tests/test_rule_linked_evolution_legality.py app/tests/test_world_rule_parameter_schema.py app/tests/test_world_direction_boundary.py app/tests/test_runtime_bounded_run.py app/tests/test_public_handoff_contract_api.py app/tests/test_world_params.py app/tests/test_event_api_compat.py app/tests/test_archive_snapshot_summary.py -q
```

Initial related regression result：exit 0；`83 passed in 1.36s`。

Evaluator repair 后：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_rule_linked_evolution_legality.py app/tests/test_world_rule_parameter_schema.py app/tests/test_world_direction_boundary.py app/tests/test_runtime_bounded_run.py app/tests/test_public_handoff_contract_api.py app/tests/test_world_params.py app/tests/test_event_api_compat.py app/tests/test_archive_snapshot_summary.py -q
```

Result：exit 0；`85 passed in 1.36s`。

```text
cd backend && .venv/bin/python -m pytest app/tests -q
```

Initial backend regression result：exit 0；`334 passed in 3.35s`。

Evaluator repair 后：

```text
cd backend && .venv/bin/python -m pytest app/tests -q
```

Result：exit 0；`336 passed in 3.31s`。

```text
git diff --check
```

Result：exit 0；无输出。

Package file check：

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality"); expected={"README","intent","contract","technical-design","test-plan","plan","review"}; names={p.name for p in root.glob("*.md")}; missing=[]; [missing.append(f"{base}.md") for base in sorted(expected) if f"{base}.md" not in names]; [missing.append(f"{base}.zh.md") for base in sorted(expected) if f"{base}.zh.md" not in names]; print("files", len(names)); print("missing", missing); raise SystemExit(1 if missing else 0)'
```

Result：exit 0；`files 14`；`missing []`。

Unauthorized authorization scan：

```text
rg -n "provider_live_call_authorized(:|：) yes|generated_result_creation_authorized(:|：) yes|external_validation_authorized(:|：) yes|checker_execution_authorized(:|：) yes" docs/iterations/v0.9/0.9.7-rule-linked-evolution-and-event-legality
```

Result：exit 1；无输出。

### Implementation-Scope Evaluator

First implementation evaluator：

```text
agent: 019e9acb-95eb-7481-947e-0ac6604b4490
scope: read-only 0.9.7 implementation review
status: FAIL
```

Findings：

- P1：direct-final 和 Agent-private mutation checks 未扫描全部 candidate surfaces，包括 refs、probability/causality evidence 和 patch values。
- P1：package `review.md` 和 `review.zh.md` 仍只有 documentation-stage evidence，未 close implementation contract。
- P2：HTTP validation redaction 仍会在 validation-error `loc` 中回显 `private_goal` 等 private extra-field names。

Repairs：

- `_direct_final_fact_diagnostics` 现在递归扫描 `candidate.model_dump()` 返回的完整 public candidate structure。
- Focused tests 已覆盖藏在 probability evidence、causality evidence 和 patch values 中的 direct-final/private-state markers。
- `_PRIVATE_VALIDATION_MARKERS` 已加入 underscore variants，包括 `private_goal`、`private_memory`、`private_prompt` 和 `private_evaluator_data`。
- Focused tests 已覆盖 HTTP validation errors 中的 private extra-field names。
- 本节已记录 implementation closeout evidence。

Final implementation evaluator：

```text
agent: 019e9acb-95eb-7481-947e-0ac6604b4490
scope: read-only 0.9.7 implementation re-review
status: PASS
```

Verdict：PASS，无 P0/P1/P2 findings。Evaluator 报告一个 non-blocking P3，原因是本 review 在这次更新前仍保留 pending final re-review placeholder。

### Compatibility Review

- Existing `/world/events` 和 `/world/event-steps` response shapes 保持兼容；未改变 `Event` required fields，empty `refs` serialization 仍保持原行为。
- Existing `/world/params` 和 `/world/params/apply` behavior 保持兼容；`0.9.7` 没有把 `/world/params/apply` 复用为 event legality entrypoint。
- Existing runtime bounded-run、world direction、generated rule/parameter、public manifest、snapshot/archive 和 event API compatibility suites 均通过。
- Generated rule/parameter schemas 本身不授予 runtime writable paths；`0.9.7` 按 request 评估 rule-linked public paths，并只应用 accepted diff 覆盖的 public parameter patches。

### Scope Review

本包未执行 live provider calls、未创建 generated results、未执行 checker、未修改 checker fixtures、未运行 external validation、未修改 Validation Client、未修改 frontend UI、未实现 Agent continuity、narrative projection、diagnostic dialogue、durable scheduling 或 deployment infrastructure，也未修改 `backend/worldengine/`。

### Unresolved P1/P2/P3

- 无。

### Final Route

Implementation complete。Handoff 进入
`0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence`
documentation-package creation/review。Evidence execution、live provider calls、generated-result creation、checker execution、external validation、Agent continuity implementation、frontend UI、durable scheduling、Validation Client changes 和 `backend/worldengine/` changes 仍未授权。
