from models.mlo import MLO


class MLOMongoTranslator:
    def to_document(self, model: MLO):
        document = model.model_dump(by_alias=True)
        document.pop("theme", None)
        return document

    def from_document(self, document: dict) -> MLO:
        return MLO(**document)
