from dataclasses import dataclass

from src.app.domain.user.entity import User


@dataclass(frozen=True)
class RegisterUserCommand:
    user: User
