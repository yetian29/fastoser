from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.app.domain.base.uow import IUnitOfWork


class Uow(IUnitOfWork):
    """
    Provides a unit of work pattern for managing transactions and repositories in
    an asynchronous SQLAlchemy session.
    """

    def __init__(self, async_session_factory: async_sessionmaker[AsyncSession]) -> None:
        self._async_session_factory = async_session_factory

    async def __aenter__(self):
        self._async_session = self._async_session_factory()
        return await super().__aenter__()

    async def commit(self) -> None:
        await self._async_session.commit()

    async def rollback(self) -> None:
        await self._async_session.rollback()

    async def close(self) -> None:
        await self._async_session.close()
