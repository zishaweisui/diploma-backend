from bson.objectid import ObjectId

from infrastructure_exceptions import InvalidRequestException, NotFoundException


class RecommendationsService:
    def __init__(self, games_repository):
        self.games_repository = games_repository

    async def get_recommendation(self, user_id: ObjectId):
        ...
