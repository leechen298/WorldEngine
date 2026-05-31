# 计划

Status: review complete

## 目标

创建并 review `0.6.4` AI-assisted plan import boundary package，然后仅在
`implementation_authorized: yes` 后实现。

## 已读输入

- `AGENTS.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/v0.6-plan.md`
- `0.6.1` generation contract
- `0.6.3` structured plan compiler contract 和 review
- 当前 generation schemas 和 core implementation

## 执行步骤

1. 创建七个必需 package docs 和中文镜像。
2. 初始 status 保持 `planned / ready for review`，并保持
   `implementation_authorized: no`。
3. 运行 documentation checks。
4. 请求 documentation/contract evaluator review。
5. Evaluator PASS 后，记录 `implementation_authorized: yes` 并同步 parent status surfaces。
6. 只实现已批准的 import schema/core/test files。
7. 运行 focused、adjacent、full backend、diff 和 scope checks。
8. 请求 code-review、validation-evidence 和 closeout consistency evaluators。

## 停止条件

- Authorization 前开始 implementation。
- Import 需要 live provider access、prompts、network、credentials、API、frontend、
  persistence、runtime、Agent/memory、external validation、projection、concrete content 或
  `backend/worldengine/`。
- Imported plans 绕过 structured validation。

## 交接

Closeout 后，`0.6.5-generation-validation-metadata-and-preview-api` 接收已评审的
import/provenance semantics，用于 API exposure。
