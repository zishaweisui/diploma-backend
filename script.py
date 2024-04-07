import asyncio

from models.game_release import GameRelease, Publisher
from structure import structure

repository = structure.instantiate("game_releases_repository")


async def fetch_game_releases(api_data):
    data = api_data['results']
    for release in data:
        model = GameRelease(
            release_date=release.get("release_date"),
            distribution_type=release.get("distribution_type"),
            name=release.get("name"),
            region=release.get("region"),
            platform=release.get("platform"),
            publishers=[Publisher(**publisher) for publisher in release.get("publishers")],
            images_api_url=release.get("images_api_url")
        )
        await repository.create(model)


async def main():
    data = {
    "error": "OK",
    "limit": 100,
    "offset": 0,
    "number_of_page_results": 100,
    "number_of_total_results": 177550,
    "status_code": 1,
    "results": [
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1010838,
            "name": "THE SHRiNK Season Two",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:622392",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-622392",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-622392",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-622392",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-622392",
            "association": "5000-622392",
            "publishers": [
                {
                    "name": "OMVN Publishing"
                }
            ],
            "developers": [
                {
                    "name": "OMVN Publishing"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Online",
            "id": 1014499,
            "name": "Big Adventure: Trip to Europe 7",
            "region": "North America",
            "platform": "Macintosh",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:620660",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-620660",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-620660",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-620660",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-620660",
            "association": "5000-620660",
            "publishers": [
                {
                    "name": "Big Fish Games"
                }
            ],
            "developers": [
                {
                    "name": "AVI Games"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1014462,
            "name": "Bunny Girl C**ming for my Carrot",
            "region": "North America",
            "platform": "Linux",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:624196",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-624196",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-624196",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-624196",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-624196",
            "association": "5000-624196",
            "publishers": [
                {
                    "name": "Cherry Kiss Games"
                }
            ],
            "developers": [
                {
                    "name": "Norn"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1014098,
            "name": "Bunny Girl C**ming for my Carrot",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:624196",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-624196",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-624196",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-624196",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-624196",
            "association": "5000-624196",
            "publishers": [
                {
                    "name": "Cherry Kiss Games"
                }
            ],
            "developers": [
                {
                    "name": "Norn"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1013893,
            "name": "Ignis",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:624126",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-624126",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-624126",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-624126",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-624126",
            "association": "5000-624126",
            "publishers": [
                {
                    "name": "Hot Drink Studios"
                }
            ],
            "developers": [
                {
                    "name": "Hot Drink Studios"
                }
            ]
        },
        {
            "upc": "0742839255441",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Retail",
            "id": 1013656,
            "name": "GunLord X",
            "region": "Europe",
            "platform": "PlayStation 4",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:95965",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-95965",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-95965",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-95965",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-95965",
            "association": "5000-95965",
            "publishers": [
                {
                    "name": "NG:DEV.TEAM"
                },
                {
                    "name": "EastAsiaSoft"
                }
            ],
            "developers": [
                {
                    "name": "NG:DEV.TEAM"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1012436,
            "name": "illumination (Early Access)",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:623230",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-623230",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-623230",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-623230",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-623230",
            "association": "5000-623230",
            "publishers": [
                {
                    "name": "illumination"
                }
            ],
            "developers": [
                {
                    "name": "illumination"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1012411,
            "name": "Dream fish",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:623207",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-623207",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-623207",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-623207",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-623207",
            "association": "5000-623207",
            "publishers": [
                {
                    "name": "Dream fish"
                }
            ],
            "developers": [
                {
                    "name": "Dream fish"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1012410,
            "name": "shock wave (shock wave) (Early Access)",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:623206",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-623206",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-623206",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-623206",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-623206",
            "association": "5000-623206",
            "publishers": [
                {
                    "name": "shock wave"
                }
            ],
            "developers": [
                {
                    "name": "shock wave"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1012090,
            "name": "NO REPORT",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:623100",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-623100",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-623100",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-623100",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-623100",
            "association": "5000-623100",
            "publishers": [
                {
                    "name": "Cartilage Studio"
                }
            ],
            "developers": [
                {
                    "name": "Carlig Narcis Constantin"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1011416,
            "name": "TIS 2 - True Idle Simulator 2",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:622869",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-622869",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-622869",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-622869",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-622869",
            "association": "5000-622869",
            "publishers": [
                {
                    "name": "PhantomHeadache"
                }
            ],
            "developers": [
                {
                    "name": "PhantomHeadache"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1011342,
            "name": "The Zombie Wave",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:622823",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-622823",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-622823",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-622823",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-622823",
            "association": "5000-622823",
            "publishers": [
                {
                    "name": "Snow Flake"
                }
            ],
            "developers": [
                {
                    "name": "Snow Flake"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1010904,
            "name": "THE SHRiNK Season Two",
            "region": "North America",
            "platform": "Linux",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:622392",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-622392",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-622392",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-622392",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-622392",
            "association": "5000-622392",
            "publishers": [
                {
                    "name": "OMVN Publishing"
                }
            ],
            "developers": [
                {
                    "name": "OMVN Publishing"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Online",
            "id": 1014501,
            "name": "Amazing Vacation: Los Angeles",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:624331",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-624331",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-624331",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-624331",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-624331",
            "association": "5000-624331",
            "publishers": [
                {
                    "name": "Big Fish Games"
                }
            ],
            "developers": [
                {
                    "name": "Big Fish Games"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1010835,
            "name": "Run for the Bus",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:622389",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-622389",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-622389",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-622389",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-622389",
            "association": "5000-622389",
            "publishers": [
                {
                    "name": "mizu"
                }
            ],
            "developers": [
                {
                    "name": "mizu"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1010652,
            "name": "I commissioned some invisible people 0",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:622301",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-622301",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-622301",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-622301",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-622301",
            "association": "5000-622301",
            "publishers": [
                {
                    "name": "Follow The Fun"
                }
            ],
            "developers": [
                {
                    "name": "Follow The Fun"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1010638,
            "name": "Cosmic Tankinator",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:622287",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-622287",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-622287",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-622287",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-622287",
            "association": "5000-622287",
            "publishers": [
                {
                    "name": "Sven Holm Pileborg"
                }
            ],
            "developers": [
                {
                    "name": "Sven Holm Pileborg"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1010618,
            "name": "PARADISE SHOOTING!!",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:622267",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-622267",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-622267",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-622267",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-622267",
            "association": "5000-622267",
            "publishers": [
                {
                    "name": "PRODUCTION PENCIL"
                }
            ],
            "developers": [
                {
                    "name": "Poison"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1010561,
            "name": "Project Canvas",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:622216",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-622216",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-622216",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-622216",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-622216",
            "association": "5000-622216",
            "publishers": [
                {
                    "name": "Project Canvas"
                }
            ],
            "developers": [
                {
                    "name": "Project Canvas"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1010525,
            "name": "The Russian Roulette Game : PR (Early Access)",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:622192",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-622192",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-622192",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-622192",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-622192",
            "association": "5000-622192",
            "publishers": [
                {
                    "name": "Sprt2D"
                }
            ],
            "developers": [
                {
                    "name": "Sprt2D"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1010355,
            "name": "CARS",
            "region": "North America",
            "platform": "Macintosh",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:622095",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-622095",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-622095",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-622095",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-622095",
            "association": "5000-622095",
            "publishers": [
                {
                    "name": "Playables"
                }
            ],
            "developers": [
                {
                    "name": "Mario von Rickenbach"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1010301,
            "name": "Speedway Challenge 2024",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:622136",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-622136",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-622136",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-622136",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-622136",
            "association": "5000-622136",
            "publishers": [
                {
                    "name": "Artur Berkowski Berobasket"
                }
            ],
            "developers": [
                {
                    "name": "Artur Berkowski Berobasket"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1010253,
            "name": "CARS",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:622095",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-622095",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-622095",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-622095",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-622095",
            "association": "5000-622095",
            "publishers": [
                {
                    "name": "Playables"
                }
            ],
            "developers": [
                {
                    "name": "Mario von Rickenbach"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1010243,
            "name": "Oops! What if they love me too much?",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:622085",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-622085",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-622085",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-622085",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-622085",
            "association": "5000-622085",
            "publishers": [
                {
                    "name": "Free Studio"
                }
            ],
            "developers": [
                {
                    "name": "Free Studio"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1009970,
            "name": "Find 101 Doomers",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:622023",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-622023",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-622023",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-622023",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-622023",
            "association": "5000-622023",
            "publishers": [
                {
                    "name": "White Box"
                }
            ],
            "developers": [
                {
                    "name": "White Box"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1014649,
            "name": "Human Milk Seller",
            "region": "North America",
            "platform": "Linux",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:619525",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-619525",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-619525",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-619525",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-619525",
            "association": "5000-619525",
            "publishers": [
                {
                    "name": "BoJeux"
                }
            ],
            "developers": [
                {
                    "name": "BoJeux"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Switch eShop",
            "id": 1016004,
            "name": "Frowntown",
            "region": "Europe",
            "platform": "Nintendo Switch",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:624433",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-624433",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-624433",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-624433",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-624433",
            "association": "5000-624433",
            "publishers": [
                {
                    "name": "Elushis"
                }
            ],
            "developers": [
                {
                    "name": "Elushis"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1015079,
            "name": "CARS",
            "region": "North America",
            "platform": "Linux",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:622095",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-622095",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-622095",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-622095",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-622095",
            "association": "5000-622095",
            "publishers": [
                {
                    "name": "Playables"
                }
            ],
            "developers": [
                {
                    "name": "Mario von Rickenbach"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Epic Games Store",
            "id": 1014746,
            "name": "Dead Space 3",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:143600",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-143600",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-143600",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-143600",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-143600",
            "association": "5000-143600",
            "publishers": [
                {
                    "name": "Electronic Arts"
                },
                {
                    "name": "Sony DADC Brasil"
                }
            ],
            "developers": [
                {
                    "name": "Visceral Games"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "PlayStation Store PS4",
            "id": 1014734,
            "name": "Lab Crisis",
            "region": "Europe",
            "platform": "PlayStation 4",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:565220",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-565220",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-565220",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-565220",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-565220",
            "association": "5000-565220",
            "publishers": [
                {
                    "name": "Xitilon"
                }
            ],
            "developers": [
                {
                    "name": "Xitilon"
                },
                {
                    "name": "Lovixama"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "PlayStation Store PS4",
            "id": 1014733,
            "name": "Ski game",
            "region": "Europe",
            "platform": "PlayStation 4",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:624406",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-624406",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-624406",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-624406",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-624406",
            "association": "5000-624406",
            "publishers": [
                {
                    "name": "Xitilon"
                }
            ],
            "developers": [
                {
                    "name": "Xitilon"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "PlayStation Store PS4",
            "id": 1014731,
            "name": "Ski game",
            "region": "Japan",
            "platform": "PlayStation 4",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:624406",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-624406",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-624406",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-624406",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-624406",
            "association": "5000-624406",
            "publishers": [
                {
                    "name": "Xitilon"
                }
            ],
            "developers": [
                {
                    "name": "Xitilon"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "PlayStation Store PS4",
            "id": 1014730,
            "name": "Lab Crisis",
            "region": "Japan",
            "platform": "PlayStation 4",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:565220",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-565220",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-565220",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-565220",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-565220",
            "association": "5000-565220",
            "publishers": [
                {
                    "name": "Xitilon"
                }
            ],
            "developers": [
                {
                    "name": "Xitilon"
                },
                {
                    "name": "Lovixama"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1014667,
            "name": "The Dark Realm",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:560181",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-560181",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-560181",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-560181",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-560181",
            "association": "5000-560181",
            "publishers": [
                {
                    "name": "Palek"
                }
            ],
            "developers": [
                {
                    "name": "Palek"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1014664,
            "name": "Earth, Fire, And Wind",
            "region": "North America",
            "platform": "Macintosh",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:615473",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-615473",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-615473",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-615473",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-615473",
            "association": "5000-615473",
            "publishers": [
                {
                    "name": "Serious Mlerm"
                },
                {
                    "name": "Serious Mlerm LLC"
                }
            ],
            "developers": [
                {
                    "name": "Serious Mlerm"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1014663,
            "name": "MarineVerse Cup - Sailboat Racing (Early Access)",
            "region": "North America",
            "platform": "Macintosh",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:499466",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-499466",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-499466",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-499466",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-499466",
            "association": "5000-499466",
            "publishers": [
                {
                    "name": "MarineVerse"
                }
            ],
            "developers": [
                {
                    "name": "MarineVerse"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1014653,
            "name": "To Kill A King",
            "region": "North America",
            "platform": "Linux",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:533154",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-533154",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-533154",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-533154",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-533154",
            "association": "5000-533154",
            "publishers": [
                {
                    "name": "1SiGn Games"
                }
            ],
            "developers": [
                {
                    "name": "1SiGn Games"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1014652,
            "name": "Sergei and the Tax Return",
            "region": "North America",
            "platform": "Linux",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:612884",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-612884",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-612884",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-612884",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-612884",
            "association": "5000-612884",
            "publishers": [
                {
                    "name": "Pre-Tech PC Services"
                }
            ],
            "developers": [
                {
                    "name": "Pre-Tech PC Services"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1009477,
            "name": "Exit 13 Gallery Escape",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:621650",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-621650",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-621650",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-621650",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-621650",
            "association": "5000-621650",
            "publishers": [
                {
                    "name": "Enigma Games"
                }
            ],
            "developers": [
                {
                    "name": "Enigma Games"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "PlayStation Store PS5",
            "id": 1014637,
            "name": "Rainbow Cotton Remaster",
            "region": "Australia",
            "platform": "PlayStation 5",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:1691",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-1691",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-1691",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-1691",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-1691",
            "association": "5000-1691",
            "publishers": [
                {
                    "name": "Success"
                },
                {
                    "name": "ININ Games"
                },
                {
                    "name": "Strictly Limited Games"
                }
            ],
            "developers": [
                {
                    "name": "Success"
                },
                {
                    "name": "Kritzelkratz"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "PlayStation Store PS4",
            "id": 1014631,
            "name": "Ski game",
            "region": "Australia",
            "platform": "PlayStation 4",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:624406",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-624406",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-624406",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-624406",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-624406",
            "association": "5000-624406",
            "publishers": [
                {
                    "name": "Xitilon"
                }
            ],
            "developers": [
                {
                    "name": "Xitilon"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "PlayStation Store PS4",
            "id": 1014630,
            "name": "Lab Crisis",
            "region": "Australia",
            "platform": "PlayStation 4",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:565220",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-565220",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-565220",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-565220",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-565220",
            "association": "5000-565220",
            "publishers": [
                {
                    "name": "Xitilon"
                }
            ],
            "developers": [
                {
                    "name": "Xitilon"
                },
                {
                    "name": "Lovixama"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "PlayStation Store PS4",
            "id": 1014627,
            "name": "Rainbow Cotton Remaster",
            "region": "Australia",
            "platform": "PlayStation 4",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:1691",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-1691",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-1691",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-1691",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-1691",
            "association": "5000-1691",
            "publishers": [
                {
                    "name": "Success"
                },
                {
                    "name": "ININ Games"
                },
                {
                    "name": "Strictly Limited Games"
                }
            ],
            "developers": [
                {
                    "name": "Success"
                },
                {
                    "name": "Kritzelkratz"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1014550,
            "name": "Content Warning",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:624337",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-624337",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-624337",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-624337",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-624337",
            "association": "5000-624337",
            "publishers": [
                {
                    "name": "LandFall Games"
                }
            ],
            "developers": [
                {
                    "name": "LandFall Games"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "PlayStation Store PS5",
            "id": 1014537,
            "name": "Rainbow Cotton Remaster",
            "region": "Europe",
            "platform": "PlayStation 5",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:1691",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-1691",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-1691",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-1691",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-1691",
            "association": "5000-1691",
            "publishers": [
                {
                    "name": "Success"
                },
                {
                    "name": "ININ Games"
                },
                {
                    "name": "Strictly Limited Games"
                }
            ],
            "developers": [
                {
                    "name": "Success"
                },
                {
                    "name": "Kritzelkratz"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "PlayStation Store PS4",
            "id": 1014536,
            "name": "Rainbow Cotton Remaster",
            "region": "Europe",
            "platform": "PlayStation 4",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:1691",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-1691",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-1691",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-1691",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-1691",
            "association": "5000-1691",
            "publishers": [
                {
                    "name": "Success"
                },
                {
                    "name": "ININ Games"
                },
                {
                    "name": "Strictly Limited Games"
                }
            ],
            "developers": [
                {
                    "name": "Success"
                },
                {
                    "name": "Kritzelkratz"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "PlayStation Store PS5",
            "id": 1014526,
            "name": "Cazzarion: Gunslinger",
            "region": "North America",
            "platform": "PlayStation 5",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:624336",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-624336",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-624336",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-624336",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-624336",
            "association": "5000-624336",
            "publishers": [
                {
                    "name": "Armin Unold"
                }
            ],
            "developers": [
                {
                    "name": "Armin Unold"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "PlayStation Store PS5",
            "id": 1014525,
            "name": "Drift Streets Japan",
            "region": "North America",
            "platform": "PlayStation 5",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:624330",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-624330",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-624330",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-624330",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-624330",
            "association": "5000-624330",
            "publishers": [
                {
                    "name": "RandomSpin"
                }
            ],
            "developers": [
                {
                    "name": "RandomSpin"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "PlayStation Store PS4",
            "id": 1014504,
            "name": "Drift Streets Japan",
            "region": "North America",
            "platform": "PlayStation 4",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:624330",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-624330",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-624330",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-624330",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-624330",
            "association": "5000-624330",
            "publishers": [
                {
                    "name": "RandomSpin"
                }
            ],
            "developers": [
                {
                    "name": "RandomSpin"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Online",
            "id": 1014502,
            "name": "Big Adventure: Trip to Europe 7",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:620660",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-620660",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-620660",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-620660",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-620660",
            "association": "5000-620660",
            "publishers": [
                {
                    "name": "Big Fish Games"
                }
            ],
            "developers": [
                {
                    "name": "AVI Games"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 953881,
            "name": "Bring The Chickens Home (Early Access)",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:596270",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-596270",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-596270",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-596270",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-596270",
            "association": "5000-596270",
            "publishers": [
                {
                    "name": "Clyde Smets"
                }
            ],
            "developers": [
                {
                    "name": "Clyde Smets"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 999164,
            "name": "Evostrike",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:616612",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-616612",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-616612",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-616612",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-616612",
            "association": "5000-616612",
            "publishers": [
                {
                    "name": "DrTronik"
                }
            ],
            "developers": [
                {
                    "name": "DrTronik"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 998191,
            "name": "MoeSpotter - Uncover the Girls' Mysteries!",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:616335",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-616335",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-616335",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-616335",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-616335",
            "association": "5000-616335",
            "publishers": [
                {
                    "name": "ROGames"
                }
            ],
            "developers": [
                {
                    "name": "ROGames"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 996396,
            "name": "Relationship Anarchy",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:615655",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-615655",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-615655",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-615655",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-615655",
            "association": "5000-615655",
            "publishers": [
                {
                    "name": "Sandra Moen"
                }
            ],
            "developers": [
                {
                    "name": "Sandra Moen"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 994688,
            "name": "Lost Hope (Early Access)",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:614982",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-614982",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-614982",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-614982",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-614982",
            "association": "5000-614982",
            "publishers": [
                {
                    "name": "Shadow Sparks Studio"
                }
            ],
            "developers": [
                {
                    "name": "Shadow Sparks Studio"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 993275,
            "name": "Perfect Poses",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:614389",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-614389",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-614389",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-614389",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-614389",
            "association": "5000-614389",
            "publishers": [
                {
                    "name": "QuantumTechno Games"
                }
            ],
            "developers": [
                {
                    "name": "QuantumTechno Games"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 992741,
            "name": "Unsolved Mysteries 2: The Bridge Master",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:614039",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-614039",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-614039",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-614039",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-614039",
            "association": "5000-614039",
            "publishers": [
                {
                    "name": "GameMaker"
                }
            ],
            "developers": [
                {
                    "name": "GameMaker"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 986462,
            "name": "FAN POP RHYTHM STAGE ~ Aim for the Heart ~",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:611723",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-611723",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-611723",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-611723",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-611723",
            "association": "5000-611723",
            "publishers": [
                {
                    "name": "SERIALGAMES Inc."
                }
            ],
            "developers": [
                {
                    "name": "SERIALGAMES Inc."
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 983686,
            "name": "Holy Maid Academy",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:610693",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-610693",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-610693",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-610693",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-610693",
            "association": "5000-610693",
            "publishers": [
                {
                    "name": "Shiravune"
                }
            ],
            "developers": [
                {
                    "name": "Liquid"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 978162,
            "name": "Code Has Price",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:608392",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-608392",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-608392",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-608392",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-608392",
            "association": "5000-608392",
            "publishers": [
                {
                    "name": "Fewjix"
                }
            ],
            "developers": [
                {
                    "name": "Fewjix"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 973253,
            "name": "Invaders 360",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:606323",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-606323",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-606323",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-606323",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-606323",
            "association": "5000-606323",
            "publishers": [
                {
                    "name": "Holo Games GbR"
                }
            ],
            "developers": [
                {
                    "name": "Holo Games GbR"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 961942,
            "name": "Dark Age",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:600513",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-600513",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-600513",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-600513",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-600513",
            "association": "5000-600513",
            "publishers": [
                {
                    "name": "SeluGames"
                }
            ],
            "developers": [
                {
                    "name": "SeluGames"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 953901,
            "name": "Bring The Chickens Home (Early Access)",
            "region": "North America",
            "platform": "Linux",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:596270",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-596270",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-596270",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-596270",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-596270",
            "association": "5000-596270",
            "publishers": [
                {
                    "name": "Clyde Smets"
                }
            ],
            "developers": [
                {
                    "name": "Clyde Smets"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1000620,
            "name": "Inside The Memory",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:617382",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-617382",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-617382",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-617382",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-617382",
            "association": "5000-617382",
            "publishers": [
                {
                    "name": "Garnet Bloom"
                }
            ],
            "developers": [
                {
                    "name": "Garnet Bloom"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 950124,
            "name": "Pawggle",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:594007",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-594007",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-594007",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-594007",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-594007",
            "association": "5000-594007",
            "publishers": [
                {
                    "name": "Pandaroo Interactive"
                }
            ],
            "developers": [
                {
                    "name": "Pandaroo Interactive"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 947294,
            "name": "ASTRA: Knights of Veda",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:592733",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-592733",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-592733",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-592733",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-592733",
            "association": "5000-592733",
            "publishers": [
                {
                    "name": "HYBE IM"
                }
            ],
            "developers": [
                {
                    "name": "FLINT"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 944091,
            "name": "Drevepsina",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:591379",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-591379",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-591379",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-591379",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-591379",
            "association": "5000-591379",
            "publishers": [
                {
                    "name": "yiotro"
                }
            ],
            "developers": [
                {
                    "name": "yiotro"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 941928,
            "name": "Protocol Delta",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:590700",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-590700",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-590700",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-590700",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-590700",
            "association": "5000-590700",
            "publishers": [
                {
                    "name": "itsBoats"
                }
            ],
            "developers": [
                {
                    "name": "itsBoats"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 927788,
            "name": "Roll It To The End (Early Access)",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:585263",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-585263",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-585263",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-585263",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-585263",
            "association": "5000-585263",
            "publishers": [
                {
                    "name": "STORMY RISE"
                }
            ],
            "developers": [
                {
                    "name": "STORMY RISE"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 925839,
            "name": "I Can See You",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:584689",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-584689",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-584689",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-584689",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-584689",
            "association": "5000-584689",
            "publishers": [
                {
                    "name": "Skyward Games"
                }
            ],
            "developers": [
                {
                    "name": "Skyward Games"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 915140,
            "name": "Elder Trial",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:579971",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-579971",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-579971",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-579971",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-579971",
            "association": "5000-579971",
            "publishers": [
                {
                    "name": "Amii"
                }
            ],
            "developers": [
                {
                    "name": "Amii"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 857633,
            "name": "Art of Stunt",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:559496",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-559496",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-559496",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-559496",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-559496",
            "association": "5000-559496",
            "publishers": [
                {
                    "name": "ZHANG FAN"
                }
            ],
            "developers": [
                {
                    "name": "ZHANG FAN"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 857560,
            "name": "Art of Stunt",
            "region": "North America",
            "platform": "Macintosh",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:559496",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-559496",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-559496",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-559496",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-559496",
            "association": "5000-559496",
            "publishers": [
                {
                    "name": "ZHANG FAN"
                }
            ],
            "developers": [
                {
                    "name": "ZHANG FAN"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 857551,
            "name": "Art of Stunt",
            "region": "North America",
            "platform": "Linux",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:559496",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-559496",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-559496",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-559496",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-559496",
            "association": "5000-559496",
            "publishers": [
                {
                    "name": "ZHANG FAN"
                }
            ],
            "developers": [
                {
                    "name": "ZHANG FAN"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 834567,
            "name": "Freakland",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:546596",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-546596",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-546596",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-546596",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-546596",
            "association": "5000-546596",
            "publishers": [
                {
                    "name": "kunst Games"
                }
            ],
            "developers": [
                {
                    "name": "kunst Games"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1003293,
            "name": "Chuno",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:618820",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-618820",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-618820",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-618820",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-618820",
            "association": "5000-618820",
            "publishers": [
                {
                    "name": "tamanegi7"
                }
            ],
            "developers": [
                {
                    "name": "tamanegi7"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1009075,
            "name": "The Noob Adventures: Fool For Love",
            "region": "North America",
            "platform": "Linux",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:621404",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-621404",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-621404",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-621404",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-621404",
            "association": "5000-621404",
            "publishers": [
                {
                    "name": "Ping Group"
                }
            ],
            "developers": [
                {
                    "name": "Ping Group"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1009050,
            "name": "Sir Fallen",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:621443",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-621443",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-621443",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-621443",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-621443",
            "association": "5000-621443",
            "publishers": [
                {
                    "name": "Neverknow247"
                }
            ],
            "developers": [
                {
                    "name": "Neverknow247"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1009045,
            "name": "Bull-Bia Ricky",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:621438",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-621438",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-621438",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-621438",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-621438",
            "association": "5000-621438",
            "publishers": [
                {
                    "name": "TakaEVP"
                }
            ],
            "developers": [
                {
                    "name": "TakaEVP"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1009010,
            "name": "The Noob Adventures: Fool For Love",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:621404",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-621404",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-621404",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-621404",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-621404",
            "association": "5000-621404",
            "publishers": [
                {
                    "name": "Ping Group"
                }
            ],
            "developers": [
                {
                    "name": "Ping Group"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1008945,
            "name": "Dungeons & Cardboard",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:621342",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-621342",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-621342",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-621342",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-621342",
            "association": "5000-621342",
            "publishers": [
                {
                    "name": "Ornithocornicorp"
                }
            ],
            "developers": [
                {
                    "name": "Ornithocornicorp"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1008271,
            "name": "Brass Necessity (Early Access)",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:621102",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-621102",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-621102",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-621102",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-621102",
            "association": "5000-621102",
            "publishers": [
                {
                    "name": "Popped Corn Bytes"
                }
            ],
            "developers": [
                {
                    "name": "Zackery Turman"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1007904,
            "name": "Asteroid Drift",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:620980",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-620980",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-620980",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-620980",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-620980",
            "association": "5000-620980",
            "publishers": [
                {
                    "name": "Warder Games"
                }
            ],
            "developers": [
                {
                    "name": "Warder Games"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1007633,
            "name": "Ario",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:620861",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-620861",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-620861",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-620861",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-620861",
            "association": "5000-620861",
            "publishers": [
                {
                    "name": "Artax Games"
                }
            ],
            "developers": [
                {
                    "name": "Vata Games"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1006938,
            "name": "Project Circle",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:620464",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-620464",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-620464",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-620464",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-620464",
            "association": "5000-620464",
            "publishers": [
                {
                    "name": "gg game"
                }
            ],
            "developers": [
                {
                    "name": "gg game"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1006663,
            "name": "Piece It!",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:620390",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-620390",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-620390",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-620390",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-620390",
            "association": "5000-620390",
            "publishers": [
                {
                    "name": "Qey Studios"
                }
            ],
            "developers": [
                {
                    "name": "Qey Studios"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1005083,
            "name": "Twilight Survivors",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:616341",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-616341",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-616341",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-616341",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-616341",
            "association": "5000-616341",
            "publishers": [
                {
                    "name": "DORIDORI STUDIO"
                }
            ],
            "developers": [
                {
                    "name": "DORIDORI STUDIO"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1004888,
            "name": "Human Milk Seller",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:619525",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-619525",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-619525",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-619525",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-619525",
            "association": "5000-619525",
            "publishers": [
                {
                    "name": "BoJeux"
                }
            ],
            "developers": [
                {
                    "name": "BoJeux"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 833342,
            "name": "DEVICE 0101 (Early Access)",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:545769",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-545769",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-545769",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-545769",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-545769",
            "association": "5000-545769",
            "publishers": [
                {
                    "name": "SADARI GAMES"
                }
            ],
            "developers": [
                {
                    "name": "SADARI GAMES"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1003149,
            "name": "The book by the blue",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:618757",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-618757",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-618757",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-618757",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-618757",
            "association": "5000-618757",
            "publishers": [
                {
                    "name": "Travel oblivion"
                }
            ],
            "developers": [
                {
                    "name": "Travel oblivion"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1002403,
            "name": "Where Is George",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:618377",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-618377",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-618377",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-618377",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-618377",
            "association": "5000-618377",
            "publishers": [
                {
                    "name": "SoftStoneGames"
                }
            ],
            "developers": [
                {
                    "name": "SoftStoneGames"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1002225,
            "name": "I got GOONED by a FEMBOY",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:618323",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-618323",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-618323",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-618323",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-618323",
            "association": "5000-618323",
            "publishers": [
                {
                    "name": "owlyboi"
                }
            ],
            "developers": [
                {
                    "name": "owlyboi"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1001673,
            "name": "157 (Early Access)",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:617905",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-617905",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-617905",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-617905",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-617905",
            "association": "5000-617905",
            "publishers": [
                {
                    "name": "Alphagames Group"
                }
            ],
            "developers": [
                {
                    "name": "Alphagames Group"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1001504,
            "name": "TILE PERFECT",
            "region": "North America",
            "platform": "Linux",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:617707",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-617707",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-617707",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-617707",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-617707",
            "association": "5000-617707",
            "publishers": [
                {
                    "name": "Shinogame"
                }
            ],
            "developers": [
                {
                    "name": "Shinogame"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1001470,
            "name": "HEAVENS STAIRS",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:617784",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-617784",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-617784",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-617784",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-617784",
            "association": "5000-617784",
            "publishers": [
                {
                    "name": "blain"
                }
            ],
            "developers": [
                {
                    "name": "blain"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1001366,
            "name": "Finally Free",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:617732",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-617732",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-617732",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-617732",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-617732",
            "association": "5000-617732",
            "publishers": [
                {
                    "name": "agapiOS"
                }
            ],
            "developers": [
                {
                    "name": "agapiOS"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1001322,
            "name": "TILE PERFECT",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:617707",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-617707",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-617707",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-617707",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-617707",
            "association": "5000-617707",
            "publishers": [
                {
                    "name": "Shinogame"
                }
            ],
            "developers": [
                {
                    "name": "Shinogame"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1001196,
            "name": "Caden's Climb",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:617623",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-617623",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-617623",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-617623",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-617623",
            "association": "5000-617623",
            "publishers": [
                {
                    "name": "SillyMan Studios"
                }
            ],
            "developers": [
                {
                    "name": "Mr. Climb"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1000625,
            "name": "MOUTHOLE",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:617387",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-617387",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-617387",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-617387",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-617387",
            "association": "5000-617387",
            "publishers": [
                {
                    "name": "Anything Nose Productions"
                }
            ],
            "developers": [
                {
                    "name": "Anything Nose Productions"
                }
            ]
        },
        {
            "upc": "",
            "release_date": "2024-04-01 12:00:00",
            "distribution_type": "Steam",
            "id": 1000624,
            "name": "I got CUCKED by a FUTANARI",
            "region": "North America",
            "platform": "PC",
            "game_api_url": "https://www.gamespot.com/api/games/?filter=id:617386",
            "reviews_api_url": "https://www.gamespot.com/api/reviews/?filter=association:5000-617386",
            "articles_api_url": "https://www.gamespot.com/api/articles/?filter=association:5000-617386",
            "videos_api_url": "https://www.gamespot.com/api/videos/?filter=association:5000-617386",
            "images_api_url": "https://www.gamespot.com/api/images/?filter=association:5000-617386",
            "association": "5000-617386",
            "publishers": [
                {
                    "name": "owlyboi"
                }
            ],
            "developers": [
                {
                    "name": "owlyboi"
                }
            ]
        }
    ],
    "version": "1.0"
}
    await fetch_game_releases(data)


if __name__ == "__main__":
    asyncio.run(main())
