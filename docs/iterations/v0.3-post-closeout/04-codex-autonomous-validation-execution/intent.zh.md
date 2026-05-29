# 意图

## 问题 / 目的

本包把后续独立 Codex review 与规划包分开。它后续会记录 reviewer evidence、commands、
unsupported claims、findings 和 recommendation。

## 为什么现在需要

campaign 需要先有持久模板，避免 autonomous validation 被临时写成没有证据支撑的 release claim。

## 与路线图的关系

review 结果可以帮助判断 v0.4 规划是否可以信任 v0.3 loader 和 bridge claims。
它不启动 v0.4 实现。

## 非目标

- 在本文档轮次中执行 review。
- 修改代码或测试。
- 修复 findings。
- 添加 fixtures 或外部仓库。
- 改变发布状态。

## 预期交接

后续 review 填写完成后，`05-final-validation-bundle` 可以把它与 E2E / integration
validation evidence 综合。
