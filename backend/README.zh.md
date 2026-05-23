# Backend

Status: v0.1 active backend

英文版本：`README.md`。

本目录包含当前 WorldEngine v0.1 scaffold 使用的 FastAPI backend。Active implementation
位于 `backend/app/`。

`backend/worldengine/` 是 legacy pre-v0.1 code，没有接入 active FastAPI application。

## Quick Start

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

backend 默认地址是 `http://localhost:8000`。

## Environment

| Variable | Default | Purpose |
|---|---:|---|
| `APP_HOST` | `0.0.0.0` | 运行 `python app/main.py` 时使用的 host。 |
| `APP_PORT` | `8000` | 运行 `python app/main.py` 时使用的 port。 |
| `CORS_ORIGINS` | `http://localhost:5173,http://127.0.0.1:5173` | 允许的 frontend origins。 |
| `WORLD_STEP_SECONDS` | `600` | 每个 runtime step 推进的秒数。 |
| `WORLD_SNAPSHOT_INTERVAL_TICKS` | `10` | Snapshot 创建间隔。 |
| `WORLD_SUMMARY_INTERVAL_TICKS` | `20` | Summary 创建间隔。 |
| `WORLD_DRYRUN_STEPS` | `20` | Dry-run simulation 长度。 |
| `WORLD_DRYRUN_MAX_AVG_EVENTS_PER_TICK` | `20` | Dry-run event-rate limit。 |
| `WORLD_DRYRUN_MAX_TOTAL_EVENTS` | `500` | Dry-run total event limit。 |
| `WORLD_DRYRUN_MAX_FINAL_COUNTER` | `100000` | Dry-run counter upper bound。 |

## Current API Groups

- `GET /health`
- `GET /runtime/state`
- `POST /runtime/step`
- `GET /world/events`
- `GET /world/event-steps`
- `GET /world/params`
- `POST /world/params/apply`
- `POST /world/agent/params/propose-and-apply`
- `GET /world/snapshots`
- `GET /world/snapshots/{snapshot_id}`
- `GET /world/summaries`
- `GET /world/summaries/{summary_id}`

Endpoint 级别细节见 `../docs/api-reference-v0.1.md`。

## Current Runtime Behavior

- `RuntimeEngine` 通过 `/runtime/step` 手动推进 ticks。
- `InMemoryEventLog` 存储 runtime、module 和 params events。
- 默认 world module tree 运行 `heartbeat` 和 `counter` 示例。
- World param patches 会先 static validation 和 dry-run，再 apply。
- Snapshots 和 summaries 会按配置 interval 在内存中创建。
- `ParamsAgent` 可以通过 mock LLM provider 提出并应用经过验证的 world param patches。

v0.1 不会加载 `WorldSpec`、生成 worlds、持久化 production world state，也不会运行
Agent perception/action/memory loop。

## Structure

- `app/api` - FastAPI app factory、exception handling 和 routes。
- `app/core` - clock、scheduler、event bus 和 runtime engine。
- `app/world` - world state、params、modules、validation、dry-run 和 archive。
- `app/agent` - params-agent service 与 LLM provider protocol。
- `app/infra` - placeholder repository ports 和 SQLite adapters。
- `app/schemas` - shared Pydantic models。
- `data` - placeholder seed JSON files；v0.1 中不是 active WorldSpec input。

## Verification

```bash
cd backend
.venv/bin/python -m pytest app/tests
```

最新记录的 closeout result：

- `63 passed in 2.93s`

见 `../docs/testing/v0.1-test-map.md` 和
`../docs/testing/results/2026-05-23-v0.1-closeout.md`。
