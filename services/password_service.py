from wrappers.bcrypt_wrapper import BcryptWrapper


class PasswordService:
    def __init__(self, bcrypt_wrapper) -> None:
        self.bcrypt_wrapper: BcryptWrapper = bcrypt_wrapper

    async def create_hash(self, password: str) -> str:
        return await self.bcrypt_wrapper.get_password_hash(password)

    async def check(self, password, password_hash):
        return await self.bcrypt_wrapper.verify_password(password, password_hash)

    async def generate_password(self, password_length=None):
        return await self.bcrypt_wrapper.generate_password(password_length)
