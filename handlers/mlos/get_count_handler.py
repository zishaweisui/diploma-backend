from handlers.base_handler import BaseHandler


class GetCountHandler(BaseHandler):
    async def handle(self, filtering, principal=None):
        return await self.execute(principal, self.service.count, filtering)
