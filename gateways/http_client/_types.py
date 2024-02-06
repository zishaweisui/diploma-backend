from enum import StrEnum
from typing import Mapping

from pydantic import BaseModel

QueryParamsTypes = str | int | bool | float
JsonObject = list[any] | dict[str, any]


RequestData = Mapping[str, any]
Headers = Mapping[str, str]
QueryParams = Mapping[str, QueryParamsTypes]


class Response(BaseModel):
    status_code: int
    body: str


class HttpMethod(StrEnum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PUT = "PUT"
