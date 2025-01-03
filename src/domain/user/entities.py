

from src.domain.base.entities import BaseEntity
from src.domain.user.value_objects import UserEmail, UserName, UserPassword


@dataclass
class User(BaseEntity[UserOID, UserCreatedAt]):
    username: UserName
    email: UserEmail
    password: UserPassword
    is_active: bool = False
