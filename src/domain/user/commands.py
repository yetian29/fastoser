from dataclasses import dataclass
from src.domain.user.entities import User


@dataclass(frozen=True)
class RegisterUserCommand:
    user: User
