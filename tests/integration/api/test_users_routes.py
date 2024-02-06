import pytest
from bson import ObjectId
from faker import Faker
from httpx import AsyncClient

from models.login import LoginRequest
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


async def __auth_headers(created_user: User) -> dict:
    auth_service = structure.instantiate("auth_service")
    login_request = LoginRequest(email=created_user.email, password="qweQWE123")
    token_pair = await auth_service.login(login_request)
    created_user.token_pairs.append(token_pair)
    await users_repository.update(created_user)
    return {
        "Authorization": "Token " + created_user.token_pairs[0].access_token
    }


def __get_user_attributes(email=None) -> dict:
    return {
        "role": "superadmin",
        "roles": [
            "admin"
            ],
        "email": email or "test@yolo.com",
        "profile": {
            "first_name": f.first_name(),
            "last_name": f.last_name()
            },
        "password": "qweQWE123"
    }


@pytest.mark.anyio
async def test_create_user(client: AsyncClient):
    user_attributes = __get_user_attributes()

    superadmin = await __create_user()
    response = await client.post(
        "/v1/users", json=user_attributes, headers=await __auth_headers(superadmin))

    assert response.status_code == 200
    user = await users_repository.find_by_email(user_attributes["email"])
    assert user is not None


@pytest.mark.anyio
async def test_create_user_existing_email(client: AsyncClient):
    existing_user = await __create_user()
    user_attributes = __get_user_attributes(email=existing_user.email)

    response = await client.post(
        "/v1/users", json=user_attributes, headers=await __auth_headers(existing_user))
    assert response.status_code == 400
    assert response.json()["user"][0]["key"] == "error_already_exists"


@pytest.mark.anyio
async def test_create_user_invalid_attributes(client: AsyncClient):
    user_attributes = {}
    superadmin = await __create_user()

    response = await client.post(
        "/v1/users", json=user_attributes, headers=await __auth_headers(superadmin))
    assert response.status_code == 422


@pytest.mark.anyio
async def test_create_user_no_auth(client: AsyncClient):
    user_attributes = __get_user_attributes()

    response = await client.post("/v1/users", json=user_attributes)
    assert response.status_code == 401


@pytest.mark.anyio
async def test_create_user_invalid_token(client: AsyncClient):
    invalid_auth_headers = {"Authorization": "Token invalid_token"}
    user_attributes = __get_user_attributes()

    response = await client.post("/v1/users", json=user_attributes, headers=invalid_auth_headers)
    assert response.status_code == 401
    exist_user = await users_repository.find_by_email(user_attributes["email"])
    assert exist_user is None


@pytest.mark.anyio
async def test_get_users_page(client: AsyncClient):
    await __clear_database()
    for _ in range(2):
        await __create_user()

    superadmin = await __create_user()
    response = await client.get("/v1/users", headers = await __auth_headers(superadmin))

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["page"] == 1
    assert response.json()["page_count"] == 1
    assert len(response.json()["items"]) == 3


@pytest.mark.anyio
async def test_get_all_users(client: AsyncClient):
    await __clear_database()
    for _ in range(2):
        await __create_user()

    superadmin = await __create_user()
    response = await client.get("/v1/all_users", headers = await __auth_headers(superadmin))

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 3


@pytest.mark.anyio
async def test_get_all_users_no_auth(client: AsyncClient):
    response = await client.get("/v1/users")
    assert response.status_code == 401


@pytest.mark.anyio
async def test_get_all_users_invalid_token(client: AsyncClient):
    invalid_auth_headers = {"Authorization": "Token invalid_token"}
    response = await client.get("/v1/users", headers=invalid_auth_headers)
    assert response.status_code == 401


@pytest.mark.anyio
async def test_get_one_user(client: AsyncClient):
    created_user = await __create_user()
    response = await client.get(
        f"/v1/users/{str(created_user.id)}", headers = await __auth_headers(created_user))

    assert response.status_code == 200
    response_body = response.json()
    assert response_body["id"] == str(created_user.id)
    assert response_body["email"] == created_user.email
    assert response_body["profile"]["first_name"] == created_user.profile.first_name
    assert response_body["profile"]["last_name"] == created_user.profile.last_name


@pytest.mark.anyio
async def test_get_one_user_no_auth(client: AsyncClient):
    response = await client.get(f"/v1/users/{str(ObjectId())}")
    assert response.status_code == 401


@pytest.mark.anyio
async def test_get_one_user_invalid_token(client: AsyncClient):
    invalid_auth_headers = {"Authorization": "Token invalid_token"}
    response = await client.get(f"/v1/users/{str(ObjectId())}", headers=invalid_auth_headers)
    assert response.status_code == 401


@pytest.mark.anyio
async def test_update_user(client: AsyncClient):
    existing_user = await __create_user()
    updated_attributes = __get_user_attributes(email=existing_user.email)

    response = await client.put(f"/v1/users/{existing_user.id}",
            json=updated_attributes, headers=await __auth_headers(existing_user))

    assert response.status_code == 200
    response_body = response.json()
    assert response_body["id"] == str(existing_user.id)
    assert response_body["email"] == existing_user.email
    assert response_body["profile"]["first_name"] == updated_attributes.get("profile")["first_name"]
    assert response_body["profile"]["last_name"] == updated_attributes.get("profile")["last_name"]
    updated_user = await users_repository.find_by_email(updated_attributes["email"])
    assert updated_user.token_pairs == []


@pytest.mark.anyio
async def test_update_user_existing_email(client: AsyncClient):
    existing_user = await __create_user()
    updating_user = await __create_user()
    updated_attributes = __get_user_attributes(email=existing_user.email)

    response = await client.put(f"/v1/users/{updating_user.id}",
            json=updated_attributes, headers=await __auth_headers(existing_user))

    assert response.status_code == 400
    assert response.json()["user"][0]["key"] == "error_already_exists"


@pytest.mark.anyio
async def test_update_user_without_password(client: AsyncClient):
    existing_user = await __create_user()
    updated_attributes = __get_user_attributes(email=existing_user.email)

    response = await client.put(f"/v1/users/{existing_user.id}",
            json=updated_attributes, headers = await __auth_headers(existing_user))

    assert response.status_code == 200
    response_body = response.json()
    assert response_body["id"] == str(existing_user.id)
    assert response_body["email"] == existing_user.email
    assert response_body["profile"]["first_name"] == updated_attributes.get("profile")["first_name"]
    assert response_body["profile"]["last_name"] == updated_attributes.get("profile")["last_name"]


@pytest.mark.anyio
async def test_update_user_invalid_attributes(client: AsyncClient):
    updated_attributes = {}
    superadmin = await __create_user()

    response = await client.put(f"/v1/users/{str(ObjectId())}",
            json=updated_attributes, headers=await __auth_headers(superadmin))

    assert response.status_code == 422


@pytest.mark.anyio
async def test_update_user_no_auth(client: AsyncClient):
    updated_attributes = __get_user_attributes()

    response = await client.put(f"/v1/users/{str(ObjectId())}", json=updated_attributes)
    assert response.status_code == 401


@pytest.mark.anyio
async def test_update_user_invalid_token(client: AsyncClient):
    invalid_auth_headers = {"Authorization": "Token invalid_token"}
    updated_attributes = __get_user_attributes()

    response = await client.put(f"/v1/users/{str(ObjectId())}", json=updated_attributes, headers=invalid_auth_headers)
    assert response.status_code == 401


@pytest.mark.anyio
async def test_delete_user(client: AsyncClient):
    existing_user = await __create_user()

    response = await client.delete(f"/v1/users/{existing_user.id}", headers = await __auth_headers(existing_user))

    assert response.status_code == 200
    exist_user = await users_repository.get(existing_user.id)
    assert exist_user is None


@pytest.mark.anyio
async def test_delete_user_no_auth(client: AsyncClient):
    response = await client.delete(f"/v1/users/{str(ObjectId())}")
    assert response.status_code == 401


@pytest.mark.anyio
async def test_delete_user_invalid_token(client: AsyncClient):
    invalid_auth_headers = {"Authorization": "Token invalid_token"}
    response = await client.delete(f"/v1/users/{str(ObjectId())}", headers=invalid_auth_headers)
    assert response.status_code == 401


@pytest.mark.anyio
async def test_delete_missing_user(client: AsyncClient):
    superadmin = await __create_user()
    response = await client.delete(f"/v1/users/{str(ObjectId())}", headers=await __auth_headers(superadmin))
    assert response.status_code == 404


@pytest.mark.anyio
async def test_get_me(client: AsyncClient):
    existing_user = await __create_user()
    response = await client.get("/v1/me", headers = await __auth_headers(existing_user))

    assert response.status_code == 200
    response_body = response.json()
    assert response_body["id"] == str(existing_user.id)
    assert response_body["email"] == existing_user.email


@pytest.mark.anyio
async def test_get_me_no_auth(client: AsyncClient):
    response = await client.get("/v1/me")
    assert response.status_code == 401


@pytest.mark.anyio
async def test_get_me_invalid_token(client: AsyncClient):
    invalid_auth_headers = {"Authorization": "Token invalid_token"}
    response = await client.get("/v1/me", headers=invalid_auth_headers)
    assert response.status_code == 401
