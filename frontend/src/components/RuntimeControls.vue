<template>
  <a-card title="Runtime Controls">
    <a-space direction="vertical" :size="12">
      <a-button data-test="runtime-step-button" type="primary" :loading="stepping" @click="handleStep">
        {{ stepping ? "Stepping..." : "Step" }}
      </a-button>
      <a-alert v-if="error" type="error" show-icon :message="error" />
    </a-space>
  </a-card>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { Alert as AAlert, Button as AButton, Card as ACard, Space as ASpace } from "ant-design-vue";
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
