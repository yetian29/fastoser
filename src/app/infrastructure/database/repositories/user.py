from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.domain.user.repository import IUserRepository
from src.app.infrastructure.database.models.user import UserORM


class UserRepository(IUserRepository):
    def __init__(self, async_session: AsyncSession) -> None:
        self._async_session = async_session

    async def get_user_by_username(self, username: str) -> UserORM | None:
        stmt = select(UserORM).where(UserORM.username == username)
        return await self._async_session.scalar(stmt)

    async def get_user_by_email(self, email: str) -> UserORM | None:
        stmt = select(UserORM).where(UserORM.email == email)
        return await self._async_session.scalar(stmt)

    async def get_user_by_oid(self, oid: UUID) -> UserORM | None:
        stmt = select(UserORM).where(UserORM.oid == oid)
        return await self._async_session.scalar(stmt)

    async def create_user(self, user_orm: UserORM) -> UserORM:
        self._async_session.add(user_orm)
        await self._async_session.flush()
        await self._async_session.refresh(user_orm)
        return user_orm

    async def update_user(self, user_orm: UserORM) -> UserORM:
        stmt = (
            update(UserORM)
            .where(UserORM.oid == user_orm.oid)
            .values(is_active=user_orm.is_active)
        )
        await self._async_session.execute(stmt)
        return user_orm

    async def delete_user(self, oid: UUID) -> UserORM | None:
        user_orm = await self.get_user_by_oid(oid)
        if not user_orm:
            return None
        await self._async_session.delete(user_orm)
        await self._async_session.flush()
        return user_orm
