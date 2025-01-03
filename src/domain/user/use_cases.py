

from dataclasses import dataclass
from src.domain.user.commands import RegisterUserCommand
from src.domain.user.entities import User
from src.domain.user.services import IUserService

@dataclass(frozen=True)
class RegisterUserUseCase:
    user_service: IUserService

    async def execute(self, command: RegisterUserCommand) -> User:
        if await self.user_service.get_user_by_email(
            email = command.user.email
        ):
            fail(UserHasBeenRegistedException)
        return await self.user_service.create_user(user)


@dataclass(frozen=True)
class LoginUserUseCase:
    user_service: IUserService
    pwd_service: IPasswordService

    async def execute(self, command: LoginUserCommand) -> str:
        user = await self.user_service.get_user_by_username_or_email(
            username = command.username,
            email = command.email
        )
        if not self.pwd_service.verify_password(
            plain_password = command.password,
            password = user.password
        ):
            fail(PasswordIncorrectException)
        access_token = generate_acess_token_and_is_active_account(user)
        await user_service.update(user)
        return access_token



