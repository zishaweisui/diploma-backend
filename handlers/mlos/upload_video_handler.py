from handlers.base_handler import BaseHandler


class UploadMLOVideoHandler(BaseHandler):
    async def handle(self, mlo_id, template_id, file, principal=None):
        return await self.execute(
            principal, self.service.upload_video, mlo_id, template_id, file)
