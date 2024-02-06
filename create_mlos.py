import asyncio
import random

from faker import Faker

from models import MLO, Theme
from models.mlo import MLOStatus
from structure import structure

color_themes = [
    {
        "name": "Red",
        "color": "#7C4040",
        "color_light": "#D3BFBF",
        "color_dark": "#500000",
        "font_color": "#FFFFFF"
    },
    {
        "name": "Green",
        "color": "#446440",
        "color_light": "#C1CBBF",
        "color_dark": "#063000",
        "font_color": "#FFFFFF"
    },
    {
        "name": "Blue",
        "color": "#404464",
        "color_light": "#BFC1CB",
        "color_dark": "#000630",
        "font_color": "#FFFFFF"
    },
    {
        "name": "Brown",
        "color": "#7C5E40",
        "color_light": "#D3C9BF",
        "color_dark": "#502800",
        "font_color": "#FFFFFF"
    },
    {
        "name": "Purple",
        "color": "#7549EA",
        "color_light": "#C4BED2",
        "color_dark": "#140049",
        "font_color": "#FFFFFF"
    }
]


async def create_themes():
    tasks = []
    themes_repository = structure.instantiate("themes_repository")
    if len(color_themes) == await themes_repository._count_by_aggregation([]):
        results = await themes_repository._find_by_aggregation([])
        return [model.id for model in results]
    for theme_data in color_themes:
        theme = Theme(**theme_data)
        tasks.append(themes_repository.create(theme))
        print(f"Created - {theme_data['name']}")
    return await asyncio.gather(*tasks)


async def create_mlos(themes):
    mlos_repository = structure.instantiate("mlos_repository")
    locations_repository = structure.instantiate("locations_repository")
    f = Faker()
    emails = [f.email() for _ in range(1000)]
    statuses = [MLOStatus.DRAFT, MLOStatus.PUBLISHED, MLOStatus.UNPUBLISHED]

    unclaimed_count = await count_unclaimed_locations()
    print(f"{unclaimed_count = }")
    tasks = []
    for index, email in enumerate(emails):
        if index == unclaimed_count:
            break
        existing = await mlos_repository.find_by_email(email)
        if existing:
            continue
        unclaimed_location = await locations_repository.collection.find_one({"is_claimed": False})

        zip_code = unclaimed_location.get("zip_code")
        mlo_attrs = {
            "status": random.choice(statuses),
            "email": email,
            "first_name": f.first_name(),
            "last_name": f.last_name(),
            "headshot": None,
            "website": f.url(),
            "nmls_license": str(f.random_number(digits=6)),
            "phone_number": f.phone_number(),
            "zip_code": zip_code,
            "theme_id": random.choice(themes)
        }
        mlo_attrs["web_app_id"] = (
            f"{mlo_attrs.get('first_name')}"
            f"{mlo_attrs.get('last_name')}-"
            f"{mlo_attrs.get('nmls_license')}"
        )
        locations_repository.collection.update_many(
            {"zip_code": zip_code},
            {"$set": {"is_claimed": True}}
        )
        mlo = MLO(**mlo_attrs)
        tasks.append(mlos_repository.create(mlo))
        print(f"Created MLO - {email}")
    await asyncio.gather(*tasks)


async def count_unclaimed_locations():
    locations_repository = structure.instantiate("locations_repository")
    return await locations_repository.collection.count_documents({"is_claimed": {"$ne": True}})


async def main():
    themes = await create_themes()
    await create_mlos(themes)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
