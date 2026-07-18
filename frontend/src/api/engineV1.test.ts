import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import {
  EngineV1ApiError,
  createWorldPackage,
  createWorldSession,
  exportSessionEvidence,
  getEngineCapabilities,
  getPublicProjection,
  getWorldPackage,
  getWorldSession,
  pollWorldEvents,
  stepWorldSession,
  submitWorldAction,
  submitWorldDirection,
  submitWorldFeedback,
} from "./engineV1";

const API_BASE_URL = "http://localhost:8000";

function jsonResponse(data: unknown, status = 200): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}

describe("Engine V1 API client", () => {
  const fetchMock = vi.fn<typeof fetch>();

  beforeEach(() => {
    fetchMock.mockImplementation(async () =>
      jsonResponse({ code: 0, data: {}, msg: "ok" }),
    );
    vi.stubGlobal("fetch", fetchMock);
  });

  afterEach(() => {
    vi.unstubAllGlobals();
  });

  it("uses the independent /api/v1 discovery and query routes", async () => {
    await getEngineCapabilities();
    await getWorldPackage("package / one");
    await getWorldSession("session / one");
    await getPublicProjection("session / one");
    await pollWorldEvents("session / one", { afterSequence: 7, limit: 40 });
    await exportSessionEvidence("session / one");

    expect(fetchMock.mock.calls.map(([url]) => url)).toEqual([
      `${API_BASE_URL}/api/v1/capabilities`,
      `${API_BASE_URL}/api/v1/world-packages/package%20%2F%20one`,
      `${API_BASE_URL}/api/v1/sessions/session%20%2F%20one`,
      `${API_BASE_URL}/api/v1/sessions/session%20%2F%20one/projection`,
      `${API_BASE_URL}/api/v1/sessions/session%20%2F%20one/events?after_sequence=7&limit=40`,
      `${API_BASE_URL}/api/v1/sessions/session%20%2F%20one/evidence`,
    ]);
    expect(fetchMock.mock.calls.every(([, init]) => init === undefined)).toBe(true);
  });

  it("serializes every mutation as JSON on its versioned route", async () => {
    const brief = {
      seed: "seed-1",
      premise: "public premise",
      constraints: {},
      state_variables: [
        { key: "world_signal", initial: 0, minimum: -10, maximum: 10, step: 1 },
      ],
      agent_count: 1 as const,
      step_seconds: 1,
    };
    const calls = [
      () => createWorldPackage({ request_id: "package-1", brief }),
      () =>
        createWorldSession({
          request_id: "session-1",
          package_id: "package-1",
          package_hash: "a".repeat(64),
        }),
      () =>
        stepWorldSession("session-1", {
          request_id: "step-1",
          step_count: 2,
          expected_revision: 0,
        }),
      () =>
        submitWorldDirection("session-1", {
          request_id: "direction-1",
          window_id: "window-1",
          expected_revision: 0,
          kind: "bounded_pressure",
          target_ref: "world_signal",
          summary: "bounded",
          magnitude: 1,
        }),
      () =>
        submitWorldAction("session-1", {
          request_id: "action-1",
          expected_revision: 1,
          action_id: "action.adjust.world_signal",
          target_ref: "world_signal",
          amount: 1,
        }),
      () =>
        submitWorldFeedback("session-1", {
          request_id: "feedback-1",
          expected_revision: 2,
          feedback_type: "local_outcome_observed",
          summary: "observed",
          related_event_ref: "event-1",
        }),
    ];

    for (const call of calls) {
      await call();
    }

    const routeAndBody = fetchMock.mock.calls.map(([url, init]) => ({
      url,
      method: init?.method,
      contentType: new Headers(init?.headers).get("Content-Type"),
      body: JSON.parse(String(init?.body)) as Record<string, unknown>,
    }));
    expect(routeAndBody.map(({ url }) => url)).toEqual([
      `${API_BASE_URL}/api/v1/world-packages`,
      `${API_BASE_URL}/api/v1/sessions`,
      `${API_BASE_URL}/api/v1/sessions/session-1/steps`,
      `${API_BASE_URL}/api/v1/sessions/session-1/directions`,
      `${API_BASE_URL}/api/v1/sessions/session-1/actions`,
      `${API_BASE_URL}/api/v1/sessions/session-1/feedback`,
    ]);
    expect(routeAndBody.every(({ method }) => method === "POST")).toBe(true);
    expect(routeAndBody.every(({ contentType }) => contentType === "application/json")).toBe(true);
    expect(routeAndBody[2].body).toMatchObject({ request_id: "step-1", step_count: 2 });
    expect(routeAndBody[3].body).toMatchObject({
      window_id: "window-1",
      kind: "bounded_pressure",
    });
  });

  it("preserves the public conflict reason from the API envelope", async () => {
    fetchMock.mockResolvedValueOnce(
      jsonResponse(
        {
          code: 40,
          msg: "expected_revision does not match current session revision",
          data: { reason_code: "stale_revision", current_revision: 4 },
        },
        409,
      ),
    );

    const error = await stepWorldSession("session-1", {
      request_id: "step-stale",
      step_count: 1,
      expected_revision: 2,
    }).catch((caught: unknown) => caught);

    expect(error).toBeInstanceOf(EngineV1ApiError);
    expect(error).toMatchObject({
      status: 409,
      code: 40,
      data: { reason_code: "stale_revision", current_revision: 4 },
    });
  });

  it("rejects a successful HTTP response with an invalid API envelope", async () => {
    fetchMock.mockResolvedValueOnce(jsonResponse({ code: 7, data: null, msg: "not ok" }));

    await expect(getEngineCapabilities()).rejects.toMatchObject({
      name: "EngineV1ApiError",
      status: 200,
      code: 7,
      message: "not ok",
    });
  });
});
