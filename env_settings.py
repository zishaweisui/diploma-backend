from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    env: str
    app_name: str
    s3_bucket: str
    server_username: str
    email: str
    base_domain: str
    web_app_base_domain: str
    web_app_scheme: str
    docker_shared_volume_path: str
    slack_token: str | None

    # rabbit
    rabbitmq_host: str
    rabbitmq_username: str
    rabbitmq_password: str
    rabbitmq_port: int

    jwt_secret: str
    jwt_access_ttl_minutes: int
    jwt_refresh_ttl_hours: int
    bcrypt_complicity: int
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_region: str
    s3_bucket_name: str
    s3_public_bucket_name: str
    s3_temp_bucket_name: str

    mongo_scheme: str
    mongo_username: str
    mongo_password: str
    mongo_host: str
    mongo_port: str
    mongo_name: str

    logs_enabled: bool

    console_log_level: str
    console_log_enable_timestamp: bool

    rollbar_log_level: str
    rollbar_access_token: str

    rabbitmq_host: str
    rabbitmq_username: str
    rabbitmq_password: str
    rabbitmq_port: int

    # redis cache
    cache_redis_host: str
    cache_redis_port: int
    cache_redis_db: int
    cache_redis_default_timeout: float
    cache_redis_password: str

    # Google
    gmail_service_account_creds_path: str
    gmail_service_account_scopes: str
    gmail_service_account_email: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings():
    return Settings()
