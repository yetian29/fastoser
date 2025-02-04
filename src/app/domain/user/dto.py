

from abc import ABC, abstractmethod

from src.app.domain.user.entities import User
from src.app.infrastructure.database.models.user import UserORM


class IUserDto(ABC):
    @abstractmethod
    def from_entity(entity: User) -> "UserORM":
        pass
        