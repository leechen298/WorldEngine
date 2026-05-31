# 评审

状态：final / closeout complete

## Changed Files

最终 v0.4 closeout 包含三类变更：

- 公开状态面：`README.md`、`README.zh.md`、`docs/roadmap.md`、`docs/roadmap.zh.md`。
- `docs/iterations/v0.4/**` 下的 v0.4 iteration package 和 evidence docs。
- 已授权 backend implementation/test files：
  - `backend/app/schemas/agent_loop.py`
  - `backend/app/agent/perception.py`
  - `backend/app/agent/action_adapter.py`
  - `backend/app/agent/loop_service.py`
  - `backend/app/api/routes/world_agent.py`
  - `backend/app/api/app_factory.py`
  - `backend/app/tests/test_agent_perception.py`
  - `backend/app/tests/test_agent_action_adapter.py`
  - `backend/app/tests/test_agent_loop_service.py`
  - `backend/app/tests/test_agent_loop_api.py`

未修改 frontend、fixture、migration、external validation runner、projection app 或 legacy `backend/worldengine/` implementation files。

## Files Read

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/current-implementation.md`
- `docs/backend-implementation.md`
- `docs/iterations/v0.4/**` 下的 active v0.4 package documents
- `backend/app/**` 下由 v0.4 触及的 active backend files

## Commands Run

TDD 和 backend 验证：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_agent_action_adapter.py app/tests/test_agent_loop_api.py -q
cd backend && .venv/bin/python -m pytest app/tests/test_agent_perception.py app/tests/test_agent_action_adapter.py app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py -q
cd backend && .venv/bin/python -m pytest app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py app/tests/test_params_agent.py app/tests/test_event_api_compat.py app/tests/test_runtime_step.py -q
cd backend && .venv/bin/python -m pytest app/tests tests -q
```

文档和范围验证：

```bash
git status --short --branch
git diff --check
python3 -c "from pathlib import Path; base=Path('docs/iterations/v0.4/0.4.7-v0.4-final-closeout'); docs=['README','intent','contract','technical-design','test-plan','plan','review','final-closeout']; missing=[str(base/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (base/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(x) for x in missing]; raise SystemExit(1 if missing else 0)"
python3 -c "<changed-file scope guard over git status --short>"
python3 -c "<stale public-status scan over README.md, README.zh.md, docs/roadmap.md, docs/roadmap.zh.md>"
python3 -c "<stale v0.4 status scan excluding command-log self-matches>"
```

## Test Results

- 针对 review feedback 的 red regression run：`3 failed, 12 passed`；失败证明 `noop` 接受 patches，且 loop request/action intent extra fields 会被静默忽略。
- 修复后聚焦 regression：`15 passed in 0.29s`。
- 聚焦 perception/action/loop/API 命令：`24 passed in 0.36s`。
- 聚焦 backend/API compatibility 命令：`35 passed in 0.55s`。
- 全 backend 回归：`139 passed in 0.98s`。
- `git diff --check` passed。
- Final closeout docs/mirrors check 通过，结果为 `missing=0`。
- Changed-file scope guard 通过；针对已授权 v0.4 public status、docs、backend implementation 和 backend test 文件集合，结果为 `changed_files_count=82`、`out_of_scope=0`。
- Stale public-status scan 未发现过时的 planning、ready-for-review 或未实现 v0.4 claims。
- Stale final-status scan 未在 active v0.4 status surfaces 下发现过时的 in-progress、candidate 或 incomplete final-route claims。

## Compatibility Review

v0.4 保持 additive：

- `PerceptionFrame`、`ActionIntent`、`ActionResult`、`LoopStepRequest` 和 `LoopStepResponse` 是新增 agent-loop schemas。
- `ActionIntent`、`LoopStepRequest` 和 loop action patch items 现在拒绝未知字段，并使用既有 422 API envelope，避免 action-boundary payload 被静默丢弃。
- `noop` 仍然无 effect，但现在会拒绝 unexpected `patches`，不产生 event，也不修改状态。
- `params.patch` 使用严格的 `ActionParamPatchItem` schema，保持与 `ParamPatchItem` 兼容，然后继续复用 `ParamValidator`、`ParamDryRunValidator` 和 `WorldState.apply_patch()`。
- `POST /world/agent/loop/step` 是 additive。
- 既有 `/world/agent/params/propose-and-apply`、runtime、event APIs、archive behavior、frontend、fixtures、migrations 和 legacy `backend/worldengine/` 保持兼容。

## Scope Review

最终 scope guard 不是 docs-only。它明确允许已评审的 v0.4 backend implementation/test files 和 public status docs；它会拒绝无关文件，当前结果为 `out_of_scope=0`。

v0.4 仍排除 memory/self-continuity、world generation、external validation runner readiness、projection readiness、concrete world/demo content、frontend changes、fixtures、migrations 和 `backend/worldengine/` 下的新 runtime features。

## Subagent / Evaluator Checkpoint

整个 campaign 使用了 subagent/evaluator checkpoints：

- implementation children 的 documentation/contract authorization checks；
- implementation-scope review；
- code review；
- validation-evidence review；
- documentation closeout consistency checks；
- release-candidate review；
- final closeout review。

Final closeout evaluator 已批准 final status flip。之后的 external review 发现该 flip 后仍有 P1/P2/P3 不一致；本 review 记录修复结果。

Post-repair subagent/evaluator checkpoints 已完成：

- code/API evaluator 确认无 P1/P2，并发现一个 `noop` 携带 `patches` 的 API-level coverage gap；
- 该 P3 已通过 route-level API regression 修复，覆盖 HTTP 200 rejected result、无 params mutation、无 `params.applied` event；
- documentation/status evaluator 确认无 P1，并发现一个 P2 scope wording issue 与 P3 documentation clarity issues；
- wording 和 evidence-entry issues 已在 parent README、root README 和 0.4.7 docs 中修复；
- final read-only evaluator 已复核 public status、active child state、changed-file scope、stale status scans 和 API coverage，结论为无 P1/P2/P3。
- 后续 P2 review 发现 nested `patches[*]` unknown fields 仍会被静默丢弃；已通过严格 loop patch-item schema validation 和 API regression 修复，验证 422、无 mutation、无 `params.applied` event。

## External Review Repair

已修复最新 review findings：

- P1：根 `README.md`、`README.zh.md`、`docs/roadmap.md` 和 `docs/roadmap.zh.md` 现在都报告 v0.4 `final / closeout complete`。
- P1：本顶层 review 现在记录真实 mixed docs/backend changed-file scope，不再沿用初始 docs-only scope。
- P2：`ActionIntent` 和 `LoopStepRequest` 现在禁止 unknown fields；API regressions 验证 422 且不修改状态。
- P2：nested loop `params.patch` items 现在通过严格 `ActionParamPatchItem` 禁止 unknown fields；API regressions 验证 422、无 mutation、无 event。
- P2：`CURRENT_STATE.md` 和 parent README 现在一致说明 final closeout 后没有 active child。
- P3：`noop` 携带 unexpected patches 时现在返回 rejected `ActionResult`，且不修改状态、不产生 event。

## Commands Not Run

未运行 frontend、browser E2E、Agent smoke、build、fixture、migration 和 external validation runner commands，因为 v0.4 未修改或授权这些 surface。

## Unresolved P1/P2/P3

- P1：none。
- P2：none。
- P3：none。

## Final Assessment

final / closeout complete
