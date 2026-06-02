# 技术设计

## 文档与实现结构

本包修复现有检查器和文档表面；不创建新的运行时行为。

受影响的实现文件：

- `tools/testing/validate_external_validation_report.py`
- `tools/testing/test_validate_external_validation_report.py`
- `tools/testing/validate_readiness_manifest.py`
- `tools/testing/test_validate_readiness_manifest.py`
- `tools/testing/validate_projection_read_model_contract.py`
- `tools/testing/test_validate_projection_read_model_contract.py`

受影响的公共文档 / Schema 文件：

- `docs/testing/external-validation-report-schema.json`
- `docs/contracts/v0.7-readiness-manifest-schema.json`
- `docs/validation-report-template.md`
- `docs/contracts/projection-read-model-contract.md`
- `docs/testing/results/2026-06-02-v0.7-overall-validation.md`
- `docs/testing/results/2026-06-02-v0.7-overall-validation.zh.md`

## 修复设计

### 外部验证报告检查器

- 把“accepted 等同已解决”的 P1/P2 语义替换为“只有 resolved 才算关闭”的语义。
- 对报告中的每个字符串增加通用禁止内容扫描。
- 保留合成哨兵词以兼容现有夹具，同时增加针对私有路径、UI 选择器标记、
  隐藏重置标记、判题器术语、转录文本术语、种子数据术语和事件载荷术语的真实通用模式。
- 继续接受有效的抽象标识符。

### 就绪清单检查器

- 用同样风格对全部清单字符串做通用泄漏扫描。
- 将命令字符串作为公开命令校验：不允许绝对本地路径、父目录穿越、
  私有运行器术语、UI 选择器文本、判题器术语、转录文本术语或事件载荷术语。
- 保留当前基于公共仓库相对路径的检查。

### 投影读模型检查器

- 扩展已允许字段中的禁止术语，覆盖 `private`、`application_state` 和等价的
  应用 / 私有状态表述。
- 保留安全公共摘要字段的有界后缀允许语义。

### JSON Schema 与语义权威

- 在 JSON Schema 能表达的地方收紧 Schema。
- 在 JSON Schema 无法表达语义文本扫描的地方，加入“Schema 有效但检查器无效”
  输入的回归测试，并文档化检查器语义权威。

### 模板与状态文本漂移

- 在 `docs/validation-report-template.md` 增加简短字段映射提示。
- 更新投影读模型契约状态，使其与已审查 / 修复上下文对齐，但不声明投影就绪 PASS。

## 兼容性策略

- 先为每个 V07-CR 问题添加预期失败测试。
- 用最小检查器变更让这些测试通过。
- 重新运行所有 `tools/testing` 测试和现有 Agent smoke / autonomous 检查器测试。
- 除非 Schema 收紧有意需要，不改变有效公共契约载荷。

## 防漂移规则

- 不增加具体外部世界示例。
- 不修改或暂存已知无关的 v0.8 边界工作树项：
  `docs/roadmap.md`、`docs/scope-boundaries.md`、v0.7 根规划文档、
  v0.7 handoff / final-closeout 边界文档或 `docs/iterations/v0.8/**`。
- 不把检查器 / Schema PASS 写成外部测试套件或产品就绪 PASS。
- 在 V07-CR 阻断门禁不再发现未解决 P1/P2 阻断项，且验证结果
  用当前会话证据记录它们已修复之前，不声明 clean pass。
