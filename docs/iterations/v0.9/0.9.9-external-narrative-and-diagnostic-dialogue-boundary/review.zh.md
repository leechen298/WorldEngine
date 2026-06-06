# Review

英文原文：`review.md`。

Status：implementation complete / verification passed

implementation_authorized: yes
provider_live_call_authorized: no
generated_result_creation_authorized: no
checker_execution_authorized: no
external_validation_authorized: no

## Changed Files

Documentation draft：

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

Documentation drafting 阶段未修改 runtime、schema、API、frontend、checker、fixture、
generated-result、external repository 或 Validation Client files。

当前 worktree 说明：仓库中已存在本 goal state 早前留下的 v0.9 `backend/app`
implementation changes 和 earlier child-package files。本 review 中的 `0.9.9`
documentation-stage scope 仅限上面列出的 new `0.9.9` package documentation files；
不声明、不授权、不 stage、也不 close 任何 pre-existing non-`0.9.9` implementation changes。

Implementation closeout：

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

Documentation checks：

```text
git diff --check
```

Result：exit 0；无输出。

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary"); expected={"README","intent","contract","technical-design","test-plan","plan","review"}; names={p.name for p in root.glob("*.md")}; missing=[]; [missing.append(f"{base}.md") for base in sorted(expected) if f"{base}.md" not in names]; [missing.append(f"{base}.zh.md") for base in sorted(expected) if f"{base}.zh.md" not in names]; print("files", len(names)); print("missing", missing); raise SystemExit(1 if missing else 0)'
```

Result：exit 0；`files 14`；`missing []`。

```text
rg -n "implementation_authorized(:|：) yes|provider_live_call_authorized(:|：) yes|generated_result_creation_authorized(:|：) yes|external_validation_authorized(:|：) yes|checker_execution_authorized(:|：) yes|Status(:|：).*implementation complete" docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary
```

从 `README.md`、`README.zh.md`、`plan.md` 和 `plan.zh.md` 中移除 exact future-authorization
wording 前，初次结果为 exit 0，命中 explanatory prose。修复后：exit 1，无输出。

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary"); pairs=[("README.md","README.zh.md"),("intent.md","intent.zh.md"),("contract.md","contract.zh.md"),("technical-design.md","technical-design.zh.md"),("test-plan.md","test-plan.zh.md"),("plan.md","plan.zh.md"),("review.md","review.zh.md")]; missing=[str(root/x) for pair in pairs for x in pair if not (root/x).exists()]; bad=[]; [bad.append(str(root/b)+": missing mirrored status") for a,b in pairs if (root/a).exists() and (root/b).exists() and "Status:" in (root/a).read_text() and "Status：" not in (root/b).read_text()]; [bad.append(str(root/b)+": missing implementation authorization no") for a,b in pairs if (root/a).exists() and (root/b).exists() and "implementation_authorized: no" in (root/a).read_text() and "implementation_authorized: no" not in (root/b).read_text()]; print("missing", missing); print("bad", bad); raise SystemExit(1 if missing or bad else 0)'
```

Result：exit 0；`missing []`；`bad []`。

```text
rg -n "0\.9\.7 documentation gate complete|0\.9\.7.*implementation authorized|0\.9\.8.*Status: planned|0\.9\.8.*Status：planned|0\.9\.9.*Status: planned|0\.9\.9.*Status：planned|0\.9\.8-brain-inspired-agent-continuity-and-consolidation-evidence-implementation-authorized" docs/iterations/v0.9/v0.9-plan.md docs/iterations/v0.9/v0.9-plan.zh.md docs/iterations/v0.9/CURRENT_STATE.md docs/iterations/v0.9/CURRENT_STATE.zh.md docs/iterations/v0.9/README.md docs/iterations/v0.9/README.zh.md
```

同步 parent `v0.9-plan.md` 和 `v0.9-plan.zh.md` 前，初次结果为 exit 0，命中 stale
status。修复后：exit 1，无输出。

## Test Results

Documentation drafting 阶段未运行 code tests，因为当时 implementation 尚未授权。

Implementation closeout verification：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_external_narrative_diagnostic_boundary.py -q
```

Result：exit 0；`23 passed in 0.53s`。

```text
cd backend && .venv/bin/python -m pytest app/tests/test_external_narrative_diagnostic_boundary.py app/tests/test_agent_continuity_consolidation_evidence.py app/tests/test_event_api_compat.py app/tests/test_runtime_bounded_run.py app/tests/test_archive_snapshot_summary.py app/tests/test_public_handoff_contract_api.py app/tests/test_rule_linked_evolution_legality.py -q
```

Result：exit 0；`102 passed in 1.83s`。

```text
cd backend && .venv/bin/python -m pytest app/tests -q
```

Result：exit 0；`389 passed in 4.37s`。

```text
git diff --check
```

Result：exit 0；无输出。

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.9-external-narrative-and-diagnostic-dialogue-boundary"); expected={"README","intent","contract","technical-design","test-plan","plan","review"}; names={p.name for p in root.glob("*.md")}; missing=[]; [missing.append(f"{base}.md") for base in sorted(expected) if f"{base}.md" not in names]; [missing.append(f"{base}.zh.md") for base in sorted(expected) if f"{base}.zh.md" not in names]; print("files", len(names)); print("missing", missing); raise SystemExit(1 if missing else 0)'
```

Result：exit 0；`files 14`；`missing []`。

## Compatibility Review

Draft contract 要求与 existing event、runtime、snapshot/archive、world direction、
rule-linked event legality、Agent continuity、Agent memory 和 public handoff surfaces
保持 additive compatibility。

Implementation compatibility review：

- Existing event、runtime、archive/snapshot、Agent continuity 和 rule-linked legality
  response shapes 保持 additive-compatible。
- 新 projection 和 diagnostic endpoints 是 additive public surfaces。
- Accepted projection/diagnostic artifacts 不追加 canonical events、不写 Agent memory、
  不修改 world state，也不记录 in-world dialogue。
- Public event refs 会 against event log 校验；public snapshot refs 会 against snapshot store 校验。
- Agent continuity refs 在本包中保持 public type-only refs，并为后续 checker consumption 做准备。

## Scope Review

Draft scope 限定为 future active-backend public narrative projection 和 out-of-world
diagnostic dialogue boundary evidence。Provider live calls、generated-result creation、
checker execution 或 fixture changes、external validation、Validation Client changes、
frontend UI、player-in-world chat、narrative game content、diagnostic-to-memory bridges、
durable scheduling 和 `backend/worldengine/` changes 仍未授权。

Implementation scope review：

- Implementation 保持在 `backend/app/`，以及本 package review/README 和 parent v0.9
  route/status handoff docs。
- 未添加 `backend/worldengine/`、frontend、Validation Client、external repository、checker
  fixture、generated-result、durable scheduling、player-in-world chat、narrative game content
  或 diagnostic-to-memory bridge work。
- Live provider calls、generated-result creation、checker execution 和 external validation
  未运行，且仍未授权。

## Subagent Findings

Documentation/contract evaluator：

```text
agent: 019e9b28-a596-79f2-b414-6256cf0237e1
scope: read-only 0.9.9 documentation/contract/design/test-plan review
status: FAIL
```

Findings：

- P1：parent `v0.9-plan.md` 和 `v0.9-plan.zh.md` 仍保留 stale `0.9.7`
  implementation-authorized 以及 `0.9.8`/`0.9.9` planned statuses。
- P2：本 review 未明确记录 dirty worktree 中有 earlier v0.9 work 留下的 pre-existing
  non-`0.9.9` backend implementation changes。

Repairs：

- 同步 parent `v0.9-plan.md` 和 `v0.9-plan.zh.md` 到当前 `0.9.8` complete /
  `0.9.9` documentation-review state。
- 添加上面的 current worktree note，区分 `0.9.9` documentation-stage scope 与
  pre-existing implementation changes。

Documentation/contract re-review：

```text
agent: 019e9b28-a596-79f2-b414-6256cf0237e1
scope: read-only 0.9.9 documentation/contract/design/test-plan re-review
status: PASS
```

Verdict：PASS，无 P0/P1/P2/P3 findings。Evaluator 建议只授权 active `0.9.9`
implementation scope，同时保持 provider live calls、generated-result creation、checker
execution、external validation、frontend、Validation Client 和 `backend/worldengine/`
work 未授权。

Implementation-scope evaluator：

```text
agent: 019e9b36-fdc3-73f0-97fc-d493a852612c
scope: read-only 0.9.9 implementation review
status: FAIL
```

Findings：

- P1：accepted projection/diagnostic artifacts 可以没有 source refs。
- P1：narrative 或 diagnostic text 可以声称 canonical mutation，而 flags 仍为 false。
- P1：HTTP validation redaction 缺少 raw provider request/response variants。
- P2：schema-level private marker rejection 缺失。
- P2：focused tests 未覆盖这些 negative cases。

Repairs：

- Projection 和 diagnostic helpers 现在要求至少一个 public evidence ref。
- Helpers 会拒绝声称 canonical state mutated、canonical events appended、Agent memory written
  或 in-world dialogue recorded 的文本。
- External projection schemas 现在执行 schema-level private marker rejection。
- HTTP validation-error sanitizer 现在 redacts raw provider request/response marker variants。
- Focused tests 现在覆盖 diagnostic extra fields、schema private marker validation、raw provider
  request loc redaction、empty refs、textual mutation claims、explicit canonical event append flags
  和 expanded marker variants。

Implementation re-review：

```text
agent: 019e9b36-fdc3-73f0-97fc-d493a852612c
scope: read-only 0.9.9 implementation re-review
status: PASS
```

Verdict：PASS，无 P0/P1/P2/P3 findings。Evaluator 报告 routes 对 projection/diagnostic
surfaces 保持 additive 和 non-mutating，accepted artifacts 保持所有 canonical/event/memory/dialogue
flags 为 false，scope check 中没有 frontend 或 `backend/worldengine/` changes。

## Unresolved P1/P2/P3

- Implementation repairs 和 closeout evidence update 后无。

## Final Assessment

本包记录的 scoped active-backend `0.9.9` narrative projection and diagnostic dialogue
boundary work 已完成 implementation。

Final route：

```text
0.9.10-llm-backed-autonomous-checker-and-fixtures-documentation-package-needed
```
