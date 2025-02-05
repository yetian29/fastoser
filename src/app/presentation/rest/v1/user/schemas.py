import re
from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, field_validator

from src.app.domain.user.entity import User
from src.app.domain.user.exception import DomainValidationException

   

class UserRegisterInSchema(BaseModel):
    username: str
    email: str
    password: str
    
    @property
    def hash_password(self, plain_password: str) -> str:
        pass


    @field_validator("username", mode="after")
    @classmethod
    def validate_username(cls, value):
        if not value:
            raise DomainValidationException(
                "UserName invalid. UserName can't be blank."
            )
        elif len(value) < 4:
            raise DomainValidationException(
                "UserName invalid. UserName is too short, username has to between 4 to 16 character."
            )
        elif len(value) > 16:
            raise DomainValidationException(
                "UserName invalid. UserName is too long, username has to between 4 to 16 character."
            )
        return value

    @field_validator("email", mode="after")
    @classmethod
    def validate_email(cls, value):
        # Regular expression for email validation
        # This pattern validates:
        # - Local part can contain letters, numbers, and certain special characters
        # - Domain part must contain letters, numbers, dots, and hyphens
        # - TLD must be at least 2 characters

        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_pattern, value):
            raise DomainValidationException(
                "UserEmail invalid. UserEmail has to be formatted same as 'example@gmail.com'"
            )
        return value


   
    def to_entity(
        self,
        oid: UUID = uuid4(),
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
        is_active: bool = False,
    ) -> User:
        return User(
            oid=oid,
            username=self.username,
            email=self.email,
            password=self.hash_password,
            created_at=created_at,
            updated_at=updated_at,
            is_active=is_active,
        )
