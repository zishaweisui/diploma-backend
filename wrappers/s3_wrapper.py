import asyncio
import uuid
from pathlib import Path

from botocore.exceptions import ClientError

from models.uploaded_file import SharedUploadedFile, UploadedFile


class S3Wrapper:
    def __init__(self, session, bucket_name, key_prefix):
        self.session = session
        self.bucket_name = bucket_name
        self.key_prefix = key_prefix
        self.default_lifetime = 28800

    async def move_file(self, source_bucket, source_key, destination_bucket):
        async with self.session.client("s3") as s3_client:
            try:
                await s3_client.copy_object(
                    CopySource={"Bucket": source_bucket, "Key": source_key},
                    Bucket=destination_bucket,
                    Key=source_key
                )
                await s3_client.delete_object(Bucket=source_bucket, Key=source_key)

            except ClientError as e:
                print(f"An error occurred while moving the file: {e}")

    async def upload_file(self, file, principal=None):
        if not file:
            return None
        path = Path(file.filename)
        key = self.__generate_key(path.name)
        async with self.session.client("s3") as s3_client:
            await s3_client.upload_fileobj(file, self.bucket_name, key)
        return SharedUploadedFile(
            path=key,
            filename=path.name,
            link=await self.link(key)
        )

    async def upload_public_file(self, file, principal=None):
        if not file:
            return None
        path = Path(file.filename)
        key = self.__generate_key(path.name)
        async with self.session.client("s3") as s3_client:
            await s3_client.upload_fileobj(file, self.bucket_name, key)
        return SharedUploadedFile(
            path=key,
            filename=path.name,
            link=self.public_link(key)
        )

    async def upload_files(self, files: list, principal=None):
        if not files:
            return None
        uploaded_files = []
        async with self.session.client("s3") as s3_client:
            tasks = []
            for file in files:
                path = Path(file.filename)
                key = self.__generate_key(path.name)
                task = s3_client.upload_fileobj(file, self.bucket_name, key)
                uploaded_files.append(UploadedFile(key=key, path=path.name))
                tasks.append(task)
            await asyncio.gather(*tasks)
        return uploaded_files

    async def upload_io_file(self, io_file):
        if not io_file:
            return None
        key = self.__generate_key(io_file.name)
        async with self.session.client("s3") as s3_client:
            await s3_client.upload_fileobj(io_file, self.bucket_name, key)
        return UploadedFile(path=key, filename=io_file.name)

    async def download_file(self, download_path, save_target):
        if not download_path or not save_target:
            return None
        async with self.session.client("s3") as s3_client:
            await s3_client.download_file(
                Bucket=self.bucket_name,
                Key=download_path,
                Filename=save_target
            )

    async def link(self, key, lifetime: int = None):
        if not key:
            return None

        async with self.session.client("s3") as s3_client:
            try:
                return await s3_client.generate_presigned_url(
                    "get_object",
                    Params={"Bucket": self.bucket_name, "Key": key},
                    ExpiresIn=lifetime or self.default_lifetime
                )
            except ClientError as e:
                print(f"An error occurred while presenting the file: {e}")
                return None

    def public_link(self, key):
        if not key:
            return None
        return f"https://{self.bucket_name}.s3.amazonaws.com/{key}"

    async def exists(self, key):
        if not key:
            return None
        async with self.session.client("s3") as s3_client:
            try:
                await s3_client.head_object(Bucket=self.bucket_name, Key=key)
            except ClientError:
                return False
        return True

    async def delete_file(self, key):
        async with self.session.client("s3") as s3_client:
            try:
                await s3_client.delete_object(Bucket=self.bucket_name, Key=key)
            except ClientError:
                print("Client error", key)
                pass

    async def delete_files(self, keys_objects: list):
        async with self.session.client("s3") as s3_client:
            try:
                await s3_client.delete_objects(
                    Bucket=self.bucket_name, Delete={"Objects": keys_objects}
                )
            except ClientError as ex:
                print(f"An error occurred while orphan files deletion: {ex}")
                pass

    def __generate_key(self, filename):
        return self.key_prefix + str(uuid.uuid4()) + "/" + filename
