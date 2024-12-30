from dataclasses import dataclass
from src.domain.user.value_objects import UserEmail, UserName, UserPassword
from src.domain.user.entities import User


@dataclass(frozen=True)
class RegisterUserCommand:
    user: User


@dataclass(frozen=True)
class LoginUserCommand:
    username: UserName
    email: UserEmail
    password: UserPassword
