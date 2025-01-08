from dataclasses import dataclass
from typing import Generic, TypeVar

from src.domain.base.value_objects import BaseValueObject

BaseEntityOID = TypeVar("BaseEntityOID", bound=BaseValueObject)
BaseEntityCreatedAt = TypeVar("BaseEntityCreatedAt", bound=BaseValueObject)


@dataclass
class BaseEntity(Generic[BaseEntityOID, BaseEntityCreatedAt]):
    oid: BaseEntityOID
    created_at: BaseEntityCreatedAt
