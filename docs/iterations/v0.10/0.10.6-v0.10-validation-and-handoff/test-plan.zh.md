# 测试计划

英文版本：`test-plan.md`。

## 后端

从 `backend` 运行：

```bash
python3 -m pytest app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py app/tests/test_llm_worldview_generation_api.py app/tests/test_archive_snapshot_summary.py
```

预期结果：所选测试全部通过，并记录准确的 pass/fail 数量。任何失败都按 `FAIL` 处理，除非能证明
它不属于 v0.10 reviewed scope。

## 前端

从 `frontend` 运行：

```bash
pnpm test
pnpm build
pnpm test:e2e -- dashboard.spec.ts
```

预期结果：

- `pnpm test`：frontend unit tests 全部通过，记录 test file 和 test 数量。
- `pnpm build`：TypeScript 和 Vite build 通过，记录所有 warning。
- `pnpm test:e2e -- dashboard.spec.ts`：targeted dashboard E2E 通过。如果 sandboxed web
  server 无法绑定本地端口，记录精确失败，并且只在获得 elevated permissions 后重跑。

如果 E2E 被 sandbox port binding 阻塞，使用 approved elevated permissions 重跑，并记录两次
attempts。

## Manifest 检查

从 `backend` 运行：

```bash
python3 - <<'PY'
from fastapi.testclient import TestClient
from app.api.app_factory import create_app
payload = TestClient(create_app()).get('/manifest').json()
print(payload['worldengine_version'])
print(payload['manifest_status'])
print([(item['method'], item['path'], item['status'], item['validation_status']) for item in payload['public_surfaces'] if item['path'].startswith('/sessions')])
print(payload['checker_handoff']['unsupported_items'])
PY
```

预期结果：

- `worldengine_version` 为 `v0.10`。
- manifest status 保持诚实；provider/live evidence 可以继续是 blocked。
- session create/from-worldview/run/pause/resume/snapshots surfaces 可发现，且状态为
  implemented/pass。
- unsupported items 不把 v0.11/v0.12 work 声明为已完成。

## 文档与空白检查

从 repo root 运行：

```bash
git diff --check
```

预期结果：没有 whitespace errors。

## 记录规则

- 除非本 package closeout session 实际运行了对应命令或流程，否则不得声明 test、build、E2E、
  manifest、provider、Validation Client 或 checker result 通过。
- 记录准确 command、working directory、result 和相关 pass/fail counts。
- 如果某个命令被 skipped、blocked，或使用 elevated permissions 重跑，必须记录原因。
- 不得把 earlier package evidence 转成新的 PASS，除非当前 closeout command 重新运行或直接检查了它。

本包不运行 live provider tests、external Validation Client suites 或 v0.11/v0.12 feature validation。
