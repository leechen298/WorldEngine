# Review

英文原文：`review.md`。

状态：review complete

implementation_authorized: yes
provider_live_call_authorized: no
external_validation_authorized: no

## 文档阶段评审

日期：2026-06-13

这个包准备 session-scoped narrative 和 diagnostic inspection surfaces 的已评审 contract。Documentation evaluator review 已通过，implementation 仅在本 package 范围内授权。

## 变更文件

新增：

```text
docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces/README.md
docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces/README.zh.md
docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces/intent.md
docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces/intent.zh.md
docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces/contract.md
docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces/contract.zh.md
docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces/technical-design.md
docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces/technical-design.zh.md
docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces/test-plan.md
docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces/test-plan.zh.md
docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces/plan.md
docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces/plan.zh.md
docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces/review.md
docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces/review.zh.md
```

Implementation changed：

```text
backend/app/schemas/session.py
backend/app/api/routes/session.py
backend/app/api/routes/world.py
backend/app/tests/test_session_narrative_diagnostic_inspection_api.py
backend/app/tests/test_external_narrative_diagnostic_boundary.py
```

## 已运行命令

文档门禁：

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces')
required = [
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
]
print({'missing': [n for n in required if not (pkg / n).exists()],
       'empty': [n for n in required if (pkg / n).exists() and not (pkg / n).read_text().strip()]})
PY
rg -n "implementation_authorized: yes|provider_live_call_authorized: yes|external_validation_authorized: yes" docs/iterations/v0.12/0.12.3-narrative-and-diagnostic-inspection-surfaces docs/iterations/v0.12/CURRENT_STATE.md docs/iterations/v0.12/README.md docs/iterations/v0.12/review.md
python3 active-package whitespace check
```

结果：

- `git diff --check` 通过，无输出。
- package completeness check 返回 `{'missing': [], 'empty': []}`。
- authorization scan 没有发现 active yes authorization fields。命中项是 parent historical command examples、package command examples 或要求未来授权的 contract text。
- package whitespace check 返回 `{'checked_files': 14, 'problems': []}`。
- documentation evaluator repair 后，`git diff --check` 仍通过，package completeness 仍返回 `{'missing': [], 'empty': []}`，anchored active yes authorization scan 无命中，package whitespace check 仍返回 `{'checked_files': 14, 'problems': []}`。

TDD red：

```bash
cd backend
python3 -m pytest app/tests/test_session_narrative_diagnostic_inspection_api.py -q
```

结果：

- 新聚焦测试文件初始失败，结果为 `6 failed`：session narrative/diagnostic endpoints 和 manifest surfaces 返回 404 或不存在。

Implementation verification：

```bash
cd backend
python3 -m pytest app/tests/test_session_narrative_diagnostic_inspection_api.py -q
python3 -m pytest app/tests/test_session_narrative_diagnostic_inspection_api.py app/tests/test_external_narrative_diagnostic_boundary.py app/tests/test_session_agent_runtime_loop_api.py app/tests/test_session_agent_memory_consolidation_api.py app/tests/test_public_handoff_contract_api.py
git diff --check
python3 active-package whitespace check
python3 session inspection read-only public evidence probe
git diff --name-only -- backend/worldengine
```

Implementation-scope evaluator repair 前的结果：

- 新 session narrative/diagnostic inspection API tests 通过，`6 passed`。
- 聚焦后端验证通过，`47 passed`。
- `git diff --check` 通过，无输出。
- active-package whitespace check 返回 `{'checked_files': 19, 'problems': []}`。
- read-only public evidence probe 返回 `{'projection_status':
  'accepted', 'diagnostic_status': 'accepted', 'diagnostic_classification':
  'out_of_world_diagnostic', 'event_count_unchanged': True,
  'memory_unchanged': True, 'direction_queue_unchanged': True,
  'projection_redaction_status': 'passed', 'diagnostic_redaction_status':
  'passed'}`。
- `git diff --name-only -- backend/worldengine` 无输出。

Implementation-scope evaluator repair verification：

```bash
cd backend
python3 -m pytest app/tests/test_session_narrative_diagnostic_inspection_api.py -q
python3 -m pytest app/tests/test_session_narrative_diagnostic_inspection_api.py app/tests/test_external_narrative_diagnostic_boundary.py app/tests/test_session_agent_runtime_loop_api.py app/tests/test_session_agent_memory_consolidation_api.py app/tests/test_public_handoff_contract_api.py
git diff --check
python3 package/parent whitespace check
python3 fake caller-supplied ref probe
rg stale parent status scan
```

结果：

- 新 session narrative/diagnostic inspection API tests 通过，`7 passed`。
- 聚焦后端验证通过，`48 passed`。
- `git diff --check` 通过，无输出。
- package/parent whitespace check 返回 `{'checked_files': 25, 'problems': []}`。
- fake caller-supplied ref probe 返回 `{'status': 'rejected',
  'diagnostic_codes': ['non_canonical_public_ref'], 'accepted_fake_ref':
  False}`。
- parent stale status scan 只命中 parent review evidence 中较早 package handoff 的 historical route records。

## 兼容性评审

计划中的变更对现有 world-level projection、session Agent runtime、memory/consolidation 和 manifest surfaces 是 additive。聚焦 suite 中现有 world-level projection、session Agent runtime、Agent memory 和 public handoff tests 均通过。

## 范围评审

Implementation 保持在已授权 package 范围内。Provider live-call 和 external validation authorization 保持关闭。本包未做 frontend、persistence/migration、Validation Client、checker automation、complete MVP closeout 或 `backend/worldengine/` 变更。

## 未解决发现

- P1：无记录。
- P2：无 open 项。初始 documentation P2 已修复并 re-review PASS。
- P3：无 open 项。初始 documentation P3 已修复。

## 当前判断

PASS。聚焦 implementation verification 和 implementation-scope evaluator re-review 支持本 scoped read-only inspection surfaces package closeout。

## Documentation Evaluator

只读 documentation evaluator `019ebde6-742c-7513-a9f1-23c3b76a47c5`：初始 NOT PASS。

Findings and repairs：

- P2 exact command issue：focused pytest command 使用 `app/tests/...`，但未说明 backend working directory。已通过在 pytest command 前加入 `cd backend` 修复。
- P3 memory ref clarity：technical design 提到 `source_memory_refs`，但未说明如何映射到现有 evidence ref type。已修复为默认使用 existing public summary-style refs，即 `ref_type: "summary"`，除非经评审确认需要 additive type。

Re-review result：PASS。无剩余 P1/P2 findings。Implementation 可在本 package 范围内授权。Provider live-call 和 external validation 仍未授权。

## Implementation-Scope Evaluator

只读 implementation evaluator `019ebdf0-4146-7811-a559-61cc566803a4`：初始 NOT PASS。

Findings and repairs：

- P2 provenance validation：当其他 public evidence 存在时，session inspection 会接受 caller-supplied fake refs。已通过在接受 caller-supplied event、snapshot、Agent 和 memory summary refs 前校验 canonical public evidence 修复，并增加 fake `source_event_refs` 回归测试。
- P2 parent status drift：focused implementation verification 后，v0.12 parent `CURRENT_STATE`、`README` 和 `review` 仍显示 `0.12.3` documentation-needed / implementation unauthorized。已修复 parent status，改为 `0.12.3` implementation complete with evaluator P2 repair and re-review in progress。
- P2 parent plan status drift：re-review 发现 `v0.12-plan.md` 和 `v0.12-plan.zh.md` 仍显示 `0.12.3` planned / documentation package needed。已修复 package status fields，使其与当前 implementation repair/re-review 状态一致。
- P2 previous package handoff route drift：re-review 发现 `0.12.2` package plans 仍直接指向旧的 `0.12.3` documentation-needed route。已修复为引用 parent `CURRENT_STATE.md` 中的 active `0.12.3` route，而不是 stale concrete route。

Final re-review result：PASS。无剩余 P1/P2 findings。精确的 `0.12.3` documentation-needed route 只出现在 parent historical handoff evidence；fake caller-supplied refs 会被拒绝；parent route/status surfaces 已同步。
