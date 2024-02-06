import asyncio

from background_app import app


@app.task(ignore_result=True)
def jaja():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print("JAJAJA"))
