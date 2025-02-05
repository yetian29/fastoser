import re

from pydantic.dataclasses import dataclass

from src.app.domain.base.value_object import BaseValueObject
from src.app.domain.user.exception import DomainValidationException


@dataclass(frozen=True)
class UserName(BaseValueObject):
    value: str

    def validate(self) -> None:
        if not self.value:
            raise DomainValidationException("UserName invalid. UserName can'tbe blank.")
        elif len(self.value) < 4:
            raise DomainValidationException(
                "UserName invalid. UserName is too short, username has to between 4 to 16 character."
            )
        elif len(self.value) > 16:
            raise DomainValidationException(
                "UserName invalid. UserName is too long, username has to between 4 to 16 character."
            )

    def __post_init__(self) -> None:
        self.validate()


@dataclass(frozen=True)
class UserEmail(BaseValueObject):
    value: str

    def validate(self) -> None:
        # Regular expression for email validation
        # This pattern validates:
        # - Local part can contain letters, numbers, and certain special characters
        # - Domain part must contain letters, numbers, dots, and hyphens
        # - TLD must be at least 2 characters

        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_pattern, self.value):
            raise DomainValidationException(
                "UserEmail invalid. UserEmail has to be formatted same as 'example@gmail.com'"
            )

    def __post_init__(self) -> None:
        self.validate()
