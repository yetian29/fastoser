from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.domain.user.repository import IUserRepository
from src.app.infrastructure.database.models.user import UserORM


class UserRepository(IUserRepository):
    def __init__(self, async_session: AsyncSession) -> None:
        self._async_session = async_session

    async def get_user_by_username(self, username: str) -> UserORM | None:
        async with self._async_session as session:
            stmt = select(UserORM).where(UserORM.username == username)
            return await session.scalar(stmt)

    async def get_user_by_email(self, email: str) -> UserORM | None:
        async with self._async_session as session:
            stmt = select(UserORM).where(UserORM.email == email)
            return await session.scalar(stmt)

    async def get_user_by_oid(self, oid: UUID) -> UserORM | None:
        async with self._async_session as session:
            stmt = select(UserORM).where(UserORM.oid == oid)
            return await session.scalar(stmt)

    async def create_user(self, user_orm: UserORM) -> UserORM:
        async with self._async_session as session:
            session.add(user_orm)
            await session.commit()
            await session.refresh(user_orm)
            return user_orm

    async def update_user(self, user_orm: UserORM) -> UserORM:
        async with self._async_session as session:
            session.add(user_orm)
            await session.commit()
            await session.refresh(user_orm)
            return user_orm

    async def delete_user(self, oid: UUID) -> UserORM | None:
        async with self._async_session as session:
            stmt = select(UserORM).where(UserORM.oid == oid)
            user = await session.scalar(stmt)
            user_tmp = user
            if not user:
                return None
            await session.delete(user)
            await session.commit()
            return user_tmp
