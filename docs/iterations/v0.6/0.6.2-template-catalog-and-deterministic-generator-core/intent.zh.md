# 意图

Status: review complete

## 问题 / 目的

v0.6 已从 `0.6.1` 获得已评审 generation concepts，但还没有可执行的 non-AI
generator baseline。下一步安全动作是实现一个小型 deterministic core，把已评审的
generic templates 转成当前合法 `WorldSpec` 数据，并且不引入 API、frontend、
persistence、AI-provider 或 runtime-step changes。

## 为什么现在做

`0.6.1` review complete 后，`CURRENT_STATE.md` 指向本 package。v0.6 sequence 要求
先有 deterministic template generation，之后才能做 structured plan compilation 和
AI-assisted plan import。

## 与 roadmap 的关系

本 package 是 v0.6 World Generation v1 的第一个 implementation-bearing slice。它实
现 generic、inspectable 的 baseline generator，同时保留 v0.3 loader/runtime-context
bridge、v0.4 Agent Loop 和 v0.5 memory substrate。

## 非目标

- 不实现 structured generation plan compilation；这属于 `0.6.3`。
- 不实现 AI-assisted plan import；这属于 `0.6.4`。
- 不暴露 backend API routes、metadata/preview API、regeneration、dashboard UI、
  E2E smoke、external validation readiness 或 projection readiness。
- 不添加 durable persistence、migrations、live external AI-provider calls、generated
  seed files 或 concrete world content。
- 不修改现有 `WorldSpec`、`WorldCell`、`EntityRef`、loader、runtime-context、
  runtime-step、Agent、memory、API、params、archive、frontend、fixture 或
  `backend/worldengine/` behavior。

## 预期交接

实现并 review 后，`0.6.3` 接收：

- generic generation schemas。
- deterministic template catalog semantics。
- deterministic template-to-`WorldSpec` generation logic。
- generated output 是 loader-valid 且 generic 的 focused evidence。
- 相邻 schema、loader 和 runtime-context surfaces 的 compatibility evidence。
