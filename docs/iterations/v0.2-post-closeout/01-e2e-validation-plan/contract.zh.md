# Contract

状态：`planned / ready for review`

## Public concepts

- E2E validation：repository 存在 runnable framework 时的 browser E2E。
- Integration validation：backend deterministic tests 和 route-level checks。
- API smoke validation：使用 TestClient 或 curl 的 public endpoint checks。
- Release claim validation：对比 v0.2 release docs、observed behavior 和 reviewed
  evidence。
- Concrete demo-world regression check：确认 validation 不把具体 demo-world details
  重新引入 core docs 或 code。

## 允许修改

- 在本目录下新增 validation planning docs。
- 定义 future execution checks 和 fallback rules。
- 定义 report evidence requirements。

## 禁止修改

- 本 package 不运行 backend、frontend、E2E、API smoke、runtime、schema execution、
  fixture、migration 或 autonomous validation commands。
- 不修改 implementation files。
- 不改变 v0.2 release status。
- 不硬编码 observed branch name。
- 不添加 concrete demo-world details。

## 兼容性要求

本 plan 必须保留现有 v0.2 closeout wording。它可以说明需要 fresh validation
evidence，但不得暗示 v0.2 incomplete 或 reopened。

## 范围外 follow-ups

- 执行 E2E / integration / API smoke validation。
- 修复 execution 发现的 failures。
- 增加缺失的 E2E framework support。
- 更新 runtime、API、schema 或 frontend behavior。
