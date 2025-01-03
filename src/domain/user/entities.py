

@dataclass
class User:
    oid: UUID
    username: str
    email: str
    password: str 
    is_active: bool
