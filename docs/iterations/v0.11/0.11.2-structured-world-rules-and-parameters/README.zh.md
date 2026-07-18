# 0.11.2 Structured World Rules And Parameters

英文版本：`README.md`。

状态：`implementation complete / focused verification passed`
类型：mixed implementation package
implementation_authorized: yes
provider_live_call_authorized: no
external_validation_authorized: no

## 目标

把 structured public rules、parameters、constraints 和 boundaries attach 到 world session，
让后续 v0.11 event generation 可以引用 public legality evidence。

本包复用已有 rule-parameter schemas 和 validators。不实现 event generation 或 direction
handling。

## 范围

评审后允许：

- 新增 additive session-scoped rule/parameter attach 和 summary API。
- 复用 `GeneratedRuleParameterSet`、`validate_generated_rule_parameter_set` 和
  `build_public_world_rule_summary`。
- 在 in-memory session store 中保存 accepted rule summaries。
- 更新 manifest discovery。
- 增加 focused backend tests，覆盖 valid attach、invalid refs/types/private markers、
  summary access 和 existing params compatibility。

禁止：

- 不运行 live provider calls。
- 不实现 direction queue。
- 不实现 event generation 或 diff application。
- 不实现 fidelity scoring。
- 不实现 Validation Client，也不声明 external PASS。
- 不做 durable persistence/migrations。
- 不在本仓库存 concrete demo-world seed data。
- 不修改 `backend/worldengine/`。

## Expected Deliverables

- Session rule/parameter attach endpoint。
- Session rule/parameter summary endpoint。
- Public validation diagnostics 和 redaction-safe summary。
- Focused backend tests 和 review evidence。

## 状态检查清单

- [x] Package documents drafted。
- [x] Documentation / contract evaluator complete。
- [x] implementation_authorized: yes。
- [x] Implementation complete。
- [x] Verification complete。
- [x] Evaluator closeout complete。
