import logging

from rollbar.logger import RollbarHandler

from .handlers import ConsoleLogHandler

Level = str | int


logger = logging.getLogger("VA")
# This is set to debug to handle all possible levels
# decision on which levels should be logged to console or
# rollbar is taken on handlers level. Each handler has it's
# own level and this is configured in app settings.
logger.setLevel(logging.DEBUG)
logger.propagate = False


def _level_to_int(level: Level) -> int | None:
    if isinstance(level, str):
        upper_level = level.upper()

        if upper_level not in logging._nameToLevel:
            return None

        return logging._nameToLevel[upper_level]
    elif isinstance(level, int):
        return level
    else:
        return None


def _initialize_console_handler(level: Level, enable_timestamp: bool):
    lvl = _level_to_int(level)

    if lvl is None:
        return

    handler = ConsoleLogHandler(enable_timestamp)
    handler.setLevel(lvl)
    logger.addHandler(handler)


def _initialize_rollbar_handler(access_token: str, environment: str, level: Level):
    lvl = _level_to_int(level)

    if lvl is None:
        return

    if lvl < logging.INFO:
        lvl = logging.INFO

    handler = RollbarHandler(
        access_token=access_token,
        environment=environment,
        level=lvl,
    )
    logger.addHandler(handler)


def initialize(
    env: str,
    enabled: bool,
    console_log_level: Level,
    console_enable_timestamp: bool,
    rollbar_access_token: str,
    rollbar_log_level: Level,
):
    _initialize_console_handler(console_log_level, console_enable_timestamp)

    allowed_envs = ["prod", "dev"]

    if env in allowed_envs:
        _initialize_rollbar_handler(rollbar_access_token, env, rollbar_log_level)

    logger.disabled = not enabled
