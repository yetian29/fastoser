from dataclasses import dataclass

from src.app.application.cqrs.user.command import LoginUserCommand, RegisterUserCommand
from src.app.domain.user.entity import User
from src.app.domain.user.service import IUserLoginService, IUserService


@dataclass(frozen=True)
class RegisterUserUseCase:
    user_service: IUserService

    async def execute(self, command: RegisterUserCommand) -> User:
        await self.user_service.create_user(user=command.user)


@dataclass(frozen=True)
class LoginUserUseCase:
    login_service: IUserLoginService
    user_service: IUserService

    async def execute(self, command: LoginUserCommand):
        if command.username is not None:
            user = await self.user_service.get_user_by_username(
                username=command.username
            )
        if command.email is not None:
            user = await self.user_service.get_user_by_email(email=command.email)
        self.login_service.verify_password(
            plain_password=command.password, hashed_password=user.password
        )
