from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.app.infrastructure.database.models.base import BaseORM
from src.app.infrastructure.database.models.mixin import TimeStampMixin, UUIDOidMixin


class UserORM(BaseORM, UUIDOidMixin, TimeStampMixin):
    __tablename__ = "user"
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=False)
