# 0.7.3 Contract Bundle And Readiness Manifest

Status: review complete
Type: mixed
implementation_authorized: yes

## 目标

定义并暴露一个通用的 public readiness manifest。外部验证套件可以通过它发现
WorldEngine 的公开合同面、支持的能力区域、readiness claim 分类和脱敏证据链接，
而不需要了解私有仓库结构。

## 范围

允许范围：

- 创建本 child package 文档集与中文镜像。
- 添加 `docs/contracts/v0.7-readiness-manifest-schema.json`。
- 添加 `docs/contracts/v0.7-readiness-manifest.json`。
- 添加 `tools/testing/validate_readiness_manifest.py`。
- 添加 `tools/testing/test_validate_readiness_manifest.py`。
- Review 和 implementation closeout 后更新 package review evidence 与 parent
  v0.7 route/status surfaces。

禁止范围：

- 不加入私有外部套件配置、私有仓库路径、具体外部世界数据、具体世界名、UI
  selectors、oracle internals、transcripts、event payloads、hidden reset APIs、
  seed data 或 consumer-specific naming。
- 不修改 runtime、API、frontend、persistence、migrations、generated result
  directories、external repositories 或 `backend/worldengine/`。
- 不声明 external suite PASS、product readiness、projection application readiness、
  runtime/API/frontend PASS、E2E PASS、live Agent smoke PASS 或 release readiness。

## 交付物

- 完整 package docs 与中文镜像。
- 代码变更开始前，先记录已评审通过的 implementation authorization。
- Public readiness manifest schema。
- Public v0.7 readiness manifest，包含合同面标识、版本标记、能力区域、
  readiness claim taxonomy 和脱敏证据引用。
- Generic checker 与 focused tests，用于检查 manifest 完整性、public path 约束、
  claim classification 和 forbidden private-detail markers。
- Review evidence，以及 handoff to `0.7.4`。

## Status Checklist

- [x] Package documents drafted。
- [x] Chinese mirrors drafted。
- [x] Documentation/contract evaluator complete。
- [x] Implementation authorization recorded。
- [x] Manifest/schema/checker/tests complete。
- [x] Focused tests complete。
- [x] Implementation-scope evaluator complete。
- [x] Code-review evaluator complete。
- [x] Validation-evidence evaluator complete。
- [x] Closeout consistency review complete。
- [x] Parent v0.7 route updated。

## 最终评估状态

当前值：`review complete`。

本 package 已实现 approved manifest schema/json/checker/test scope，并把 public
contract discovery semantics 交接给 `0.7.4`。
