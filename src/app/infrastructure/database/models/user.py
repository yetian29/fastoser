    
from sqlalchemy import String
from src.app.infrastructure.database.models.base import BaseORM
from src.app.infrastructure.database.models.mixin import TimeStampMixin, UUIDOidMixin
from sqlalchemy.orm import Mapped, mapped_column


class UserORM(BaseORM, UUIDOidMixin, TimeStampMixin):
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] 
    is_active: Mapped[bool] = mapped_column(default=False)
