from dataclasses import dataclass
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.core.config.settings import settings


class DatabaseManager:
    def __init__(self, url: str = settings.database.pg_dsn) -> None:
        self.async_engine = create_async_engine(
            url=url,
            echo=True
        )
        # expire_on_commit - don't expire objects after transaction commit
        self.async_session = async_sessionmaker(self.async_engine, expire_on_commit=False)



