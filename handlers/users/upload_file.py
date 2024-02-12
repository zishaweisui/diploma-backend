from handlers.base_handler import BaseHandler


class UploadUserFileHandler(BaseHandler):
    async def handle(self, file, principal=None):
        return await self.execute(principal, self.service.upload_file, file)
