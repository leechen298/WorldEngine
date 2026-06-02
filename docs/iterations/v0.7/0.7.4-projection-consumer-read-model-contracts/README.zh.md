# 0.7.4 Projection Consumer Read Model Contracts

Status: review complete
Type: mixed
implementation_authorized: yes

## 目标

定义通用、只读的 projection consumer read-model contracts，覆盖 runtime、event、Agent
loop、bounded memory context、generation-readiness 和 readiness-manifest summaries；
不构建 product application。

## 范围

允许范围：

- 创建本 child package 文档集与中文镜像。
- 添加 `docs/contracts/projection-read-model-contract.md`。
- 添加 `docs/contracts/projection-read-model-schema.json`。
- 添加 `tools/testing/validate_projection_read_model_contract.py`。
- 添加 `tools/testing/test_validate_projection_read_model_contract.py`。
- Review 和 closeout 后更新 package review evidence 与 parent v0.7 route/status surfaces。

禁止范围：

- 不添加 projection product UI、game UI、concrete world viewer、product dashboard、
  packaging flow、external app repository、write API、hidden reset API、private
  runner hook、persistence、migration 或 consumer-specific backend behavior。
- 不暴露 private application state、concrete worlds、character names、location names、
  maps、story rules、seed data、UI selectors、raw memory records、provider secrets、
  prompts、traces、transcripts 或 event payloads。
- 不声明 projection application readiness、product readiness、external consumer PASS、
  runtime/API/frontend PASS 或 v0.8 readiness。

## 交付物

- 完整 package docs 与中文镜像。
- 代码变更开始前，先记录 reviewed implementation authorization。
- Public projection read-model contract。
- Projection read-model schema，包含 bounded、read-only payload families。
- Generic checker 与 focused tests，用于验证 required model families、read-only
  fields、redaction rules、no write capability 和 forbidden markers。
- Review evidence，以及 handoff to `0.7.5`。

## Status Checklist

- [x] Package documents drafted。
- [x] Chinese mirrors drafted。
- [x] Documentation/contract evaluator complete。
- [x] Implementation authorization recorded。
- [x] Contract/schema/checker/tests complete。
- [x] Focused tests complete。
- [x] Implementation-scope evaluator complete。
- [x] Code-review evaluator complete。
- [x] Validation-evidence evaluator complete。
- [x] Closeout consistency review complete。
- [x] Parent v0.7 route updated。

## 最终评估状态

当前值：`review complete`。

Implementation 和 validation evidence 已记录。Parent v0.7 route 已 handoff 到
`0.7.5-quality-regression-and-compatibility-evidence`。
