from typing import AsyncIterator

import pytest
from httpx import AsyncClient
from pytest_httpx import HTTPXMock

from main import application
from structure import structure

users_repository = structure.instantiate("users_repository")

test_server_host = "testserver"


@pytest.fixture
def non_mocked_hosts() -> list:
    return [test_server_host]


@pytest.fixture(autouse=True)
def auto_httpx_mock(httpx_mock: HTTPXMock):
    """
    Mock all http requests except those that are specified
    in `non_mocked_hosts` fixture.
    """
    httpx_mock.add_response(
        status_code=200,
        json={
            "url": "https://example.com"
        }
    )


@pytest.fixture
def assert_all_responses_were_requested() -> bool:
    """
    Disable assertion of requests mocked by `pytest_httpx`.

    I.e. exception will not be thrown in case if request was mocked
    and was not called in a particular test.
    """
    return False


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture(scope="session")
async def client() -> AsyncIterator[AsyncClient]:
    async with AsyncClient(app=application, base_url=f"http://{test_server_host}") as _client:
        yield _client
