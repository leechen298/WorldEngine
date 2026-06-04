# 0.8.9 详细实施计划

状态：计划完成 / 待实现

英文镜像：`implementation-task-plan.md`。

本文把 0.8.9 的后续实现拆成可以交给未来聊天逐项执行、逐项验证、逐项记录的
任务。当前 package 仍是 documentation-only planning package；实现必须在用户明
确 review 并授权后开始。

## 0. 实现前置条件

未来实现聊天必须先读取：

```text
AGENTS.md
docs/project-north-star.md
docs/product-model.md
docs/scope-boundaries.md
docs/roadmap.md
docs/iterations/README.md
docs/iterations/AGENTS.md
docs/iterations/v0.8/README.zh.md
docs/iterations/v0.8/CURRENT_STATE.zh.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/README.zh.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/contract.zh.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/technical-design.zh.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/test-plan.zh.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/validation-client-contract-handoff.zh.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/implementation-task-plan.zh.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/contract-readiness-checklist.zh.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/implementation-handoff-prompt.zh.md
```

实现前必须确认：

- 本 package 已通过用户 review。
- 当前聊天明确授权 implementation。
- 目标只限 WorldEngine public contract。
- 不修改 Validation Client 仓库。
- 不加入具体 demo-world、具体角色、具体地图或应用专属逻辑。

## 1. 候选文件责任

未来实现可优先检查并修改：

```text
backend/app/main.py
backend/app/api/app_factory.py
backend/app/api/routes/__init__.py
backend/app/api/routes/health.py
backend/app/api/routes/world_generation.py
backend/app/api/routes/world.py
backend/app/schemas/api.py
backend/app/schemas/world_generation.py
backend/app/schemas/world.py
backend/app/core/world_generation.py
backend/app/tests/test_generation_core_readiness_api.py
backend/app/tests/test_world_generation_schema.py
```

如需要独立 contract 或 schema 文档，可创建：

```text
docs/contracts/validation-client-handoff-manifest.md
docs/contracts/validation-client-handoff-manifest.zh.md
```

禁止修改：

```text
backend/worldengine/
Validation Client repository
demo-specific world fixtures
private prompt files
provider credential storage
external validator implementation
```

## 2. 推荐任务顺序

每个 task 应单独提交。若某 task 发现设计缺口，先停下更新本 package 的 contract、
technical design 或 test plan，再继续。

### Task 1: Public handoff schemas

目标：定义 `/manifest`、`POST /worlds` 和 director guidance 的 public response
shape。

实现内容：

- 新增或扩展 Pydantic schema，包含：
  - manifest schema version。
  - WorldEngine public version label。
  - provider public readiness。
  - public surface ids。
  - redaction flags。
  - blockers and warnings。
  - public world creation request / response。
  - public director guidance request / response。
- 字段必须只表达 public summary，不允许 provider raw trace、private prompt 或
  Agent private state。

测试重点：

- schema 可以序列化。
- redaction flags 默认为不包含 secrets。
- forbidden private fields 不在 response model 中。

验证命令：

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests/test_world_generation_schema.py app/tests/test_generation_core_readiness_api.py -q
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
git diff --check
```

### Task 2: `GET /manifest`

目标：提供 Validation Client 可读取的 public readiness document。

实现内容：

- 新增 public route `GET /manifest`。
- route 返回 public provider readiness、public surfaces、redaction flags、blockers
  和 warnings。
- provider readiness 只能公开：
  - provider class。
  - readiness。
  - credential source class。
  - public model label。
- 未配置 provider 时返回 `blocked` 或 `unknown`，不能伪造 ready。

测试重点：

- `GET /manifest` 返回 200。
- response 包含 `/health`、`/openapi.json`、`/worlds`。
- secrets、private prompts、provider raw traces 不出现在 response。
- provider 未配置时有 public blocker 或 warning。

验证命令：

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests/test_generation_core_readiness_api.py -q
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
git diff --check
```

### Task 3: OpenAPI-discoverable `POST /worlds`

目标：让 Validation Client 能自动发现并调用 world creation endpoint。

实现内容：

- 新增 public `POST /worlds`，或确保现有 endpoint 满足 Validation Client discovery
  规则。
- 推荐 operation id 为 `create_world` 或 `createWorld`。
- response 必须包含：
  - public `world_id`。
  - `status`。
  - `public_initial_state` 或 `initial_state`。
  - `visualization` 或 `visualization_payload`。
- 实现可以复用现有 world generation core，但不得引入 concrete demo-world fixtures。

测试重点：

- OpenAPI 中能看到 `POST /worlds`。
- `POST /worlds` 可以用基础 `world_prompt` 创建 public world response。
- response 不包含 private generation prompt、provider raw response、internal helper
  path。

验证命令：

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests/test_generation_core_readiness_api.py app/tests/test_deterministic_world_generation.py -q
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
git diff --check
```

### Task 4: Public director guidance endpoint

目标：支持验证客户端提交高层演化方向，但不直接操控 Agent 私有状态。

实现内容：

- 新增 `POST /worlds/{world_id}/director-guidance`，或记录为明确不支持并返回
  public unavailable reason。
- request 接收：
  - `instruction_text`。
  - optional `branch_id`。
  - optional `tick`。
  - optional public context。
- response 返回：
  - `accepted`、`applied`、`blocked` 或 `unavailable`。
  - public explanation。
  - optional public event id。
- 不允许直接写 Agent memory、private goal、identity、relationship、self_state。

测试重点：

- endpoint 出现在 OpenAPI。
- 正常请求返回 public status。
- 禁止字段不会被接受为 Agent private mutation。

验证命令：

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests/test_agent_loop_api.py app/tests/test_generation_core_readiness_api.py -q
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
git diff --check
```

### Task 5: Provider readiness redaction

目标：确保 provider 状态可以公开，但凭据和 raw trace 永不公开。

实现内容：

- 从环境配置或 provider abstraction 读取 public readiness label。
- 返回 credential source class，例如 `environment`、`not_configured` 或 `unknown`。
- 返回 public model label。
- 不返回 API key、authorization header、account id、raw request、raw response。

测试重点：

- 配置缺失时 readiness 不是 fake ready。
- public response 不包含 forbidden terms 的真实敏感值。
- redaction flags 与 response 内容一致。

验证命令：

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests/test_generation_core_readiness_api.py -q
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
git diff --check
```

### Task 6: Validation Client compatibility probe

目标：用外部客户端现有接口证明 contract 可被消费。

验证步骤：

1. 启动 WorldEngine：

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

2. 另一个 shell 验证 WorldEngine：

```bash
curl -i http://127.0.0.1:8000/health
curl -i http://127.0.0.1:8000/manifest
curl -i http://127.0.0.1:8000/openapi.json
curl -i -H 'Content-Type: application/json' \
  -d '{"world_prompt":"一个可观察的小型像素世界"}' \
  http://127.0.0.1:8000/worlds
```

3. 启动 Validation Client API：

```bash
cd /Users/leechen/projects/WorldEngine-Validation-Client
uv run --project apps/api uvicorn app.main:app --host 127.0.0.1 --port 8765 --app-dir apps/api
```

4. 验证客户端 discovery：

```bash
curl -i http://127.0.0.1:8765/health/worldengine
curl -i -H 'Content-Type: application/json' \
  -d '{"session_name":"Codex contract check","world_prompt":"一个可观察的小型像素世界"}' \
  http://127.0.0.1:8765/sessions/worldengine
```

完成标准：

- `/health/worldengine` 报告 `world_creation: available`。
- `POST /sessions/worldengine` 成功。
- 仍不声明 Codex autonomous validation PASS 或 human validation PASS。

### Task 7: Full regression and review closeout

目标：给未来实现写入可靠 review evidence。

必须运行：

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine/backend
.venv/bin/python -m pytest app/tests -q
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
git diff --check
rg -n "api_key|apikey|secret|token|password|credential|authorization|private_prompt|provider raw|raw_response|private memory|private goal|self_state|hidden_context" backend/app docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest
```

必须更新：

```text
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/review.md
docs/iterations/v0.8/0.8.9-external-validation-provider-and-handoff-manifest/review.zh.md
```

完成标准：

- `contract-readiness-checklist.zh.md` 可被填写为本次 contract readiness evidence。
- review 记录 changed files、commands、test results、compatibility review、scope
  review 和 unresolved findings。
- 结论只能写 WorldEngine public contract ready for Validation Client autonomous
  validation。
- 不写 external validation PASS。
- 不写 human validation PASS。

## 3. Stop Rules

- 如果需要具体 demo-world content，停止。
- 如果 public response 会暴露 secrets、private prompt、provider raw trace 或
  private Agent state，停止并 FAIL。
- 如果需要修改 Validation Client，停止并记录为 downstream task。
- 如果实现会改变 v0.8 final closeout 含义，停止。
- 如果 director guidance 会直接改 Agent private state，停止。
- 如果测试无法证明 OpenAPI discoverability，不能声明 contract ready。
