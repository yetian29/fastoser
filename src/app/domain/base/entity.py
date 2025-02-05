from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic.dataclasses import dataclass


@dataclass
class BaseEntity:
    oid: UUID
    created_at: datetime
    updated_at: datetime

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, BaseEntity):
            return self.oid == other.oid
        return False
