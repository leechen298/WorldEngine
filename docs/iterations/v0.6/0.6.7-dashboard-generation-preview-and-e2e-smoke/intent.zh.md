# 意图

状态：review complete

## 问题

`0.6.6` 已暴露 generation preview、regeneration 和 loader/runtime-context readiness
的 stable backend/API semantics。v0.6 仍需要 dashboard-facing workflow 来使用这些
APIs，并需要 browser smoke test 证明 operator workflow 可见且端到端 wired。

## 目标

- 使用现有 backend generation routes 添加 focused dashboard generation preview workflow。
- 保持 workflow generic 和 inspectable，不引入 concrete world content 或 hidden
  provider behavior。
- 展示 validation status、bounded metadata、preview summary、diagnostics 和
  runtime-readiness status，且不泄露 raw prompts 或 private provenance。
- 保持现有 dashboard runtime、timeline、world-params、agent、memory、backend API 和
  E2E behavior 兼容。
- 为 dashboard preview smoke 添加 focused frontend 与 E2E evidence。

## 非目标

- 不 redesign backend generation API。
- 不做 full editor、template catalog UI、persistence、save/publish/install flow、
  runtime activation 或 projection application。
- 不添加 live AI provider behavior 或 prompt execution。
- 不声明 external validation readiness、product readiness、release readiness、
  generation-quality approval、Agent smoke 或 autonomous validation。

## North Star 对齐

本 package 通过 dashboard 让 generated worlds 可 inspect，同时保持 engine boundary generic。
它证明 preview loop 可操作，但不会把 generated worlds 提升为 live runtime state。

## 交接

完成后，`0.6.8-v0.6-evidence-and-compatibility-audit` 接收 dashboard preview 与
E2E smoke evidence，用于 v0.6 audit package。
