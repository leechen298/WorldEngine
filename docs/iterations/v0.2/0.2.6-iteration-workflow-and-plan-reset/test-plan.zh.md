# 测试计划

英文版本：`test-plan.md`

## 文档检查

- 编辑前后检查 repository state。
- 检查 Markdown diff 没有 whitespace errors。
- 检查 0.2.7 到 0.2.12 的 detailed plan acceptance gate。
- 检查 release wording 没有声明 final release。
- 检查 residual concrete demo anchors 已移除或抽象化。

## 命令

```bash
git status --short --branch
git diff --check
```

## Concrete Demo Anchor Sweep

使用 `/tmp` 或其他 untracked path 下的 temporary pattern file。不要把 concrete
pattern list 写进 tracked Markdown。

Review 只记录 command purpose 和 classification，使用以下抽象描述：

- historical concrete fixture wording
- historical concrete fixture pathname
- legacy concrete demo anchor
- concrete demo anchor sweep

## 详细计划验收闸

最终输出前，确认 `docs/iterations/v0.2/v0.2-plan.md` 和
`docs/iterations/v0.2/v0.2-plan.zh.md` 对 0.2.7 到 0.2.12 的每个 package
都包含必需字段：

- Package name / 包名
- Status / 状态
- Type / 类型
- Goal / 目标
- Why this exists / 存在原因
- Inputs / required reading / 输入与必读文件
- Allowed changes / 允许变更
- Forbidden changes / 禁止变更
- Expected deliverables / 预期交付
- Expected tests / verification / 预期测试与验证
- Compatibility constraints / 兼容性约束
- Scope guardrails / 范围护栏
- Exit criteria / 退出条件
- Handoff to next package / 交接给下一包

如果有字段缺失，记录 P2 finding，且不得声称 plan is ready。

## 验收标准

- `0.2.6-iteration-workflow-and-plan-reset` 存在，并包含 required package files
  及中文镜像。
- `00-chatgpt-plan.md` / `.zh.md`、`development-workflow.md` / `.zh.md` 和
  `final-review-bundle-template.md` / `.zh.md` 存在。
- v0.2 index 和 plan docs 把 0.2.6 指向 workflow and plan reset，而不是
  final closeout。
- `v0.2-plan.md` 和 `v0.2-plan.zh.md` 为 0.2.7 到 0.2.12 提供完整
  quasi-package specifications。
- roadmap v0.2 entries 匹配新的 package sequence，且不重写 v0.3+
  technical direction。
- release docs 保持 draft / planned / not released。
- 没有 runtime、schema、API、frontend、backend test 或 fixture files changed。

## 未运行项

本 package 是 documentation-only，不要求 backend 或 frontend tests。如果误改 code、
schema、API、frontend、test 或 fixture files，必须停止并记录 scope violation。
