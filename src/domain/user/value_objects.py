from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from src.domain.base.value_objects import BaseValueObject


@dataclass(frozen=True)
class UserOID(BaseValueObject):
    value: UUID


@dataclass(frozen=True)
class UserCreatedAt(BaseValueObject):
    value: datetime


@dataclass(frozen=True)
class UserName(BaseValueObject):
    value: str


@dataclass(frozen=True)
class UserEmail(BaseValueObject):
    value: str


@dataclass(frozen=True)
class UserPassword(BaseValueObject):
    value: str
