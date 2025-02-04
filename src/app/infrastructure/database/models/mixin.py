from datetime import datetime
from typing import Annotated
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from uuid import UUID, uuid4


class UUIDOidMixin:
    oid: Mapped[UUID] = mapped_column(primary_key=True, unique=True, default=uuid4)

class TimeStampMixin:
    timestamp = Annotated[
        datetime,
        mapped_column(
            default=func.now(),
            server_default=func.now()
        )
        
    ]
    created_at: Mapped[timestamp]
    updated_at: Mapped[timestamp] = mapped_column(onupdate=func.now(), server_onupdate=func.now())