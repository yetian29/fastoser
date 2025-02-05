from abc import ABC, abstractmethod

from src.app.domain.user.entity import User
from src.app.infrastructure.database.models.user import UserORM


class IUserDto(ABC):
    @staticmethod
    @abstractmethod
    def from_entity(entity: User) -> "UserORM":
        pass

    @abstractmethod
    def to_entity(self, user_orm: UserORM) -> User:
        pass
