from handlers.base_handler import BaseHandler


class DeleteGameHandler(BaseHandler):
    async def handle(self, game_id, principal=None):
        return await self.execute(principal, self.service.delete_game, game_id)
