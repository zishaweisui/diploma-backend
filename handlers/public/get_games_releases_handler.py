from handlers.base_handler import BaseHandler


class GetPublicGamesReleasesHandler(BaseHandler):
    async def handle(self, principal=None):
        return await self.execute(principal, self.service.get_games_releases)
