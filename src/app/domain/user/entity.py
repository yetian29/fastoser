from pydantic.dataclasses import dataclass

from src.app.domain.base.entity import BaseEntity
from src.app.domain.user.value_object import UserEmail, UserName


@dataclass
class User(BaseEntity):
    username: UserName
    email: UserEmail
    password: str
    is_active: bool = False
