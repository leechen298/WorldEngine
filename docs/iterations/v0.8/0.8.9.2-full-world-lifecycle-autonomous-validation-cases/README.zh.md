# 0.8.9.2 完整世界生命周期自主验证用例

Status: implementation complete / AUTONOMOUS_LIFECYCLE_CASE_READY
Type: mixed validation package
implementation_authorized: user-authorized by active goal on 2026-06-04
evidence_execution_authorized: yes, bounded to test protocol, checker fixtures, and validation commands

英文版本：`README.md`。

## Package

Name: `0.8.9.2-full-world-lifecycle-autonomous-validation-cases`

本 package 用来补齐当前自主验证覆盖，让后续验证可以判断完整的 WorldEngine
生命周期，而不是只验证 Validation Client UI smoke，或历史 dashboard saved-result
场景。

## Goal

新增一个 checker 支持的自主验证场景，覆盖完整 WorldEngine 生命周期：

- 通过外部客户端表面创建世界。
- 验证 WorldEngine 返回可运行的 public world state。
- 推进世界 tick。
- 观察 state、event、snapshot 和 replay evidence。
- 观察由 WorldEngine evidence 支撑的 in-world Agent 行为，而不是客户端脚本行为。
- 追加自然语言方向时，只影响外部事件或世界环境。
- 导出 evidence，供另一个 Agent 复核，且不包含 private prompts、secrets 或 hidden
  WorldEngine internals。

## Required Documents

- [x] `README.md`
- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`
- [x] Chinese mirrors

## Scope Summary

允许：

- autonomous testing protocol docs。
- full lifecycle autonomous scenario docs。
- autonomous result schema/checker extensions。
- focused checker unit tests。
- generic checker fixtures。
- review evidence。

禁止：

- core runtime behavior changes。
- provider API implementation。
- Validation Client repository changes。
- concrete validation-world seed content。
- private prompt、raw provider response、private Agent memory、private goals、
  `self_state`、hidden context、credentials 或 account data 进入 fixtures 或 public
  evidence。

## Handoff

本 package 已让完整 WorldEngine 生命周期验证用例可以被 saved-result checker 执行。
它本身仍不证明 live WorldEngine PASS；后续还必须生成真实 evidence 并验证对应
result directory。
