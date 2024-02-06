import asyncio

from models.mlo import MLOStatus
from structure import structure


async def migrate_mlo_unpublished():
    mlos_repository = structure.instantiate("mlos_repository")

    await mlos_repository.collection.update_many(
        {"status": MLOStatus.UNPUBLISHED},
        {"$set": {"zip_code": None}}
    )


async def main():
    await migrate_mlo_unpublished()

if __name__ == "__main__":
    asyncio.run(main())
