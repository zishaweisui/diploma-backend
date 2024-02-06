from handlers.base_handler import BaseHandler


class GetMLOHandler(BaseHandler):
    async def handle(self, mlo_id, principal=None):
        return await self.execute(principal, self.service.get_mlo, mlo_id)
