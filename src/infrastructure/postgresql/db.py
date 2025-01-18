from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.core.config.settings import settings


class DatabaseManager:
    """echo=True: Kiểm soát việc ghi nhật ký các câu lệnh SQL được thực thi bởi Engine, để gỡ lỗi các truy vấn SQL"""

    """echo_pool=True: Kiểm soát việc ghi nhật ký các sự kiện nhóm kết nối,để theo dõi và gỡ lỗi hành vi của nhóm kết nối, đảm bảo các kết nối được quản lý chính xác."""
    """hide_parameter=True: ngăn chặn việc lộ thông tin nhạy cảm, cụ thể là giá trị của các tham số truy vấn"""
    """pool_size=10: Kích thước pool kết nối (tối đa 10 kết nối)"""
    """max_overflow=20: Cho phép vượt quá tối đa 20 kết nối"""
    """pool_timeout=30: Thời gian tối đa chờ kết nối trong 30 giây"""
    """pool_recycle=3600: Tái tạo kết nối sau mỗi 1 giờ"""

    def __init__(
        self, url: str = settings.database.pg_dsn, is_dev: str = settings.environment
    ) -> None:
        self.echo: bool = is_dev == "development"
        self.async_engine = create_async_engine(
            url=url,
            echo=self.echo,
            echo_pool=self.echo,
            isolation="READ COMMITTED",
            hide_parameters=True,
            pool_size=10,
            max_overflow=20,
            pool_timeout=30,
            pool_recycle=3600,
        )

        # expire_on_commit - don't expire objects after transaction commit
        self.async_session = async_sessionmaker(
            bind=self.async_engine, expire_on_commit=False
        )
