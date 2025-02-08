from abc import ABC, abstractmethod
from datetime import timedelta
from uuid import UUID

from src.app.domain.user.entity import User


class IUserLoginService(ABC):
    @abstractmethod
    async def verify_password(plain_password: str, hashed_password: str) -> bool:
        pass

    @abstractmethod
    async def create_access_token_and_is_acitive_account(
        user: User, expires_delta: timedelta | None = None
    ):
        pass


class IUserService(ABC):
    @abstractmethod
    async def get_user_by_username(self, username: str) -> User:
        pass

    @abstractmethod
    async def get_user_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    async def get_user_by_oid(self, oid: UUID) -> User:
        pass

    @abstractmethod
    async def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    async def update_user(self, user: User) -> User:
        pass

    @abstractmethod
    async def delete_user(self, oid: UUID) -> User:
        pass
