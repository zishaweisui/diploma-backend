from handlers.base_handler import BaseHandler


class DeleteUserHandler(BaseHandler):
    async def handle(self, user_id, principal=None):
        return await self.execute(principal, self.service.delete_user, user_id)
