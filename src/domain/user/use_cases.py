from dataclasses import dataclass
from src.domain.user.commands import LoginUserCommand, RegisterUserCommand
from src.domain.user.entities import User
from src.domain.user.errors import PasswordInvalidException
from src.domain.user.services import ILoginService, IPasswordService, IUserService
from src.helper.errors import fail


@dataclass(frozen=True)
class RegisterUserUseCase:
    user_service: IUserService

    async def execute(self, command: RegisterUserCommand) -> User:
        return await self.user_service.create(user=command.user)


@dataclass(frozen=True)
class LoginUserUseCase:
    user_service: IUserService
    password_service: IPasswordService
    login_service: ILoginService

    async def exeucte(self, command: LoginUserCommand) -> str:
        user = await self.user_service.get_by_username_or_email(
            username=command.username, email=command.email
        )
        if not self.password_service.verify_password(command.password, user.password):
            fail(
                PasswordInvalidException("Invalid password. The password is incorrect")
            )
        access_token = self.login_service.generate_access_token_and_is_active_account(
            user
        )
        await self.user_service.update(user)
        return access_token
