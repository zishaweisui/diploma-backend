from handlers.base_handler import BaseHandler


class CreateUserHandler(BaseHandler):
    async def handle(self, user, principal=None):
        return await self.execute(principal, self.service.create_user, user)
