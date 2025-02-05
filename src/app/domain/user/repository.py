from abc import ABC, abstractmethod
from uuid import UUID

from src.app.infrastructure.database.models.user import UserORM


class IUserRepository(ABC):
    @abstractmethod
    async def get_user_by_username(self, username: str) -> UserORM:
        pass

    @abstractmethod
    async def get_user_by_email(self, email: str) -> UserORM:
        pass

    @abstractmethod
    async def get_user_by_oid(self, oid: UUID) -> UserORM:
        pass

    @abstractmethod
    async def create_user(self, user_orm: UserORM) -> UserORM:
        pass

    @abstractmethod
    async def update_user(self, user_orm: UserORM) -> UserORM:
        pass

    @abstractmethod
    async def delete_user(self, oid: UUID) -> UserORM:
        pass
