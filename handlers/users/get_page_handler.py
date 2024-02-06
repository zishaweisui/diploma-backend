from handlers.base_handler import BaseHandler


class GetUsersPageHandler(BaseHandler):
    async def handle(self, paging, principal=None):
        return await self.execute(principal, self.service.get_page, paging)
