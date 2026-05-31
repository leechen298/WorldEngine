import { expect, type APIRequestContext, test } from "@playwright/test";

const API_BASE_URL = process.env.E2E_API_BASE_URL ?? "http://127.0.0.1:8000";

type ApiEnvelope<T> = {
  code: number;
  data: T;
  msg: string;
};

type RuntimeState = {
  tick_id: number;
  world_time_seconds: number;
  step_seconds: number;
};

type WorldEvent = {
  id: string;
  tick_id: number;
  type: string;
  source: string;
  payload: Record<string, unknown>;
};

type WorldParams = Record<string, unknown>;

type LoopStepResponse = {
  perception: {
    runtime: RuntimeState & { is_running: boolean };
    params: WorldParams;
    recent_events: WorldEvent[];
  };
  intent: {
    type: string;
    reason?: string | null;
    patches: Array<Record<string, unknown>>;
  };
  result: {
    status: string;
    applied: boolean;
    action_type: string;
    event_id?: string | null;
    patches: Array<Record<string, unknown>>;
    errors: Array<Record<string, unknown>>;
    metrics: Record<string, unknown>;
    params: WorldParams;
    message: string;
  };
};

async function getApiData<T>(request: APIRequestContext, path: string): Promise<T> {
  const response = await request.get(`${API_BASE_URL}${path}`);
  expect(response.ok()).toBeTruthy();
  const payload = (await response.json()) as ApiEnvelope<T>;
  expect(payload.code).toBe(0);
  return payload.data;
}

async function postApiData<T>(
  request: APIRequestContext,
  path: string,
  data?: Record<string, unknown>,
): Promise<T> {
  const response = await request.post(`${API_BASE_URL}${path}`, data === undefined ? undefined : { data });
  expect(response.ok()).toBeTruthy();
  const payload = (await response.json()) as ApiEnvelope<T>;
  expect(payload.code).toBe(0);
  return payload.data;
}

async function getRuntimeState(request: APIRequestContext): Promise<RuntimeState> {
  return getApiData<RuntimeState>(request, "/runtime/state");
}

async function getWorldParams(request: APIRequestContext): Promise<WorldParams> {
  return getApiData<WorldParams>(request, "/world/params");
}

async function getRecentEvents(request: APIRequestContext): Promise<WorldEvent[]> {
  const page = await getApiData<{ items: WorldEvent[] }>(request, "/world/events?limit=100");
  return page.items;
}

function readParamValue(value: unknown): unknown {
  if (value && typeof value === "object" && "value" in value) {
    return (value as Record<string, unknown>).value;
  }
  return value;
}

function readCounterIncrement(params: WorldParams): unknown {
  const counter = params.counter;
  if (!counter || typeof counter !== "object") {
    return undefined;
  }
  const increment = (counter as Record<string, unknown>).increment;
  return readParamValue(increment);
}

function paramsAppliedEventIds(events: WorldEvent[]): Set<string> {
  return new Set(events.filter((event) => event.type === "params.applied").map((event) => event.id));
}

async function expectNoParamsMutationOrAppliedEvent(
  request: APIRequestContext,
  paramsBefore: WorldParams,
  appliedBefore: Set<string>,
): Promise<void> {
  expect(await getWorldParams(request)).toEqual(paramsBefore);
  expect(paramsAppliedEventIds(await getRecentEvents(request))).toEqual(appliedBefore);
}

async function postExpectValidationError(
  request: APIRequestContext,
  data: Record<string, unknown>,
): Promise<ApiEnvelope<{ errors: Array<{ type: string }> }>> {
  const response = await request.post(`${API_BASE_URL}/world/agent/loop/step`, { data });
  expect(response.status()).toBe(422);
  const body = (await response.json()) as ApiEnvelope<{ errors: Array<{ type: string }> }>;
  expect(body.code).toBe(30);
  expect(body.data.errors).not.toHaveLength(0);
  return body;
}

test.describe.configure({ mode: "serial" });

test("agent-loop-noop returns bounded perception without mutation", async ({ request }) => {
  const paramsBefore = await getWorldParams(request);
  await postApiData<RuntimeState>(request, "/runtime/step");
  const runtimeBeforeLoop = await getRuntimeState(request);
  const appliedBefore = paramsAppliedEventIds(await getRecentEvents(request));

  const data = await postApiData<LoopStepResponse>(request, "/world/agent/loop/step", {
    event_limit: 1,
  });

  expect(data.perception.runtime.tick_id).toBe(runtimeBeforeLoop.tick_id);
  expect(data.perception.recent_events).toHaveLength(1);
  expect(data.perception.recent_events[0].tick_id).toBe(runtimeBeforeLoop.tick_id);
  expect(data.perception.recent_events[0].type).not.toBe("");
  expect(data.intent.type).toBe("noop");
  expect(data.intent.reason).toBe("default deterministic noop");
  expect(data.result.status).toBe("noop");
  expect(data.result.applied).toBe(false);
  expect(data.result.action_type).toBe("noop");
  expect(data.result.message).toBe("No action applied.");
  expect(await getWorldParams(request)).toEqual(paramsBefore);
  expect(paramsAppliedEventIds(await getRecentEvents(request))).toEqual(appliedBefore);
});

test("agent-loop-params-patch applies patch and emits agent.loop event", async ({ request }) => {
  const currentIncrement = readCounterIncrement(await getWorldParams(request));
  const targetIncrement = currentIncrement === 7 ? 8 : 7;

  const data = await postApiData<LoopStepResponse>(request, "/world/agent/loop/step", {
    event_limit: 5,
    intent: {
      type: "params.patch",
      reason: "e2e loop accepted patch",
      patches: [
        {
          op: "set",
          path: "counter.increment",
          value: { value: targetIncrement, type: "number" },
        },
      ],
    },
  });

  expect(data.intent.type).toBe("params.patch");
  expect(data.intent.reason).toBe("e2e loop accepted patch");
  expect(data.result.status).toBe("accepted");
  expect(data.result.applied).toBe(true);
  expect(data.result.action_type).toBe("params.patch");
  expect(data.result.event_id).toEqual(expect.any(String));
  expect(readCounterIncrement(data.result.params)).toBe(targetIncrement);
  expect(readCounterIncrement(await getWorldParams(request))).toBe(targetIncrement);

  const event = (await getRecentEvents(request)).find((item) => item.id === data.result.event_id);
  expect(event).toBeTruthy();
  expect(event?.type).toBe("params.applied");
  expect(event?.source).toBe("agent.loop");
  expect(event?.payload.reason).toBe("e2e loop accepted patch");
  expect((event?.payload.patches as Array<Record<string, unknown>>)[0].path).toBe("counter.increment");
});

test("agent-loop-reserved-path params-patch returns rejected result without mutation", async ({ request }) => {
  const paramsBefore = await getWorldParams(request);
  const appliedBefore = paramsAppliedEventIds(await getRecentEvents(request));

  const data = await postApiData<LoopStepResponse>(request, "/world/agent/loop/step", {
    intent: {
      type: "params.patch",
      reason: "e2e loop rejected reserved path",
      patches: [
        {
          op: "set",
          path: "runtime.secret",
          value: 3,
        },
      ],
    },
  });

  expect(data.intent.type).toBe("params.patch");
  expect(data.result.status).toBe("rejected");
  expect(data.result.applied).toBe(false);
  expect(data.result.action_type).toBe("params.patch");
  expect(data.result.event_id ?? null).toBeNull();
  expect(data.result.errors[0].reason).toBe("reserved_prefix");
  await expectNoParamsMutationOrAppliedEvent(request, paramsBefore, appliedBefore);
});

test("agent-loop-noop intent rejects patches without mutation", async ({ request }) => {
  const paramsBefore = await getWorldParams(request);
  const appliedBefore = paramsAppliedEventIds(await getRecentEvents(request));

  const data = await postApiData<LoopStepResponse>(request, "/world/agent/loop/step", {
    intent: {
      type: "noop",
      patches: [
        {
          op: "set",
          path: "counter.increment",
          value: 3,
        },
      ],
    },
  });

  expect(data.intent.type).toBe("noop");
  expect(data.result.status).toBe("rejected");
  expect(data.result.applied).toBe(false);
  expect(data.result.action_type).toBe("noop");
  expect(data.result.event_id ?? null).toBeNull();
  expect(data.result.errors[0].reason).toBe("unexpected_payload");
  await expectNoParamsMutationOrAppliedEvent(request, paramsBefore, appliedBefore);
});

test("agent-loop-empty params-patch rejects without mutation", async ({ request }) => {
  const paramsBefore = await getWorldParams(request);
  const appliedBefore = paramsAppliedEventIds(await getRecentEvents(request));

  const data = await postApiData<LoopStepResponse>(request, "/world/agent/loop/step", {
    intent: {
      type: "params.patch",
      patches: [],
    },
  });

  expect(data.result.status).toBe("rejected");
  expect(data.result.applied).toBe(false);
  expect(data.result.action_type).toBe("params.patch");
  expect(data.result.event_id ?? null).toBeNull();
  expect(data.result.errors[0].reason).toBe("empty_patch");
  await expectNoParamsMutationOrAppliedEvent(request, paramsBefore, appliedBefore);
});

test("agent-loop-dry-run rejection returns metrics without mutation", async ({ request }) => {
  const paramsBefore = await getWorldParams(request);
  const appliedBefore = paramsAppliedEventIds(await getRecentEvents(request));

  const data = await postApiData<LoopStepResponse>(request, "/world/agent/loop/step", {
    intent: {
      type: "params.patch",
      reason: "e2e duplicate path dry-run rejection",
      patches: [
        {
          op: "set",
          path: "counter.increment",
          value: { value: 1, type: "number" },
        },
        {
          op: "set",
          path: "counter.increment",
          value: { value: 1, type: "number" },
        },
      ],
    },
  });

  expect(data.result.status).toBe("rejected");
  expect(data.result.applied).toBe(false);
  expect(data.result.errors.some((error) => error.reason === "high_frequency_toggle")).toBeTruthy();
  expect(data.result.metrics.duplicate_set_paths).toEqual(["counter.increment"]);
  expect(data.result.metrics.policy).toEqual(expect.any(Object));
  await expectNoParamsMutationOrAppliedEvent(request, paramsBefore, appliedBefore);
});

test("agent-loop-multi-patch and remove flow updates params and event evidence", async ({ request }) => {
  const currentIncrement = readCounterIncrement(await getWorldParams(request));
  const targetIncrement = currentIncrement === 5 ? 6 : 5;

  const data = await postApiData<LoopStepResponse>(request, "/world/agent/loop/step", {
    intent: {
      type: "params.patch",
      reason: "e2e multi patch and remove",
      patches: [
        {
          op: "set",
          path: "counter.increment",
          value: { value: targetIncrement, type: "number" },
        },
        {
          op: "set",
          path: "scene.weather",
          value: { value: "rain", type: "string" },
        },
        {
          op: "remove",
          path: "scene.weather",
        },
      ],
    },
  });

  expect(data.result.status).toBe("accepted");
  expect(data.result.applied).toBe(true);
  expect(data.result.action_type).toBe("params.patch");
  expect(data.result.event_id).toEqual(expect.any(String));
  expect(data.result.event_id).not.toBe("");
  expect(data.result.patches).toHaveLength(3);
  expect(readCounterIncrement(await getWorldParams(request))).toBe(targetIncrement);
  expect((await getWorldParams(request)).scene).toBeUndefined();

  const event = (await getRecentEvents(request)).find((item) => item.id === data.result.event_id);
  expect(event).toBeTruthy();
  expect(event?.id).toBe(data.result.event_id);
  expect(event?.type).toBe("params.applied");
  expect(event?.source).toBe("agent.loop");
  expect(event?.payload.reason).toBe("e2e multi patch and remove");
  expect(event?.payload.patches).toEqual([
    {
      op: "set",
      path: "counter.increment",
      value: { value: targetIncrement, type: "number" },
    },
    {
      op: "set",
      path: "scene.weather",
      value: { value: "rain", type: "string" },
    },
    {
      op: "remove",
      path: "scene.weather",
      value: null,
    },
  ]);
});

test("agent-loop-rejected-action preserves state and returns 200 result", async ({ request }) => {
  const paramsBefore = await getWorldParams(request);
  const appliedBefore = paramsAppliedEventIds(await getRecentEvents(request));

  const data = await postApiData<LoopStepResponse>(request, "/world/agent/loop/step", {
    intent: {
      type: "world.spawn",
      metadata: { source: "e2e" },
    },
  });

  expect(data.result.status).toBe("rejected");
  expect(data.result.applied).toBe(false);
  expect(data.result.action_type).toBe("world.spawn");
  expect(data.result.errors[0].reason).toBe("unsupported_action");
  expect(data.result.event_id ?? null).toBeNull();
  await expectNoParamsMutationOrAppliedEvent(request, paramsBefore, appliedBefore);
});

test("agent-loop-schema-errors stay 422 and do not mutate params", async ({ request }) => {
  const paramsBefore = await getWorldParams(request);
  const appliedBefore = paramsAppliedEventIds(await getRecentEvents(request));

  const zeroLimitBody = await postExpectValidationError(request, { event_limit: 0 });
  expect(zeroLimitBody.data.errors[0].type).toBe("greater_than_equal");
  await expectNoParamsMutationOrAppliedEvent(request, paramsBefore, appliedBefore);

  const highLimitBody = await postExpectValidationError(request, { event_limit: 201 });
  expect(highLimitBody.data.errors[0].type).toBe("less_than_equal");
  await expectNoParamsMutationOrAppliedEvent(request, paramsBefore, appliedBefore);

  const requestExtraBody = await postExpectValidationError(request, {
    event_limit: 1,
    unexpected: "drop-me",
    intent: {
      type: "params.patch",
      patches: [{ op: "set", path: "counter.increment", value: 8 }],
    },
  });
  expect(requestExtraBody.data.errors[0].type).toBe("extra_forbidden");
  await expectNoParamsMutationOrAppliedEvent(request, paramsBefore, appliedBefore);

  const patchExtraBody = await postExpectValidationError(request, {
    intent: {
      type: "params.patch",
      patches: [
        {
          op: "set",
          path: "counter.increment",
          value: 8,
          unexpected_patch_field: true,
        },
      ],
    },
  });
  expect(patchExtraBody.data.errors[0].type).toBe("extra_forbidden");
  await expectNoParamsMutationOrAppliedEvent(request, paramsBefore, appliedBefore);
});
