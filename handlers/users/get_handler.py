from handlers.base_handler import BaseHandler


class GetUserHandler(BaseHandler):
    async def handle(self, user_id, principal=None):
        return await self.execute(principal, self.service.get_user, user_id)
