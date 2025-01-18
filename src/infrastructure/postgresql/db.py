from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.core.config.settings import settings


class DatabaseManager:
    def __init__(
        self, url: str = settings.database.pg_dsn, is_dev: str = settings.environment
    ) -> None:
        self.echo: bool = is_dev == "development"
        self.async_engine = create_async_engine(
            url=url, echo=self.echo, echo_pool=self.echo, isolation="READ COMMITTED"
        )
        # expire_on_commit - don't expire objects after transaction commit
        self.async_session = async_sessionmaker(
            bind=self.async_engine, expire_on_commit=False
        )
