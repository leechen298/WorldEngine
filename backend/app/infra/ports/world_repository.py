from typing import Protocol

from app.schemas.world import WorldSnapshot


class WorldRepositoryPort(Protocol):
    def get_world(self) -> WorldSnapshot:
        """Fetch a world snapshot from persistence."""
