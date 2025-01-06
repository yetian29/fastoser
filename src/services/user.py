from datetime import datetime, timedelta

from src.domain.user.entities import User
from src.domain.user.services import ILoginService, IPasswordService, IUserService

import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PasswordService(IPasswordService):
    def get_password_hash(self, plain_password: str) -> str:
        return pwd_context.hash(plain_password)

    def verify_password(self, plain_password: str, hashed_password: str) -> True:
        return pwd_content.verify(plain_password, hashed_password)


class LoginService(ILoginService):
    def generate_access_token(
        user: User, expires_delta: timedelta | None = None
    ) -> str:
        if expires_delta:
            expire = datetime.now() + timedelta(expires_delta)
        else:
            expire = datetime.now() + timedelta(minutes=15)
        data = {"sub": user.oid, "exp": expire}
        encodted_jwt = jwt.encode(
            data, settings.SECRET_KEY, algorithm=settings.ALGORITHM
        )
        return encodted_jwt

    def is_active_account(user: User) -> None:
        user.is_active = True


class UserService(IUserService):
    pass
