from app.schemas.agent import AgentSnapshot


class SqliteAgentRepository:
    """Placeholder SQLite adapter for agent persistence."""

    def __init__(self, db_path: str = "backend/data/worldengine.db") -> None:
        self.db_path = db_path

    def get_agent(self) -> AgentSnapshot:
        return AgentSnapshot()
