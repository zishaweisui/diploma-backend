from pydantic import BaseModel

from models.uploaded_file import UploadedFile


class UploadedFileMongoTranslator(BaseModel):
    def to_document(self, model: UploadedFile):
        document = model.model_dump(by_alias=True)
        document.pop("link", None)
        return document
