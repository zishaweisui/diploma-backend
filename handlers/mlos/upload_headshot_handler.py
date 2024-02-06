from handlers.base_handler import BaseHandler


class UploadMLOHeadshotHandler(BaseHandler):
    async def handle(self, mlo_id, file, principal=None):
        return await self.execute(
            principal, self.service.change_headshot, mlo_id, file)
