# Natural-Language Iteration Documentation Triggers

Status: reusable agent routing guide

英文版本：`natural-language-iteration-documentation-triggers.md`。

当用户说出这类短 iteration-documentation request 时使用本指南：

```text
生成 <version> 文档
编写 <version> 文档
规划 <version> 每个迭代
生成 <version> 迭代包
创建 <version> iteration docs
```

## Primary Workflow

执行 `docs/iterations/AGENTS.zh.md` 中的 Codex Plan-Mode Document Generation
Standard。

起草 project-direction work 前，也要遵守 `AGENTS.zh.md` 和
`docs/iterations/README.md` 的 required reading，尤其是：

- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.zh.md`

## Boundary

这个 trigger 只创建或更新可 review 的 iteration documentation。它不授权 runtime、schema、
API、frontend、test、fixture、migration 或 external repository implementation。

如果用户同时要求 iteration documentation 和 implementation，先完成 documentation stage，
并说明 implementation 必须等待相关 package documents review/approval。

## 新版本默认范围

对于新版本，短 version-documentation request 默认只创建 version-level package：

- parent generation plan。
- version index。
- version plan。
- campaign state docs。
- child package sequence。
- version plan 内的 planned-package specifications。

默认不要为每个 planned child iteration 创建完整文档目录。

## Planned Child Package Rule

Version plan 中的 planned child packages 是 route-map specifications，不是 approved
execution contracts，也不是 implementation authorization。

只有满足以下任一条件时，才创建具体 child package document set：

- 用户明确点名该 child package。
- 用户要求创建或完成该 child package。
- 已 review 的 active package 明确授权创建下一个 child package documents。

## Required Output Discipline

生成或更新 iteration documentation 时：

- 保持 package status 真实：在 review 批准下一阶段前，只能是 proposed、planned、
  ready-for-review 或等价状态。
- 明确 child-package sequence、boundaries 和 stop rules。
- 列出生成或更新的文件。
- 记录 documentation checks，例如 `git diff --check`。
- docs-only 请求未运行 code tests 时要明说。
- 不要从 documentation alone 暗示 implementation、validation 或 closeout。

## Existing Package Handling

如果匹配 version 或 package files 已存在：

1. 读取当前 `README.md`、`GOAL_RUNNER.md`、`CURRENT_STATE.md`、
   `CAMPAIGN_PLAN.md` 和存在的 `review.md`。
2. 保持 active package boundary。
3. 更新现有 docs，不创建重复 authority surfaces。
4. 如果多个文件 status text 漂移，把它视为 documentation finding，修复后再报告 ready。
