import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";

import MemoryPanel from "./MemoryPanel.vue";

const summary = {
  id: "summary-1",
  from_tick: 1,
  to_tick: 5,
  created_at: "2026-05-24T00:00:00+08:00",
  text: "The world advanced and counter events were recorded.",
  stats: {
    total_events: 6,
    type_counts: {
      "tick.advanced": 5,
      "module.counter": 1,
    },
  },
};

describe("MemoryPanel", () => {
  it("exposes stable selectors for summary text and stats", () => {
    const wrapper = mount(MemoryPanel, {
      props: {
        summary,
        loading: false,
        error: "",
      },
    });

    expect(wrapper.find("[data-test='memory-panel']").exists()).toBe(true);
    expect(wrapper.get("[data-test='memory-summary-text']").text()).toContain(
      "counter events were recorded",
    );
    expect(wrapper.get("[data-test='memory-summary-stats']").text()).toContain("module.counter");
  });

  it("exposes a stable selector for the empty state", () => {
    const wrapper = mount(MemoryPanel, {
      props: {
        summary: null,
        loading: false,
        error: "",
      },
    });

    expect(wrapper.find("[data-test='memory-panel']").exists()).toBe(true);
    expect(wrapper.get("[data-test='memory-summary-empty']").text()).toContain("No summaries yet");
  });
});
