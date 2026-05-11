from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import List


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Database
    DATABASE_URL: str

    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Application
    APP_NAME: str = "AbsenIN API"
    APP_DEBUG: bool = True  # Changed from DEBUG to APP_DEBUG to avoid conflict

    # CORS: comma-separated origin list, or "*" to allow all.
    # When "*" is used, allow_credentials is disabled because browsers reject
    # the combination of wildcard origin + credentials.
    CORS_ORIGINS: str = "*"

    # Face recognition
    FACE_MODEL_DIR: str = "model"
    FACE_MODEL_METHOD: str = "mtcnn"
    FACE_RECOGNITION_THRESHOLD: float = 0.60

    @property
    def CORS_ORIGINS_LIST(self) -> List[str]:
        """Parse CORS_ORIGINS string into a clean list."""
        raw = (self.CORS_ORIGINS or "").strip()
        if not raw or raw == "*":
            return ["*"]
        return [origin.strip() for origin in raw.split(",") if origin.strip()]

    class Config:
        env_file = ".env"
        case_sensitive = False  # Changed to False to be more flexible
        env_prefix = ""  # No prefix


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
