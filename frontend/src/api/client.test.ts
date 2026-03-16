import { afterEach, describe, expect, it, vi } from "vitest";

import {
  applyWorldParams,
  ApiClientError,
  fetchHealth,
  getWorldParams,
  getWorldEvents,
  getRuntimeState,
  stepRuntime,
} from "./client";

const fetchMock = vi.fn();

vi.stubGlobal("fetch", fetchMock);

describe("api client", () => {
  afterEach(() => {
    fetchMock.mockReset();
  });

  it("unwraps successful response data", async () => {
    fetchMock.mockResolvedValue(
      new Response(
        JSON.stringify({
          code: 0,
          msg: "ok",
          data: {
            tick_id: 3,
            world_time_seconds: 1800,
            step_seconds: 600,
            updated_at: "2026-03-09T00:00:00+00:00",
          },
        }),
        {
          status: 200,
          headers: { "Content-Type": "application/json" },
        },
      ),
    );

    await expect(getRuntimeState()).resolves.toEqual({
      tick_id: 3,
      world_time_seconds: 1800,
      step_seconds: 600,
      updated_at: "2026-03-09T00:00:00+00:00",
    });
    expect(fetchMock).toHaveBeenCalledWith("http://localhost:8000/runtime/state", undefined);
  });

  it("throws ApiClientError for http errors with api payload", async () => {
    fetchMock.mockResolvedValue(
      new Response(
        JSON.stringify({
          code: 20,
          msg: "Unauthenticated",
        }),
        {
          status: 401,
          headers: { "Content-Type": "application/json" },
        },
      ),
    );

    await expect(fetchHealth()).rejects.toMatchObject({
      name: "ApiClientError",
      message: "Unauthenticated",
      status: 401,
      code: 20,
    });
  });

  it("throws ApiClientError when success status has non-zero business code", async () => {
    fetchMock.mockResolvedValue(
      new Response(
        JSON.stringify({
          code: 29,
          msg: "Conflict",
          data: null,
        }),
        {
          status: 200,
          headers: { "Content-Type": "application/json" },
        },
      ),
    );

    await expect(stepRuntime()).rejects.toMatchObject({
      name: "ApiClientError",
      message: "Conflict",
      status: 200,
      code: 29,
    });
  });

  it("builds query strings for world events", async () => {
    fetchMock.mockResolvedValue(
      new Response(
        JSON.stringify({
          code: 0,
          msg: "ok",
          data: {
            items: [],
            next_cursor: "evt-2",
            has_more: true,
            limit: 10,
          },
        }),
        {
          status: 200,
          headers: { "Content-Type": "application/json" },
        },
      ),
    );

    await expect(
      getWorldEvents({ from_tick: 2, to_tick: 4, cursor: "evt-9", limit: 10 }),
    ).resolves.toEqual({
      items: [],
      next_cursor: "evt-2",
      has_more: true,
      limit: 10,
    });
    expect(fetchMock).toHaveBeenCalledWith(
      "http://localhost:8000/world/events?from_tick=2&to_tick=4&cursor=evt-9&limit=10",
      undefined,
    );
  });

  it("loads world params", async () => {
    fetchMock.mockResolvedValue(
      new Response(
        JSON.stringify({
          code: 0,
          msg: "ok",
          data: {
            counter: {
              increment: 2,
            },
          },
        }),
        {
          status: 200,
          headers: { "Content-Type": "application/json" },
        },
      ),
    );

    await expect(getWorldParams()).resolves.toEqual({
      counter: {
        increment: 2,
      },
    });
    expect(fetchMock).toHaveBeenCalledWith("http://localhost:8000/world/params", undefined);
  });

  it("posts params patches", async () => {
    fetchMock.mockResolvedValue(
      new Response(
        JSON.stringify({
          code: 0,
          msg: "ok",
          data: {
            heartbeat: {
              enabled: false,
            },
          },
        }),
        {
          status: 200,
          headers: { "Content-Type": "application/json" },
        },
      ),
    );

    await expect(
      applyWorldParams({
        patches: [
          {
            op: "set",
            path: "heartbeat.enabled",
            value: false,
          },
        ],
      }),
    ).resolves.toEqual({
      heartbeat: {
        enabled: false,
      },
    });
    expect(fetchMock).toHaveBeenCalledWith("http://localhost:8000/world/params/apply", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        patches: [
          {
            op: "set",
            path: "heartbeat.enabled",
            value: false,
          },
        ],
      }),
    });
  });

  it("throws fallback error for non-json responses", async () => {
    fetchMock.mockResolvedValue(
      new Response("server unavailable", {
        status: 503,
        headers: { "Content-Type": "text/plain" },
      }),
    );

    await expect(fetchHealth()).rejects.toMatchObject({
      name: "ApiClientError",
      message: "Request failed: 503",
      status: 503,
      code: 503,
    });
  });
});
