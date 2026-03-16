<template>
  <main class="dashboard">
    <h1>WorldEngine Dashboard</h1>

    <section class="health">
      <strong>Backend health:</strong>
      <span v-if="loading"> checking...</span>
      <span v-else-if="error"> {{ error }}</span>
      <span v-else>{{ health?.status }} ({{ health?.service }})</span>
    </section>

    <section class="panel-grid">
      <RuntimeControls />
      <TimelinePanel />
      <WorldPanel />
      <AgentPanel />
      <MemoryPanel />
    </section>
  </main>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { fetchHealth, type HealthResponse } from "../api/client";
import RuntimeControls from "../components/RuntimeControls.vue";
import TimelinePanel from "../components/TimelinePanel.vue";
import WorldPanel from "../components/WorldPanel.vue";
import AgentPanel from "../components/AgentPanel.vue";
import MemoryPanel from "../components/MemoryPanel.vue";

const health = ref<HealthResponse | null>(null);
const loading = ref<boolean>(true);
const error = ref<string>("");

onMounted(async () => {
  try {
    health.value = await fetchHealth();
  } catch (err) {
    error.value = err instanceof Error ? err.message : "Unknown error";
  } finally {
    loading.value = false;
  }
});
</script>
