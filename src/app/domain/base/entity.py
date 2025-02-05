from dataclasses import dataclass
from datetime import datetime
from typing import Any

from src.app.domain.base.value_object import EntityCreatedAt, EntityOid


@dataclass
class BaseEntity:
    oid: EntityOid
    created_at: EntityCreatedAt
    updated_at: datetime

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, BaseEntity):
            return self.oid == other.oid
        return False
