from models.user import User


class UserMongoTranslator:
    def to_document(self, model: User):
        return model.model_dump(by_alias=True)

    def from_document(self, document: dict) -> User:
        return User(**document)
