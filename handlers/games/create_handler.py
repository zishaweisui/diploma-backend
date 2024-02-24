from handlers.base_handler import BaseHandler


class CreateGameHandler(BaseHandler):
    async def handle(self, game, principal=None):
        return await self.execute(principal, self.service.create_game, game)
