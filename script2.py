import asyncio

from structure import structure

repository = structure.instantiate("game_releases_repository")


async def main():
    nintendo_url = "https://cdn-wp.thesportsrush.com/2024/01/196bec46-nintendo-switch-logo-computer-background-908-927-hd-wallpapers.jpg?format=auto&w=640&q=75"
    xbox_url = "https://logowik.com/content/uploads/images/xbox5244.jpg"
    pc_url = "https://www.personalcomputercare.nl/plaatjes/nodig-game-pc.jpg"
    ps_url = "https://images.cgames.de/images/gsgp/290/sony-playstation_6133575.jpg"
    mobile_url = "https://scandasia.com/wp-content/uploads/2023/01/mobile_gaming.png"
    oculus_url = "https://www.logodesignlove.com/images/logos/old-oculus-logo.jpg"
    cursor = repository.collection.find({})
    async for document in cursor:
        release_id = document.get("_id")
        platform_type = document.get("platform").split()[0]
        url = document.get("images_api_url")

        match platform_type:
            case "PC":
                url = pc_url
            case "Linux":
                url = pc_url
            case "Macintosh":
                url = pc_url
            case "Xbox":
                url = xbox_url
            case "PlayStation":
                url = ps_url
            case "Nintendo":
                url = nintendo_url
            case "Android":
                url = mobile_url
            case "iOS":
                url = mobile_url
            case "Oculus":
                url = oculus_url
            case _:
                print("BLYAT")
                print(release_id, url)

        await repository.collection.update_one(
            {"_id": release_id},
            {"$set": {"image_url": url}}
        )

    await repository.collection.update_many(
        {},
        {"$unset": {"images_api_url": ""}}
    )


if __name__ == "__main__":
    asyncio.run(main())
