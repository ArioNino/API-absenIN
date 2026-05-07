from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional


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
    
    class Config:
        env_file = ".env"
        case_sensitive = False  # Changed to False to be more flexible
        env_prefix = ""  # No prefix


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
