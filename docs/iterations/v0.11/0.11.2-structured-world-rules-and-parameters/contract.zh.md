# Contract

英文版本：`contract.md`。

## Public Concepts

- `session_rule_parameter_set`：attach 到 session 的 structured public rule/parameter evidence。
- `rule_parameter_validation`：来自现有 validators 的 public accepted/rejected result。
- `public_rule_summary`：redaction-safe summary，包含 parameter paths、rule ids、boundary ids、
  diagnostics count 和 redaction status。

## Allowed Changes

- 为 session storage 增加 rule parameter validation 和 summary fields。
- 新增 `POST /sessions/{session_id}/rules` 和 `GET /sessions/{session_id}/rules`
  或等价 additive endpoints。
- 复用现有 rule-parameter schemas/validators。
- 增加 manifest discovery entries 和 focused backend tests。
- 更新 docs 和 route status。

## Forbidden Changes

- 不实现 runtime event generation。
- 不实现 direction queue 或 user guidance interpretation。
- 不直接修改 Agent private memory、goals、injury、death、inventory 或 hidden state。
- 不运行 live provider calls。
- 不实现 Validation Client。
- 不做 durable persistence/migrations。
- 不新增 concrete demo-world fixtures 或 `backend/worldengine/` changes。

## Compatibility Requirements

- 现有 `/world/params` behavior 保持不变。
- 现有 session create/run/snapshot behavior 保持不变，只允许 additive rule summary
  fields/endpoints。
- 被 rejected 或包含 private marker 的 rule sets 不得在 public diagnostics 或 summaries 中 echo
  private values。
- 被 accepted 的 rule sets 必须只引用 public structured parameter/rule ids。

## Out-of-Scope Follow-Ups

- Natural-language direction queue 属于 `0.11.3`。
- Rule-compliant event generation/diffs 属于 `0.11.4`。
- Fidelity validation 属于 `0.11.5`。
