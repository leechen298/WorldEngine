import { flushPromises, mount } from "@vue/test-utils";
import { nextTick } from "vue";
import { describe, expect, it, vi } from "vitest";

import { ApiClientError } from "../api/client";
import WorldPanel from "./WorldPanel.vue";

const { applyWorldParamsMock, proposeAndApplyMock, getWorldParamsMock } = vi.hoisted(() => ({
  applyWorldParamsMock: vi.fn(),
  proposeAndApplyMock: vi.fn(),
  getWorldParamsMock: vi.fn(),
}));

vi.mock("../api/client", async (importOriginal) => {
  const actual = await importOriginal<typeof import("../api/client")>();
  return {
    ...actual,
    applyWorldParams: applyWorldParamsMock,
    proposeAndApplyWorldParams: proposeAndApplyMock,
    getWorldParams: getWorldParamsMock,
  };
});

function makeApiError(
  msg: string,
  errors: { path: string; reason: string; detail: string }[],
): ApiClientError {
  return new ApiClientError(msg, { status: 422, code: 30, data: { errors } });
}

describe("WorldPanel error display", () => {
  it("shows only msg when there are no error details", async () => {
    applyWorldParamsMock.mockRejectedValue(new Error("Network error"));

    const wrapper = mount(WorldPanel, {
      props: { params: {}, loading: false },
    });
    await wrapper.find("input").setValue("counter.increment");
    await nextTick();
    await wrapper.find("button").trigger("click");
    await flushPromises();

    expect(wrapper.text()).toContain("Network error");
    expect(wrapper.find("ul.apply-error-list").exists()).toBe(false);
  });

  it("shows msg + detail lines on static validator 422", async () => {
    applyWorldParamsMock.mockRejectedValue(
      makeApiError("Param validation failed", [
        { path: "counter.increment", reason: "out_of_range", detail: "Value must be ≤ 1000." },
      ]),
    );

    const wrapper = mount(WorldPanel, {
      props: { params: {}, loading: false },
    });
    await wrapper.find("input").setValue("counter.increment");
    await nextTick();
    await wrapper.find("button").trigger("click");
    await flushPromises();

    expect(wrapper.text()).toContain("Param validation failed");
    expect(wrapper.text()).toContain("counter.increment: Value must be ≤ 1000.");
  });

  it("shows msg + detail lines on dry-run 422", async () => {
    applyWorldParamsMock.mockRejectedValue(
      makeApiError("Dry-run validation failed", [
        { path: "counter.increment", reason: "numeric_divergence", detail: "Counter diverged to 2000000 (max 100000)." },
      ]),
    );

    const wrapper = mount(WorldPanel, {
      props: { params: {}, loading: false },
    });
    await wrapper.find("input").setValue("counter.increment");
    await nextTick();
    await wrapper.find("button").trigger("click");
    await flushPromises();

    expect(wrapper.text()).toContain("Dry-run validation failed");
    expect(wrapper.text()).toContain("counter.increment: Counter diverged to 2000000 (max 100000).");
  });

  it("omits path prefix when path is empty", async () => {
    applyWorldParamsMock.mockRejectedValue(
      makeApiError("Dry-run validation failed", [
        { path: "", reason: "event_flood", detail: "Simulation produced too many events (avg 25.0/tick, max 20)." },
      ]),
    );

    const wrapper = mount(WorldPanel, {
      props: { params: {}, loading: false },
    });
    await wrapper.find("input").setValue("counter.increment");
    await nextTick();
    await wrapper.find("button").trigger("click");
    await flushPromises();

    const listText = wrapper.find("ul.apply-error-list").text();
    expect(listText).not.toMatch(/^:/);
    expect(listText).toContain("Simulation produced too many events");
  });

  it("emits applied and clears errors on success", async () => {
    applyWorldParamsMock.mockRejectedValue(
      makeApiError("Param validation failed", [
        { path: "counter.increment", reason: "out_of_range", detail: "Value must be ≤ 1000." },
      ]),
    );

    const wrapper = mount(WorldPanel, { props: { params: {}, loading: false } });
    await wrapper.find("input").setValue("counter.increment");
    await nextTick();
    await wrapper.find("button").trigger("click");
    await flushPromises();

    expect(wrapper.find("ul.apply-error-list").exists()).toBe(true);

    applyWorldParamsMock.mockResolvedValue({ counter: { increment: { value: 2, type: "number" } } });
    await wrapper.find("button").trigger("click");
    await flushPromises();

    expect(wrapper.emitted("applied")).toHaveLength(1);
    expect(wrapper.find("ul.apply-error-list").exists()).toBe(false);
  });
});

describe("WorldPanel agent button", () => {
  it("exposes stable selectors for agent auto-tune controls and feedback", async () => {
    const freshParams = { counter: { increment: { value: 2, type: "number" } } };
    proposeAndApplyMock.mockResolvedValue({
      applied: true,
      patches: [{ op: "set", path: "counter.increment", value: { value: 2, type: "number" } }],
      attempts: 1,
    });
    getWorldParamsMock.mockResolvedValue(freshParams);

    const wrapper = mount(WorldPanel, { props: { params: {}, loading: false } });

    expect(wrapper.get("[data-test='world-agent-goal-input']").exists()).toBe(true);
    await wrapper.get("[data-test='world-agent-autotune-button']").trigger("click");
    await flushPromises();

    expect(wrapper.get("[data-test='world-agent-success']").text()).toContain("Applied 1 patch(es)");
    expect(wrapper.get("[data-test='world-agent-patches']").text()).toContain("counter.increment");

    proposeAndApplyMock.mockRejectedValue(
      makeApiError("Agent proposal rejected after max attempts", [
        { path: "counter.increment", reason: "out_of_range", detail: "Value must be <= 1000." },
      ]),
    );

    await wrapper.get("[data-test='world-agent-autotune-button']").trigger("click");
    await flushPromises();

    expect(wrapper.get("[data-test='world-agent-error']").text()).toContain(
      "Agent proposal rejected after max attempts",
    );
  });

  it("shows success message and emits fresh params after LLM auto-tune", async () => {
    const freshParams = { counter: { increment: { value: 2, type: "number" } } };
    proposeAndApplyMock.mockResolvedValue({
      applied: true,
      patches: [{ op: "set", path: "counter.increment", value: { value: 2, type: "number" } }],
      attempts: 1,
    });
    getWorldParamsMock.mockResolvedValue(freshParams);

    const wrapper = mount(WorldPanel, { props: { params: {}, loading: false } });
    const agentBtn = wrapper.findAll("button").find((b) => b.text().includes("LLM Auto-Tune"));
    expect(agentBtn).toBeTruthy();

    await agentBtn!.trigger("click");
    await flushPromises();

    expect(wrapper.text()).toContain("Applied 1 patch(es) in 1 attempt(s)");
    const emitted = wrapper.emitted("applied");
    expect(emitted).toHaveLength(1);
    expect(emitted![0][0]).toEqual(freshParams);
  });

  it("shows errors when agent proposal is rejected", async () => {
    proposeAndApplyMock.mockRejectedValue(
      makeApiError("Agent proposal rejected after max attempts", [
        { path: "counter.increment", reason: "out_of_range", detail: "Value must be ≤ 1000." },
      ]),
    );

    const wrapper = mount(WorldPanel, { props: { params: {}, loading: false } });
    const agentBtn = wrapper.findAll("button").find((b) => b.text().includes("LLM Auto-Tune"));

    await agentBtn!.trigger("click");
    await flushPromises();

    expect(wrapper.text()).toContain("Agent proposal rejected after max attempts");
    expect(wrapper.text()).toContain("counter.increment: Value must be ≤ 1000.");
  });
});
