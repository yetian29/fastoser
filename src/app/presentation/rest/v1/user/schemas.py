import re
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, field_validator


class UserRegisterInSchema(BaseModel):
    username: str
    email: str
    password: str

    @field_validator("username", mode="after")
    @classmethod
    def validate_username(cls, value):
        if not value:
            raise ValueError("UserName invalid. UserName can't be blank.")
        elif len(value) < 4:
            raise ValueError(
                "UserName invalid. UserName is too short, username has to between 4 to 16 character."
            )
        elif len(value) > 16:
            raise ValueError(
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
        if not value:
            raise ValueError("UserEmail invalid. UserEmail can't be blank.")
        elif not re.match(email_pattern, value):
            raise ValueError(
                "UserEmail invalid. UserEmail has to be formatted same as 'example@gmail.com'"
            )
        return value


class UserRegisterOutSchema(BaseModel):
    oid: UUID
    username: str
    email: str
    password: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
