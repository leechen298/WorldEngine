from app.schemas.world import WorldSnapshot


class SqliteWorldRepository:
    """Placeholder SQLite adapter for world persistence."""

    def __init__(self, db_path: str = "backend/data/worldengine.db") -> None:
        self.db_path = db_path

    def get_world(self) -> WorldSnapshot:
        return WorldSnapshot()
