from abc import ABC, abstractmethod

from src.domain.user.entities import User


class IPasswordService(ABC):
    @abstractmethod
    def generate_password(self, plain_password: str) -> str:
        pass

    @abstractmethod
    def verify_password(self, plain_password: str, password: str) -> True:
        pass


class ILoginService(ABC):
    @abstractmethod
    def generate_access_token(
        user: User, expires_delta: timedelta | None = None
    ) -> str:
        pass

    @abstractmethod
    def is_active_account(user: User) -> None:
        pass


class IUserService(ABC):
    @abstractmethod
    async def get_user_by_username_or_email(
        username: str | None = None, email: str | None = None
    ) -> User:
        pass

    @abstractmethod
    async def get_user_by_email(email: str) -> User:
        pass

    @abstractmethod
    async def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    async def update_user(self, user: User) -> User:
        pass
