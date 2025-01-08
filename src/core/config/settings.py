from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


@lru_cache
def get_settings():
    return Settings()


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = "HS256"

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)


settings = get_settings()
