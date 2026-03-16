from app.schemas.world import WorldSnapshot
from app.world.modules.base import WorldModule
from app.world.modules.composite import CompositeModule
from app.world.modules.examples import CounterModule, HeartbeatModule


class WorldService:
    """Placeholder world service for V1 scaffold."""

    def get_world(self) -> WorldSnapshot:
        return WorldSnapshot()


def get_default_module_tree() -> WorldModule:
    root = CompositeModule(
        "root",
        children=[
            HeartbeatModule("heartbeat"),
            CounterModule("counter"),
        ],
    )
    root.set_module_path("root")
    return root
