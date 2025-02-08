from dataclasses import dataclass

from src.app.domain.user.entity import User


@dataclass(frozen=True)
class RegisterUserCommand:
    user: User


@dataclass(frozen=True)
class LoginUserCommand:
    username: str | None = None
    email: str | None = None
    password: str
