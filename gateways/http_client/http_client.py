
import httpx

from ._exceptions import (
    ConnectError,
    GenericRequestException,
    HttpStatusException,
    InvalidUrlException,
    ReadTimeoutException,
    TimeoutException,
)
from ._types import (
    Headers,
    HttpMethod,
    JsonObject,
    QueryParams,
    RequestData,
    Response,
)

DEFAULT_TIMEOUT = 10.0


class HttpClient:
    async def get(
            self,
            url: str,
            *,
            params: QueryParams | None = None,
            timeout: int | None = None,
    ) -> Response:
        return await self._run_request(
            HttpMethod.GET,
            url,
            None,
            None,
            params,
            timeout,
        )

    async def post(
        self,
        url: str,
        data: RequestData | None = None,
        json: JsonObject | None = None,
        headers: Headers | None = None,
        params: QueryParams | None = None,
        timeout: float | None = DEFAULT_TIMEOUT,
    ) -> Response:
        return await self._run_request(
            HttpMethod.POST,
            url,
            data,
            json,
            headers,
            params,
            timeout,
        )

    async def put(
        self,
        url: str,
        data: RequestData | None = None,
        json: JsonObject | None = None,
        headers: Headers | None = None,
        params: QueryParams | None = None,
        timeout: float | None = DEFAULT_TIMEOUT,
    ) -> Response:
        return await self._run_request(
            HttpMethod.PUT,
            url,
            data,
            json,
            headers,
            params,
            timeout,
        )

    async def delete(
        self,
        url: str,
        data: RequestData | None = None,
        headers: Headers | None = None,
        params: QueryParams | None = None,
        timeout: float | None = DEFAULT_TIMEOUT,
    ) -> Response:
        return await self._run_request(
            HttpMethod.DELETE,
            url,
            data,
            None,
            headers,
            params,
            timeout,
        )

    async def _run_request(
        self,
        method: HttpMethod,
        url: str,
        data: RequestData | None = None,
        json: JsonObject | None = None,
        headers: Headers | None = None,
        params: QueryParams | None = None,
        timeout: float | None = DEFAULT_TIMEOUT,
    ) -> Response:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.request(
                    method=method,
                    url=url,
                    data=data,
                    json=json,
                    headers=headers,
                    params=params,
                    timeout=timeout
                )
                response.raise_for_status()
                return Response(status_code=response.status_code, body=response.text)
            except httpx.InvalidURL as e:
                raise InvalidUrlException from e
            except httpx.HTTPStatusError as e:
                raise HttpStatusException(
                    status_code=e.response.status_code,
                    body=e.response.text,
                    content=e.response.content
                ) from e
            except httpx.TimeoutException as e:
                raise TimeoutException from e
            except Exception as e:
                raise GenericRequestException from e

    async def download_file(self, url: str) -> bytes | None:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url)
                response.raise_for_status()
            except Exception as e:
                print(f"Failed to download/upload image from {url}: {e}")
                return None
            else:
                return response.content

    async def download_zip(self, headers, url: str) -> bytes | None:
        async with httpx.AsyncClient(headers=headers, timeout=60) as client:
            try:
                response = await client.get(url, follow_redirects=True)
                response.raise_for_status()
            except httpx.ReadTimeout as e:
                raise ReadTimeoutException from e
            except httpx.ConnectError as e:
                raise ConnectError from e
            except httpx.HTTPStatusError as e:
                raise HttpStatusException(
                    status_code=e.response.status_code, body=e.response.text,
                    content=e.response.content
                ) from e
            else:
                if response.headers.get("content-type") != "application/x-zip-compressed":
                    return None
                return response.content
