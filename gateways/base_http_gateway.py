from .http_client import HttpClient


class BaseHttpGateway:
    def __init__(self, http: HttpClient):
        self.http = http
