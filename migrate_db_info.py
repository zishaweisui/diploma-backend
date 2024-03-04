import asyncio
import pandas as pd

from structure import structure
from models.game import Game

repository = structure.instantiate("games_repository")


async def extract_game_info(df):
    raw_games = []
    async with asyncio.TaskGroup() as tg:
        for item in df.itertuples(index=False):
            genres = []
            for column in ["positive_ratings", "negative_ratings", "average_playtime", "median_playtime"]:
                data = item[column]
                if isinstance(data, int):
                    continue
                if isinstance(data, str) and data.startswith("Steam"):
                    continue
                genres.append(data)

        attributes = {
            "steam_id": item.appid,
            "name": item.name,
            "developer": item.developer,
            "publisher": item.publisher,
            "genres": genres
        }
        game = Game(**attributes)
        raw_games.append(game)

        return raw_games


async def create_games(raw_games: list[Game]):
    file = "steam_media_data.csv"
    target_columns = ["steam_appid", "header_image"]
    df = pd.read_csv(file, dtype={"steam_appid": int, "header_image": str})[target_columns]

    hash_map = df.set_index('steam_appid')['header_image'].to_dict()

    for game in raw_games:
        steam_appid = game.steam_id
        if steam_appid in hash_map:
            header_image = hash_map[steam_appid]
            game.header_image = header_image
        else:
            game.header_image = None

        await repository.create(game)


if __name__ == "__main__":
    async def migrate_db_info():
        main_file = "steam.csv"
        target_columns = ["appid", "name", "developer", "publisher", "positive_ratings",
                          "negative_ratings", "average_playtime", "median_playtime"]

        df = pd.read_csv(main_file, dtype={"appid": int, "name": str, "developer": str, "publisher": str,
                                      "positive_ratings": str, "negative_ratings": str, "average_playtime": str,
                                      "median_playtime": str})[target_columns]

        print(f"{df = }")
        raw_games = await extract_game_info(df)
        await create_games(raw_games)


    asyncio.run(migrate_db_info())
