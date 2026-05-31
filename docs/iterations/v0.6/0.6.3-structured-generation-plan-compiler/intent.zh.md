# 意图

Status: review complete

## 存在原因

`0.6.2` 已证明 deterministic template-to-`WorldSpec` baseline。v0.6 还需要
structured plan path，让后续 AI-assisted generation 把 normalized data 交给 engine，
而不是隐藏的 prose side effects。

`0.6.3` 创建这个 compiler boundary。它让调用方用已评审的数据描述目标 world structure，
deterministically validate 这些数据，并把它们编译为现有 `WorldSpec` shape，同时不添加
API、frontend、runtime、persistence 或 provider behavior。

## 预期结果

Implementation 和 review 后：

- structured plans 有明确 schema semantics。
- invalid plans 返回带 path 和 source context 的 stable diagnostics。
- valid plans 编译为 loader-valid `WorldSpec` output。
- `0.6.2` 的 template generator behavior 保持兼容。
- concrete world content 或 external-provider behavior 不进入 core repository。

## 非目标

- 不实现 AI-assisted plan import；这属于 `0.6.4`。
- 不暴露 public API routes、dashboard UI、preview API 或 regeneration。
- 不修改 runtime tick behavior、Agent/memory behavior、persistence、migrations，或
  external validation/projection readiness。
- 不让 plan compiler 执行 prompts、scripts 或 arbitrary rules。

## 交接

`0.6.4-ai-assisted-generation-boundary-and-plan-import` 接收已评审 structured plan
input semantics 和 compiler diagnostics。
