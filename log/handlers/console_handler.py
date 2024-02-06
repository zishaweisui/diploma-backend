import logging

from colorlog import ColoredFormatter

_console_formatter = ColoredFormatter(
    "{thin}{asctime}{reset} {log_color}[{name} | {levelname:8s}]: {message}",
    datefmt="%Y-%m-%d %H:%M:%S",
    reset=True,
    log_colors={
        "DEBUG": "blue",
        "WARNING": "yellow",
        "WARN": "yellow",
        "ERROR": "red",
        "CRITICAL": "purple",
    },
    style="{",
)


_console_formatter_without_timestamp = ColoredFormatter(
    "{log_color}[{name} | {levelname:8s}]: {message}",
    datefmt="%Y-%m-%d %H:%M:%S",
    reset=True,
    log_colors={
        "DEBUG": "blue",
        "WARNING": "yellow",
        "WARN": "yellow",
        "ERROR": "red",
        "CRITICAL": "purple",
    },
    style="{",
)


class ConsoleLogHandler(logging.StreamHandler):
    def __init__(self, enable_timestamp: bool):
        super().__init__()
        if enable_timestamp:
            self.setFormatter(_console_formatter)
        else:
            self.setFormatter(_console_formatter_without_timestamp)
