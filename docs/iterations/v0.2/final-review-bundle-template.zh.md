# 最终审核包模板

英文版本：`final-review-bundle-template.md`

## 包名

`<package-name>`

## 分支

`<branch>`

## 基准提交

`<base-commit>`

## 当前提交

`<head-commit>`

## 状态

`<status>`

## 摘要

说明本 package 改了什么，以及明确没有改什么。

## 变更文件

| 文件 | 变更 |
|---|---|

## 契约对照

把每一条 contract requirement 映射到满足它的 changed files 和 evidence。

## 禁止变更确认

确认没有发生 forbidden runtime、schema、API、frontend、test、fixture、
external repository 或 concrete demo-world changes。

## 已运行命令

```bash
```

## 测试结果

记录准确的命令结果。如果某个命令没有运行，说明原因。

## grep 残留分类

记录 concrete demo anchor sweep 结果，只使用抽象分类。不要包含 concrete pattern list。

## Codex A 审核发现

| 严重级别 | 发现 | 状态 |
|---|---|---|

## Codex B 修复

| 发现 | 修复 |
|---|---|

## 未解决 P1/P2/P3

- P1：
- P2：
- P3：

## 兼容性审核

说明 runtime behavior、API response shapes、schema behavior、frontend behavior、
tests 和 fixtures 是否保持兼容。

## 范围审核

说明 diff 是否停留在 package contract 内。

## 下一步建议

说明下一个 package 或 review action。

## 请求 ChatGPT 整体审核

请求 ChatGPT 审核 scope、evidence、compatibility、unresolved findings 和
next-step readiness。
