# Natural-Language Implementation Triggers

Status: reusable agent routing guide

英文版本：`natural-language-implementation-triggers.md`。

当用户说出这类简短 implementation 或 completion request 时使用本指南：

```text
完成 <iteration-package>
实现 <iteration-package>
开发 <iteration-package>
complete <iteration-package>
implement <iteration-package>
develop <iteration-package>
```

## Primary Workflow

执行 `docs/iterations/AGENTS.zh.md`，然后在
`docs/iterations/**/<iteration-package>/` 下定位被点名的 package。

这个 trigger 启动 iteration-package gate。它本身不自动授权 runtime、schema、API、frontend、
test、fixture、migration 或 external repository changes。

## Required Reading

规划或执行前必须：

- 读取 `AGENTS.zh.md`。
- 读取 `docs/iterations/README.md`。
- 读取 `docs/iterations/AGENTS.zh.md`。
- 在 `docs/iterations/**/<iteration-package>/` 下定位匹配 package。
- 如果 package 包含 `README.md`、`GOAL_RUNNER.md`、`CURRENT_STATE.md` 或
  `CAMPAIGN_PLAN.md`，规划或执行前先读取这些文件。
- implementation 阶段按顺序读取 package documents：`intent.md`、`contract.md`、
  `technical-design.md`、`test-plan.md`、`plan.md` 和 `review.md`。

## Gate Rules

如果 required iteration package 或已 review 的 implementation-stage documents 不存在，停在
documentation stage，先补齐缺失的 package documents 供 review。

如果 implementation 暴露 design gap，停止 implementation，更新相关 package documents，并且只在
更新后的 contract、design、test plan 或 execution plan 经过 review 后继续。

implementation 必须限定在 active package。不要实现 adjacent versions 或方便顺手做的 follow-on
capabilities。
