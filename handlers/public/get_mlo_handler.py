from handlers.base_handler import BaseHandler


class GetMLOWebAppHandler(BaseHandler):
    async def handle(self, web_app_id, principal=None):
        return await self.execute(principal, self.service.get_mlo_by_web_app_id, web_app_id)
