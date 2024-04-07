from models.game_release import GameRelease


class GameReleasesService:
    def __init__(self, repository):
        self.repository = repository

    async def get_games_releases(self, principal=None) -> list[GameRelease]:
        return await self.repository.get_list()
