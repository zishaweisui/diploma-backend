from handlers.base_handler import BaseHandler


class GetPublicGamesHandler(BaseHandler):
    async def handle(self, principal=None):
        return await self.execute(principal, self.service.get_games)
