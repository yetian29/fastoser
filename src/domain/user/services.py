from abc import ABC, abstractmethod
from src.domain.user.entities import User


class IPasswordService(ABC):
    @abstractmethod
    def generate_hash_password(self, plain_password: str) -> str:
        pass

    @abstractmethod
    def verify_password(self, plain_password: str, hash_password: str) -> bool:
        pass


class ILoginService(ABC):
    @abstractmethod
    def generate_access_token_and_is_active_account(self, user: User) -> str:
        pass


class IUserService(ABC):
    @abstractmethod
    async def get_by_username_or_email(
        self, username: str | None = None, email: str | None = None
    ) -> User:
        pass

    @abstractmethod
    async def create(self, user: User) -> User:
        pass

    @abstractmethod
    async def update(self, user: User) -> User:
        pass
