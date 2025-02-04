from dataclasses import dataclass
from datetime import datetime
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel


@dataclass
class BaseEntity(BaseModel):
    oid: UUID | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, BaseEntity):
            return self.oid == other.oid
        return False

    def __post_init__(self) -> None:
        if self.oid is None:
            self.oid = uuid4()
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()
