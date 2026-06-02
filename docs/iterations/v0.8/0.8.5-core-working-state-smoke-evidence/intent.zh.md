# Intent

## Problem

v0.8 不能只靠 documentation 达到 minimum working-state claim。`0.8.3` 已证明一个 bounded
core-readiness slice，`0.8.4` 已定义 handoff evidence 如何分类，但 campaign 仍需要针对
WorldEngine normal operation 所需 public core surfaces 的 broader current-session smoke
matrix。

如果没有本 package，后续 audit 或 release-candidate work 可能从以下来源过度声明：

- historical v0.7/v0.6 evidence。
- 单一 focused readiness probe。
- documentation-only handoff contracts。
- 未覆盖 claimed surface 的 tests。

## Objective

定义并 review v0.8 core-side working-state smoke evidence 的 command matrix、evidence
classes、artifact boundaries 和 non-claims。

Review 后，本 package 只能运行授权 commands，并且只能记录这些 commands 实际证明的 evidence。

## Non-Goals

- 不实现或运行 external validator。
- 不导入、clone 或运行 external app repository。
- 不添加 product-specific scenarios、concrete validation worlds、private transcripts、
  screenshots、UI selectors、private paths、oracle details、provider traces、prompts、
  secrets 或 external event payloads。
- 不为了 validation pass 修改 product/runtime behavior。
- 不声明 external validation PASS、external consumer PASS、product readiness、projection
  application readiness、full autonomous PASS 或 final v0.8 readiness。

## Success Criteria

Documentation review 通过时，本 package 必须：

- 命名 exact command groups 及其 proof boundaries。
- 区分 in-scope、skipped、blocked 和 out-of-scope checks。
- 定义 redacted evidence 和 artifact rules。
- 记录 v0.3 到 v0.7 surfaces 的 compatibility expectations。
- 在 review 前保持 implementation 和 evidence execution authorization 关闭。
