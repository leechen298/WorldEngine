# Plan

英文原文：`plan.md`。

## 阶段 1：文档门禁

1. 创建完整 package document set 和镜像。
2. 运行 documentation completeness、authorization 和 whitespace checks。
3. 请求 documentation evaluator review。
4. 记录 findings，并在需要时修复文档。
5. 只有 review 通过后才授权 implementation。

## 阶段 2：TDD Red

1. 在 `backend/app/tests/test_session_narrative_diagnostic_inspection_api.py` 增加聚焦失败测试。
2. 覆盖 session/tick-range/branch/Agent-focused narrative projection。
3. 覆盖 out-of-world diagnostic inspection。
4. 覆盖 read-only behavior 和 redaction failures。

## 阶段 3：实现

1. 增加 additive public inspection schemas。
2. 增加 read-only inspection helper logic，尽量复用 external projection boundary validation。
3. 增加 session route endpoints。
4. 增加 manifest surfaces。
5. 实现保持在 active package scope 内，并避开 `backend/worldengine/`。

## 阶段 4：验证

1. 运行新的聚焦测试文件。
2. 运行 `test-plan.md` 中的 package focused suite。
3. 运行 `git diff --check`。
4. 运行 active-package whitespace checks。
5. 运行一个小型 public evidence probe，证明没有 event/memory/direction-queue mutation。

## 阶段 5：评审与交接

1. 请求 implementation-scope evaluator review。
2. 修复所有 scope 内 P1/P2 findings。
3. 记录 changed files、commands、results、compatibility、scope review、evaluator evidence 和 unresolved findings。
4. 更新 parent route 到 `0.12.4-validation-client-mvp-evidence-handoff`。
