from handlers.base_handler import BaseHandler


class GetMLOWebAppInfoHandler(BaseHandler):
    async def handle(self, mlo_id, principal=None):
        return await self.execute(principal, self.service.get_web_app_info, mlo_id)
