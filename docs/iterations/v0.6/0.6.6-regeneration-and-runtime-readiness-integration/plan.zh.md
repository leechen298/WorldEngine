# 计划

状态：review complete

## 目标

创建并评审 `0.6.6` regeneration and runtime-readiness package，然后只在
`implementation_authorized: yes` 后 implementation。

## 已读取输入

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/v0.6-plan.md`
- `0.6.5` generation preview API contract and review
- `backend/app/core/worldspec_loader.py`
- `backend/app/core/runtime_context.py`
- `backend/app/core/runtime_engine.py`
- `backend/app/tests/test_worldspec_loader.py`
- `backend/app/tests/test_runtime_context_bridge.py`
- `backend/app/tests/test_runtime_step.py`

## 执行步骤

1. 创建七份必需 package docs 和中文镜像。
2. 初始状态保持为 `planned / ready for review`，且
   `implementation_authorized: no`。
3. 运行 documentation checks。
4. 请求 documentation/contract evaluator review。
5. Evaluator PASS 后，记录 `implementation_authorized: yes` 并同步 parent status
   surfaces。
6. 只实现已批准的 regeneration/readiness schema/core/route/test files。
7. 运行 focused、full backend、diff 和 scope checks。
8. 请求 implementation-scope、code-review、validation-evidence 和 closeout
   consistency evaluators。
9. 如果全部 checks 通过，标记 `0.6.6` review complete，并交接给 `0.6.7`。

## 要创建或更新的文件

Documentation stage：

- `docs/iterations/v0.6/0.6.6-regeneration-and-runtime-readiness-integration/**`
- parent v0.6 status 和 review files。

Implementation stage 授权后：

- `backend/app/schemas/world_generation.py`
- `backend/app/core/world_generation.py`
- `backend/app/api/routes/world_generation.py`
- `backend/app/tests/test_generation_regeneration_api.py`
- 仅在需要时更新 existing focused compatibility tests。
- 本 package review files 和 parent status surfaces。

## 明确范围外文件

- `frontend/**`
- `backend/worldengine/**`
- persistence/repository modules。
- migrations。
- fixtures。
- generated output artifacts。
- external repositories。
- provider SDKs、prompt libraries、network clients 或 background workers。
- `backend/app/api/app_factory.py` 和 `backend/app/api/routes/__init__.py`，除非重新打开
  documentation review。

## 停止条件

- 授权前开始 implementation。
- Regeneration 需要 persistence 或 durable history。
- Readiness checks mutate live runtime state。
- Runtime readiness 变成 full runtime migration。
- 必须改变 `RuntimeEngine.step` 或 event payload semantics。
- Raw `WorldSpec` data 泄露进 runtime events 或 readiness summaries。
- Implementation 需要 approved list 之外的文件。

## 交接

Closeout 后，`0.6.7-dashboard-generation-preview-and-e2e-smoke` 接收稳定
regeneration/readiness API semantics，用于 dashboard preview work。
