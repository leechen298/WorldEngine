# 意图

状态：review complete

## 问题

`0.6.2` 已能从已评审 templates 生成 `WorldSpec` 数据，`0.6.3` 已能编译
structured plans，`0.6.4` 已能导入带 redacted provenance 的 provider-independent
structured plans。消费者仍然需要稳定的 backend API surface，用来校验 request、返回
bounded generation metadata，并在后续 package 加入 regeneration、runtime-readiness
或 dashboard flows 前预览 generated `WorldSpec`。

## 目标

- 通过现有 FastAPI application 暴露 generation preview。
- 保留当前 `ApiResponse(code, data, msg)` success envelope 和
  `ApiErrorResponse(code, msg, data)` validation-error envelope。
- 复用现有 template、plan 和 imported-plan validation，不引入并行 validator。
- 只返回 public `WorldSpec` preview data、deterministic diagnostics 和 bounded
  metadata/provenance。
- 区分 request shape errors 与 generation validation failures：
  - invalid HTTP request shape 使用现有 422 handler 和 API error envelope。
  - invalid generation content 返回 200 preview result，其中
    `validation_status: failed`、包含 diagnostics，且不包含 generated
    `WorldSpec`。

## 非目标

- 不添加 dashboard UI 或 frontend workflow。
- 不添加 durable persistence 或 migrations。
- 不添加 regeneration behavior。
- 不声明 runtime loading/readiness。
- 不添加 live AI provider calls、prompt execution、provider SDKs、background jobs
  或 network access。
- 不声明 external validation readiness、projection readiness、product readiness、
  release readiness、autonomous validation 或 generation-quality claim。

## 用户与消费者

本 package 面向需要在运行或保存 generated worlds 前检查 generation results 的
backend/API consumers。它为后续 v0.6 package 做准备，同时避免把 WorldEngine 变成
application-specific backend。

## 北极星对齐

本 package 通过 generic API 暴露可评审的 generated-world structure，推进 north-star
world generation capability。它保持 generation contract-driven、inspectable、在测试中
deterministic，并与 external projection applications 保持分离。

## 交接

完成后，`0.6.6-regeneration-and-runtime-readiness-integration` 接收 public preview 和
metadata semantics，用于 bounded regeneration 和 runtime-readiness checks。
