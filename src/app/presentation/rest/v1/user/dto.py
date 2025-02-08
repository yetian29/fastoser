from datetime import datetime
from uuid import UUID, uuid4

from src.app.domain.user.dto import IUserDTO1
from src.app.domain.user.entity import User
from src.app.infrastructure.config.settings import settings
from src.app.presentation.rest.v1.user.schemas import (
    UserRegisterInSchema,
    UserRegisterOutSchema,
)


class UserDto(IUserDTO1):
    def get_password_hash(self, plain_password: str) -> str:
        return settings.pwd_context.hash(plain_password)

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

    def from_entity(entity: User) -> UserRegisterOutSchema:
        return UserRegisterOutSchema(
            oid=entity.oid,
            username=entity.username,
            email=entity.email,
            password=entity.password,
            is_active=entity.is_active,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
