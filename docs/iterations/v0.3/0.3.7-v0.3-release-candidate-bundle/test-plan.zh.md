# 测试计划

## 验证范围

本包仅文档。验证聚焦于文档存在、状态一致、发布候选表述、镜像同步、变更文件
范围、未解决问题可见性和证据可追溯性。

除非实现文件发生变更，否则不需要后端、前端、API 冒烟、E2E、Agent 冒烟、
运行时、schema、fixture、迁移或构建测试。如果任何此类文件发生变更，停止并视为
契约违规。

## 必需检查

### 文档健康检查

```bash
git diff --check
```

预期结果：退出码 `0`。

### 必需文件存在性

```bash
test -f docs/iterations/v0.3/v0.3-release-candidate-bundle.md
test -f docs/iterations/v0.3/v0.3-release-candidate-bundle.zh.md
test -f docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.md
test -f docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.zh.md
```

预期结果：所有命令退出码均为 `0`。

### 包镜像存在性

```bash
for f in README intent contract technical-design test-plan plan review; do
  test -f "docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/$f.md" &&
  test -f "docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/$f.zh.md" ||
  exit 1
done
```

预期结果：退出码 `0`。

### 状态一致性

```bash
rg -n '0\.3\.7-v0\.3-release-candidate-bundle|Status: ready for review|状态：待评审|状态：`待评审`' \
  docs/iterations/v0.3/README.md \
  docs/iterations/v0.3/README.zh.md \
  docs/iterations/v0.3/v0.3-plan.md \
  docs/iterations/v0.3/v0.3-plan.zh.md \
  docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/README.md \
  docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/README.zh.md
```

预期结果：退出码 `0`；状态与文档阶段待评审一致。

### 发布状态表述检查

```bash
rg -n 'not final|not released|release candidate|release-candidate|0\.3\.8|final closeout|final release|未发布|最终收口|发布候选' \
  docs/releases/v0.3.md \
  docs/releases/v0.3.zh.md \
  docs/iterations/v0.3/v0.3-release-candidate-bundle.md \
  docs/iterations/v0.3/v0.3-release-candidate-bundle.zh.md \
  docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.md \
  docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.zh.md
```

预期结果：退出码 `0`；表述确认候选状态，且不声明最终发布。

### 证据可追溯检查

```bash
rg -n '0\.3\.[0-7]|evidence-index|compatibility-audit|findings|review\.md|implemented|documented|tested|planned|not implemented|partial|historical|finding|已实现|已文档化|已测试|未实现|问题' \
  docs/iterations/v0.3/v0.3-release-candidate-bundle.md \
  docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.md
```

预期结果：退出码 `0`；发布候选声明引用证据和状态类别。

### 具体演示锚点扫描

使用临时未跟踪 pattern 文件，并只在 `review.md` 记录抽象结果类别。不要提交具体
pattern 列表。

预期结果：没有主动方向匹配。任何残留匹配必须分类为历史包证据、仅评审文本或
假阳性。

### 变更文件范围护栏

```bash
git status --porcelain=v1 -uall | rg -v '^( M|\?\?) docs/iterations/v0\.3/'
```

预期结果：退出码 `1` 且无输出，表示变更文件限制在批准的 v0.3 迭代文档路径内。

## 不计划运行的测试

- 不计划运行后端测试，因为本包不得修改后端实现文件。
- 不计划运行前端测试，因为本包不得修改前端实现文件。
- 不计划运行 API 冒烟、E2E、Agent 冒烟、运行时、schema、fixture、迁移或构建
  测试，因为本包仅文档。

## 失败处理

- 如果实现文件发生变更，停止，并仅在用户批准后回退本包的越界编辑。
- 如果发现 P1/P2 证据缺口，清晰记录，并保持最终收口阻塞。
- 如果发布措辞暗示最终状态，在评审前修正。
