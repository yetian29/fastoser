from dataclasses import dataclass

from src.app.domain.user.entity import User
from src.app.domain.user.exception import BaseUserException
from src.app.domain.user.repository import IUserRepository
from src.app.domain.user.service import IUserLoginService, IUserService
from src.app.infrastructure.config import settings
from src.app.infrastructure.database.dto import UserDto


class UserLoginService(IUserLoginService):
    async def verify_password(plain_password: str, hashed_password: str) -> bool:
        return await settings.pwd_context.verify(plain_password, hashed_password)


@dataclass(frozen=True)
class UserService(IUserService):
    user_repository: IUserRepository

    async def get_user_by_username(self, username: str) -> User:
        user = await self.user_repository.get_user_by_username(username)
        if user is None:
            raise BaseUserException("User isn't exist")
        return user

    async def get_user_by_email(self, email: str) -> User:
        user = await self.user_repository.get_user_by_email(email)
        if user is None:
            raise BaseUserException("User isn't exist")
        return user

    async def create_user(self, user: User) -> User:
        if await self.get_user_by_username(username=user.username):
            raise BaseUserException("User name has existed")
        if await self.get_user_by_email(email=user.email):
            raise BaseUserException("User email has existed")

        return await self.user_repository.create_user(
            user_orm=UserDto.from_entity(user)
        )

    async def update_user(self, user: User) -> User:
        pass
