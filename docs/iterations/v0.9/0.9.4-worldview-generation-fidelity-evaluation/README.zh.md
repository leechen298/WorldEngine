# 0.9.4 Worldview Generation Fidelity Evaluation

英文原文：`README.md`。

Status：implementation complete / non-live focused verification passed
Type：mixed validation/implementation package

## 目标

定义并实现 deterministic public fidelity evaluation，用来判断 generated
worldview output 是否忠实反映用户公开 premise；同时在已有 bounded runtime
evidence 时，判断后续公开 runtime behavior 是否与 premise 矛盾。

## 范围

本包可新增 public schemas、deterministic backend helpers、focused tests 和
package-local review evidence，覆盖：

- immediate premise coverage evaluation。
- fidelity scoring 中的 deterministic generic fallback detection。
- public contradiction taxonomy。
- 从已公开 runtime summaries 进行 optional bounded-run consistency evaluation。
- 不 mutate world state 的 PASS / FAIL / BLOCKED scorecard output。

当 bounded runtime controls 或 run evidence 尚不可用时，`0.9.4` 可以把
run-based fidelity 标记为 `blocked`。它不得实现这些 controls；该工作归属
`0.9.5`。

## 交付物

- active backend schema path 中的 public fidelity schema additions。
- `backend/app/core/` 中的 deterministic fidelity evaluation helper。
- focused backend tests，覆盖 faithful output、missing premise coverage、
  contradictory runtime evidence、missing bounded-run evidence、generic fallback
  和 redaction failures。
- review evidence，记录 changed files、commands、compatibility、scope 和
  subagent findings。

## 当前授权

父级 v0.9 route 授权 documentation drafting。Implementation 仍未授权，直到本包
review 在 documentation/contract review 通过后把 `implementation_authorized` 从
`no` 改为 `yes`。

本 draft 不授权 provider live calls、generated-result creation、checker execution、
external validation、Validation Client changes 或 bounded runtime control
implementation。

## 最终评估状态

Reviewed non-live scope 的 implementation 已完成。Focused fidelity tests、related v0.9
regression、backend regression 和 documentation checks 已在当前会话通过。
