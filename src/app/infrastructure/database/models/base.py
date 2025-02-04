from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.ext.asyncio import AsyncAttrs

class BaseORM(AsyncAttrs, DeclarativeBase):
    pass