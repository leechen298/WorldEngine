<template>
  <main class="dashboard">
    <h1>WorldEngine Dashboard</h1>

    <section class="health">
      <strong>Backend health:</strong>
      <span v-if="loading"> checking...</span>
      <span v-else-if="error"> {{ error }}</span>
      <span v-else>{{ health?.status }} ({{ health?.service }})</span>
    </section>

    <section class="runtime">
      <strong>Runtime:</strong>
      <span v-if="runtimeLoading"> loading...</span>
      <span v-else-if="runtimeError"> {{ runtimeError }}</span>
      <span v-else>
        tick_id={{ runtime?.tick_id }}, world_time_seconds={{ runtime?.world_time_seconds }},
        step_seconds={{ runtime?.step_seconds }}
      </span>
    </section>

    <section class="panel-grid">
      <RuntimeControls @stepped="handleRuntimeStepped" />
      <TimelinePanel />
      <WorldPanel />
      <AgentPanel />
      <MemoryPanel />
    </section>
  </main>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import {
  fetchHealth,
  getRuntimeState,
  type HealthResponse,
  type RuntimeState,
} from "../api/client";
import RuntimeControls from "../components/RuntimeControls.vue";
import TimelinePanel from "../components/TimelinePanel.vue";
import WorldPanel from "../components/WorldPanel.vue";
import AgentPanel from "../components/AgentPanel.vue";
import MemoryPanel from "../components/MemoryPanel.vue";

const health = ref<HealthResponse | null>(null);
const loading = ref<boolean>(true);
const error = ref<string>("");
const runtime = ref<RuntimeState | null>(null);
const runtimeLoading = ref<boolean>(true);
const runtimeError = ref<string>("");

async function loadRuntimeState(): Promise<void> {
  try {
    runtime.value = await getRuntimeState();
    runtimeError.value = "";
  } catch (err) {
    runtimeError.value = err instanceof Error ? err.message : "Unknown error";
  } finally {
    runtimeLoading.value = false;
  }
}

async function handleRuntimeStepped(): Promise<void> {
  runtimeLoading.value = true;
  await loadRuntimeState();
}

onMounted(async () => {
  try {
    health.value = await fetchHealth();
  } catch (err) {
    error.value = err instanceof Error ? err.message : "Unknown error";
  } finally {
    loading.value = false;
  }

  await loadRuntimeState();
});
</script>
