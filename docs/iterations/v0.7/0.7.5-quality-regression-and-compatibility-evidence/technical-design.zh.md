# Technical Design

## Current State

`0.7.2`、`0.7.3` 和 `0.7.4` 已添加或 review redacted reports、readiness manifests
与 projection read models 的 checker surfaces。本 package 不新增 implementation，只把这些
surfaces 转成 current-session evidence matrix。

## Evidence Matrix Shape

`evidence-matrix.md` 应包含：

- command table，记录 exact command、exit status、result 和 supported claim。
- required classifications 的 coverage table。
- skipped/out-of-scope table，记录 reason 和 residual risk。
- v0.7 public contract surfaces 的 compatibility notes。
- unresolved findings table。

## Command Groups

Focused checker regression：

- external validation report checker tests。
- readiness manifest checker tests。
- projection read-model checker tests。

Saved-result checker regression：

- Agent smoke saved-result checker tests。
- Agent autonomous saved-result checker tests。

Schema and CLI validation：

- report schema、readiness manifest schema/json、projection read-model schema 的 JSON parsing。
- readiness manifest 与 projection read-model contract 的 CLI validation。

Scope and formatting：

- `git diff --check`。
- changed-file scope guard。

## Classification Rules

- Checker test PASS 只支持对应 checker surface。
- Saved-result checker PASS 只支持 saved-result schema/checker compatibility，不支持 live Agent
  smoke 或 autonomous runner PASS。
- JSON parse PASS 只支持 syntax，不支持 semantic runtime behavior。
- Scope guard PASS 只支持 changed-file boundary。
- Runtime/API/frontend/E2E/live Agent/full autonomous/external/projection app checks
  均为 out of scope，除非本 package 明确扩范围。

## Anti-Drift Rules

- Closeout 前 parent 与 child route/status surfaces 必须一致。
- `evidence matrix complete` 不是 v0.7 final closeout。
- 不得把 skipped/out-of-scope checks 写成 implicit PASS。
- 不得为了让 evidence pass 而修改 implementation files。
