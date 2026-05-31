# 计划

状态：review complete

## 文件

创建：

- `backend/app/schemas/agent_memory.py`
- `backend/app/agent/memory.py`
- `backend/app/tests/test_agent_memory_substrate.py`
- 本目录下的 package docs 和 mirrors。

修改：

- 仅为准确交接修改父级 v0.5 status/review surfaces。

不要触碰：

- `backend/worldengine/**`
- frontend files
- API routes
- app factory wiring
- migrations
- fixtures
- generated result artifacts
- external repositories

## 步骤

1. 读取必需 project、v0.5 和 `0.5.1` contract docs。
2. 起草完整 package docs 和中文镜像。
3. 运行 documentation checks。
4. 运行 documentation/contract evaluator。
5. 如果 evaluator 报告无 P1/blocking P2，在 `review.md` 记录
   `implementation_authorized: yes`。
6. 先添加 focused backend tests。
7. 运行 focused tests 并记录预期 red failure。
8. 添加最小 schema 和 in-memory store code。
9. 重新运行 focused tests 直到 green。
10. 运行相邻 compatibility tests。
11. 运行 implementation-scope evaluator。
12. 运行 code-review evaluator。
13. 运行 validation-evidence evaluator。
14. 只有 checks 通过后才更新 review evidence 和 closeout status。

## 停止条件

出现以下情况停止：

- 缺少必需 docs 或 mirrors。
- documentation/contract evaluator 报告 P1 或 blocking P2。
- implementation 需要 API routes、loop integration、app factory wiring 或 persistence。
- code change 触及 `backend/worldengine/**`。
- action semantics 需要改变。
- tests failed 且无法在 approved scope 内修复。

## 验证

运行 `test-plan.md` 中的 exact commands，并在 `review.md` 记录 exit status、
pass/fail counts、skipped checks 和 rationale。

## Review 更新步骤

更新 `review.md` 和 `review.zh.md`，记录 changed files、commands run、test results、
compatibility review、scope review、subagent/evaluator evidence、unresolved findings 和
final assessment。
