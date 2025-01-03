

from abc import ABC, abstractmethod

from src.domain.user.entities import User


class IUserService(ABC):
    @abstractmethod
    async def get_user_by_username_or_email(
        username: str | None = None,
        email: str | None = None
    ) -> User:
        pass

    @abstractmethod
    async def get_user_by_email(email: str) -> User:
        pass

    @abstractmethod
    async def create_user(self, user: User) -> User:
        pass
