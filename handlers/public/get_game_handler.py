from handlers.base_handler import BaseHandler


class GetPublicGameHandler(BaseHandler):
    async def handle(self, game_id, principal=None):
        return await self.execute(principal, self.service.get_game, game_id)
