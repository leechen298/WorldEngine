from __future__ import annotations

import os
from typing import Any

from pydantic import BaseModel


class WorldValidationPolicy(BaseModel):
    dry_run_steps: int = 20
    max_avg_events_per_tick: int = 20
    max_total_events: int = 500
    max_final_counter: int = 100000

    @classmethod
    def from_env(cls) -> WorldValidationPolicy:
        kwargs: dict[str, Any] = {}
        env_map = {
            "WORLD_DRYRUN_STEPS": "dry_run_steps",
            "WORLD_DRYRUN_MAX_AVG_EVENTS_PER_TICK": "max_avg_events_per_tick",
            "WORLD_DRYRUN_MAX_TOTAL_EVENTS": "max_total_events",
            "WORLD_DRYRUN_MAX_FINAL_COUNTER": "max_final_counter",
        }
        for env_key, field_name in env_map.items():
            raw = os.getenv(env_key)
            if raw is not None:
                try:
                    value = int(raw)
                    if value > 0:
                        kwargs[field_name] = value
                except ValueError:
                    pass
        return cls(**kwargs)

    @staticmethod
    def merged(
        base: WorldValidationPolicy,
        override: dict[str, Any] | WorldValidationPolicy | None,
    ) -> WorldValidationPolicy:
        if override is None:
            return base
        if isinstance(override, WorldValidationPolicy):
            override = override.model_dump(exclude_defaults=True)
        merged_data = base.model_dump()
        for key, value in override.items():
            if key in merged_data and isinstance(value, int) and value > 0:
                merged_data[key] = value
        return WorldValidationPolicy(**merged_data)
