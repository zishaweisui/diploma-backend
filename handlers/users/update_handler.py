from handlers.base_handler import BaseHandler


class UpdateUserHandler(BaseHandler):
    async def handle(self, user_id, update_user, principal=None):
        return await self.execute(principal, self.service.update_user, user_id, update_user)
