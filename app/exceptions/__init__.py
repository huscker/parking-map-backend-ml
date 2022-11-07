from typing import Any, Mapping

from starlette import status


class ApiException(Exception):
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    message: str = 'Упс! Что-то пошло не так ;('

    def __init__(self, message: str | None = None, payload: Mapping | None = None, debug: Any = None):
        self.message = message or self.message
        self.payload = payload
        self.debug = debug

    def to_json(self) -> Mapping:
        return {
            'code': self.status_code,
            'message': self.message,
            'payload': self.payload,
            'name': self.__name__,
        }


class ServerError(ApiException):
    status_code = 500
    message = 'Упс! Что-то пошло не так ;('
