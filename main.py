import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import log
from api.general import router as health_router
from api.v1.auth_routes import router as auth_router
from api.v1.public_routes import router as public_router
from api.v1.users_routes import router as users_router
from env_settings import get_settings

app_settings = get_settings()

log.initialize(
    app_settings.env,
    app_settings.logs_enabled,
    app_settings.console_log_level,
    app_settings.console_log_enable_timestamp,
    app_settings.rollbar_access_token,
    app_settings.rollbar_log_level
)

docs_url = None if app_settings.env == "prod" else "/docs"
application = FastAPI(docs_url=docs_url, redoc_url=None)
application.include_router(health_router)
application.include_router(users_router)
application.include_router(auth_router)
application.include_router(public_router)

application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@application.on_event("startup")
async def startup_db_client():
    from structure import structure

    users_repository = structure.instantiate("users_repository")
    games_repository = structure.instantiate("games_repository")

    async with asyncio.TaskGroup() as tg:
        tg.create_task(users_repository.configure_indexes())
        tg.create_task(games_repository.configure_indexes())

    print("Connected to the MongoDB databases!")
