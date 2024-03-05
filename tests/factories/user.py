from faker import Faker

from models.user import Profile, User
from structure import structure


class UserFactory:
    def __init__(self):
        self.faker = Faker()
        self.password_service = structure.instantiate("password_service")
        self.precalculated_password_hash = None

    async def generic(self, role=None, roles=None, password="qweQWE123"):
        roles = roles or ["user"]
        role = role or "admin"
        if not self.precalculated_password_hash:
            self.precalculated_password_hash = await self.password_service.create_hash("qweQWE123")
        match password:
            case "qweQWE123":
                password_hash = self.precalculated_password_hash
            case _:
                password_hash = await self.password_service.create_hash(password)

        return User(
            role=role,
            roles=roles,
            email=self.faker.email(),
            nickname=self.faker.first_name().lower(),
            password_hash=password_hash,
            profile=Profile(first_name=self.faker.first_name(), last_name=self.faker.last_name()),
            token_pairs=[],
        )

    async def create_password_hash(self, password):
        return await self.password_service.create_hash(password)
