from models.game import Game


class GameMongoTranslator:
    def to_document(self, model: Game):
        return model.model_dump(by_alias=True)

    def from_document(self, document: dict) -> Game:
        return Game(**document)
