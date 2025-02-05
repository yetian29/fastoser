from abc import ABC, abstractmethod
from datetime import datetime
from uuid import UUID, uuid4

from passlib.context import CryptContext

from src.app.domain.user.entity import User
from src.app.presentation.rest.v1.user.schemas import (
    UserRegisterInSchema,
    UserRegisterOutSchema,
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class IUserDto(ABC):
    @abstractmethod
    def to_entity(self, schema_in: UserRegisterInSchema) -> User:
        pass

    @staticmethod
    @abstractmethod
    def from_entity(entity: User) -> "UserRegisterOutSchema":
        pass


class UserDto(IUserDto):
    def get_password_hash(self, plain_password: str) -> str:
        return pwd_context.hash(plain_password)

    def to_entity(
        self,
        schema_in: UserRegisterInSchema,
        oid: UUID = uuid4(),
        is_active: bool = False,
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ) -> User:
        return User(
            oid=oid,
            is_active=is_active,
            created_at=created_at,
            updated_at=updated_at,
            username=schema_in.username,
            email=schema_in.email,
            password=self.get_password_hash(schema_in.password),
        )

    def from_entity(entity: User) -> "UserRegisterOutSchema":
        return UserRegisterOutSchema(
            oid=entity.oid,
            username=entity.username,
            email=entity.email,
            password=entity.password,
            is_active=entity.is_active,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
