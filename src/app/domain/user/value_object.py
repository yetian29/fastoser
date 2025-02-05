from dataclasses import dataclass

from src.app.domain.base.value_object import BaseValueObject


@dataclass(frozen=True)
class UserName(BaseValueObject):
    value: str


@dataclass(frozen=True)
class UserEmail(BaseValueObject):
    value: str
