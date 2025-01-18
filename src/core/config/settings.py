from enum import StrEnum
from functools import lru_cache

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(StrEnum):
    DEV = "development"
    PRODUCT = "product"


class Database(BaseModel):
    username: str
    password: str
    host: str
    port: str
    name: str

    @property
    def pg_dsn(self) -> PostgresDsn:
        return f"postgres+psycopg2://{self.username}:{self.password}@{self.host}:{self.port}/{self.name}"


class Settings(BaseSettings):
    secret_key: str
    algorithm: str = "HS256"
    database: Database
    environment: Environment = Environment.DEV

    model_config = SettingsConfigDict(
        env_file=".env", env_nested_delimiter="__", env_ignore_empty=True
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
