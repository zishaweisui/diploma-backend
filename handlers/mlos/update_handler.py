from handlers.base_handler import BaseHandler


class UpdateMLOHandler(BaseHandler):
    async def handle(self, mlo_id, update_mlo, principal=None):
        return await self.execute(principal, self.service.update_mlo, mlo_id, update_mlo)
