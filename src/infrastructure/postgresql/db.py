from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.core.config.settings import settings


class DatabaseManager:
    def __init__(self, url: str = settings.database.pg_dsn) -> None:
        self.async_engine = create_async_engine(
            url=url, echo="debug", echo_pool="debug", isolation="READ COMMITTED"
        )
        # expire_on_commit - don't expire objects after transaction commit
        self.async_session = async_sessionmaker(
            bind=self.async_engine, expire_on_commit=False
        )
