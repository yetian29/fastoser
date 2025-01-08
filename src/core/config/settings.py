from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from pydatic import BaseModel


@lru_cache
def get_settings():
    return Settings()


class Database(BaseModel):
    username: str
    password: str
    host: str
    port: str
    db: str

    @property
    def pg_dsn(self) -> PostgresDsn:
        return f"postgres://{self.username}:{self.password}@{self.host}:{self.port}/{self.db}"


class Settings(BaseSettings):
    secret_key: str
    algorithm: str = "HS256"
    database: Database

    model_config = SettingsConfigDict(env_file=".env", env_nested_delimiter="__")


settings = get_settings()
