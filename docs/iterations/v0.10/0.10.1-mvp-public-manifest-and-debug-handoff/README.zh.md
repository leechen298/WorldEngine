# 0.10.1 MVP Public Manifest And Debug Handoff

英文版本：`README.md`。

状态：`implementation complete / focused verification passed`
类型：mixed implementation package
implementation_authorized: yes
evidence_execution_authorized: no
provider_live_call_authorized: no
external_validation_authorized: no

## Goal

在后续 v0.10 session 功能依赖它之前，对齐 MVP public manifest、debug handoff
vocabulary、discoverable surface metadata、诚实的 status taxonomy 和 checker-handoff
skeleton。

实际含义是：`/manifest` 应说明这是 v0.10 MVP debug contract，列出当前存在或计划中的
public MVP/debug surfaces，保留 `pass`、`fail`、`blocked`、`not_run` 语义，暴露脱敏的
checker handoff metadata，并保持 provider ownership 和 evaluator authority 属于
WorldEngine/checker contracts，而不是外部 Validation Client。

## Scope

文档评审后允许的 implementation scope：

- public handoff manifest schema 的 additive fields。
- 对现有 public routes 和计划中的 v0.10 session routes 增加 additive MVP/debug surface
  metadata。
- `pass`、`fail`、`blocked`、`not_run` 的 public status taxonomy values and meanings。
- 保留 artifact names 和 redaction expectations 的最小 checker-handoff skeleton metadata。
- replay/worldline branch terminology 使用类似时间线分支的 branch wording，避免
  parent/source-world semantics。
- focused backend tests 覆盖 manifest compatibility、status taxonomy、redaction flags、
  blocked/not_run honesty，以及无 secret/raw provider leakage。

允许文件：

- `backend/app/schemas/world.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_public_handoff_contract_api.py`
- 本 package directory 和中文镜像。
- 用于 route/evidence update 的 v0.10 parent status/review docs。

禁止范围：

- 不实现 Validation Client repository。
- 不做 provider live calls 或 provider credential handling changes。
- 不实现 runtime session、session store、worldview-to-session creation、bounded session
  runtime、snapshot/diff engine、dashboard flow、durable persistence、migration、
  generated result 或 external validation。
- 不改 checker implementation 或 fixtures，除非本包重新修订并通过评审。
- 不暴露 raw prompts、raw provider requests/responses、provider traces、secrets、
  private Agent memory、hidden context、raw thought 或 private evaluator data。
- 不改 `backend/worldengine/`。

## Deliverables

- 已评审 package document set 和 mirrors。
- Additive v0.10 MVP manifest/debug contract schema。
- 更新后的 `/manifest` payload，包含 discoverable MVP/debug surfaces 和 checker-handoff
  skeleton。
- 证明 compatibility 和 redaction behavior 的 focused backend tests。
- 包含准确命令和结果的 review evidence。

## Status Checklist

- [x] Package documents drafted。
- [x] Documentation / contract evaluator complete。
- [x] Implementation authorized。
- [x] Implementation complete。
- [x] Focused verification complete。
- [x] Implementation-scope evaluator complete。
- [x] Code-review/evidence evaluator complete。
- [x] Review evidence updated。

## Final Assessment State

当前值：`implementation complete / focused verification passed`。

本包在 focused public manifest/debug handoff 范围内完成。它不声明 runnable session、
dashboard、provider-live、checker、external-validation、Agent autonomy 或 full MVP PASS。
