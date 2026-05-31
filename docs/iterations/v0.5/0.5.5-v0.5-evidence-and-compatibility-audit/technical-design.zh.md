# 技术设计

状态：review complete

## 设计类型

Documentation-only audit。

不授权 runtime、schema、service、API、frontend、migration、fixture 或 test
implementation。

## Audit 输入

本 audit 读取：

- `0.5.1` 到 `0.5.4` 的 child package reviews。
- 当前 git status 和 diff scope。
- 当前 docs/mirror checks。
- 在需要刷新 implementation evidence 时，读取当前 focused 和 broad backend test
  results。

## Audit 模型

Evidence 分为四组：

- contract evidence：docs-only concept 和 authorization checks。
- implementation evidence：TDD、tests、code review、validation evidence。
- compatibility evidence：touched surfaces 的 adjacent 和 broad regression tests。
- scope evidence：changed-file guards 和 forbidden-surface sentinels。

## 当前 Implementation Surface

`0.5.2` 和 `0.5.3` 是 v0.5 唯二 implementation-bearing child packages。

当前 implementation files 为：

- `backend/app/schemas/agent_memory.py`
- `backend/app/agent/memory.py`
- `backend/app/tests/test_agent_memory_substrate.py`
- `backend/app/schemas/agent_loop.py`
- `backend/app/agent/perception.py`
- `backend/app/api/app_factory.py`
- `backend/app/tests/test_agent_perception.py`
- `backend/app/tests/test_agent_loop_api.py`

## Audit 输出

Audit output 存放在本 package 的 `contract.md` 和 `review.md`。`0.5.5` 不需要单独的
generated artifact。

`0.5.6` 可以使用本 audit 作为 release-candidate bundle 的输入。
