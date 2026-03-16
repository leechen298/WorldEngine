from typing import Protocol

from app.schemas.agent import AgentSnapshot


class AgentRepositoryPort(Protocol):
    def get_agent(self) -> AgentSnapshot:
        """Fetch an agent snapshot from persistence."""
