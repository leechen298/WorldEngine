<template>
  <a-card data-test="generation-panel" title="Generation Preview">
    <a-space direction="vertical" :size="14" class="generation-stack">
      <a-form layout="vertical" class="generation-form">
        <a-form-item label="Request">
          <a-input data-test="generation-request-id-input" v-model:value="requestId" />
        </a-form-item>
        <a-form-item label="Root">
          <a-input data-test="generation-root-id-input" v-model:value="rootId" />
          <a-input data-test="generation-root-label-input" v-model:value="rootLabel" />
        </a-form-item>
        <a-form-item label="Child">
          <a-input data-test="generation-child-id-input" v-model:value="childId" />
          <a-input data-test="generation-child-label-input" v-model:value="childLabel" />
        </a-form-item>
        <a-form-item label="Seed">
          <a-input data-test="generation-seed-input" v-model:value="seed" />
        </a-form-item>
        <a-button
          type="primary"
          data-test="generation-preview-submit"
          :loading="loading"
          :disabled="!requestId.trim() || !rootId.trim()"
          @click="handlePreview"
        >
          Preview
        </a-button>
      </a-form>

      <a-alert v-if="error" data-test="generation-error" type="error" show-icon :message="error" />

      <a-descriptions v-if="preview" :column="1" size="small" bordered>
        <a-descriptions-item label="validation_status">
          <span data-test="generation-validation-status">{{ preview.validation_status }}</span>
        </a-descriptions-item>
        <a-descriptions-item label="generation_id">
          <span data-test="generation-id">{{ preview.metadata.generation_id }}</span>
        </a-descriptions-item>
        <a-descriptions-item label="source_kind">
          {{ preview.source_kind }}
        </a-descriptions-item>
        <a-descriptions-item label="summary">
          <pre data-test="generation-summary" class="generation-pre">{{ formattedSummary }}</pre>
        </a-descriptions-item>
      </a-descriptions>

      <a-alert
        v-if="preview && preview.diagnostics.length > 0"
        data-test="generation-diagnostics"
        type="error"
        show-icon
        message="Diagnostics"
      >
        <template #description>
          <ul class="generation-diagnostics">
            <li v-for="item in preview.diagnostics" :key="`${item.code}-${item.path ?? ''}`">
              {{ item.code }}: {{ item.message }}
            </li>
          </ul>
        </template>
      </a-alert>

      <a-descriptions v-if="readiness" :column="1" size="small" bordered>
        <a-descriptions-item label="readiness_status">
          <span data-test="generation-readiness-status">{{ readiness.validation_status }}</span>
        </a-descriptions-item>
        <a-descriptions-item label="loader_passed">
          {{ readiness.loader_passed }}
        </a-descriptions-item>
        <a-descriptions-item label="runtime_context_passed">
          {{ readiness.runtime_context_passed }}
        </a-descriptions-item>
      </a-descriptions>

      <a-alert
        v-if="readiness && readiness.diagnostics.length > 0"
        data-test="generation-readiness-diagnostics"
        type="error"
        show-icon
        message="Readiness diagnostics"
      >
        <template #description>
          <ul class="generation-diagnostics">
            <li v-for="item in readiness.diagnostics" :key="`${item.code}-${item.path ?? ''}`">
              {{ item.code }}: {{ item.message }}
            </li>
          </ul>
        </template>
      </a-alert>
    </a-space>
  </a-card>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";
import {
  Alert as AAlert,
  Button as AButton,
  Card as ACard,
  Descriptions as ADescriptions,
  DescriptionsItem as ADescriptionsItem,
  Form as AForm,
  FormItem as AFormItem,
  Input as AInput,
  Space as ASpace,
} from "ant-design-vue";

import {
  checkGenerationRuntimeReadiness,
  previewGeneration,
  type GenerationPreviewRequest,
  type GenerationPreviewResponse,
  type RuntimeReadinessResult,
} from "../api/client";

const requestId = ref("dashboard-preview");
const rootId = ref("root");
const rootLabel = ref("Root");
const childId = ref("child");
const childLabel = ref("Child");
const seed = ref("dashboard");
const loading = ref(false);
const error = ref("");
const preview = ref<GenerationPreviewResponse | null>(null);
const readiness = ref<RuntimeReadinessResult | null>(null);

const formattedSummary = computed(() =>
  JSON.stringify(preview.value?.metadata.preview_summary ?? {}, null, 2),
);

function buildRequest(): GenerationPreviewRequest {
  const child = childId.value.trim()
    ? [
        {
          id: childId.value.trim(),
          label: childLabel.value.trim() || null,
          entity_refs: [],
          child_cells: [],
          metadata: {},
        },
      ]
    : [];

  return {
    request_id: requestId.value.trim(),
    source_kind: "template",
    template_request: {
      request_id: requestId.value.trim(),
      template: {
        id: "template.dashboard",
        version: "1",
        root: {
          id: rootId.value.trim(),
          label: rootLabel.value.trim() || null,
          entity_refs: [],
          child_cells: child,
          metadata: { source: "dashboard" },
        },
        metadata: { category: "dashboard-preview" },
        constraints: {},
      },
      seed_material: { seed: seed.value },
      constraints: {},
    },
  };
}

async function handlePreview(): Promise<void> {
  loading.value = true;
  error.value = "";
  preview.value = null;
  readiness.value = null;

  try {
    const nextPreview = await previewGeneration(buildRequest());
    preview.value = nextPreview;
    if (nextPreview.validation_status === "passed" && nextPreview.worldspec_preview) {
      readiness.value = await checkGenerationRuntimeReadiness({
        request_id: nextPreview.request_id,
        worldspec: nextPreview.worldspec_preview,
        source_label: nextPreview.metadata.generation_id,
      });
    }
  } catch (err) {
    error.value = err instanceof Error ? err.message : "Generation preview failed";
  } finally {
    loading.value = false;
  }
}
</script>

<style scoped>
.generation-stack {
  width: 100%;
}

.generation-form {
  max-width: 720px;
}

.generation-form :deep(.ant-form-item-control-input-content) {
  display: grid;
  gap: 8px;
}

.generation-pre {
  max-height: 180px;
  margin: 0;
  overflow: auto;
  white-space: pre-wrap;
}

.generation-diagnostics {
  margin: 0;
  padding-left: 18px;
}
</style>
