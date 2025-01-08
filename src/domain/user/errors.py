from src.domain.base.errors import BaseDomainException


class BaseUserException(BaseDomainException):
    pass


class UserHasBeenRegistedException(BaseUserException):
    pass


class PasswordIncorrectException(BaseUserException):
    pass
