from ..base_handler import BaseHandler


class RefreshHandler(BaseHandler):

    async def handle(self, refresh_token_request, principal=None):
        return await self.execute(principal, self.service.refresh, refresh_token_request)
