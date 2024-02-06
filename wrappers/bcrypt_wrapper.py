from passlib.context import CryptContext
from passlib.pwd import genword


class BcryptWrapper:
    def __init__(self, rounds: int):
        self.rounds = rounds
        self.pwd_context = CryptContext(
            schemes=["bcrypt"], deprecated="auto", bcrypt__rounds=self.rounds)
        self.entropy = "secure"
        self.default_password_length = 8

    async def verify_password(self, plain_password, hashed_password) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    async def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    async def generate_password(self, length=None):
        password_length = length if length else self.default_password_length
        return genword(entropy=self.entropy, length=password_length)
