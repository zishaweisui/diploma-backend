from ..base_handler import BaseHandler


class LogoutHandler(BaseHandler):

    async def handle(self, header, principal=None):
        return await self.execute(principal, self.service.logout, header)
