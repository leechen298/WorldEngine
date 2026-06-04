# Test Plan

英文源文件：`test-plan.md`。

## 范围

测试只证明 Validation Client handoff 所需的 WorldEngine public contract readiness。不得声明 external Validation Client autonomous PASS 或 human validation PASS。

## 实现前文档检查

任何代码变更前运行：

```bash
git status --short --branch
git diff --check
```

确认本包已经获准实现。

## Focused Backend Tests

实现过程中运行：

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests/test_world_generation_schema.py app/tests/test_generation_core_readiness_api.py -q
```

预期覆盖：

- manifest、world creation、director guidance 的 schema serialization。
- `GET /manifest` 返回 200。
- manifest 包含 `/health`、`/openapi.json`、`/worlds`。
- manifest redaction flags 对 private content 为 false。
- provider 缺失时 readiness 不伪造 ready。
- OpenAPI 暴露 `POST /worlds`。
- `POST /worlds` 接受 `world_prompt`。
- `POST /worlds` 返回 top-level `world_id`、`status`、`public_initial_state`、`visualization`。
- public responses 不包含 forbidden private fields。

## Regression Tests

closeout 前运行：

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests -q
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
git diff --check
```

## Runtime Probe

启动 WorldEngine 后探测：

```bash
curl -i http://127.0.0.1:8000/health
curl -i http://127.0.0.1:8000/manifest
curl -i http://127.0.0.1:8000/openapi.json
curl -i -H 'Content-Type: application/json' \
  -d '{"world_prompt":"a small observable generic world"}' \
  http://127.0.0.1:8000/worlds
```

## Optional Validation Client Compatibility Probe

如果 Validation Client 仓库和依赖可用，可运行 `/health/worldengine` 与 `/sessions/worldengine` 探测。该探测只能支持 `WORLDENGINE_CONTRACT_READY`，不是 external validation PASS 或 human validation PASS。

## Pass Criteria

只有满足以下条件，才能结论为 `WORLDENGINE_CONTRACT_READY`：

- backend tests pass。
- runtime probes pass。
- OpenAPI 证明 `POST /worlds` discoverability。
- public responses 证明 required fields。
- redaction checks 未发现 public outputs 泄露 secret 或 private data。
- review evidence 记录 changed files、commands、test results、compatibility review、scope review、unresolved findings。
