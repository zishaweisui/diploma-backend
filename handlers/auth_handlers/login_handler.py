from ..base_handler import BaseHandler


class LoginHandler(BaseHandler):

    async def handle(self, login_request, principal=None):
        return await self.execute(principal, self.service.login, login_request)
