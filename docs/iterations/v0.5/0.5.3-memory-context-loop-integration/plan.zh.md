# 计划

状态：review complete

## 文件

创建：

- 本 package docs 和中文镜像。

授权后修改：

- `backend/app/schemas/agent_loop.py`
- `backend/app/agent/perception.py`
- `backend/app/api/app_factory.py`
- `backend/app/tests/` 下的 focused tests

不要触碰：

- `backend/worldengine/**`
- frontend files
- public memory API routes
- action adapter semantics
- migrations
- fixtures
- generated result artifacts
- external repositories

## 步骤

1. 读取 `0.5.2` review 和 memory substrate implementation。
2. 起草 package docs 和中文镜像。
3. 运行 documentation checks。
4. 运行 documentation/contract evaluator。
5. 只有 evaluator pass 后，才记录 `implementation_authorized: yes`。
6. 添加 focused failing test，并运行 TDD red。
7. 实现 additive memory context schema/perception/app wiring。
8. 重新运行 focused tests 直到 green。
9. 运行相邻 compatibility tests。
10. 运行 implementation-scope、code-review、validation-evidence 和 closeout
    consistency evaluators。
11. 只有 gates 通过后，才更新 review evidence 和 parent handoff status。

## 停止条件

出现以下情况停止：

- evaluator 报告 P1 或 blocking P2。
- implementation 需要修改 action semantics。
- implementation 需要 public memory APIs 或 loop request memory selectors。
- code 触及 `backend/worldengine/**`。
- tests failed 且超出 approved scope。

## 验证

运行 `test-plan.md` 中的 exact commands，并在 `review.md` 中记录 exit status、
pass/fail counts、skipped checks 和 rationale。

## Review 更新步骤

更新 `review.md` 和 `review.zh.md`，记录 changed files、commands run、test results、
compatibility review、scope review、evaluator evidence、unresolved findings 和 final assessment。
