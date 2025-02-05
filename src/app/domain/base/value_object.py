from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class BaseValueObject:
    pass


@dataclass(frozen=True)
class EntityOid(BaseValueObject):
    value: UUID


@dataclass(frozen=True)
class EntityCreatedAt(BaseValueObject):
    value: datetime
