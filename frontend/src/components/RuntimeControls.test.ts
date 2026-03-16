import { flushPromises, mount } from "@vue/test-utils";
import { describe, expect, it, vi } from "vitest";

import RuntimeControls from "./RuntimeControls.vue";

const { stepRuntimeMock } = vi.hoisted(() => ({
  stepRuntimeMock: vi.fn(),
}));

vi.mock("../api/client", () => ({
  stepRuntime: stepRuntimeMock,
}));

describe("RuntimeControls", () => {
  it("emits stepped after a successful runtime step", async () => {
    stepRuntimeMock.mockResolvedValue({
      tick_id: 1,
      world_time_seconds: 600,
      step_seconds: 600,
      updated_at: "2026-03-09T00:00:00+00:00",
    });

    const wrapper = mount(RuntimeControls);

    await wrapper.get("button").trigger("click");
    await flushPromises();

    expect(stepRuntimeMock).toHaveBeenCalledTimes(1);
    expect(wrapper.emitted("stepped")).toHaveLength(1);
    expect(wrapper.text()).not.toContain("Step failed");
  });

  it("shows an error when runtime step fails", async () => {
    stepRuntimeMock.mockRejectedValue(new Error("network down"));

    const wrapper = mount(RuntimeControls);

    await wrapper.get("button").trigger("click");
    await flushPromises();

    expect(wrapper.emitted("stepped")).toBeUndefined();
    expect(wrapper.text()).toContain("network down");
  });
});
