from handlers.base_handler import BaseHandler


class CreateMLOHandler(BaseHandler):
    async def handle(self, mlo, principal=None):
        return await self.execute(principal, self.service.create_mlo, mlo)
