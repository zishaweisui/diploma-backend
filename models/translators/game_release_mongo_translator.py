from models.game_release import GameRelease


class GameReleaseMongoTranslator:
    def to_document(self, model: GameRelease):
        return model.model_dump(by_alias=True)

    def from_document(self, document: dict) -> GameRelease:
        return GameRelease(**document)
