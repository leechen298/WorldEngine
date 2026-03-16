export type HealthResponse = {
  status: string;
  service: string;
};

export interface RuntimeState {
  tick_id: number;
  world_time_seconds: number;
  step_seconds: number;
  updated_at?: string | null;
}

export interface WorldEvent {
  id: string;
  tick_id: number;
  world_time_seconds: number;
  type: string;
  source: string;
  payload: Record<string, any>;
  created_at: string;
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

export async function getWorldEvents(params?: {
  from_tick?: number;
  to_tick?: number;
  limit?: number;
}): Promise<WorldEvent[]> {
  const searchParams = new URLSearchParams();

  if (params?.from_tick !== undefined) {
    searchParams.set("from_tick", String(params.from_tick));
  }
  if (params?.to_tick !== undefined) {
    searchParams.set("to_tick", String(params.to_tick));
  }
  if (params?.limit !== undefined) {
    searchParams.set("limit", String(params.limit));
  }

  const query = searchParams.toString();
  const response = await fetch(
    `${API_BASE_URL}/world/events${query ? `?${query}` : ""}`,
  );
  if (!response.ok) {
    throw new Error(`Fetch world events failed: ${response.status}`);
  }
  return (await response.json()) as WorldEvent[];
}
