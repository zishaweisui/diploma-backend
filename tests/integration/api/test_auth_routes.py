import pytest
from httpx import AsyncClient

from models.user import User
from structure import structure
from tests.factories import UserFactory

users_factory = UserFactory()
users_repository = structure.instantiate("users_repository")


async def create_user() -> User:
    user = await users_factory.generic()
    user.id = await users_repository.create(user)
    return user


@pytest.mark.anyio
async def test_wrong_attributes_login(client: AsyncClient):
    json_body = {"emAAaail": "test", "pas_Word": "qweQWE123"}
    response = await client.post("/v1/auth/login", json=json_body)
    assert response.status_code == 422


@pytest.mark.anyio
async def test_no_user_login(client: AsyncClient):
    json_body = {"email": "", "password": "qweQWE123"}
    response = await client.post("/v1/auth/login", json=json_body)
    assert response.status_code == 422


@pytest.mark.anyio
async def test_non_matching_credentials_login(client: AsyncClient):
    user = await create_user()
    json_body = {"email": user.email, "password": "not a real password"}
    response = await client.post("/v1/auth/login", json=json_body)
    assert response.status_code == 401


@pytest.mark.anyio
async def test_matching_credentials_login(client: AsyncClient):
    user = await create_user()
    json_body = {"email": user.email, "password": "qweQWE123"}
    response = await client.post("/v1/auth/login", json=json_body)
    assert response.status_code == 200
    response_body = response.json()
    for item in {"access_token", "refresh_token"}:
        assert item in response_body
    assert response_body["access_token"]
    assert response_body["refresh_token"]
