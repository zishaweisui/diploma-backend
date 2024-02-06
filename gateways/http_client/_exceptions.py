class HttpException(Exception):
    pass


class TimeoutException(Exception):
    pass


class HttpStatusException(HttpException):
    def __init__(self, status_code: int, body: str, content: bytes):
        self.status_code = status_code
        self.body = body
        self.content = content


class InvalidUrlException(HttpException):
    pass


class GenericRequestException(HttpException):
    pass


class ReadTimeoutException(HttpException):
    pass


class ConnectError(HttpException):
    pass
