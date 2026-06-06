# Review

英文原文：`review.md`。

Status：implementation complete / focused verification passed

implementation_authorized: yes
provider_live_call_authorized: no
generated_result_creation_authorized: no
external_validation_authorized: no

## 变更文件

Documentation draft：

```text
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/README.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/README.zh.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/intent.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/intent.zh.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/contract.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/contract.zh.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/technical-design.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/technical-design.zh.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/test-plan.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/test-plan.zh.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/plan.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/plan.zh.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/review.md
docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget/review.zh.md
```

Implementation files：

```text
backend/app/schemas/runtime.py
backend/app/core/runtime_engine.py
backend/app/api/routes/runtime.py
backend/app/tests/test_runtime_bounded_run.py
```

## 已运行命令

Documentation checks：

```text
git diff --check
```

结果：exit 0，无输出。

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget"); expected={"README","intent","contract","technical-design","test-plan","plan","review"}; names={p.name for p in root.glob("*.md")}; missing=[]; [missing.append(f"{base}.md") for base in sorted(expected) if f"{base}.md" not in names]; [missing.append(f"{base}.zh.md") for base in sorted(expected) if f"{base}.zh.md" not in names]; print("files", len(names)); print("missing", missing); raise SystemExit(1 if missing else 0)'
```

结果：exit 0；`files 14`；`missing []`。

```text
python3 -c 'from pathlib import Path; root=Path("docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget"); combined="\n".join(p.read_text() for p in root.glob("*.md")); required=["implementation_authorized: n[o]","provider_live_call_authorized: no","generated_result_creation_authorized: no","external_validation_authorized: no","RuntimeRunRequest","RuntimeRunSummary","pause","resume","bounded runtime"]; missing=[term for term in required if term not in combined]; print("missing", missing); raise SystemExit(1 if missing else 0)'
```

结果：documentation review authorization 前 exit 0；`missing []`。

```text
rg -n 'implementation_authorized: y[e]s|provider_live_call_authorized: y[e]s|generated_result_creation_authorized: y[e]s|external_validation_authorized: y[e]s|Status: read[y] for implementation|Status：read[y] for implementation' docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget
```

结果：documentation review authorization 前 exit 1，无输出；当时未发现 implementation
authorization 或 live execution authorization 文案。

Focused implementation test：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_runtime_bounded_run.py -q
```

Initial RED result：exit 2，符合预期，原因是缺少 `app.schemas.runtime`。

GREEN result after implementation：exit 0；`7 passed in 0.28s`。

Post-review P1/P2 regression result after adding max-duration guard and
extra-field coverage：exit 0；`8 passed in 0.31s`。

Related runtime regression：

```text
cd backend && .venv/bin/python -m pytest app/tests/test_runtime_bounded_run.py app/tests/test_runtime_step.py app/tests/test_archive_snapshot_summary.py app/tests/test_dry_run_validation.py app/tests/test_agent_loop_api.py -q
```

Initial result：exit 0；`53 passed in 0.91s`。

Post-review P1/P2 regression result：exit 0；`54 passed in 0.94s`。

Backend regression：

```text
cd backend && .venv/bin/python -m pytest app/tests -q
```

Initial result：exit 0；`296 passed in 2.84s`。

Post-review P1/P2 regression result：exit 0；`297 passed in 2.87s`。

Final closeout verification after review and parent route documentation updates：

- `git diff --check`：exit 0，无输出。
- `cd backend && .venv/bin/python -m pytest app/tests/test_runtime_bounded_run.py -q`：
  exit 0；`8 passed in 0.31s`。
- `cd backend && .venv/bin/python -m pytest app/tests/test_runtime_bounded_run.py app/tests/test_runtime_step.py app/tests/test_archive_snapshot_summary.py app/tests/test_dry_run_validation.py app/tests/test_agent_loop_api.py -q`：
  exit 0；`54 passed in 0.88s`。
- `cd backend && .venv/bin/python -m pytest app/tests -q`：exit 0；
  `297 passed in 2.72s`。

## 测试结果

Focused、related runtime 和 backend regression tests 已按上文记录通过，包括 documentation
route updates 后的 final closeout verification。Provider、checker、external validation、
generated-result、E2E、autonomous 和 Validation Client tests 未运行，因为本包不授权这些工作。

## 兼容性审查

Implementation 添加 additive runtime-control schemas、synchronous in-memory bounded run
behavior 和 runtime API endpoints，同时在 regression tests 下保持既有 `/runtime/step`、
`/runtime/state`、event、snapshot、archive、world params、Agent loop 和 world generation
behavior。

## 范围审查

Implementation 保持在 active-backend in-memory bounded runtime controls 范围内。它没有添加
live provider calls、generated-result creation、checker execution、external validation、
Validation Client code、frontend UI、durable scheduling、event legality、Agent continuity 或
`backend/worldengine/` changes。

## Subagent Findings

Read-only documentation/contract evaluator：

```text
agent: 019e98bb-e5c2-7b61-a6fc-afd598a87fd4
scope: docs/contract/test-plan/mirror review only
status: initial review complete
```

Initial verdict：FAIL，原因是一个 blocking P2；没有 P0/P1。

- P2：`test-plan.md` 和 `test-plan.zh.md` 没有明确要求 focused tests 覆盖 public run
  summary fields，虽然 contract exit criteria 要求 public run summary coverage。

已应用修复：

- `test-plan.md` 和 `test-plan.zh.md` 现在明确要求 focused tests 覆盖 public run summary
  fields。

Final documentation gate assessment：

- P0：none。
- P1：none。
- P2：本地修复后 none。
- Implementation 仅在 reviewed active-backend in-memory `0.9.5` bounded runtime control
  scope 内授权。
- Provider live calls、generated-result creation、checker execution、external validation、
  Validation Client changes、frontend UI、durable scheduling、event legality、Agent continuity
  和 `backend/worldengine/` 仍未授权。

Implementation-scope review verdict：initial FAIL，包含一个 P1 和一个 P2。

- P1：tick-targeted bounded runs 没有执行 `max_duration_seconds` guard。
- P2：extra-field rejection 已通过 `extra="forbid"` 实现，但 focused tests 未覆盖。

已应用修复：

- 增加 `RuntimeRunRequest` 和 `/runtime/run` extra-field rejection focused tests。
- 增加 tick-targeted runs 在下一步会超过 `max_duration_seconds` 前停止的 focused test。
- 增加 `max_duration_reached` stop reason。
- 更新 `RuntimeEngine.run_bounded()`，在下一步会超过 `max_duration_seconds` 前停止。

Implementation re-review verdict：PASS。

- Agent：`019e98bb-e5c2-7b61-a6fc-afd598a87fd4`。
- Result：没有新的 P0/P1/P2/P3 findings。
- P1 已关闭：tick-targeted runs 现在会在下一次 `step()` 超过
  `max_duration_seconds` 前停止，且 `max_duration_reached` 是 public stop reason。
- P2 已关闭：extra-field rejection 仍由 `extra="forbid"` 执行，并且现在已有 focused
  schema 和 API tests 覆盖。
- Scope 仍干净：reviewed `0.9.5` path 中未发现 live provider calls、
  generated-result creation、checker execution、external validation、Validation Client work、
  frontend UI work、durable scheduling/background worker behavior、event legality、Agent
  continuity 或 `backend/worldengine/` changes。

## 未解决 P1/P2/P3

- 无。

## 最终评估

Implementation 已在 reviewed active-backend in-memory bounded runtime-control scope 内完成。
Focused、related runtime 和 backend regression verification 已按上文记录通过；只读
implementation 复审报告 PASS，没有未解决 P1/P2/P3 findings。

Provider live calls、generated-result creation、checker execution、external validation、
Validation Client changes、frontend UI、durable scheduling、event legality、Agent
continuity 和 `backend/worldengine/` changes 仍未授权，也未声明通过。
