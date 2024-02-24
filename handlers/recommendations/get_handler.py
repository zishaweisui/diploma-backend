from handlers.base_handler import BaseHandler


class GetRecommendationHandler(BaseHandler):
    async def handle(self, user_id, principal=None):
        return await self.execute(principal, self.service.get_recommendation, user_id)
