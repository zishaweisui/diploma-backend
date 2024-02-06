import aioboto3
from celery import Celery
from redis import Redis

from env_settings import get_settings
from wrappers import MotorWrapper


class Dependencies:
    def __init__(self):
        self.env_settings = get_settings()

    def motor_wrapper(self):
        return MotorWrapper()

    def s3_session(self):
        return aioboto3.Session(
            aws_access_key_id=self.env_settings.aws_access_key_id,
            aws_secret_access_key=self.env_settings.aws_secret_access_key,
            region_name=self.env_settings.aws_region
        )

    def celery(self):
        queue_host = self.env_settings.rabbitmq_host
        queue_user = self.env_settings.rabbitmq_username
        queue_pass = self.env_settings.rabbitmq_password
        queue_port = self.env_settings.rabbitmq_port

        queue_uri = f"amqp://{queue_user}:{queue_pass}@{queue_host}:{queue_port}"
        return Celery(
            self.env_settings.app_name,
            broker=queue_uri,
            backend="rpc://",
            include=["background_jobs"]
        )

    def redis(self):
        redis_host = self.env_settings.cache_redis_host
        redis_port = self.env_settings.cache_redis_port
        redis_db = self.env_settings.cache_redis_db
        redis_password = self.env_settings.cache_redis_password
        redis_timeout = self.env_settings.cache_redis_default_timeout

        return Redis(
            host=redis_host,
            port=redis_port,
            password=redis_password,
            db=redis_db,
            socket_timeout=redis_timeout
        )
