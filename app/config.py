from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    PROJECT_NAME: str = "Logistics Voice Agent Backend"
    VERSION: str = "1.0.0"

    # Supabase
    SUPABASE_URL: str
    SUPABASE_SERVICE_KEY: str
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

    class Config:
        env_file = ".env"   # load from .env file at project root


@lru_cache
def get_settings():
    return Settings()

# create a singleton instance
settings = get_settings()
