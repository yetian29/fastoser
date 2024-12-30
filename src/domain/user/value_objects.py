from datetime import datetime
from src.domain.base.value_objects import BaseValueObject
from uuid import UUID
from dataclasses import dataclass


@dataclass(frozen=True)
class UserId(BaseValueObject):
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
