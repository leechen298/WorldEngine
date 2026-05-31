# 计划

Status: review complete

## 文件

文档阶段创建：

- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/README.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/README.zh.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/intent.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/intent.zh.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/contract.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/contract.zh.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/technical-design.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/technical-design.zh.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/test-plan.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/test-plan.zh.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/plan.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/plan.zh.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/review.md`
- `docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core/review.zh.md`

documentation/contract review 授权 implementation 后，可以创建：

- `backend/app/schemas/world_generation.py`
- `backend/app/core/world_generation.py`
- `backend/app/tests/test_world_generation_schema.py`
- `backend/app/tests/test_template_catalog.py`
- `backend/app/tests/test_deterministic_world_generation.py`

不触碰：

- `backend/app/api/**`
- `backend/app/schemas/api.py`
- `backend/app/schemas/world_cell.py`
- `backend/app/schemas/entity.py`
- `backend/app/core/worldspec_loader.py`
- `backend/app/core/runtime_context.py`
- `backend/app/core/runtime_engine.py`
- `backend/app/agent/**`
- `backend/app/world/**`
- `frontend/**`
- migrations、fixtures、generated result files、external repositories
- `backend/worldengine/**`

## 执行步骤

1. 读取 `CURRENT_STATE.md`、v0.6 parent docs、`0.6.1` reviewed contract 和 review
   evidence、当前 schema/loader/runtime-context code，以及现有 adjacent tests。
2. 起草本 package 的完整 docs 和中文镜像，并保持 `implementation_authorized: no`。
3. 运行 `test-plan.md` 中的 documentation-stage checks。
4. 派发 documentation/contract evaluator。
5. 如果 evaluator 报告 blocking P1/P2，则在 documentation scope 内修复或停止。
6. 如果 evaluator 报告 PASS，则更新 package `review.md` 和 `.zh.md`，记录
   `implementation_authorized: yes`，并同步 parent status surfaces。
7. 只有在授权后，才为 generation schemas、template catalog validation、
   deterministic generation、loader compatibility 和 runtime-context compatibility
   编写 tests。
8. 只实现已授权 backend schema/service modules。
9. 运行 focused tests、adjacent compatibility tests、full backend regression、
   `git diff --check` 和 implementation scope guard。
10. 按 `GOAL_RUNNER.md` 要求派发 implementation-scope、code-review、
    validation-evidence 和 closeout consistency evaluators。
11. 更新 package 和 parent review evidence。只有在无 unresolved P1/P2 时，才交接给
    `0.6.3`。

## 阶段边界

- Documentation review 必须先于 implementation 完成。
- 只有 documentation/contract evaluator PASS 后，才能在本 package `review.md` 中记录
  `implementation_authorized: yes`。
- Implementation 不得扩展到 API、frontend、persistence、runtime behavior、
  structured-plan compiler、AI import、regeneration、external validation 或 projection
  readiness。

## 停止条件

出现以下情况时停止：

- 必需 docs 或 mirrors 缺失。
- evaluator 报告 blocking P1/P2。
- implementation 需要 forbidden files。
- generated output 需要 concrete world content 或 story data。
- deterministic behavior 无法通过 stable inputs 测试。
- tests 失败且无法在授权范围内修复。
- package 与 parent docs 之间 status surface drift。

## Review 更新步骤

记录：

- changed files。
- commands run。
- exact test results。
- subagent/evaluator evidence。
- compatibility review。
- scope review。
- unresolved P1/P2/P3。
- implementation authorization state。
- final assessment and handoff。
