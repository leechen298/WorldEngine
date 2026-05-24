import { expect, type APIRequestContext, type Page, test } from "@playwright/test";

const API_BASE_URL = process.env.E2E_API_BASE_URL ?? "http://127.0.0.1:8000";

type RuntimeState = {
  tick_id: number;
  world_time_seconds: number;
  step_seconds: number;
};

type WorldEvent = {
  tick_id: number;
  type: string;
  payload: Record<string, unknown>;
};

type WorldParams = Record<string, unknown>;

type WorldSummary = {
  id: string;
  from_tick: number;
  to_tick: number;
  created_at: string;
  text: string;
  stats: {
    total_events: number;
    type_counts: Record<string, number>;
  };
};

async function getApiData<T>(request: APIRequestContext, path: string): Promise<T> {
  const response = await request.get(`${API_BASE_URL}${path}`);
  expect(response.ok()).toBeTruthy();
  const payload = (await response.json()) as { code: number; data: T; msg: string };
  expect(payload.code).toBe(0);
  return payload.data;
}

async function getRuntimeState(request: APIRequestContext): Promise<RuntimeState> {
  return getApiData<RuntimeState>(request, "/runtime/state");
}

async function getWorldParams(request: APIRequestContext): Promise<WorldParams> {
  return getApiData<WorldParams>(request, "/world/params");
}

async function getLatestSummary(request: APIRequestContext): Promise<WorldSummary | null> {
  const page = await getApiData<{ items: WorldSummary[] }>(request, "/world/summaries?limit=1&order=desc");
  return page.items[0] ?? null;
}

async function getEventsForTick(request: APIRequestContext, tickId: number): Promise<WorldEvent[]> {
  const page = await getApiData<{ items: WorldEvent[] }>(
    request,
    `/world/events?from_tick=${tickId}&to_tick=${tickId}&limit=50`,
  );
  return page.items;
}

function readCounterIncrement(params: WorldParams): unknown {
  const counter = params.counter;
  if (!counter || typeof counter !== "object") {
    return undefined;
  }
  const increment = (counter as Record<string, unknown>).increment;
  if (increment && typeof increment === "object" && "value" in increment) {
    return (increment as Record<string, unknown>).value;
  }
  return increment;
}

async function setWorldParam(page: Page, path: string, type: string, value: string): Promise<void> {
  await page.getByTestId("world-params-path-input").fill(path);
  if (type !== "string") {
    const typeSelect = page.getByTestId("world-params-type-select");
    await typeSelect.click();
    if (type === "number") {
      await page.keyboard.press("ArrowDown");
    } else if (type === "boolean") {
      await page.keyboard.press("ArrowDown");
      await page.keyboard.press("ArrowDown");
    } else if (type === "json") {
      await page.keyboard.press("ArrowDown");
      await page.keyboard.press("ArrowDown");
      await page.keyboard.press("ArrowDown");
    }
    await page.keyboard.press("Enter");
    await expect(typeSelect).toContainText(type);
  }
  await page.getByTestId("world-params-value-input").fill(value);
  await page.getByTestId("world-params-apply-button").click();
}

function isNewerSummary(summary: WorldSummary | null, before: WorldSummary | null): summary is WorldSummary {
  if (summary === null) {
    return false;
  }
  if (before === null) {
    return true;
  }
  return summary.id !== before.id && summary.to_tick > before.to_tick;
}

async function waitForNewerSummary(
  request: APIRequestContext,
  before: WorldSummary | null,
): Promise<WorldSummary> {
  let latest: WorldSummary | null = null;
  await expect
    .poll(
      async () => {
        latest = await getLatestSummary(request);
        return isNewerSummary(latest, before);
      },
      { timeout: 15_000 },
    )
    .toBe(true);
  expect(latest).not.toBeNull();
  return latest as WorldSummary;
}

async function stepRuntimeOnce(page: Page, request: APIRequestContext): Promise<number> {
  const before = await getRuntimeState(request);
  await page.getByTestId("runtime-step-button").click();
  await expect.poll(async () => (await getRuntimeState(request)).tick_id).toBe(before.tick_id + 1);
  return before.tick_id + 1;
}

test.describe.configure({ mode: "serial" });

test("dashboard-basic-runtime advances one tick and records timeline evidence", async ({ page, request }) => {
  const before = await getRuntimeState(request);

  await page.goto("/");
  await expect(page.getByTestId("backend-health-status")).toHaveText("ok");
  await expect(page.getByTestId("runtime-tick-id")).toHaveText(String(before.tick_id));

  await page.getByTestId("runtime-step-button").click();
  await expect.poll(async () => (await getRuntimeState(request)).tick_id).toBe(before.tick_id + 1);

  const after = await getRuntimeState(request);
  await expect(page.getByTestId("runtime-tick-id")).toHaveText(String(after.tick_id));

  const events = await getEventsForTick(request, after.tick_id);
  expect(events.some((event) => event.type === "tick.advanced" || event.type.startsWith("module."))).toBeTruthy();
  await expect(page.getByTestId("timeline-panel")).toContainText(/tick\.advanced|module\./);
});

test("dashboard-params-flow applies counter increment and proves it through API and events", async ({
  page,
  request,
}) => {
  await getWorldParams(request);

  await page.goto("/");
  await setWorldParam(page, "counter.increment", "number", "2");

  await expect.poll(async () => readCounterIncrement(await getWorldParams(request))).toBe(2);
  await expect(page.getByTestId("world-params-json")).toContainText('"increment"');

  const beforeStep = await getRuntimeState(request);
  await page.getByTestId("runtime-step-button").click();
  await expect.poll(async () => (await getRuntimeState(request)).tick_id).toBe(beforeStep.tick_id + 1);

  const afterStep = await getRuntimeState(request);
  const events = await getEventsForTick(request, afterStep.tick_id);
  const counterEvent = events.find((event) => event.type === "module.counter");
  expect(counterEvent?.payload.increment).toBe(2);
});

test("dashboard-invalid-param shows an error and leaves params unchanged", async ({ page, request }) => {
  const beforeParams = await getWorldParams(request);

  await page.goto("/");
  await setWorldParam(page, "system.secret", "string", "blocked");

  await expect(page.getByTestId("world-params-error")).toContainText(/Param validation failed|Reserved params/);

  const afterParams = await getWorldParams(request);
  expect(afterParams).toEqual(beforeParams);
});

test("dashboard-archive-summary creates and renders a newer archive summary", async ({ page, request }) => {
  const beforeSummary = await getLatestSummary(request);

  await page.goto("/");
  await expect(page.getByTestId("memory-panel")).toBeVisible();

  for (let step = 0; step < 4; step += 1) {
    await stepRuntimeOnce(page, request);
  }

  const latestSummary = await waitForNewerSummary(request, beforeSummary);
  expect(latestSummary.to_tick).toBeGreaterThanOrEqual(latestSummary.from_tick);
  expect(latestSummary.stats.total_events).toBeGreaterThan(0);
  expect(latestSummary.stats.type_counts["tick.advanced"]).toBeGreaterThan(0);

  await expect(page.getByTestId("memory-summary-stats")).toContainText(
    `${latestSummary.from_tick} - ${latestSummary.to_tick}`,
  );
  await expect(page.getByTestId("memory-summary-stats")).toContainText(String(latestSummary.stats.total_events));
  await expect(page.getByTestId("memory-summary-stats")).toContainText("tick.advanced");
  await expect(page.getByTestId("memory-summary-text")).toContainText(latestSummary.text);
});
