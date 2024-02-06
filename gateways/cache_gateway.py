from repositories.cache_repository import CacheRepository


class CacheGateway:
    def __init__(self, repository):
        self.repository: CacheRepository = repository
        self.booked_ttl: int = 900

    def is_booked(self, email: str, zip_code: str) -> bool:
        booked = self.repository.get_booked(zip_code)
        if not booked:
            return False
        if len(booked) > 1:
            return True
        if booked[0] == f"{email}:{zip_code}".encode("utf-8"):
            return False
        return True

    def book(self, email: str, zip_code: str):
        key = f"{email}:{zip_code}"
        self.repository.book(key, ttl=self.booked_ttl)

    def get_booked_zipcodes(self) -> list[str]:
        booked = self.repository.get_all()
        zipcodes = []
        for book in booked:
            if not isinstance(book, bytes):
                continue
            booked_zip = book.decode("utf-8").split(":")
            if len(booked_zip) == 1:
                continue
            zipcodes.append(booked_zip[-1])
        return zipcodes
