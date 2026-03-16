export type HealthResponse = {
  status: string;
  service: string;
};

export interface RuntimeState {
  tick_id: number;
  world_time_seconds: number;
  step_seconds: number;
}

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

export async function fetchHealth(): Promise<HealthResponse> {
  const response = await fetch(`${API_BASE_URL}/health`);
  if (!response.ok) {
    throw new Error(`Health check failed: ${response.status}`);
  }
  return (await response.json()) as HealthResponse;
}

export async function getRuntimeState(): Promise<RuntimeState> {
  const response = await fetch(`${API_BASE_URL}/runtime/state`);
  if (!response.ok) {
    throw new Error(`Fetch runtime state failed: ${response.status}`);
  }
  return (await response.json()) as RuntimeState;
}

export async function stepRuntime(): Promise<RuntimeState> {
  const response = await fetch(`${API_BASE_URL}/runtime/step`, {
    method: "POST",
  });
  if (!response.ok) {
    throw new Error(`Step runtime failed: ${response.status}`);
  }
  return (await response.json()) as RuntimeState;
}
