from dataclasses import dataclass

from src.app.application.cqrs.user.command import RegisterUserCommand
from src.app.domain.user.entity import User
from src.app.domain.user.service import IUserService


@dataclass(frozen=True)
class RegisterUserUseCase:
    user_service: IUserService

    async def execute(self, command: RegisterUserCommand) -> User:
        return await self.user_service.create_user(user=command.user)
