import asyncio
import pandas as pd

from structure import structure
from models.game import Game

repository = structure.instantiate("games_repository")


async def extract_game_info(df):
    raw_games = []
    for item in df.itertuples(index=False):
        if isinstance(item.genres, str) and item.genres is not None and item.genres is not "0":
            genres = item.genres.split(";")
        else:
            genres = None
        attributes = {
            "steam_id": item.appid,
            "name": item.name,
            "developer": item.developer,
            "publisher": item.publisher,
            "genres": genres,
            "header_image": None
        }
        print(attributes)
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
        target_columns = ["appid", "name", "developer", "publisher", "genres"]
        df = pd.read_csv(main_file, dtype={"appid": int, "name": str, "developer": str,
                         "publisher": str, "genres": str})[target_columns]

        print(f"{df = }")
        raw_games = await extract_game_info(df)
        await create_games(raw_games)


    asyncio.run(migrate_db_info())
