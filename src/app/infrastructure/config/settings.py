from passlib.context import CryptContext
from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseModel(BaseModel):
    host: str
    username: str
    password: str
    port: int
    name: str

    @property
    def dsn(self) -> PostgresDsn:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="example.env", env_nested_delimiter="__", env_ignore_empty=True
    )
    database: DatabaseModel
    pwd_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")


settings = Settings()
