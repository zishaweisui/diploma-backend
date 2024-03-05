import pytest
from faker import Faker
from httpx import AsyncClient

from models.user import User
from structure import structure
from tests.factories import UserFactory

f = Faker()
users_factory = UserFactory()
users_repository = structure.instantiate("users_repository")


async def __clear_database():
    await users_repository.collection.delete_many({})


@pytest.fixture(scope="function", autouse=True)
async def teardown():
    await __clear_database()


async def __create_user(status=None) -> User:
    user = await users_factory.generic(status)
    user.id = await users_repository.create(user)
    return user


def __get_user_attributes(email=None) -> dict:
    return {
        "role": "user",
        "roles": [],
        "email": email or "test@yolo.com",
        "nickname": f.first_name().lower(),
        "profile": {
            "first_name": f.first_name(),
            "last_name": f.last_name()
            },
        "password": "qweQWE123"
    }

@pytest.mark.anyio
async def test_create_user(client: AsyncClient):
    user_attributes = __get_user_attributes()

    admin = await __create_user()
    response = await client.post(
        "/v1/public/signup", json=user_attributes)

    assert response.status_code == 200
    user = await users_repository.find_by_email(user_attributes["email"])
    assert user is not None


@pytest.mark.anyio
async def test_create_user_existing_email(client: AsyncClient):
    existing_user = await __create_user()
    user_attributes = __get_user_attributes(email=existing_user.email)

    response = await client.post(
        "/v1/public/signup", json=user_attributes)
    assert response.status_code == 400
    assert response.json()["user"][0]["key"] == "error_already_exists"


@pytest.mark.anyio
async def test_create_user_invalid_attributes(client: AsyncClient):
    user_attributes = {}
    response = await client.post(
        "/v1/public/signup", json=user_attributes)
    assert response.status_code == 422
