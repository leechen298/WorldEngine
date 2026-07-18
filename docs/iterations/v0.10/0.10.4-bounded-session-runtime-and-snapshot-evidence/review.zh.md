# Review

英文版本：`review.md`。

状态：`final / focused verification passed`
implementation_authorized: yes
evidence_execution_authorized: no
provider_live_call_authorized: no
external_validation_authorized: no

## Changed Files

Documentation draft 包含本 package 的 README、intent、contract、technical-design、test-plan、
plan、review 和中文镜像。

Planned implementation files 见 `README.md`。

## Commands Run

```bash
git diff --check
```

结果：通过，无输出。

```bash
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.10/0.10.4-bounded-session-runtime-and-snapshot-evidence')
required = {
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
}
missing = sorted(name for name in required if not (pkg / name).exists())
empty = sorted(name for name in required if (pkg / name).exists() and (pkg / name).stat().st_size == 0)
print({'files': len(list(pkg.glob('*.md'))), 'missing': missing, 'empty': empty})
raise SystemExit(1 if missing or empty else 0)
PY
```

结果：`{'files': 14, 'missing': [], 'empty': []}`。

```bash
rg -n "implementation_authorized: yes|evidence_execution_authorized: yes|provider_live_call_authorized: yes|external_validation_authorized: yes" docs/iterations/v0.10/0.10.4-bounded-session-runtime-and-snapshot-evidence
```

结果：只有 plan instructions 提到未来授权字符串；没有打开 active authorization field。

## Test Results

```bash
python3 -m pytest app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py
```

evaluator fix 前 initial result：29 passed。

repeated-run snapshot evidence 修复后结果：30 passed。

```bash
python3 -m pytest app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py app/tests/test_llm_worldview_generation_api.py app/tests/test_archive_snapshot_summary.py
```

evaluator fix 前 initial result：53 passed。

repeated-run snapshot evidence 修复后结果：54 passed。

## Documentation / Contract Review

Read-only evaluator `019ebd1a-6c2f-7ce1-ae01-6b2ed62722bb`：PASS。

Evidence:

- Required mixed-package docs and mirrors 已存在：14 个 markdown files，无 missing 或 empty files。
- Active auth fields 在 approval 前保持关闭。
- Scope 排除 live provider、dashboard、checker fixtures、Validation Client、generated results、
  external validation、durable persistence/migration 和 `backend/worldengine/`。
- Allowed files 限定为 session schemas/store/routes、manifest route、focused backend tests
  和 package/parent docs。
- Test plan 覆盖 focused 和 expanded focused backend regression，并明确排除 live provider/E2E/
  Validation Client/external checker suites。
- 无 P1/P2 findings 阻止 implementation authorization。

## Compatibility Review

Draft contract 是 additive。它包装现有 runtime controls 和 snapshot stores，不破坏现有
`/runtime/*` endpoints。

## Scope Review

Draft 排除 infinite default runs、live provider calls、provider-cost execution、
dashboard UI、checker fixtures、Validation Client implementation、generated result files、
external validation、durable persistence/migration 和 `backend/worldengine/`。

Implementation closeout evaluator `019ebd1a-6c2f-7ce1-ae01-6b2ed62722bb`
initial result：BLOCKED。

Findings and resolution:

- P1: fixed。第一版 implementation 混用了 global `snapshot_count_before` 和 run-window
  filtered `snapshot_count_after`，导致 repeated bounded runs 可能返回 new snapshot ids，
  但 `snapshot_delta_count: 0`。当前 route 已改为 run 前后都记录 global snapshot counts，
  同时保留 run-window snapshot ids 作为 evidence。已新增
  `test_repeated_session_run_reports_new_snapshot_delta`。
- P2: accepted as broader dirty-worktree scope note，不是 0.10.4 implementation drift。
  evaluator 看到的是前序已完成 v0.10 packages 留下的 existing dirty files：
  `backend/app/api/app_factory.py`、`backend/app/api/routes/__init__.py` 和
  `backend/app/schemas/world.py`。0.10.4 implementation 仍限定在 allowed session schema/store、
  session route、manifest route、focused tests 和 package/parent docs。

## Unresolved Findings

Implementation closeout evaluator re-review
`019ebd1a-6c2f-7ce1-ae01-6b2ed62722bb`：PASS。

Evidence:

- P1 repeated-run snapshot evidence bug 已修复。Read-only evaluator 使用
  `WORLD_SNAPSHOT_INTERVAL_TICKS=1` 复现两个 consecutive bounded session runs；第二次 run
  报告 `snapshot_count_before: 2`、`snapshot_count_after: 4`、
  `snapshot_delta_count: 2`，并返回两个 run-window `snapshot_ids`。
- route 现在用 run 前后的 global snapshot counts 计算 delta，同时保留 run-window snapshot ids。
- P2 broader dirty-worktree scope note 已接受，不阻止 0.10.4 closeout。
  `backend/app/api/app_factory.py`、`backend/app/api/routes/__init__.py` 和
  `backend/app/schemas/world.py` 已记录为前序 v0.10 packages 的 broader dirty-worktree files，
  不是新的 0.10.4 implementation drift。
- 0.10.4 仍限定在 session schema/store、session route、manifest route、focused tests 和
  package/parent docs。
- Evaluator reran `git diff --check`：通过，无输出。

- P1: none。
- P2: none。
- P3: none。

## Final Assessment

PASS。0.10.4 implementation 已在 package scope 内完成，focused verification 已通过。
