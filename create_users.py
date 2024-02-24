import asyncio
from random import choice
from string import ascii_letters

from faker import Faker

from env_settings import get_settings
from models import User
from structure import structure


def generate_password(env):
    if env != "prod":
        return "qweQWE123"
    return "".join(choice(ascii_letters) for _ in range(12))


async def create_admins():
    users_repository = structure.instantiate("users_repository")
    password_service = structure.instantiate("password_service")
    env = get_settings().env
    f = Faker()

    emails = [
        "d.gusev@storytelling-software.com",
        "a.levinas@storytelling-software.com"
    ]

    for email in emails:
        existing = await users_repository.find_by_email(email)
        if existing:
            continue
        password = generate_password(env)
        user_attrs = {
            "email": email,
            "role": "admin",
            "roles": ["user"],
            "password_hash": await password_service.create_hash(password),
            "profile": {
                "first_name": f.first_name(),
                "last_name": f.last_name()
            },
            "token_pairs": []
        }

        user = User(**user_attrs)
        await users_repository.create(user)
        print(f"Created - {email}/{password}")


async def create_users():
    users_repository = structure.instantiate("users_repository")
    password_service = structure.instantiate("password_service")
    env = get_settings().env
    f = Faker()

    emails = [
        "d.gusev+admin@storytelling-software.com",
        "a.levinas+admin@storytelling-software.com"
    ]

    for email in emails:
        existing = await users_repository.find_by_email(email)
        if existing:
            continue
        password = generate_password(env)
        user_attrs = {
            "email": email,
            "role": "user",
            "roles": [],
            "password_hash": await password_service.create_hash(password),
            "profile": {
                "first_name": f.first_name(),
                "last_name": f.last_name()
            },
            "token_pairs": []
        }

        user = User(**user_attrs)
        await users_repository.create(user)
        print(f"Created - {email}/{password}")


async def main():
    await create_users()
    await create_admins()

if __name__ == "__main__":
    asyncio.run(main())
