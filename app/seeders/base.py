from abc import ABC, abstractmethod
from app.database import SessionLocal


class BaseSeeder(ABC):
    """Base class for all seeders."""

    def __init__(self):
        self.db = SessionLocal()
        self.inserted = 0
        self.skipped = 0

    def close(self):
        self.db.close()

    @abstractmethod
    def seed(self):
        """Override this to implement seed logic."""
        pass

    def report(self):
        """Return summary of seeding action."""
        return f"Inserted: {self.inserted}, Skipped: {self.skipped}"
