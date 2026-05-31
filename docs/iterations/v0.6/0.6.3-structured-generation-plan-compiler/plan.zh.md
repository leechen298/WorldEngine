# 计划

Status: review complete

## 目标

创建并 review `0.6.3` structured generation plan compiler package，然后仅在 package 记录
`implementation_authorized: yes` 后实现。

## 已读权威输入

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/v0.6-plan.md`
- `0.6.1` contract
- `0.6.2` contract、technical design 和 review evidence
- 当前 `backend/app/schemas/world_generation.py`
- 当前 `backend/app/core/world_generation.py`

## 执行步骤

1. 创建本 package 的七个必需 documents 和中文镜像。
2. 初始 documentation draft 保持 status 为 `planned / ready for review`，并保持
   `implementation_authorized: no`；evaluator PASS 后记录 `ready for implementation` 和
   `implementation_authorized: yes`。
3. 运行 documentation checks：diff check、required files、required terms、Chinese
   heading audit 和 changed-file scope guard。
4. 请求 documentation/contract evaluator review。
5. 如果 evaluator 报告 P1 或 blocking P2，修复 docs 并重跑检查。
6. 只有 evaluator PASS 后，才把本 package 更新为 `ready for implementation`，记录
   `implementation_authorized: yes`，并同步 parent status surfaces。
7. 只实现已批准的 schema/core/test files。
8. 运行 focused tests、adjacent compatibility tests 和 full backend tests。
9. 请求 implementation-scope、code-review、validation-evidence 和 closeout
   consistency evaluators。
10. 仅当无 unresolved P1/P2 时 close `0.6.3`。

## 停止条件

- Required package documents 或 mirrors 缺失。
- `implementation_authorized: yes` 前开始 implementation。
- Design 需要 API、frontend、persistence、runtime、Agent/memory、external validation、
  projection 或 `backend/worldengine/` changes。
- Plan compilation 依赖 free-form prompt execution 或 external provider calls。
- Generated data 变成 concrete world/story 或 application-specific content。

## 交接

Closeout 后，`0.6.4-ai-assisted-generation-boundary-and-plan-import` 接收已评审
structured plan input semantics 和 compiler evidence。
