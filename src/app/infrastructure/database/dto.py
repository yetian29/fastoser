from src.app.domain.user.dto import IUserDTO2
from src.app.domain.user.entity import User
from src.app.infrastructure.database.models.user import UserORM


class UserDto(IUserDTO2):
    def from_entity(entity: User) -> UserORM:
        return UserORM(
            oid=entity.oid,
            username=entity.username,
            email=entity.email,
            password=entity.password,
            is_active=entity.is_active,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    def to_entity(self, user_orm: UserORM) -> User:
        return User(
            oid=user_orm.oid,
            created_at=user_orm.created_at,
            updated_at=user_orm.updated_at,
            username=user_orm.username,
            email=user_orm.email,
            password=user_orm.password,
            is_active=user_orm.is_active,
        )
