from motor.motor_asyncio import AsyncIOMotorClient

from env_settings import get_settings


class MotorWrapper:
    def __init__(self) -> None:
        self.scheme = get_settings().mongo_scheme
        self.username = get_settings().mongo_username
        self.password = get_settings().mongo_password
        self.host = get_settings().mongo_host
        self.port = get_settings().mongo_port
        self.name = get_settings().mongo_name

    def get_client(self):
        url = f"{self.scheme}://{self.username}:{self.password}@{self.host}:{self.port}"
        return AsyncIOMotorClient(url)

    def get_collection(self, client: AsyncIOMotorClient, collection_name: str):
        return client[self.name][collection_name]
