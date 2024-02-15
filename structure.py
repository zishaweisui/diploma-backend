from types import LambdaType

from dependencies import Dependencies
from env_settings import get_settings
from gateways import CacheGateway
from gateways.http_client import HttpClient
from gateways.mail_gateway import GmailGateway
from handlers.auth_decorator import AuthDecoratorFactory, AuthFactory
from handlers.auth_handlers import LoginHandler, LogoutHandler, RefreshHandler
from handlers.users import (
    CreateUserHandler,
    DeleteUserHandler,
    GetMeHandler,
    GetUserHandler,
    GetUsersHandler,
    GetUsersPageHandler,
    UpdateUserHandler,
    UploadUserFileHandler,
)
from models.translators import (
    GameMongoTranslator,
    UploadedFileMongoTranslator,
    UserMongoTranslator,
)
from repositories import (
    CacheRepository,
    GamesRepository,
    UsersRepository,
)
from services import (
    AuthService,
    GamesService,
    PageService,
    PasswordService,
    PublicFilesService,
    TokensService,
    UsersService,
)
from services.builders.message_builder import MessageBuilder
from wrappers import BcryptWrapper, S3Wrapper
from wrappers.factories.mongo_index_factory import (
    ascending,
    create_mongo_index,
)

auth_factory = AuthFactory()


class Structure:
    def __init__(self, dependencies: Dependencies):
        self.dependencies = dependencies
        self.structure = {
            "page_service": {
                "class": PageService,
                "args": []
            },
            "bcrypt_wrapper": {
                "class": BcryptWrapper,
                "args": [
                    lambda: get_settings().bcrypt_complicity
                ]
            },
            "users_service": {
                "class": UsersService,
                "args": [
                    "page_service",
                    "password_service",
                    "users_repository"
                ]
            },
            "password_service": {
                "class": PasswordService,
                "args": [
                    "bcrypt_wrapper"
                ]
            },
            "users_repository": {
                "singleton": True,
                "class": UsersRepository,
                "args": [
                    lambda: self.dependencies.motor_wrapper().get_collection(
                        self.dependencies.motor_wrapper().get_client(), "users"),
                    "user_mongo_translator",
                    lambda: create_mongo_index(
                        [
                            ascending("email")
                        ]
                    )
                ]
            },
            "user_mongo_translator": {
                "class": UserMongoTranslator,
                "args": []
            },
            "create_user_handler": {
                "class": CreateUserHandler,
                "args": [
                    "users_service",
                    None
                ]
            },
            "create_user_auth_handler": lambda: self.decorate_auth_handler(
                "create_user_handler", auth_factory.liberal()
            ),
            "get_user_handler": {
                "class": GetUserHandler,
                "args": [
                    "users_service",
                    None
                ]
            },
            "get_user_auth_handler": lambda: self.decorate_auth_handler(
                "get_user_handler", auth_factory.strict(roles=["admin"])
            ),
            "get_me_handler": {
                "class": GetMeHandler,
                "args": [
                    "users_service",
                    None
                ]
            },
            "get_me_auth_handler": lambda: self.decorate_auth_handler(
                "get_me_handler", auth_factory.strict("*")
            ),
            "get_users_handler": {
                "class": GetUsersHandler,
                "args": [
                    "users_service",
                    None
                ]
            },
            "get_users_auth_handler": lambda: self.decorate_auth_handler(
                "get_users_handler", auth_factory.strict(roles=["admin"])
            ),
            "get_users_page_handler": {
                "class": GetUsersPageHandler,
                "args": [
                    "users_service",
                    None
                ]
            },
            "get_users_page_auth_handler": lambda: self.decorate_auth_handler(
                "get_users_page_handler", auth_factory.strict(roles=["admin"])
            ),
            "update_user_handler": {
                "class": UpdateUserHandler,
                "args": [
                    "users_service",
                    None
                ]
            },
            "update_user_auth_handler": lambda: self.decorate_auth_handler(
                "update_user_handler", auth_factory.strict("*")
            ),
            "delete_user_handler": {
                "class": DeleteUserHandler,
                "args": [
                    "users_service",
                    None
                ]
            },
            "delete_user_auth_handler": lambda: self.decorate_auth_handler(
                "delete_user_handler", auth_factory.strict("*")
            ),
            "user_public_file_s3_wrapper": {
                "class": S3Wrapper,
                "args": [
                    lambda: self.dependencies.s3_session(),
                    lambda: get_settings().s3_public_bucket_name,
                    lambda: "users_public_files/"
                ]
            },
            "user_file_s3_wrapper": {
                "class": S3Wrapper,
                "args": [
                    lambda: self.dependencies.s3_session(),
                    lambda: get_settings().s3_bucket_name,
                    lambda: "user_files/"
                ]
            },
            "user_files_service": {
                "class": PublicFilesService,
                "args": [
                    "user_file_s3_wrapper",
                    "user_public_file_s3_wrapper"
                ]
            },
            "upload_user_file_auth_handler": lambda: self.decorate_auth_handler(
                "upload_user_file_handler", auth_factory.strict("*")
            ),
            "upload_user_file_handler": {
                "class": UploadUserFileHandler,
                "args": [
                    "users_service",
                    None
                ]
            },
            "games_service": {
                "class": GamesService,
                "args": [
                    "page_service",
                    "games_repository"
                ]
            },
            "games_repository": {
                "singleton": True,
                "class": GamesRepository,
                "args": [
                    lambda: self.dependencies.motor_wrapper().get_collection(
                        self.dependencies.motor_wrapper().get_client(), "games"),
                    "game_mongo_translator",
                    lambda: create_mongo_index(
                        [
                            ascending("steam_id")
                        ]
                    )
                ]
            },
            "game_mongo_translator": {
                "class": GameMongoTranslator,
                "args": []
            },
            "cache_gateway": {
                "class": CacheGateway,
                "args": [
                    "cache_repository"
                ]
            },
            "cache_repository": {
                "singleton": True,
                "class": CacheRepository,
                "args": [
                    "redis",
                    lambda: 3600
                ]
            },
            "redis": lambda: self.dependencies.redis(),
            "uploaded_file_mongo_translator": {
                "class": UploadedFileMongoTranslator
            },
            "http_client": {
                "singleton": False,
                "class": HttpClient,
                "args": []
            },
            "login_handler": {
                "class": LoginHandler,
                "args": [
                    "auth_service",
                    None
                ]
            },
            "logout_handler": {
                "class": LogoutHandler,
                "args": [
                    "auth_service",
                    None
                ]
            },
            "logout_auth_handler": lambda: self.decorate_auth_handler(
                "logout_handler", auth_factory.strict("*")
            ),
            "refresh_handler": {
                "class": RefreshHandler,
                "args": [
                    "auth_service",
                    None
                ]
            },
            "auth_service": {
                "class": AuthService,
                "args": [
                    "users_repository",
                    "password_service",
                    "tokens_service"
                ]
            },
            "tokens_service": {
                "class": TokensService,
                "args": [
                    lambda: get_settings().jwt_secret,
                    lambda: get_settings().jwt_access_ttl_minutes,
                    lambda: get_settings().jwt_refresh_ttl_hours
                ]
            },
            "auth_decorator_factory": {
                "class": AuthDecoratorFactory,
                "args": [
                    "auth_service"
                ]
            },
            "message_builder": {
                "class": MessageBuilder,
                "args": []
            },
            "email_gateway": {
                "class": GmailGateway,
                "args": [
                    lambda: get_settings().gmail_service_account_creds_path,
                    lambda: get_settings().gmail_service_account_scopes.split(","),
                    "sender_email"
                ]
            },
            "sender_email": lambda: get_settings().gmail_service_account_email
        }

    def decorate_auth_handler(self, handler_key, policy):
        factory = self.instantiate("auth_decorator_factory")
        handler = self.instantiate(handler_key)
        return factory.decorate(handler, policy)

    def instantiate(self, key):
        is_singleton = False
        if hasattr(self, key):
            return getattr(self, key)
        element = self.structure[key]
        result = None

        if isinstance(element, dict):
            is_singleton = element.get("singleton")
            args = [self.__instantiate_arg(arg)
                    for arg in element.get("args", [])]
            kwargs = {}
            for key in element.get("kwargs", {}):
                kwargs[key] = self.__instantiate_arg(element["kwargs"][key])
            result = element["class"](*args, **kwargs)
        elif isinstance(element, LambdaType):
            result = element()

        if is_singleton:
            setattr(self, key, result)
            return getattr(self, key)
        return result

    def __instantiate_arg(self, arg):
        if isinstance(arg, str):
            return self.instantiate(arg)
        elif isinstance(arg, LambdaType):
            return arg()
        elif isinstance(arg, list):
            return [self.instantiate(k) for k in arg]
        elif isinstance(arg, dict):
            value = {}
            for k in arg:
                if isinstance(arg[k], LambdaType):
                    value[k] = arg[k]()
                else:
                    value[k] = self.instantiate(arg[k])
            return value
        return None


deps = Dependencies()
structure = Structure(deps)
