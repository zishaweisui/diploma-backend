from handlers.base_handler import BaseHandler


class ChangePasswordHandler(BaseHandler):
    async def handle(self, user_id, update_password, principal=None):
        return await self.execute(principal, self.service.change_password, user_id, update_password)
