from dataclasses import dataclass
from datetime import datetime, timedelta
from argon2 import PasswordHasher

from src.domain.user.services import ILoginService, IPasswordService
import jwt


@dataclass
class PasswordService(IPasswordService):
    pwd_hash: PasswordHasher

    def generate_hash_password(self, plain_password: str) -> str:
        return self.pwd_hash.hash(plain_password)

    def verify_password(self, plain_password: str, hash_password: str) -> bool:
        return self.pwd_hash.verify(hash_password, plain_password)


class LoginService(ILoginService):
    def generate_access_token_and_is_active_account(self, user: User) -> str:
        expire = datetime.now() + timedelta(minutes=15)
        data = {"sub": user.id, "exp": expire}
        encoded_jwt = jwt.encode(
            data, settings.SECRET_KEY, algorithm=settings.ALGORITHM
        )
        user.is_active = True
        return encoded_jwt
