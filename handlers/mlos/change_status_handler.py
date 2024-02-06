from handlers.base_handler import BaseHandler


class ChangeMLOStatusHandler(BaseHandler):
    async def handle(self, mlo_id, status, principal=None):
        return await self.execute(
            principal, self.service.change_status, mlo_id, status)
