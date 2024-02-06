from celery.schedules import crontab

from dependencies import Dependencies
from env_settings import get_settings

app_settings = get_settings()
deps = Dependencies()
app = deps.celery()


if app_settings.env == "local":
    app.conf.beat_schedule = {
        "jaja": {
            "task": "background_jobs.jaja",
            "schedule": crontab("20", "4")
        }
    }
