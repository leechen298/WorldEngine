# Review

英文版本：`review.md`。

状态：`validation execution authorized`
implementation_authorized: yes
evidence_execution_authorized: yes
provider_live_call_authorized: no
external_validation_authorized: no

## Changed Files

Documentation draft 包含本 package 的 README、intent、contract、technical-design、test-plan、
plan、review 和中文镜像。

Planned closeout files 见 `README.md`。

## Commands Run

```bash
git diff --check
```

结果：通过，无输出。

```bash
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.10/0.10.6-v0.10-validation-and-handoff')
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
rg -n "implementation_authorized: yes|evidence_execution_authorized: yes|provider_live_call_authorized: yes|external_validation_authorized: yes" docs/iterations/v0.10/0.10.6-v0.10-validation-and-handoff
```

结果：只有 plan instructions 提到未来授权字符串；没有打开 active authorization field。

## Test Results

Validation in progress 在 closeout 前发现一个 stale manifest evidence issue：

- P2 repair authorized within this package：0.10.5 dashboard E2E 已通过后，`/manifest`
  仍报告 "dashboard MVP session flow is planned for 0.10.5" 和
  "dashboard MVP session flow is not implemented until 0.10.5"。这是 stale closeout/discovery
  evidence issue，不是新产品功能。修复范围仅限 manifest discovery text 和 focused manifest tests。

最终 validation 前，该 stale manifest evidence issue 已修复。

Validation commands:

```bash
python3 -m pytest app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py app/tests/test_llm_worldview_generation_api.py app/tests/test_archive_snapshot_summary.py
```

结果：54 passed。

```bash
pnpm test
```

结果：7 test files passed；41 tests passed。

```bash
pnpm build
```

结果：passed。Vite 输出 existing large chunk warning。

```bash
pnpm test:e2e -- dashboard.spec.ts
```

Sandboxed attempt 结果：测试前失败，因为 backend web server 无法绑定 `127.0.0.1:18000`
（`operation not permitted`）。

Escalated rerun 结果：7 passed，包括
`dashboard-mvp-session-flow creates runs and shows snapshot evidence`。

```bash
python3 - <<'PY'
from fastapi.testclient import TestClient
from app.api.app_factory import create_app
payload = TestClient(create_app()).get('/manifest').json()
print('worldengine_version', payload['worldengine_version'])
print('manifest_status', payload['manifest_status'])
print('mvp_contract_version', payload['mvp_contract_version'])
print('provider_readiness', payload['provider']['provider_readiness'])
surfaces = [
    (item['method'], item['path'], item['status'], item['validation_status'])
    for item in payload['public_surfaces']
    if item['path'].startswith('/sessions')
]
print('session_surfaces', surfaces)
print('unsupported_items', payload['checker_handoff']['unsupported_items'])
print('blockers', payload['blockers'])
PY
```

结果：

```text
worldengine_version v0.10
manifest_status blocked
mvp_contract_version v0.10-debug-handoff
provider_readiness not_configured
session_surfaces [('POST', '/sessions', 'available', 'pass'), ('POST', '/sessions/from-worldview', 'available', 'pass'), ('GET', '/sessions', 'available', 'pass'), ('GET', '/sessions/{session_id}', 'available', 'pass'), ('GET', '/sessions/{session_id}/status', 'available', 'pass'), ('POST', '/sessions/{session_id}/run', 'available', 'pass'), ('POST', '/sessions/{session_id}/pause', 'available', 'pass'), ('POST', '/sessions/{session_id}/resume', 'available', 'pass'), ('GET', '/sessions/{session_id}/snapshots', 'available', 'pass')]
unsupported_items []
blockers []
```

`manifest_status` 仍为 `blocked`，因为 provider readiness 是 `not_configured`；这是诚实的
provider/live-evidence caveat，不是 runnable session slice failure。

```bash
git diff --check
```

结果：通过，无输出。

## Documentation / Contract Review

Read-only evaluator `019ebd39-85ed-7c71-97bf-4a5d1f3cd841`：PARTIAL。

没有 P1。在 P2 findings 修复或显式接受前，authorization 仍保持关闭。

P2 findings and repairs:

- P2 fixed：`contract.md` 未直接承载 required public concepts、allowed changes、
  forbidden changes、compatibility requirements 和 out-of-scope follow-ups。现在 contract
  已直接补齐这些 sections。
- P2 fixed：`test-plan.md` 覆盖 required command families，但缺少 explicit expected results
  和 no-unverified-claims recording rule。现在 test plan 已为每组命令补充 expected results，
  并增加只记录 current-session evidence 的 recording rules。
- P2 fixed：中文镜像保留了核心语义，但英文和中英混排过多。受影响中文镜像已改为更自然的中文
  section titles 和 explanations，同时保持 status 和 scope semantics。

Read-only evaluator re-review `019ebd39-85ed-7c71-97bf-4a5d1f3cd841`：PASS。

Evidence:

- `contract.md` 现在直接包含 Public Concepts、Allowed Changes、Forbidden Changes、
  Compatibility Requirements 和 Out-of-Scope Follow-Ups。
- `test-plan.md` 现在为 backend、frontend、E2E、manifest inspection 和 git diff checks
  补充 expected results，并增加禁止 unverified pass claims 的 Recording Rules。
- 中文镜像保持相同 status、scope、forbidden-change、compatibility、validation 和 closeout
  semantics；没有剩余 blocking mirror mismatch。
- Evaluator 运行 `git diff --check`：通过，无输出。
- Evaluator package completeness/fields check：
  `{'files': 14, 'missing': [], 'empty': [], 'missing_contract_fields': [], 'test_plan_expected_rules': True}`。
- Evaluator authorization scan 在本 update 前未发现 active authorization field open。

Authorization scope：仅限 `test-plan.md` 中列出的 validation commands 和 closeout/handoff
documentation。Provider live-call 和 external validation authorization 仍保持关闭。

## Compatibility Review

Draft contract 验证现有 v0.10 work，不授权 v0.11 或 v0.12 implementation。

## Scope Review

Draft 排除新的 runtime/API/schema/frontend/provider/checker/fixture/Validation Client/
persistence/migration implementation，除非记录 reviewed P1/P2 defect repair。Live provider、
external validation、Agent autonomy 和 `backend/worldengine/` 仍未授权。

## Unresolved Findings

- P1: none。
- P2: none。
- P3: none。

## Final Assessment

PASS。v0.10 runnable session MVP slice 在 reviewed scope 内已有证据支持。Provider live-call、
external validation、Agent autonomy、durable persistence 和 v0.11/v0.12 implementation 均未声明。

## Closeout Evaluator Partial Repair

日期：2026-06-13

Closeout evaluator `019ebd39-85ed-7c71-97bf-4a5d1f3cd841` 在初始 final assessment
之后返回 PARTIAL。没有 P1 findings。两个 P2 consistency findings 是：

- `/manifest` 中 `POST /worlds` 仍有关于 session creation 的旧 public discovery wording。
- 本 package 和 parent v0.10 status docs 需要同步到 validation evidence complete /
  closeout evaluator re-review route。

修复动作：

- 更新 `POST /worlds` public-surface note，明确 session APIs 已作为独立 MVP surfaces 实现。
- 在 `backend/app/tests/test_public_handoff_contract_api.py` 增加 regression assertion，
  防止 "session creation is future scope" 旧文案回归。
- 确认本 package README 以及 parent v0.10 README/CURRENT_STATE docs 已记录
  validation evidence complete / closeout evaluator re-review pending。

修复后重跑证据：

```bash
python3 -m pytest app/tests/test_public_handoff_contract_api.py app/tests/test_world_session_api.py app/tests/test_runtime_bounded_run.py app/tests/test_llm_worldview_generation_api.py app/tests/test_archive_snapshot_summary.py
git diff --check
python3 - <<'PY'
from app.api.app_factory import create_app
from fastapi.testclient import TestClient

payload = TestClient(create_app()).get('/manifest').json()
surfaces = {(s['method'], s['path']): s for s in payload['public_surfaces']}
print('worldengine_version', payload['worldengine_version'])
print('manifest_status', payload['manifest_status'])
print('provider_readiness', payload['provider']['provider_readiness'])
print('worlds_note', surfaces[('POST', '/worlds')]['notes'])
print('session_surfaces', [(s['method'], s['path'], s['status'], s['validation_status']) for s in payload['public_surfaces'] if s['path'].startswith('/sessions')])
print('unsupported_items', payload['checker_handoff']['unsupported_items'])
print('blockers', payload['blockers'])
PY
```

结果：backend expanded focused verification 为 `54 passed`；`git diff --check`
通过；manifest inspection 显示 `worldengine_version v0.10`，
`manifest_status blocked`，原因是 `provider_readiness not_configured`；`POST /worlds`
notes 已更新为 "session APIs are implemented as separate MVP surfaces"；全部
`/sessions*` surfaces 为 available/pass；`unsupported_items []`；`blockers []`。

Closeout evaluator re-review result：PASS。

Evaluator evidence：

- 轻量只读 evaluator `019ebd4f-b3a6-7390-833b-05c5d84eff7f`
  检查当前 source/docs，没有修改文件。
- 之前的 PARTIAL P2 findings 已修复：`/manifest` 的 `POST /worlds` note
  现在说明 session APIs 已作为独立 MVP surfaces 实现；regression test 会拒绝旧的
  "session creation is future scope" wording；final synchronization 前，package 和 parent
  v0.10 docs 已显示 validation evidence complete / closeout evaluator re-review pending。
- Evaluator commands：`git diff --check` 通过；focused TestClient manifest inspection
  显示 `worldengine_version v0.10`，`manifest_status blocked` 仅因
  `provider_readiness not_configured`，全部 `/sessions*` surfaces 为 available/pass，
  `unsupported_items []`，`blockers []`；`python3 -m pytest
  app/tests/test_public_handoff_contract_api.py` 通过，结果为 `9 passed`。
- Evaluator 未重跑或声明：full frontend unit/build/E2E、live provider calls、
  external Validation Client execution、Agent autonomy、durable persistence、
  product readiness、v0.11/v0.12 implementation 或 `backend/worldengine` work。

Final closeout status：PASS。
