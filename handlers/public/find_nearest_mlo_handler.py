from handlers.base_handler import BaseHandler


class FindNearestMLOHandler(BaseHandler):
    async def handle(self, zip_code, principal=None):
        return await self.execute(principal, self.service.find_nearest_mlo, zip_code)
