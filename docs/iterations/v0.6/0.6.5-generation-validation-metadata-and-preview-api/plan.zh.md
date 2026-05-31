# 计划

状态：review complete

## 目标

创建并评审 `0.6.5` generation validation、metadata 和 preview API package，然后只在
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
- `docs/iterations/v0.6/README.md`
- `docs/iterations/v0.6/GOAL_RUNNER.md`
- `docs/iterations/v0.6/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.6/v0.6-plan.md`
- `0.6.1` generation contract
- `0.6.2` deterministic generator core contract and review
- `0.6.3` structured plan compiler contract and review
- `0.6.4` plan import boundary contract and review
- `backend/app/schemas/api.py`
- `backend/app/api/app_factory.py`
- `backend/app/api/routes/__init__.py`
- current API envelope compatibility tests
- current generation schemas and core implementation

## 执行步骤

1. 创建七份必需 package docs 和中文镜像。
2. 初始状态保持为 `planned / ready for review`，且
   `implementation_authorized: no`。
3. 运行 documentation checks。
4. 请求 documentation/contract evaluator review。
5. Evaluator PASS 后，记录 `implementation_authorized: yes` 并同步 parent status
   surfaces。
6. 只实现已批准的 preview schema/core/route/test files。
7. 运行 focused、adjacent、full backend、diff 和 scope checks。
8. 请求 implementation-scope、code-review、validation-evidence 和 closeout
   consistency evaluators。
9. 如果全部 checks 通过，标记 `0.6.5` review complete，并交接给 `0.6.6`。

## 要创建或更新的文件

Documentation stage：

- `docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api/**`
- parent v0.6 status 和 review files。

Implementation stage 授权后：

- `backend/app/schemas/world_generation.py`
- `backend/app/core/world_generation.py`
- `backend/app/api/routes/world_generation.py`
- `backend/app/api/routes/__init__.py`
- `backend/app/api/app_factory.py`
- `backend/app/tests/test_generation_preview_api.py`
- 仅在需要时更新 existing focused generation/API compatibility tests。
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

## 停止条件

- 授权前开始 implementation。
- Documentation/contract evaluator 报告 P0/P1 或 blocking P2。
- Preview API 需要改变 existing envelopes 或 shared error handlers。
- Preview 需要 persistence、frontend UI、runtime loading/readiness、regeneration、
  live AI access、prompts、provider traces、concrete content、external validation
  internals、projection readiness 或 `backend/worldengine/**`。
- Implementation 需要 approved list 之外的文件。
- Focused 或 regression tests 失败，且无法诚实记录为 passed。

## 交接

Closeout 后，`0.6.6-regeneration-and-runtime-readiness-integration` 接收 public
preview、validation diagnostics 和 bounded metadata semantics，用于 regeneration 和
runtime-readiness work。
