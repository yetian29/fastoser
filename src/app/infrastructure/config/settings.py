from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseModel(BaseModel):
    dsn: PostgresDsn


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_nested_delimiter="__")
    database: DatabaseModel


settings = Settings()
