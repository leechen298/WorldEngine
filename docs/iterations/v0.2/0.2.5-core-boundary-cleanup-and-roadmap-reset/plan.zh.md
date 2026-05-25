# 计划

英文版本：`plan.md`

## 阶段 1：文档清理

1. 编辑前重新读取 active direction docs 和本 package contract。
2. 搜索 concrete Demo world anchors。pattern list 应保存在 temporary untracked
   path，不写入 tracked Markdown。

3. 更新 `docs/project-north-star.md` 和 `.zh.md`，移除 first concrete Demo
   surface wording，改用 external projection application / external validation world
   language。
4. 更新 `docs/product-model.md` 和 `.zh.md`，保持 product model generic，并移除
   first concrete product surface wording。
5. 更新 `docs/scope-boundaries.md` 和 `.zh.md`，移除 core repository 内允许
   concrete Demo fixtures 的表达。
6. 更新 `docs/roadmap.md` 和 `.zh.md`，使用 reset roadmap：v0.2.5 boundary
   cleanup、v0.2.6 iteration workflow and plan reset、v0.3 generic WorldSpec
   loader/runtime bridge、v0.3.5 external fixture contract readiness、v0.4
   Agent-in-World loop、v0.5 memory/self-continuity、v0.6 world generation、
   v0.7 external validation/projection readiness、v0.8 first external projection
   application readiness。
7. 更新 `AGENTS.md` 和 `AGENTS.zh.md`，从 active agent instructions 中移除 first
   concrete Demo surface guidance。
8. 更新 `README.md` 和 `README.zh.md`，从 current capability limitations 中移除
   historical concrete fixture direction runtime wording。
9. 更新 search 找到的其他 active docs，包括 architecture、glossary、release planning、
   v0.2 index 或 plan docs，只处理其中的 active concrete Demo world direction。
10. 增加 `docs/external-fixture-boundary.md`。
11. 增加 `docs/validation-report-template.md`。
12. 将 `docs/iterations/v0.2/0.2.4-worldspec-reference-fixture/` 标记为不再定义
    future roadmap direction 的 historical iteration artifact。

## 阶段 2：代码与测试清理

1. 删除 `backend/data/world_specs/historical concrete fixture path`，或用
   `backend/data/world_specs/schema_smoke_world.json` 替换。
2. 删除或重写 `backend/app/tests/test_worldspec_fixture.py` 为 generic schema smoke
   test，建议文件名为 `backend/app/tests/test_worldspec_schema_smoke.py`。
3. 确认 generic schema smoke test 验证：
   - `WorldSpec.model_validate(...)`。
   - `schema_version == "0.2"`。
   - root `WorldCell` 存在。
   - recursive `child_cells`。
   - generic `EntityRef` support。
   - `model_dump()` / `model_validate(...)` round-trip。
4. 确认 active test file 不包含 concrete Demo terms。
5. 运行 `test-plan.md` 中的 implementation-stage verification commands。
6. 更新本 package 的 `review.md`，记录 changed files、exact commands run、
   test results、compatibility review、scope review、unresolved findings 和
   final assessment。

## 阶段边界

Phase 1 和 Phase 2 可以在本 package approval 后的同一个 reviewed implementation
stage 中完成，但 implementer 必须把 edits 限定在本 contract 内。不要启动 loader、
runtime bridge、Agent loop、memory、world generation、frontend、external repository
或 new concrete Demo world work。
