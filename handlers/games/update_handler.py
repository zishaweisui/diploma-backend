from handlers.base_handler import BaseHandler


class UpdateGameHandler(BaseHandler):
    async def handle(self, game_id, update_game, principal=None):
        return await self.execute(principal, self.service.update_game, game_id, update_game)
