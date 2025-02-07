from abc import ABC, abstractmethod

from src.app.domain.user.entity import User
from src.app.infrastructure.database.models.user import UserORM
from src.app.presentation.rest.v1.user.schemas import (
    UserRegisterInSchema,
    UserRegisterOutSchema,
)


# Data transfer between presentation layer and domain layer
class IUserDTO1(ABC):
    @abstractmethod
    def to_entity(self, schema_in: UserRegisterInSchema) -> User:
        pass

    @staticmethod
    @abstractmethod
    def from_entity(entity: User) -> UserRegisterOutSchema:
        pass


# Data transfer between domain layer and infrastructure layer
class IUserDTO2(ABC):
    @staticmethod
    @abstractmethod
    def from_entity(entity: User) -> UserORM:
        pass

    @abstractmethod
    def to_entity(self, user_orm: UserORM) -> User:
        pass
