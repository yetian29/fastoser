from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.app.infrastructure.config.settings import settings


class DatabaseManager:
    def __init__(self) -> None:
        self._async_engine = create_async_engine(url=settings.database.postgres_url)
        self._async_session = async_sessionmaker(
            self._async_engine, expire_on_commit=False
        )

    @property
    def async_session_factory(self) -> async_sessionmaker[AsyncSession]:
        return self._async_session
