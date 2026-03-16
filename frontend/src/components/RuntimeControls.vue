<template>
  <section class="panel">
    <h2>Runtime Controls</h2>
    <button class="step-button" type="button" :disabled="stepping" @click="handleStep">
      {{ stepping ? "Stepping..." : "Step" }}
    </button>
    <p v-if="error" class="runtime-error">{{ error }}</p>
  </section>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { stepRuntime } from "../api/client";

const emit = defineEmits<{
  (event: "stepped"): void;
}>();

const stepping = ref<boolean>(false);
const error = ref<string>("");

async function handleStep(): Promise<void> {
  stepping.value = true;
  error.value = "";

  try {
    await stepRuntime();
    emit("stepped");
  } catch (err) {
    error.value = err instanceof Error ? err.message : "Step failed";
  } finally {
    stepping.value = false;
  }
}
</script>
