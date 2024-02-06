from handlers.base_handler import BaseHandler


class DeleteMLOHandler(BaseHandler):
    async def handle(self, mlo_id, principal=None):
        return await self.execute(principal, self.service.delete_mlo, mlo_id)
