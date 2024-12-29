

from abc import ABC
from typing import Generic, TypeVar


EntityId = TypeVar("EntityId", bound=ValueObject)

class BaseEntity(Generic[EntityId]):
    id: EntityId

