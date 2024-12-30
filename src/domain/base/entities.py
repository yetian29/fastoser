from dataclasses import dataclass
from typing import Generic, TypeVar
from datetime import datetime

from src.domain.base.value_objects import BaseValueObject

EntityId = TypeVar("EntityId", bound=BaseValueObject)
EntityCreatedAt = TypeVar("EntityCreatedAt", bound=BaseValueObject)


@dataclass
class BaseEntity(Generic[EntityId, EntityCreatedAt]):
    id: EntityId
    created_at: EntityCreatedAt
    updated_at: datetime
