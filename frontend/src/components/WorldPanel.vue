<template>
  <a-card title="World Panel">
    <a-space direction="vertical" :size="16" class="world-stack">
      <a-typography-paragraph class="world-help">
        The JSON above shows the current world parameters. Use a dot path below to update a
        single parameter. For example, set path to
        <a-typography-text code>counter.increment</a-typography-text>, choose type
        <a-typography-text code>number</a-typography-text>, and enter
        <a-typography-text code>2</a-typography-text> as the value to produce
        <a-typography-text code>{{ stringExample }}</a-typography-text>. If you need a unit,
        for example for <a-typography-text code>river.width</a-typography-text>, fill in
        <a-typography-text code>unit</a-typography-text> as well to produce
        <a-typography-text code>{{ unitExample }}</a-typography-text>.
      </a-typography-paragraph>

      <a-spin :spinning="loading">
        <a-alert v-if="error" type="error" show-icon :message="error" />
        <pre v-else class="world-params">{{ formattedParams }}</pre>
      </a-spin>

      <a-form layout="vertical" class="world-param-form">
        <a-form-item label="Path">
          <a-input v-model:value="path" :placeholder="pathPlaceholder" />
        </a-form-item>
        <a-form-item label="Type">
          <a-select v-model:value="valueType" :options="typeOptions" />
        </a-form-item>
        <a-form-item label="Value">
          <a-select
            v-if="valueType === 'boolean'"
            v-model:value="booleanValue"
            :options="booleanOptions"
          />
          <a-input
            v-else
            v-model:value="rawValue"
            :placeholder="valuePlaceholder"
          />
        </a-form-item>
        <a-form-item label="Unit (optional)">
          <a-input v-model:value="unit" :placeholder="unitPlaceholder" />
        </a-form-item>
        <a-space direction="vertical" :size="12">
          <a-button
            type="primary"
            :loading="applying"
            :disabled="!path.trim()"
            @click="handleApply"
          >
            {{ applying ? "Applying..." : "Apply" }}
          </a-button>
          <a-alert v-if="applyError" type="error" show-icon :message="applyError" />
        </a-space>
      </a-form>
    </a-space>
  </a-card>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";
import {
  Alert as AAlert,
  Button as AButton,
  Card as ACard,
  Form as AForm,
  FormItem as AFormItem,
  Input as AInput,
  Select as ASelect,
  Space as ASpace,
  Spin as ASpin,
  TypographyParagraph as ATypographyParagraph,
  TypographyText as ATypographyText,
} from "ant-design-vue";

import { applyWorldParams, type WorldParams } from "../api/client";

type ParamValueType = "string" | "number" | "boolean" | "json";

const props = withDefaults(
  defineProps<{
    params?: WorldParams | null;
    loading?: boolean;
    error?: string;
  }>(),
  {
    params: null,
    loading: false,
    error: "",
  },
);

const emit = defineEmits<{
  (event: "applied", params: WorldParams): void;
}>();

const path = ref<string>("");
const rawValue = ref<string>("");
const valueType = ref<ParamValueType>("string");
const booleanValue = ref<"true" | "false">("false");
const unit = ref<string>("");
const applying = ref<boolean>(false);
const applyError = ref<string>("");

const stringExample = '{"value":2,"type":"number"}';
const unitExample = '{"value":1,"type":"number","unit":"meter"}';
const pathPlaceholder = "Example: counter.increment";
const unitPlaceholder = "Example: meter";
const formattedParams = computed(() => JSON.stringify(props.params ?? {}, null, 2));
const typeOptions = [
  { label: "string", value: "string" },
  { label: "number", value: "number" },
  { label: "boolean", value: "boolean" },
  { label: "json", value: "json" },
] ;
const booleanOptions = [
  { label: "true", value: "true" },
  { label: "false", value: "false" },
];
const valuePlaceholder = computed(() => {
  if (valueType.value === "number") {
    return "Example: 2";
  }
  if (valueType.value === "json") {
    return 'Example: {"min":1,"max":3}';
  }
  return "Example: hello";
});

function parseInputValue(input: string, type: ParamValueType, boolValue: "true" | "false"): unknown {
  if (type === "boolean") {
    return boolValue === "true";
  }

  const trimmed = input.trim();

  if (type === "string") {
    return input;
  }

  if (!trimmed) {
    return "";
  }

  if (type === "number") {
    const parsed = Number(trimmed);
    if (Number.isNaN(parsed)) {
      throw new Error("Value must be a valid number");
    }
    return parsed;
  }

  try {
    return JSON.parse(trimmed);
  } catch {
    throw new Error("Value must be valid JSON");
  }
}

function buildPatchValue(): unknown {
  const parsedValue = parseInputValue(rawValue.value, valueType.value, booleanValue.value);
  const structuredValue: Record<string, unknown> = {
    value: parsedValue,
    type: valueType.value,
  };

  if (unit.value.trim()) {
    structuredValue.unit = unit.value.trim();
  }

  return structuredValue;
}

async function handleApply(): Promise<void> {
  applying.value = true;
  applyError.value = "";

  try {
    const nextParams = await applyWorldParams({
      patches: [
        {
          op: "set",
          path: path.value.trim(),
          value: buildPatchValue(),
        },
      ],
    });
    path.value = "";
    rawValue.value = "";
    valueType.value = "string";
    booleanValue.value = "false";
    unit.value = "";
    emit("applied", nextParams);
  } catch (err) {
    applyError.value = err instanceof Error ? err.message : "Apply failed";
  } finally {
    applying.value = false;
  }
}
</script>

<style scoped>
.world-stack {
  width: 100%;
}

.world-params {
  max-height: 240px;
  overflow: auto;
  margin: 0;
  padding: 12px;
  background: rgba(15, 23, 42, 0.06);
  border-radius: 8px;
  font-size: 12px;
}

.world-help {
  margin-top: 0;
  font-size: 13px;
  line-height: 1.5;
}

.world-param-form {
  width: 100%;
}

.world-error {
  color: #b42318;
}
</style>
