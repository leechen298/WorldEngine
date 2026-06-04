# Intent

英文版本：`intent.md`。

## Problem

当前 WorldEngine autonomous validation checker 支持的是历史 dashboard
saved-result 场景。它不支持用户要求的完整能力链路：创建世界、让世界随时间运行、
观察 in-world Agent 自主行为、追加外部方向，并导出可复核 evidence。

如果没有 checker 支持的完整场景，验证聊天很容易只跑 UI smoke，然后过度声明
WorldEngine readiness。

## Goal

新增明确的 full-lifecycle autonomous validation case 和 checker 支持，让后续验证
基于 evidence 判定失败或通过，而不是靠叙述。

## Non-goals

- 不实现或修复 WorldEngine runtime behavior。
- 不实现 live provider calls。
- 不修改 Validation Client repository。
- 不在本仓库存储 concrete demo worlds、characters、maps、story rules 或 private
  validation oracle content。
- 不从 checker fixtures 声称 live autonomous PASS。

## Why Now

0.8.9.1 已提供 public handoff contract，但它明确不声明 Codex autonomous
validation、live provider、full lifecycle 或 product readiness。下一轮验证需要先有
完整用例，才能测试正确目标。

## North Star Alignment

本 package 通过让 world generation、world runtime、Agent-in-world behavior、event
evidence 和 external projection validation 可观察，服务 North Star，同时不把
WorldEngine 缩窄成单一游戏后端。
