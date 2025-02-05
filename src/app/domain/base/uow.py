from abc import ABC, abstractmethod
from typing import Self

from src.app.domain.user.repository import IUserRepository


class IUnitOfWork(ABC):
    user: IUserRepository

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: BaseException | None = None) -> None:
        if exc_type is None:
            await self.commit()
        else:
            await self.rollback()
        await self.close()

    @abstractmethod
    async def commit(self) -> None:
        pass

    @abstractmethod
    async def rollback(self) -> None:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass
