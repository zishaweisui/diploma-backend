from infrastructure_exceptions import InvalidRequestException
from models.uploaded_file import SharedUploadedFile, UploadedFile

from .files_service import FilesService


class PublicFilesService(FilesService):
    def __init__(self, s3_wrapper, public_s3_wrapper):
        super().__init__(s3_wrapper)
        self.public_s3_wrapper = public_s3_wrapper

    async def delete_public_orphan_file(self, file):
        if not file or not file.path:
            return
        await self.public_s3_wrapper.delete_file(file.path)

    async def upload_public_file(self, file):
        uploaded_file = await self.public_s3_wrapper.upload_public_file(file)
        if not uploaded_file:
            errors = {
                "upload_file": [
                    {
                        "message": "Could not upload file",
                        "key": "error_upload_file"
                    }
                ]
            }
            raise InvalidRequestException(errors)
        return uploaded_file

    async def migrate_to_public_bucket(self, files):
        for file in files:
            await self.s3_wrapper.move_file(
                self.s3_wrapper.bucket_name,
                file.path,
                self.public_s3_wrapper.bucket_name
            )

    def share_public_file(self, uploaded_file: UploadedFile | None) -> SharedUploadedFile | None:
        if not uploaded_file:
            return None
        return SharedUploadedFile(
            filename=uploaded_file.filename,
            path=uploaded_file.path,
            link=self.public_s3_wrapper.public_link(uploaded_file.path)
        )
