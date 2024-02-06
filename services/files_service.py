from infrastructure_exceptions import InvalidRequestException
from models.uploaded_file import SharedUploadedFile, UploadedFile


class FilesService:
    def __init__(self, s3_wrapper):
        self.s3_wrapper = s3_wrapper

    async def upload_io_file(self, io_file):
        return await self.s3_wrapper.upload_io_file(io_file)

    async def delete_orphan_file(self, file):
        if not file or not file.path:
            return
        await self.s3_wrapper.delete_file(file.path)

    async def delete_files(self, files):
        keys_objects = [
            {"Key": uploaded_file.path}
            for uploaded_file
            in files
        ]
        self.s3_wrapper.delete_old_files(keys_objects)

    async def upload_file(self, file):
        uploaded_file = await self.s3_wrapper.upload_file(file)
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

    async def share_file(
            self,
            uploaded_file: UploadedFile | None,
            lifetime=None
    ) -> SharedUploadedFile | None:
        if not uploaded_file:
            return None
        return SharedUploadedFile(
            filename=uploaded_file.filename,
            path=uploaded_file.path,
            link=await self.s3_wrapper.link(uploaded_file.path, lifetime)
        )

    async def delete_orphan_files(self, old_files, new_files):
        new_files_path = {file.path for file in new_files}

        files = [
            file
            for file
            in old_files
            if file.path not in new_files_path
        ]
        if not files:
            return

        keys_objects = [
            {"Key": uploaded_file.path}
            for uploaded_file
            in files
        ]
        self.s3_wrapper.delete_old_files(keys_objects)
